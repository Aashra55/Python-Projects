def main():
    print("How old are they?")
    
    Anton : int = 21
    Beth : int = Anton + 6 # Beth is 6 years older than Anton
    Chen : int = Beth + 20 # Chen is 20 years older than Beth
    Drew : int = Chen + Anton # Drew is as old as Chen's age plus Anton's age
    Ethan : int = Chen # Ethan is the same age as Chen
    
    print(f"Anton is {str(Anton)} years old.")
    print(f"Beth is {str(Beth)} years old.")
    print(f"Chen is {str(Chen)} years old.")
    print(f"Drew is {str(Drew)} years old.")
    print(f"Ethan is {str(Ethan)} years old.")

if __name__ == '__main__':
    main()
    
