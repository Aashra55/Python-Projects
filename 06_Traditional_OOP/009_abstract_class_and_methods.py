from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def area(self):
        return 20 * 10

area = Rectangle().area()
print(area)

