class Book:
    total_books = 0  # Class variable to keep track of total books
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return cls.total_books
        
obj1 = Book.increment_book_count()
obj2 = Book.increment_book_count()

print(obj1)
print(obj2)

