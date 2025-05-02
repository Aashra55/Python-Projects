class Bank:
    bank_name = "Bank of Python"  # Class variable
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  
        print(f"Bank name changed to: {cls.bank_name}")
        
bank1 = Bank()
bank2 = Bank()

# Before changing the class variable
print("Before changing the class variable:")
print(f"Bank 1 Name: {bank1.bank_name}")
print(f"Bank 2 Name: {bank2.bank_name}")
print("--------------------------------------------------")

# Changing the class variable 
Bank.change_bank_name("Bank of Code")

# After changing the class variable
print("After changing the class variable:")
print(f"Bank 1 Name: {bank1.bank_name}")
print(f"Bank 2 Name: {bank2.bank_name}")



