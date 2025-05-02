from colorama import Fore, Style

print(Fore.MAGENTA+"Enter the values you want to sum up!"+Style.RESET_ALL)

first_number = input(Fore.CYAN+"Enter first number: "+Style.RESET_ALL)
second_number = input(Fore.CYAN+"Enter second number: "+Style.RESET_ALL)


if first_number.isnumeric() and second_number.isnumeric():
    result = int(first_number)+int(second_number)

    print(Fore.GREEN+f"The sum of {int(first_number)} and {int(second_number)} is {result}"+Style.RESET_ALL)
else:
    print(Fore.RED+"Please enter valid numbers"+Style.RESET_ALL)



