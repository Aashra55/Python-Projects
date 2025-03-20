INCHES_PER_FOOT = 12

def main():
    print("Converting feet to inches")
    
    feet = float(input("Enter the number of feet: "))
    
    if feet:
        inches = feet * INCHES_PER_FOOT
        print(f"{feet} feet is equal to {inches} inches")
    else:
        print("Please enter a valid number of feet") 
        
if __name__ == '__main__':
    main()
    
