import math

def main ():
    print("Calculating the hypotenuse of a right triangle")
    
    a = float(input("Enter the length of side AB: "))
    b = float(input("Enter the length of side AC: "))
    
    if a and b:
        if a < 0 or b < 0:
            print("Sides cannot be negative")
        elif a == 0 or b == 0:
            print("Sides cannot be zero")
        else : 
            c = math.sqrt(a ** 2 + b ** 2)
            print(f"The length of side BC is {c}")
    else:
        print("Please enter a valid length")
        
if __name__ == '__main__':
    main()
    
