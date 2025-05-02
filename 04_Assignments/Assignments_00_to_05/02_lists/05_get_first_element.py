def get_first_element(lst):
    """Returns the first element of the list"""
    print(f"The first element of the list is '{lst[0]}'")

def get_lst_from_user():
    """Returns a list of numbers from the user"""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst_from_user()
    get_first_element(lst)
    

if __name__ == "__main__":
    main()
    
