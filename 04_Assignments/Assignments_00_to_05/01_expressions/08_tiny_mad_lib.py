SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    print("Welcome to the Tiny Mad Libs!")
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    
    print(SENTENCE_START+f"{adjective} {noun} {verb}!") 
    
if __name__ == "__main__":
    main()
    

