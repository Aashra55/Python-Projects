MIN_LENGTH = 3

def shorten_list(lst):
    """Shortens the list to the minimum length"""
    while len(lst) > MIN_LENGTH:
        last_elem = lst.pop()
        print(last_elem)
    print(f"The shortened list is {lst}")
    
        
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
    shorten_list(lst)
    

if __name__ == "__main__":
    main()
    
