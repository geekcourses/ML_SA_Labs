# simple library system


class Book:
    def __init__(self, isbn, title, author, status='available', borrower=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.status = status
        self.borrower = borrower

    def __str__(self):
        return f"""
Book with ISBN: {self.isbn},
    Title: {self.title},
    Author: {self.author},
    Status: {self.status},
    Borrower: {self.borrower}
        """

    def borrow(self, borrower):
        if self.status == 'available':
            self.status = 'borrowed'
            self.borrower = borrower
            return True
        else:
            return False

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            return True
        else:
            return False


class Library:
    def __init__(self) -> None:
        self.books = []

    def __str__(self) -> str:
        return str(self.books)

    def add_book(self, new_book):
        for book in self.books:
            if book.isbn == new_book.isbn:
                print(f"Warning: Book with ISBN {isbn} already exists.")
                return

        self.books.append(new_book)
        print(f"{new_book.title} has been added to the library.")

    def borrow_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrow(borrower):
                    print(f"{book.title} has been borrowed by {borrower}.")
                else:
                    print(f"Book with ISBN: {isbn} is not available in the library.")
                    return
            else:
                print(f"Book with ISBN: {isbn} does not exist in the library.")

    def return_book(self, isbn):
        """ Return a book to the library.

        Args:
            isbn: The ISBN of the book

        Returns:
            None
        """
        for book in self.books:
            if book.isbn == isbn:
                if book.return_book():
                    print(f"{book.title} has been returned to the library.")
                    return
                else:
                    print(f"Book with ISBN: {isbn} was not borrowed.")
                    return
            else:
                print(f"Book with ISBN: {isbn} does not exist in the library.")

    def list_books(self):
        for book in self.books:
            print(book)

### now we test the functions
if __name__=="__main__":
    library = Library()
    print( library )

    book1 =  Book(1111,"Moby-Dick", "Herman Melville")
    book2 =  Book(2222,"The Master & Margharita", "Mikhail Bulgakov")


    library.add_book(book1)
    library.add_book(book2)

    library.borrow_book(1111, 'Victoria')
    library.return_book(2222)

    # add_new_book(2222,"The Master & Margharita", "Mikhail Bulgakov")
    # borrow_book(1111, 'Victoria')
    # borrow_book(1111, 'Geroge')
    library.list_books()