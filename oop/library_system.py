class Book:
    def __init__(self, title: str, author: str):
        """
        Initialize a Book instance.

        :param title: The title of the book.
        :param author: The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the Book instance.

        :return: A string in the format "Book: (title) by (author)".
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook instance.

        :param title: The title of the eBook.
        :param author: The author of the eBook.
        :param file_size: The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the EBook instance.

        :return: A string in the format "EBook: (title) by (author), File Size: (file_size)KB".
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook instance.

        :param title: The title of the print book.
        :param author: The author of the print book.
        :param page_count: The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the PrintBook instance.

        :return: A string in the format "PrintBook: (title) by (author), Page Count: (page_count)".
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Add a book to the library.

        :param book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library, printing their details.
        """
        for book in self.books:
            print(book)
