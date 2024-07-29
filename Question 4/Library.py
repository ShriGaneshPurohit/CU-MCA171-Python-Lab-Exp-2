# LibraryManager.py

import Data

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year
        }

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def get_book_details(self, isbn):
        return self.books.get(isbn)

    def search_books(self, search_term, search_by="title"):
        return [details for isbn, details in self.books.items() if search_term.lower() in details[search_by].lower()]

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, **details):
        if isbn in self.books:
            self.books[isbn].update(details)

    def check_availability(self, isbn):
        return isbn in self.books

if __name__ == "__main__":
    library = LibraryManager()
    books_data = Data.books

    for book in books_data:
        library.add_book(**book)

    # Demonstrate functionality
    print("Listing all books:")
    print(library.list_books())

    isbn_to_check = "9780134743356"
    print(f"\nDetails of book with ISBN {isbn_to_check}:")
    print(library.get_book_details(isbn_to_check))

    search_term = "Operating Systems"
    print(f"\nBooks with title containing '{search_term}':")
    print(library.search_books(search_term))

    print("\nChecking availability of ISBN 9780134743356:")
    print(library.check_availability("9780134743356"))

    print("\nUpdating the year of ISBN 9780134743356:")
    library.update_book("9780134743356", year=2023)
    print(library.get_book_details("9780134743356"))

    print("\nRemoving book with ISBN 9780134743356:")
    library.remove_book("9780134743356")
    print(library.check_availability("9780134743356"))