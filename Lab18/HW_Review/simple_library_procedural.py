# Library Data Structure
library = []

def add_book(isbn, title, author, status='available', borrower=None):
    """ Add new book to the library.
        A book cannot be added if another book with the same ISBN already exists in the library.
    Args:
        isbn: The ISBN of the book
        title: The title of the book
        author: The author of the book
        status: The status of the book (available or borrowed)
        borrower: The name of the borrower

    Returns:
        None
    """
    # Check if a book with the same ISBN already exists in the library
    for book in library:
        if book['isbn'] == isbn:
            print(f"A book with ISBN {isbn} already exists in the library.")
            return

    # Add the new book to the library
    library.append({
        'isbn': isbn,
        'title': title,
        'author': author,
        'status': status,
        'borrower': borrower
    })
    print(f"{title} has been added to the library.")

def borrow_book(isbn, borrower):
    """ Borrow a book from the library.
    Args:
        isbn: The ISBN of the book
        borrower: The name of the borrower
    Returns:
        None
    """
    # Check if the book exists and is available in the library
    for book in library:
        if book['isbn'] == isbn and book['status'] == 'available':
            book['status'] = 'borrowed'
            book['borrower'] = borrower
            print(f"{book['title']} has been borrowed by {borrower}")
            return

    print(f"Book with ISBN: {isbn} is not available in the library.")

def return_book(isbn):
    """ Return a book to the library.

    Args:
        isbn: The ISBN of the book

    Returns:
        None
    """
    for book in library:
        if book['isbn'] == isbn and book['status'] == 'borrowed':
            book['status'] = 'available'
            book['borrower'] = None
            print(f"{book['title']} has been returned")
            return

    print(f"Book with ISBN: {isbn} did not exists or it was not borrowed")


def list_books():
    """ List all books in the library

    Args:
        None

    Returns:
        None
    """
    for book in library:
        print(f"ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}, Borrower: {book['borrower']}")

# Usage
add_book(1111,"Python Programming", "Jon Doe")
add_book(2222, "Learning AI", "Jane Smith")
borrow_book(1111, 'Ivan')
borrow_book(1111, 'Stoyan')
list_books()
