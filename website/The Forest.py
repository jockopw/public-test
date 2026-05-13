inventory = []

def get_input(prompt):
    while True:
        choice = input(prompt)

        if choice.lower() == "inventory":
            show_inventory()
            continue

        if choice.lower() == "call the authorities":
            if "Phone" in inventory:
                print()
                print("You quickly call the authorities and explain everything.")
                print("Sirens echo through the abandoned town.")
                print()
                print("The Old Mans dead body rots away before the police arrive.")
                print()
                print("You survived.")
                print()
                print("ENDING REACHED: Saved By The Authorities")
                exit()
            else:
                print()
                print("You don't have a phone.")
                continue

        if choice == "Call the authorities using the radio":
            if "Radio" in inventory:
                print()
                print("You quickly call the authorities and explain everything.")
                print("Sirens echo through the abandoned town.")
                print()
                print("The Old Mans dead body rots away before the police arrive.")
                print()
                print("You survived.")
                print()
                print("ENDING REACHED: Saved By The Authorities, But At What Cost?")
                exit()
            else:
                print()
                print("You don't have a radio.")
                continue

        return choice
    
def show_inventory():
    print()
    print("=== INVENTORY ===")
    
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print("-", item)

    print("=================")
    print()

print("You wake up in the forest. You see a path ahead of you.")
print()

while True:
    choice = get_input("Do you want to go left or right? ")
    if choice == "left":
        print()
        break
    elif choice == "right":
        print()
        print("You walk down the right path and disappear into the forest... (to be continued)")
        exit()
    else:
        print()
        print("Invalid choice. Try again.")


while True:
    print()
    print("You find a house. You knock on the door and an old man answers. He invites you in and gives you a warm meal, but you are unsure if you can trust him.")
    print()
    print("Do you want to stay and eat the meal or leave the house?")
    print()
    print("A.) Stay and eat the meal")
    print("B.) Leave the house")

    choice = input("Make your choice (Type a letter): ")

    if choice == "A":
        print()
        break

    elif choice == "B":
        print()
        print("You leave the house safely and continue your journey.")
        exit()

    else:
        print()
        print("Invalid choice. Try again.")


while True:
    print()
    print("You decide to stay and eat the meal. The meal is poisoned and you blackout")
    print()
    print("You wake up in a dark room, nauseated, and dizzy. You look around and only see a small window and a door.")
    print()
    print("A.) Try to escape through the window")
    print("B.) Try to escape through the door")

    choice = get_input("Make your choice (Type a letter): ")

    if choice == "A":
        print()
        print("You try to escape through the window, but it is too small and you get stuck. The old man catches you.")
        print()
        continue

    elif choice == "B":
        print()
        print("You try to escape through the door, but it is locked with a passcode.")
        print()
        print("You think to yourself why is it a math equation?")
        break

    else:
        print()
        print("Invalid choice. Try again.")


