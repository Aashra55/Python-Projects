"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random 

DICE_NUMBERS = 6

def roll_dice():
    die_one = random.randint(1, DICE_NUMBERS)
    die_two = random.randint(1, DICE_NUMBERS)
    
    total = die_one + die_two
        
    print(f"Total of two dice {total}")

def main():
    print("Welcome to the Dice Roll Simulator!")
    
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("Thanks for playing:)")
    
if __name__ == "__main__":
    main()
    
