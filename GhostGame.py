# Ghost Game
from random import randint

def ghost_game():
    print("ghost game")
    feeling_brave = True
    score = 0

    while feeling_brave:
        ghost_door1 = randint(1, 3)
        # ghost_door2 = randint(1, 3)
        print("three doors ahead...")
        print("a ghost is behind one")
        print("Which door do you want to open")
        door = input("1, 2 or 3")
        door_num = int(door)
        # if door_num == ghost_door1 or door_num == ghost_door2:
        if door_num == ghost_door1:
            print("ghost")
            feeling_brave = False
        else:
            print("no ghost!")
            score = score+1

    print("run away")
    print("game over! you scored", score)


if __name__ == '__main__':
    ghost_game()
