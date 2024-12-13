class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, keyword):
        return [book.get_details() for book in self.books if keyword.lower() in book.title.lower()]

    def list_books(self):
        return [book.get_details() for book in self.books]