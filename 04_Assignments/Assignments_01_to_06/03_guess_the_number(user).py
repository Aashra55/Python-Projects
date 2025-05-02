import random

def main(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c" :
        guess = random.randint(low, high)
        feedback = input(f"Is my guess '{guess}' too high[h], too low[L] or correct[C]? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("Yay, I guessed correct!")
    
if __name__ == "__main__":
    main(10)

    

