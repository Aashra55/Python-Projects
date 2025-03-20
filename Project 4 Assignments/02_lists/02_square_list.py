def square_list(lst):
    return [i ** 2 for i in lst]

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared_list = square_list(lst)
    print(f"The squared list is {squared_list}")
    
if __name__ == "__main__":
    main()
    
    
