# book_class.py

class Book:
    """A class representing a book with title, author, and year."""
    
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
