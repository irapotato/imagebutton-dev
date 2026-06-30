init python:
    import random

    def roll_dice():
        global dice_total
        dice_total = random.randint(1,6)


label start:

    show screen dice_button

    "roll the dice"
    

    "output is [dice_total]"


    return
