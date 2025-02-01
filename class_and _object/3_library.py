#creating the book class
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display_details(self):
        print(f"\n Title of the book: {self.title}")
        print(f"Author of the book: {self.author}")
        print(f"isbn of the book: {self.isbn}")

#creating the library management system        
class Library:
    #creating the list for books
    def __init__(self):
        self.books=[]
    
    #Adding the book to library collection    
    def add_books(self):
        title=input("enter the title of the book: ")
        author=input("enter the author of the book: ")
        isbn=input("enter the isbn of the book: ")
        new_book=Book(title,author,isbn)
        self.books.append(new_book)
        print(f"book {title} successfully added")
    
    #removing the book from library collection    
    def remove_books(self):
        isbn=input("enter the isbn of the book to remove: ")
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"book {book.title} successfully removed")
                return 
        print("book not found")
     
    #displaying the library collection   
    def display_books(self):
        if not self.books:
            print("no books in the library!")
        else:
            print("\n Library collection:")
            for book in self.books:
                book.display_details()
 
#object for Library class               
library=Library()

#main funtion for input 
def main():
    while True:
        action = input("\nEnter 'a' to add a book, 'r' to remove a book, 'd' to display books, 'q' to quit: ")
        if action == 'a':
            library.add_books()
        elif action == 'r':
            library.remove_books()
        elif action == 'd':
            library.display_books()
        elif action == 'q':
            print("Exiting Library System.")
            break
        else:
            print("Invalid input. Please try again.")
            
#running the main            
main()
        
        
        
    