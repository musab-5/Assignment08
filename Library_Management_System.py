class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.books_borrowed = []

class Library:
    def __init__(self):
        self.books = []  # List to store book objects
        self.patrons = []  # List to store patron objects

    def add_book(self, book):
        self.books.append(book)  # Add a book object to the library's list of books

    def add_patron(self, patron):
        self.patrons.append(patron)  # Add a patron object to the library's list of patrons

    def borrow_book(self, patron, book):
        if book.available_copies > 0:
            patron.books_borrowed.append(book)
            book.available_copies -= 1
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print("No available copies of the book.")

    def return_book(self, patron, book):
        if book in patron.books_borrowed:
            patron.books_borrowed.remove(book)
            book.available_copies += 1
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("The patron did not borrow this book.")

    def display_all_books(self):
        for book in self.books:
            print(f"'{book.title}' by {book.author}")

    def display_all_patrons(self):
        for patron in self.patrons:
            print(f"{patron.name} (Patron ID: {patron.patron_id})")

# Example usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("Book 1", "Author 1", "ISBN123", 5)
    book2 = Book("Book 2", "Author 2", "ISBN456", 3)

    patron1 = Patron("Patron 1", 1)
    patron2 = Patron("Patron 2", 2)

    library.add_book(book1)
    library.add_book(book2)

    library.add_patron(patron1)
    library.add_patron(patron2)

    library.borrow_book(patron1, book1)
    library.borrow_book(patron2, book1)
    library.return_book(patron1, book1)

    library.display_all_books()
    library.display_all_patrons()
