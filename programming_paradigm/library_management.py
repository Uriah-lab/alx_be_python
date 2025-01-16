class Book:
    """
    A class representing a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out.
        :return: True if the book was successfully checked out, False if it was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Mark the book as available.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Check if the book is available.
        :return: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    A class representing a library that manages a collection of books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library's collection.
        :param book: An instance of the Book class.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        :param title: The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have successfully checked out '{title}'.")
                return
        print(f"'{title}' is not available or does not exist in the library.")

    def return_book(self, title):
        """
        Return a book by its title.
        :param title: The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You have successfully returned '{title}'.")
                return
        print(f"'{title}' is not currently checked out or does not exist in the library.")

    def list_available_books(self):
        """
        List all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
