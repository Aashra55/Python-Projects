def get_numebrs():
    phonebook = {}
    name = input("Enter name: ")
    while name != "":
        number = input("Enter number: ")
        phonebook[name] = number
        name = input("Enter name: ")
    return phonebook

def print_numbers(phonebook):
    for name in phonebook:
        print(str(name) + '->' + phonebook[name])
        
def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        elif name not in phonebook:
            print(name + 'is not in phonebook')
        else:
            print(name + ':' + phonebook[name])
            
def main():
    numbers = get_numebrs()
    print_numbers(numbers)
    lookup_numbers(numbers)
    
if __name__ == "__main__":
    main()
    


