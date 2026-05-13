from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

app.secret_key = "supersecretkey"


# CREATE DATABASE TABLE
def create_table():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


create_table()


# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# SIGNUP PAGE
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect("/login")

        except:
            return "Username already exists"

    return render_template("signup.html")


# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[2]

            if check_password_hash(stored_password, password):

                session["username"] = username

                return redirect("/dashboard")

        return "Invalid username or password"

    return render_template("login.html")


# DASHBOARD PAGE
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


app.run(debug=True)