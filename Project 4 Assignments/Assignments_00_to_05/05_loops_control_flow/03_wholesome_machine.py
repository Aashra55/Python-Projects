AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following Affirmation: "+AFFIRMATION)
    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("That's not the Affirmation!")
        print("Please type the following Affirmation: "+AFFIRMATION)
        user_feedback = input()
    print("That's right :)")


if __name__ == "__main__":
    main()
    
        
    