def add_many_numbers(list_of_numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    sum_of_numbers = 0
    for number in list_of_numbers:
        sum_of_numbers += number
        
    return sum_of_numbers

def main():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    add_many_numbers(list_of_numbers) 
    print(f"The sum of the numbers in the list is {add_many_numbers(list_of_numbers)}")
    
if __name__ == "__main__":
    main()
    

