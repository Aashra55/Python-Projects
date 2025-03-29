from colorama import Fore, Style

def main():
    print(Fore.MAGENTA+"Welcome to the Agreement Bot!"+Style.RESET_ALL)
    
    question = input(Fore.CYAN+"What's your favorite animal? "+Style.RESET_ALL)
    
    if question :
        print(Fore.YELLOW+f"My favorite animal is also {question}!"+Style.RESET_ALL)
    else:
        print(Fore.RED+"You didn't enter anything!"+Style.RESET_ALL)

if __name__ == '__main__':
    main()
    
