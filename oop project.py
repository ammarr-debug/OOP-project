from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    def __init__(self, name, person_id):
        self._name = name
        self.__id = person_id

    @property
    def name(self):
        return self._name

    @property
    def person_id(self):
        return self.__id

    @abstractmethod
    def display_role(self):
        pass


class Member(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.borrowed_books = []

    def display_role(self):
        return "Member"

    def borrow(self, book):
        if book.borrow_copy():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' successfully.")
            return True

        print(f"'{book.title}' is not available.")
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_copy()
            print(f"{self.name} returned '{book.title}' successfully.")
            return True

        print(f"{self.name} did not borrow '{book.title}'.")
        return False


class Librarian(Person):
    def display_role(self):
        return "Librarian"

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book):
        library.remove_book(book)


class Book(ABC):
    def __init__(self, title, author, genre, available_copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.__available_copies = available_copies

    @property
    def available_copies(self):
        return self.__available_copies

    def borrow_copy(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            return True
        return False

    def return_copy(self):
        self.__available_copies += 1

    @abstractmethod
    def get_book_type(self):
        pass


class PhysicalBook(Book):
    def __init__(self, title, author, genre, available_copies, shelf_number):
        super().__init__(title, author, genre, available_copies)
        self.shelf_number = shelf_number

    def get_book_type(self):
        return "Physical Book"


class EBook(Book):
    def __init__(self, title, author, genre, available_copies, file_size):
        super().__init__(title, author, genre, available_copies)
        self.file_size = file_size

    def get_book_type(self):
        return "E-Book"

    def download(self):
        print(f"Downloading '{self.title}'...")


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False


class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = LibraryCatalog()
        self.members = []
        self.librarians = []

    def add_book(self, book):
        self.catalog.add_book(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, book):
        if self.catalog.remove_book(book):
            print(f"'{book.title}' removed from the library.")
        else:
            print(f"'{book.title}' was not found.")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} added as a member.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"{member.name} removed from the library.")
        else:
            print("Member not found.")

    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        print(f"{librarian.name} added as a librarian.")

    def show_books(self, genre=None):
        print("\nLibrary Books:")

        found = False

        for book in self.catalog.books:
            if genre is None or book.genre == genre:
                status = "Available" if book.available_copies > 0 else "Unavailable"

                print(
                    f"{book.title} | "
                    f"{book.get_book_type()} | "
                    f"{book.genre} | "
                    f"{status} | "
                    f"Copies: {book.available_copies}"
                )

                found = True

        if not found:
            print("No matching books found.")


class Loan:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = date.today()

    def show_loan(self):
        print(
            f"{self.member.name} borrowed "
            f"'{self.book.title}' on {self.borrow_date}"
        )


def show_book_type(book):
    print(book.get_book_type())


library = Library("My Library")

member = Member("Ahmed", 101)
librarian = Librarian("Sara", 201)

physical_book = PhysicalBook(
    "Harry Potter",
    "J.K. Rowling",
    "Fantasy",
    2,
    "A12"
)

ebook = EBook(
    "Python Basics",
    "John Smith",
    "Programming",
    5,
    "10 MB"
)

library.add_member(member)
library.add_librarian(librarian)

librarian.add_book(library, physical_book)
librarian.add_book(library, ebook)

library.show_books()

print("\nBorrowing:")

if member.borrow(physical_book):
    loan = Loan(member, physical_book)
    loan.show_loan()

library.show_books()

print("\nTrying to borrow again:")

member.borrow(physical_book)

print("\nReturning:")

member.return_book(physical_book)

library.show_books()

print("\nBooks in Fantasy genre:")

library.show_books("Fantasy")

print("\nBooks in Programming genre:")

library.show_books("Programming")

print("\nPolymorphism:")

show_book_type(physical_book)
show_book_type(ebook)

print("\nMember Information:")

print("Name:", member.name)
print("ID:", member.person_id)

print("\nE-Book:")

ebook.download()