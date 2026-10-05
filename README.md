# Library Management System

## Project Overview

This project is a simple Library Management System developed using Python and Object-Oriented Programming (OOP).

The system allows a library to manage books, members, librarians, and borrowing operations. It demonstrates important OOP concepts such as abstraction, encapsulation, inheritance, polymorphism, method overriding, and Python-style method overloading.

## Features

- Add and remove books
- Add members
- Add librarians
- Support physical books and e-books
- Borrow books
- Return books
- Check book availability
- Track the number of available copies
- Record borrowing dates
- Display library books
- Download e-books
- Handle invalid borrowing and returning operations


## Main Classes

### `Person`

An abstract base class representing a general person in the library.

- Attributes: Name, Person ID
- Method: `display_role()`

### `Member`

Inherits from `Person`.

- Borrow books
- Return books
- Store borrowed books

### `Librarian`

Inherits from `Person`.

- Add books to the library
- Remove books from the library

### `Book`

An abstract base class representing a general book.

- Attributes: Title, Author, Genre, Available copies
- Handles borrowing and returning copies

### `PhysicalBook`

Inherits from `Book`.

- Contains a shelf number

### `EBook`

Inherits from `Book`.

- Contains a file size
- Provides a download function

### `LibraryCatalog`

Stores the books available in the library.

### `Library`

Represents the main library system.

- Manages books
- Manages members
- Manages librarians
- Manages the library catalog

### `Loan`

Represents a borrowing operation between a member and a book.

- Stores the member
- Stores the book
- Records the borrowing date

---

## OOP Concepts Demonstrated

### Abstraction

`Person` and `Book` are abstract classes using `ABC` and `@abstractmethod`.

They define common behavior that their child classes must implement.

### Encapsulation

Private and protected attributes are used to control access to data:

- `_name`
- `__id`
- `__available_copies`

Properties are used to provide controlled access to private data.

### Inheritance

The project uses several inheritance relationships:

- `Member` inherits from `Person`
- `Librarian` inherits from `Person`
- `PhysicalBook` inherits from `Book`
- `EBook` inherits from `Book`

### Method Overriding

Child classes provide their own implementations of inherited methods:

- `display_role()`
- `get_book_type()`

For example, `PhysicalBook` returns `"Physical Book"` while `EBook` returns `"E-Book"`.

### Polymorphism

The `show_book_type()` function accepts different types of books and calls the same method:

```python
show_book_type(physical_book)
show_book_type(ebook)
