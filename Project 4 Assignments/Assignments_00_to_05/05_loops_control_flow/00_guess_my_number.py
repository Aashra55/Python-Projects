import random

def main():
    secret_number = random.randint(1,99)
    
    guess = int(input("Enter the number you guess: "))
    
    while guess != secret_number:
        if guess < secret_number :
            print("Your Guess is too low!")
        else:
            print("Your guess is too high")
        print()
        guess = int(input("Enter a new guess: "))
    print("Congrats! You guess the right number.")
    
if __name__ == "__main__":
    main()
    
