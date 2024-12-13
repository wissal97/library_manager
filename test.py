from library import Library, Book

def main():
    library = Library("City Library")
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

    library.add_book(book1)
    library.add_book(book2)

    print(f"Welcome to {library.name}!")
    print("List of Books:")
    for book_details in library.list_books():
        print(book_details)

    print("\nSearch for '1984':")
    for book in library.search_book("1984"):
        print(book)

if __name__ == "__main__":
    main()