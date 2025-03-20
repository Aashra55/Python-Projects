def get_list(lst):
    """Returns the list"""
    print(lst)

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
    get_list(lst)
    

if __name__ == "__main__":
    main()
    
