def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        amount = int(input('How many ' + fruit + ' do you want? '))
        total_cost += price * amount
    print('Total cost: $' + str(total_cost))
    
if __name__ == "__main__":
    main()
    
