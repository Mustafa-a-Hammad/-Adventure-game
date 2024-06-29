import time
import random


def print_pause(message):
    print(message)
    time.sleep(2.5)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been curse the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("To your left is a huge tree.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def choose_action():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 3 to go to the huge tree.")
    while True:
        choice = input("What would you like to do? "
                       "(Please enter 1, 2, or 3): ")
        if choice == "1":
            house()
            break
        elif choice == "2":
            cave()
            break
        elif choice == "3":
            tree()
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def house():
    print_pause("You approach the door of the house.")
    print_pause("It creaks open, and you step inside"
                " to find a cozy living room.")
    print_pause("However, the house is empty. You head back to the field.")
    choose_action()


def fight(enemy):
    print_pause("You do your best...")
    if random.choice([True, False]):
        print_pause(f"You have defeated the {enemy}!")
        print_pause("Congratulations, you have won the game!")
    else:
        print_pause(f"The {enemy} has defeated you. You have lost the game.")
    play_again()


def cave():
    enemies = ["troll", "dragon", "wicked fairie", "pirate", "goblin"]
    enemy = random.choice(enemies)
    print_pause("You peer cautiously into the cave.")
    print_pause("It is very dark and spooky, but you step inside anyway. "
                f"Suddenly, you see a {enemy}!")
    print_pause(f"The {enemy} attacks you!")
    while True:
        choice = input("Would you like to (1) fight or (2) run away? ")
        if choice == "1":
            fight(enemy)
            break
        elif choice == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.")
            choose_action()
            break
        else:
            print("Invalid input. Please enter 1 or 2.")


def tree():
    print_pause("You approach the huge tree. "
                "Its branches are thick and the leaves form a dense canopy.")
    print_pause("As you get closer, "
                "you notice a rope hanging from one of the branches.")
    print_pause("Do you want to (1) climb the tree or "
                "(2) head back to the field?")
    while True:
        choice = input("Please enter 1 or 2: ")
        if choice == "1":
            climb_tree()
            break
        elif choice == "2":
            print_pause("You head back to the field.")
            choose_action()
            break
        else:
            print("Invalid input. Please enter 1 or 2.")


def climb_tree():
    print_pause("You start climbing the tree using the rope.")
    print_pause("As you reach the top, you find a Treasure map!")
    print_pause("You take the Treasure map and climb back down.")
    print_pause("Congratulations, "
                "you have found a hidden treasure!")
    print_pause("This treasure helped get rid of the curse evil fairie")
    print_pause("you won the game!")
    play_again()


def play_again():
    while True:
        try:
            choice = input("Would you like to play again?"
                           "(y/n): ").strip().lower()
            if choice == "y":
                print_pause("Excellent! Restarting the game ...")
                main()
                break
            elif choice == "n":
                print_pause("Thanks for playing! See you next time.")
                break
            else:
                print("Invalid input. Please enter y or n.")
        except UnicodeDecodeError:
            print("Invalid input encoding. Please try again.")


def main():
    intro()
    choose_action()


if __name__ == "__main__":
    main()
