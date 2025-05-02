from colorama import Fore, Style

def main():
    print(Fore.MAGENTA+"Welcome to the Triangle Perimeter Calculator!"+Style.RESET_ALL)
    
    first_side = input(Fore.CYAN+"Enter the length of first side: "+Style.RESET_ALL)
    second_side = input(Fore.CYAN+"Enter the length of second side: "+Style.RESET_ALL)
    third_side = input(Fore.CYAN+"Enter the length of third side: "+Style.RESET_ALL)
    
    if first_side.isnumeric() and second_side.isnumeric() and third_side.isnumeric():
        result = int(first_side)+int(second_side)+int(third_side)
        
        print(Fore.GREEN+f"The perimeter of the triangle with sides {int(first_side)}, {int(second_side)} and {int(third_side)} is {result}"+Style.RESET_ALL)
    
if __name__ == '__main__':
    main()
    
    
