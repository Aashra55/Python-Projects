"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random 

DICE_NUMBERS = 6

def main():
    die_one = random.randint(1, DICE_NUMBERS)
    die_two = random.randint(1, DICE_NUMBERS)
    total = die_one + die_two
    
    print("Dice have {DICE_NUMBERS} sides")
    print(f"First die: {die_one}")
    print(f"Second die: {die_two}")
    print(f"Total of two dice: {total}")
    
if __name__ == "__main__":
    main()
    

