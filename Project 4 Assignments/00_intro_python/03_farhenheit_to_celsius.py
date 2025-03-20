from colorama import Fore, Style

def main():
    print(Fore.LIGHTMAGENTA_EX+"Welcome to the Fahrenheit to Celsius converter!"+Style.RESET_ALL)
    
    degrees_fahrenheit = input(Fore.CYAN+"Enter the temperature in Fahrenheit: "+Style.RESET_ALL)

    if degrees_fahrenheit.isnumeric():
        result = (float(degrees_fahrenheit) - 32) * 5.0/9.0
        print(Fore.YELLOW+f"The temperature in Celsius is {result}"+Style.RESET_ALL)
    else:
        print(Fore.RED+"Please enter a valid number"+Style.RESET_ALL)

if __name__ == '__main__':
    main()
    
    
