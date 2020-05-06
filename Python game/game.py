import time
import random


def game():
    c = 0

    def choice():
        while(True):
            print(" ")
            print("Enter 1 to knock on the door of the house.")
            time.sleep(1)
            print("Enter 2 to peer into the cave.")
            time.sleep(1)
            print("What would you like to do?")
            time.sleep(1)
            print("(Please enter 1 or 2.)")
            time.sleep(1)
            a = (input())
            if(a == '1' or a == '2'):
                return a
                break
    enemies = ["troll", "wicked fairie", "pirate"]
    enemy = random.choice(enemies)

    def start():
        print("You find yourself standing in an open field, filled with grass "
              "and", "yellow wildflowers.")
        time.sleep(1)
        print("Rumor has it that a " + enemy + " is somewhere around here, and"
              " has", "been terrifying the nearby village.")
        time.sleep(1)
        print("In front of you is a house.")
        time.sleep(1)
        print("To your right is a dark cave.")
        time.sleep(1)
        print("In your hand you hold your trusty (but not effective) dagger.")
        time.sleep(1)

    def cave():
        print(" ")
        print("You peer cautiously into the cave.")
        time.sleep(1)
        print("It turns out to be only a very small cave.")
        time.sleep(1)
        print("Your eye catches a glint of metal behind a rock.")
        time.sleep(1)
        print("You have found the magical Sword of Ogoroth!")
        time.sleep(1)
        print("You discard your silly old dagger and take the sword with you.")
        time.sleep(1)
        print("You walk back out to the field.")
        time.sleep(1)

    def emptycave():
        print(" ")
        print("You peer cautiously into the cave.")
        time.sleep(1)
        print("You've been here before, and gotten all the good stuff. "
              "It's just an empty cave now.")
        time.sleep(1)
        print("You walk back out to the field.")
        time.sleep(1)

    def door():
        print(" ")
        print("You approach the door of the house.")
        time.sleep(1)
        print("You are about to knock when the door opens and out steps a "
              + enemy + " .")
        time.sleep(1)
        print("Eep! This is the " + enemy + " house!")
        time.sleep(1)
        print("The " + enemy + " attacks you!")
        time.sleep(1)

    def escape():
        print(" ")
        print("You run back into the field. Luckily, "
              "you don't seem to have been followed.")
        time.sleep(1)

    def victory():
        print(" ")
        print("As the " + enemy + " moves to attack, you unsheath your sword.")
        time.sleep(1)
        print("The Sword of Ogoroth shines brightly in your hand as you "
              "brace yourself for the attack.")
        time.sleep(1)
        print("But the " + enemy + " takes one look at your shiny new toy "
              "and runs away!")
        time.sleep(1)
        print("You have rid the town of the "
              + enemy + " . You are victorious!")

    def fightchoice():
        print(" ")
        print("Would you like to (1) fight or (2) run away?")
        fch = (input())
        return fch

    def defeat():
        print(" ")
        print("You do your best...")
        time.sleep(1)
        print("but your dagger is no match for the " + enemy)
        time.sleep(1)
        print("You have been defeated!")
        time.sleep(1)

    start()
    a = choice()
    while(True):
        if(a == '1'):
            door()
            fch = fightchoice()
            if(fch == '1' and c == 0):
                defeat()
                exitpoint()
                break
            elif(fch == '2'):
                escape()
                a = choice()
            elif(fch == '1' and c != 0):
                victory()
                exitpoint()
                break
        if(a == '2'):
            if(c == 0):
                cave()
                c = c + 1
                a = choice()
            else:
                emptycave()
                a = choice()


def exitpoint():
    print("Would you like to play again? (y/n)")
    e = input()
    if(e == 'n'):
        print(" ")
        print("See you soon!")
        time.sleep(1.5)
        exit()
    elif(e == 'y'):
        print(" ")
        print("Excellent choice!!, Restarting the game")
        time.sleep(1.5)
        game()
    else:
        exitpoint()


game()
