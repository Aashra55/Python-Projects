def get_num_list():
    
    number_list = []
    num : str = str(input("Enter a number or press Enter to exit:"))
    
    while num != "":
        number_list.append(num)
        num : str = str(input("Enter a number or press Enter to exit:"))
        
    return number_list

def count_nums(num_list):
    
    num_dict = {}
    
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
            
    return num_dict

def main():
    
    number_list = get_num_list()
    num_dict = count_nums(number_list)
    
    for key, value in num_dict.items():
        print(f"{key} appears {value} time(s).")
        
if __name__ == "__main__":
    main()
    
    
