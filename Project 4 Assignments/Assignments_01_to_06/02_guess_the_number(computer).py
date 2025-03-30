import random 

def main():
    number = random.randint(1,10)
    guessed_number  = 0
    while guessed_number != number:
        guessed_number = int(input("Guess the number between 1 and 10: "))
        if guessed_number < number:
            print("Your guess is too low. Try again: ")
        elif guessed_number > number : 
            print("Your guess is too high. Try again: ")
    print("Congrats! You guessed the right number!")
    
if __name__ == "__main__":
    main()


