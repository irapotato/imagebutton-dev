init python:
    import random

    # python function to roll a d6 (random number between 1 and 6)
    def roll_dice():
        global dice_total
        dice_total = random.randint(1,6)

label start:

    show screen dice_button
    "roll the dice"
    #modal imagebutton for dice roll
    #modal ib remains modal after press.
    #if button is modal and required to advance, need to hide button after use

    hide screen dice_button
    "output is [dice_total]"

    return