while True:
    print()
    print("What is 12 x 15?")
    print()
    choice = get_input("Answer: ")

    if choice == "180":
        print()
        print("You correctly solve the math equation and escape the room and the old man is nowhere to be seen near the room.")
        print()
        print("You look around the house and find a note that says 'Congratulations on escaping the house, but the torture is not over yet. I am waiting. -The Old Man'")
        print()
        print("You look around the house and find a knife, food and a rope. The inventory is now unlocked. Type 'inventory' to view your inventory.")
        inventory.append("Knife")
        inventory.append("Food")
        inventory.append("Rope")
        print()
        print("You look around the house and find the front door unlocked and you step outside and you look around and see that you are no longer in a forest, but in a abandoned town.")
        print()
        print("You walk around the town and find a map that shows a location of a safe house. You decide to head there.")
        print()
        choice = get_input("Do you want to head to the safe house? (Type 'yes' or 'no'): ")
        if choice.lower() == "yes":
            print()
            print("You head to the safe house and find a group of people who are also trying to escape")
            print()
            print("In that moment.")
            print("You realize.")
            print("You are not alone.")
            print()
            print("They offer you some food and you are not sure if you can trust them, but you eat it anyways.")
            print()
            print("It turns out the food is actually safe and you start to feel better.")
            print()
            print("You hang out at the house for a while.")
            print()
            print("One day, you decide to go outside and explore the town. You find a group of people who are being attacked by The Old Man. When you try to help them, The Old Man dissappers into thin air")
            print()
            print("Scared, you run back to the safe house and tell the people inside about what you saw. They tell you that The Old Man is really not an old man, but a demon whos mission is to kill as much people as possible.")
            print()
            print("They tell you that he uses the house as a trap to lure people in and then he tortures them and then he kills them. They also tell you that he is always watching and that he can see everything.")
            print()
            print("You ask the group if they have any idea how to defeat The Old Man and they tell you that they have been trying to figure out a way to defeat him, but they have not been successful yet.")
            print()
            print("They ask you if they should explore the town more to find a way to win against The Old Man.")
            print()
            choice = get_input("Should they explore the town more to find a way to win against The Old Man? (Type 'yes' or 'no'): ")
        elif choice.lower() == "no":
            print()
            print("You decide not to explore the town more and you stay at a building nearby.")
            print()
            print("You eventually find some people who are willing to help you.")
            print()
            print("They give you a book that talks about the story of The Old Man, The Forest, and The Abandoned Town.")
            inventory.append("Book")
            print()
            print("Type 'Book' to read the book.")
            print()
            print("The people ask you if you want to go to their safe house")
            print()
            print("You say yes.")
            print()
            print("You follow them into their safe house.")
            print()
            print("You are now safe for now, but you are still scared and you don't know what to do next.")
            print()
            print("You suddenly see a human transforming into a demon.")
            print()
            print("Scared for your life, you run out of the safe house and you are now being chased by the demon.")
            print()
            print("You run back into The Old Mans House and you are now trapped in the house with no way out")
            print()
            print("The Old Man appears infront of you, he transform into a demon and he starts to chase you around the house and you are scared for your life and you don't know what to do, but you eventually find a way to escape the house, by finding a portal back to the real world.")
            print()
            print("You are now back in the forest and you see a city.")
            print()
            print("You can run into the city and tell people about what you just witnessed and went through.")
            print()
            print("You are unsure if you can trust these people.")
            choice = get_input("Do you want to run into the city and tell people about what you just witnessed and went through? (Type 'yes' or 'no'): ")
            if choice.lower() == "yes":
                print()
                print("You tell the people in the city about what you just witnessed and went through and they don't believe you and they think you are crazy and they call the authorities on you and you are arrested for being a crazy person.")
                print()
                print("ENDING REACHED: Not Believed By Society, But At Least You're Alive")
                exit()
            elif choice.lower() == "no":
                print()
                print("You decide not to tell anybody and stay quiet about what you just witnessed and went through and you are now living a normal life, but you are still scared and you don't know what to do.")
                print()
                print("ENDING REACHED: Survived The Villian Of The Left Path")
                exit()
            else:
                print("Invalid choice. Try again.")
                
        else:
            print("Invalid choice. Try again.")

        if choice.lower() == "yes":
            print()
            print("You and the group decide to explore the town more to find a way to win against The Old Man. You find a library and you find a book that talks about The Old Man and it says that The Old Man is vulnerable to fire and the Crucifix.")
            print()
            print("You and the group decide to find a way to make a fire and you find some matches in the house and you find some wood in the house and you make a fire.")
            print()
            print("You and the group found a Molotov in one of the abandoned stores and you use it to set a trap for The Old Man.")
            inventory.append("Molotov")
            print()
            print("Now all you need is to get The Crucifix.")
            print()
            print("You and the group decide to search the town for a church to find a crucifix. You find a church and you go inside and you find a crucifix and you take it.")
            inventory.append("Crucifix")
            print()
            print("You remember the rope in your inventory and you decide to set up a trap for The Old Man using the rope and the crucifix and the molotov.")
            print()
            print("You set up the trap and you think of a trap for The Old Man")
            print()
            print("A.) Collapsing Floor Trap")
            print("B.) Swinging Molotov Trap")
            print("C.) Chase Trap")

            choice = get_input("What trap do you want to set up for The Old Man? (You can only pick one.) ")

            if choice.lower() == "a":
                print()
                print("Materials: 1 Rope, 1 Crucifix, 1 Molotov")
                print("You have set up the Collapsing Floor Trap, do this at your own risk.")
                print()

                choice = get_input("Do you want to activate the trap? (Yes/No): ")

                if choice.lower() == "yes":
                    print()
                    print("You have just finished building the trap.")
                    print()
                    print("The next step is to lure The Old Man into the trap so you can activate it and kill him.")
                    print()
                    print("You and your friend Charlie goes to the town sqaure and you make some noise to attract The Old Man")
                    print()
                    print("The Old Man hears your noise and he starts to chase you and Charlie into the town square.")
                    print()
                    print("You succesfully lead him to the trap.")
                    print()
                    print("He falls into the trap and suddenly he flies out using his wings.")
                    print()
                    print("He is now flying and he is trying to attack you and Charlie, but Charlie uses the crucifix to weaken The Old Man, but it is too late now, The Old Man is too powerful")
                    print()
                    print("The Old Man targets you first, Charlie tries to protect you with his life, and The Old Man has killed Charlie.")
                    print()
                    print("You run, but The Old Man pins you to the ground. You remember the knife in your inventory")
                    print()
                    choice = get_input("Do you want to use the knife to try to escape The Old Man? (Yes/No): ")
                    if choice.lower() == "no":
                        print()
                        print("You decide not to use the knife and you are still pinned to the ground by The Old Man and he eventually kills you.")
                        print()
                        print("Game. Over.")
                        exit()
                    elif choice.lower() == "yes":
                        print()
                        print("You use the knife to try to escape The Old Man and you manage to cut yourself free and you run away from him and you hide in an abandoned building and you are safe for now.")
                        print("You have lost 1 Knife.")
                        inventory.remove("Knife")
                        print()
                        print("You have survived, but you lost 20 health points and you are now at 80 health points.")
                        print()
                        choice = get_input("Do you want to eat your Food in your inventory to restore your health? (Yes/No): ")
                        if choice.lower() == "yes":
                            print()
                            print("You eat the food and you restore your health back to 100 health points.")
                            inventory.remove("Food")
                            print()
                            print("You have used the food and it is now removed from your inventory.")
                            print()
                            print("Now, you need to find a way to defeat The Old Man using the materials you have left in you inventory.")
                            print()
                            print("All you can do is rebuild the trap.")
                            print()
                            print("You find a sword for the trap in the abandoned building.")
                            print("You can use the sword to cut of The Old Mans wings once he falls in the trap.")
                            inventory.append("Sword")
                            print()
                            choice = get_input("Do you want to rebuild the trap? (Yes/No): ")
                            if choice.lower() == "yes":
                                print()
                                print("You have just finished rebuilding the trap.")
                                print()
                                print("The next step is to lure The Old Man into the trap so you can activate it and kill him.")
                                if "Rope" in inventory:
                                    print("Rope used in trap setup.")
                                    inventory.remove("Rope")

                                if "Molotov" in inventory:
                                    print("Molotov ignites the trap!")
                                    inventory.remove("Molotov")

                                if "Crucifix" in inventory:
                                    print("Crucifix weakens The Old Man's presence.")
                                    inventory.remove("Crucifix")

                                print()
                                print("The Collapsing Floor Trap activates!")
                                print()
                                print("Now you wait.")
                                print("The Old Man is still hunting for you.")
                                print("You are hiding in the abandoned building and you are waiting for The Old Man.")
                                print()
                                print("You go to The Town Sqaure for for the last time and you make some noise.")
                                print()
                                print("The Old Man hears you and he starts to chase you into the town square.")
                                print()
                                print("You eventually lead him into the trap.")
                                print()
                                print("He falls into the trap and suddenly tries to fly out with his wings once again.")
                                print()
                                print("But you're ready for him this time, you use the sword to cut off his wings and he falls to the ground and dies.")
                                print()
                                print("Congratulations! You have defeated The Old Man.")
                            elif choice.lower() == "no":
                                print()
                                print("You decide not to rebuild the trap and you are still hiding in the abandoned building and you are scared and hungry.")
                                print()
                                print("You are uncertain if The Old Man is still hunting for you or if he has given up.")
                                print()
                                print("You accidently make some noise and The Old Man hears you and he eventually finds you")
                                print()
                                print("Then, he murders you.")
                                print()
                                print("Game. Over.")
                                exit()
                            choice = get_input("Do you want to search The Old Man's body for items? (Yes/No): ")
                            if choice.lower() == "yes":
                                print()
                                print("You search The Old Man and find the radio that he uses.")
                                inventory.append("Radio")
                                print()
                                print("But you also find out that Charlie died trying to save you.")
                                print()
                                print("You feel guilty for not being able to save Charlie.")
                                print()
                                print("You want to tell your group before you all leave the forest.")
                                print()
                                choice = get_input("Do you want to tell your group about Charlie's death? (Yes/No): ")
                                if choice.lower() == "yes":
                                    print()
                                choice = get_input("Do you want to call the authorities? (Type 'Call the authorities using the radio'): ")
                            elif choice.lower() == "no":
                                    print()
                                    print("You decide not to tell your group about Charlie's death.")
                                    print()
                                    print("You search The Old Man and find the radio that he uses.")
                                    inventory.append("Radio")
                                    print()
                                    print("But you also find out that Charlie died trying to save you.")
                                    print()
                                    print("You feel guilty for not being able to save Charlie.")
                                    print()
                                    choice = get_input("Do you want to call the authorities? (Type 'Call the authorities using the radio'): ")    



                            else:
                                print("You cancel the trap.")
                        else:
                            print()
                            print("You decide not to eat the food and you are now at 80 health points.")
                                
            elif choice.lower() == "b":
                print()
                print("You prepare for a Swinging Molotov Trap.")
                print("Description: You use the rope to create a swinging mechanism for the Molotov.")
                print("Materials used: 1 Molotov and 1 Rope")
                print()

                choice = get_input("Do you want to activate the trap? (Yes/No): ")

                if choice.lower() == "yes":
                    print()
                    print("The Molotov has started swinging")
                    print()
                    print("You have just finishd building the trap.")
                    print()
                    print("The next step is to lure The Old Man into the trap so he can be killed.")
                    print()
                    print("You setup a decoy staircase so he dies by the Molotov")
                    print()
                    print("You have found The Old Man.")
                    print()
                    print("He chases you into the staircase.")
                    print()
                    print("He sees the Molotov as hes chasing you.")
                    print()
                    print("He goes another way and dodges the Molotov!")
                    print()
                    print("Your plan has failed, The Old Man saw through your schemes.")
                    print()
                    print("He continues to chase you and you eventually die.")
                    print()
                    print("Game. Over.")
                    print()
                    print("ENDING REACHED: A Little Unlucky")
                    exit()

                if "Molotov" in inventory:
                    print("Molotov ignites the trap!")
                    inventory.remove("Molotov")
                    
                if "Rope" in inventory:
                    print("Rope used in trap setup.")
                    inventory.remove("Rope")
                    
                    

            elif choice.lower() == "c":
                print()
                print("You prepare for a Chase Trap.")
                print("Description: You use the rope to create a tripwire and the crucifix to ward off The Old Man's pursuit. When The Old Man chases you,")
                print("you lead him into the trap, and the tripwire causes him to stumble, give you a chance to burn him with the Molotov, succesfully killing him.")
                print()
                print("Materials used: 1 Rope, 1 Crucifix, 1 Molotov")
                print()

                choice = get_input("Do you want to activate the trap? (Yes/No): ")

                if choice.lower() == "yes":
                    print()
                    print("You have just finished building the trap.")
                    print()
                    print("The next step is to lure The Old Man into the trap so you can activate it and kill him.")
                    print()
                    print("You found The Old Man and you start to run and he starts to chase you, you lead him into the trap and you activate it and successfully kill him.")
                    print()
                    print("Congratulations! You have defeated The Old Man.")
                    print()
                    print("You and the group are now safe and you can finally escape the town and start a new life.")
                    print()
                    print("You found a phone in The Old Mans house!")
                    inventory.append("Phone")
                    print()
                    print("You use the phone to call for help and you are rescued by the authorities.")

                    choice = get_input("Do you want to call the authorities? (Type 'call the authorities'): ")

                    if "Rope" in inventory:
                        print("Rope used in trap setup.")
                        inventory.remove("Rope")

                    if "Molotov" in inventory:
                        print("Molotov ignites the trap!")
                        inventory.remove("Molotov")

                    if "Crucifix" in inventory:
                        print("Crucifix weakens The Old Man's presence.")
                        inventory.remove("Crucifix")

            elif choice.lower() == "no":
                print()
                print("You and the group decide not to explore the town.")
                print()
                print("You stay at the safe house and you are eventually attacked by The Old Man")
                print()
                print("You look behind you and you see The Old Man chasing you")
                print()
                print("You manage to escape him and run into deeper into the abandoned town, you are confused and you don't know where to go, but you eventually find a group of people.")
                print()
                print("It turns out that they are demons disguised as humans.")
                print()
                print("You fight with all your might but its pointless and you get killed by the demons.")
                print()
                print("Game. Over.")
                exit()
            else:
                print("Invalid trap choice.")
        elif choice.lower() == "no":
            print()
            print("You decide not to head to the safe house and continue to wander around the town, but you eventually get lost.")
            print()
            print("Your found the safe house, but you are too late and the people inside were attacked by The Old Man.")
            print()
            print("You look behind you and you see The Old Man standing there with a sinister smile on his face. You try to run, but he catches you and kills you.")
            print()
            print("Game. Over.")
            exit()
        break

    else:
        print()
        print("Wrong answer. Try again.")