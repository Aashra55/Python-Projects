import random

def main():
    user = input("'r' for rock, 'p' for 'paper' and 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print ('tie')
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print ('You Won!')
    else :
        print ("You Lose!")

if __name__ == "__main__":
    main()
    


