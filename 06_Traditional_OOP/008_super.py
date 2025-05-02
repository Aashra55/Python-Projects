class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def subject(self, subject):
        print(f"Teacher of {subject}")
        
Teacher('Alice').subject('Mathematics')

