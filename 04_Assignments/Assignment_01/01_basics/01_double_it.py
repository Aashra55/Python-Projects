def main():
    print('Square the number until 100')
    user_input = int(input("Enter any number less than 100: "))
    
    while user_input <= 100:
        print(user_input)
        user_input = user_input**2
    
if __name__ == "__main__":
    main()
    

