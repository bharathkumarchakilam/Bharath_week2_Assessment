class Book:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return Book(self.title + " - " + other.title)

    def __str__(self):
        return self.title

book1 = Book("Harry Potter")
book2 = Book("The Hobbit")

series = book1 + book2
print(series)
