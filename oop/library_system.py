# Base class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the parent class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the parent class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        self.books.append(book)  # Add a book to the collection

    def list_books(self):
        for book in self.books:
            print(book)  # Use the __str__ method of each book type
