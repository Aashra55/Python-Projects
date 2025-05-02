class Employee:
    def __init__(self):
        self.name = "Joseph"
        self._salary = 50000
        self.__ssn = "123-456-789"
        
employee = Employee()
print(employee.name)  # Public variable
"""To acess the public variable is simple, i had not to do anything special."""
print(employee._salary)  # Protected variable
"""To access the protected variable, i had to use a single underscore before the variable name."""
print(employee._Employee__ssn)  # Private variable (name mangling)
"""To access the private variable, i had to use a double underscore before the variable name
as well as the class name with single underscore before the variable name."""

