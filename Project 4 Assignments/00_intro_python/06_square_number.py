from colorama import Fore, Style

def main():
    print(Fore.MAGENTA+"Let's square a number!"+Style.RESET_ALL)
    
    number = input(Fore.CYAN+"Enter a number: "+Style.RESET_ALL)
    
    if number.isnumeric():
        answer = int(number)**2
        print(Fore.GREEN+f"The square of {number} is {answer}"+Style.RESET_ALL)

if __name__ == '__main__':
    main()
    
