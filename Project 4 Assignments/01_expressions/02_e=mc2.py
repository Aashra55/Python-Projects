C = 299792458 # Speed of light in m/s

def main():
    print("Calculating the energy of an object")
    
    mass = float(input("Enter the mass of the object in kg: "))
    
    if mass:
        if mass < 0:
            print("Mass cannot be negative")
        elif mass == 0:
            print("Mass cannot be zero")
        else:
            energy = mass * C ** 2
            print(f"The energy of the object is {energy} Joules")
    else:
        print("Please enter a valid mass")
        
if __name__ == '__main__':
    main()
    
