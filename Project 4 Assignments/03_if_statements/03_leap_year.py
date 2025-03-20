def main():
    year = int(input("Please input a year: "))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
if __name__ == "__main__":
    main()
    
# The output of this program should look like this:
# Please input a year: 2000
# 2000 is a leap year.
# Please input a year: 1900
# 1900 is not a leap year.

