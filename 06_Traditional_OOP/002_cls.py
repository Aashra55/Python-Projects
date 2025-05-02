class Counter:
    
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def showCount(cls):
        print(f"Total object created {cls.count}")
        
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.showCount()

