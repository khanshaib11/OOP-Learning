
class Library:
    def __init__(self,name):
        self.name = name 
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)   
    
    def description(self):
        return [f"{book.title} by {book.author}" for book in self.books]
            
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author 



library  = Library("The New York public library" )
book1 = Book("Garry Potter...", "J.K Rowling")   
book2 = Book("The Hobbit..." , "J. R. R. Tolkein")
book3 = Book("The Color of Magic"," Terry Pratchet") 

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.description():
    print(book)