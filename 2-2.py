import random

dice = random.randint(1, 6)
prize_dice = random.randint(1, 6)

while True:
    if dice != 6:
        print(dice)
        break
    elif dice == 6:
        print("you win you can re-roll the dice again" )
        print("prize dice")
        break
