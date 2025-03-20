def main():
    print("Calculate the division with remainder")
    
    dividend = int(input("Please Enter the number to be divided: "))
    divisor = int(input("Please Enter the number to divided by: "))
    
    if dividend and divisor and divisor != 0:
        quotient = dividend // divisor
        remainder = dividend % divisor
        print(f"The result of the division is {quotient} with remainder {remainder}")
    else:
        print("Please give a valid input!")
        
if __name__ == "__main__":
    main()
    
