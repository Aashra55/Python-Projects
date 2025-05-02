PETURKSBOUIPO_VOTING_AGE = 16
STANLAU_VOTING_AGE = 25
MAYENGUA_VOTING_AGE = 48

def main():
    user_age = int(input("How old are you? "))
    
    if user_age >= PETURKSBOUIPO_VOTING_AGE:
        print(f"You are eligible to vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}.")
    else:
        print(f"You are not eligible to vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_VOTING_AGE}.")
        
    if user_age >= STANLAU_VOTING_AGE:
        print(f"You are eligible to vote in Stanlau where the voting age is {STANLAU_VOTING_AGE}.")
    else:
        print(f"You are not eligible to vote in Stanlau where the voting age is {STANLAU_VOTING_AGE}.")    
    
    if user_age >= MAYENGUA_VOTING_AGE:
        print(f"You are eligible to vote in Mayengua where the voting age is {MAYENGUA_VOTING_AGE}.")
    else:
        print(f"You are not eligible to vote in Mayengua where the voting age is {MAYENGUA_VOTING_AGE}.")    
    
    if user_age < 16 :
        print("You are not eligible to vote in any country.")
        
if __name__ == "__main__":
    main()
    
