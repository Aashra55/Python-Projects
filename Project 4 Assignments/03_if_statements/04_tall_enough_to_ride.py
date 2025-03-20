MIN_HEIGHT = 50

def main():
    user_height = int(input("How tall are you? "))
    
    if user_height >= MIN_HEIGHT:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride.")
        
if __name__ == "__main__":
    main()
    
