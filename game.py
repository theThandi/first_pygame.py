import time
import random


def random_event():
    events = ["Happiness", "The realm", "Liam", "Purgatory"]
    random_event = random.choice(events)

    if random_event == "Happiness":
        print_pause(
            "The bundle wiggles in your arms and you see it is a little puppy. You have found pure happiness!"
        )
        win()
    elif random_event == "The realm":
        print_pause("You gingerly pick it up and open it...")
        print_pause("The bundle engulfs you and you are lost to the nether realm")
        lose()
    elif random_event == "Liam":
        print_pause(
            "Liam Neeson appears before you and takes you by the hand and leads you into darkness"
        )
        win()
    elif random_event == "Purgatory":
        print_pause(
            "Nothing happens. You stand holding the bundle in an eternal purgatory"
        )
        lose()


def print_pause(game_instructions):
    print(game_instructions)
    time.sleep(1)


def the_start():
    print_pause("Hello, welcome to the game.")
    print_pause(
        "Please follow the instructions carefully and make your decisions wisely,"
    )
    print_pause("it's a matter of preserving your life as you know it...")
    print_pause("or your soul finding it's way into another realm.")
    print_pause("The choice is yours\n")
    print_pause("...and remember who made the game - she loves an easter egg...\n")


def yellow():
    print_pause("The yellow glow increases as you walk towards it")
    print_pause("You arrive and see that it emanates from a rock about the size of you")

    while True:
        yellow_answer = (
            input("Do you think it's wise to touch it. 'yes' or 'no'? : ")
            .lower()
            .strip()
        )
        if yellow_answer == "yes":
            print_pause("You reach your hand forwards and touch the golden rock")
            print_pause("Your fingers start to disintegrate before you")
            print_pause(
                "You look up and see that you are surrounded by strange beings. They're moving towards you"
            )
            print_pause("They grab you as your material body turns to dust")
            lose()
            break
        elif yellow_answer == "no":
            print_pause("Your choices are your own")
            print_pause("We must all live with the outcomes of them")
            print_pause(
                "The rock glows before you and you find that you are standing in a beautiful garden"
            )
            print_pause("A troll is standing staring at you in absolute amazement")
            print_pause(
                "They shake their head in confusion but then ask you if you're hungry"
            )
            win()
            break
        else:
            print_pause("You must have some sort of opinion!")


def green():
    print_pause(
        "Mesmerised, you wander up to the light and find yourself mindlessly staring at it"
    )
    print_pause("You see a switch and reach out your hand")
    while True:
        green_answer = (
            input("Do you flick the switch 'up' or 'down'? : ").lower().strip()
        )
        if green_answer == "up":
            print_pause("You feel light and start to float upwards")
            print_pause(
                "You find that if you swing your head and shoulders you can turn and when you lean forwards you move"
            )
            win()
            break
        elif green_answer == "down":
            print_pause(
                "The ground beneath you disappears and you find yourself falling"
            )
            print_pause("You brace for an impact")
            print_pause("But there seems to be no end...")
            print_pause("You are stuck in an eternal downward projectury of purgatory")
            print_pause("At least you're not hungry...")
            lose()
            break
        else:
            print_pause("You can't do nothing! Pick one!")


def red():
    print_pause(
        "The red flicker grows as you move towards it, turning into what looks like an emergency strobe"
    )
    print_pause("Underneath the flashing emergency light you see a dark bundle")
    print_pause("Do you pick up the mysterious bundle or do you run away?")
    while True:
        red_answer = input("Please choose 'pick up' or 'run' : ").lower().strip()
        if red_answer == "pick up":
            random_event()
            break
        elif red_answer == "run":
            print_pause(
                "You are weak and foolish! You have lost your chance for true happiness!"
            )
            print_pause(
                "You look up and see that you are surrounded by strange beings. They're moving towards you"
            )
            print_pause("They grab you as your material body turns to dust")
            lose()
        else:
            print_pause("Thems not the rules.")


def win():
    print_pause("Graduconlations homie! You did a good job! So proud omg!")
    print_pause("Would you like to play again?")
    while True:
        replay_answer = input("yes/no : ").lower().strip()
        if replay_answer == "yes":
            choice_one()
        elif replay_answer == "no":
            break
        else:
            print_pause("but like...do you wanna play again?")


def lose():
    print_pause("You lost. Sucker.")
    print_pause("Would you like to play again?")
    while True:
        replay_answer = input("yes/no : ").lower().strip()
        if replay_answer == "yes":
            choice_one()
        elif replay_answer == "no":
            break
        else:
            print_pause("Accept defeat, bitch, but like...do you wanna play again?")


def snoek():
    print_pause("Aaah, my dear Snoek, I believe your horse is very ill?")
    print_pause("Your Momma Snoek has something for you to make it all better")
    print_pause("Return to the game now and play without fretting")


def patate():
    print_pause("Look at you!!!")
    print_pause("You're soooooOoooooOOOOooo STINKY!")
    print_pause("Eew! Go play the game!")


def choice_one():
    print_pause("You're standing in the dark and have no idea where you are.")
    print_pause(
        "You start to panic but realise that won't help, so you calm yourself down by taking some deep breaths"
    )
    print_pause(
        "Now that you are calm, you turn in a circle and realise that you can see three sources of light surrounding you."
    )
    print_pause("A yellow glow, a green blinking hexagon, and a red flicker")

    while True:
        first_answer = (
            input(
                "Please choose if you want to walk towards 'yellow', 'green' or 'red'? : "
            )
            .lower()
            .strip()
        )
        if first_answer == "yellow":
            yellow()
            break
        elif first_answer == "green":
            green()
            break
        elif first_answer == "red":
            red()
            break
        elif first_answer == "snoek":
            snoek()
        elif first_answer == "patate":
            patate()
        else:
            print_pause("Them's not the rules, puddin'. Make a choice?")


# Start the game
the_start()
choice_one()
