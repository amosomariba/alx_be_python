# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and author, and set it as not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out
