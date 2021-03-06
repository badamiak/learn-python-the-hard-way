from sys import exit

prompt_sign = "> "
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(prompt_sign)
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, lear to type a number.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
    
def bear_room():
    print("There's a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(prompt_sign)

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
def cthulhu_room():
    print("Here you see the great evil C'thulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you _flee_ for your life or eat you _head_?")

    choice = input(prompt_sign)

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why: str):
    print(f"{why} You died. Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your _right_ and _left_")
    print("Which one do you take?")

    choice = input(prompt_sign)

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starce.")

start()