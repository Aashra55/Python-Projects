class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
    
result = Student("John Doe", 85)
print("Student Details:")
print("-------------------")
result.display()

