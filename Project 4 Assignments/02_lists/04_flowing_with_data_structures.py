def add_three_copies(lst, data):
    for i in range(3):
        lst.append(data)
        
def main():
    data = input("Enter a data: ")
    my_list = []
    print(f"Before adding three copies of {data} to the list: {my_list}")
    add_three_copies(my_list, data)
    print(f"After adding three copies of {data} to the list: {my_list}")
    
if __name__ == "__main__":
    main()
    
