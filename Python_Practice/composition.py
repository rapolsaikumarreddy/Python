class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"book {self.name}"

book = Book("harry porter")
book2 = Book("Python 101")
shelf = Bookshelf(book, book2)
print(shelf)