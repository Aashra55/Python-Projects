import random 

def main():
    total_numbers = 10
    while total_numbers > 0:
        print(random.randint(1,100))
        total_numbers = total_numbers - 1
        
if __name__ == "__main__":
    main()