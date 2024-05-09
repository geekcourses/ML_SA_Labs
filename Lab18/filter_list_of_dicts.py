library  = [
    {
        'ISBN': 1,
        'Title': 'title1',
        'Author': 'author1',
        'Status': 'Available',
        'Borrower': None
    },
    {
        'ISBN': 2,
        'Title': 'title2',
        'Author': 'author2',
        'Status': 'Available',
        'Borrower': None
    },
    {
        'ISBN': 3,
        'Title': 'title3',
        'Author': 'author3',
        'Status': 'Available',
        'Borrower': None
    },
]

print('\nvariant1 - with for loop')
for book in library:
    if book['ISBN'] == 2:
        print(book)

print('\nvariant2 - with list comrehension')
filtered_books = [book for book in library if book['ISBN'] == 2][0]
print( filtered_books )

print('\nvariant3 - with filter')

def filter_by_isbn(book):
    return book['ISBN'] == 2

# filtered_books = list(filter( filter_by_isbn, library))
filtered_books = list(filter( lambda book:book['ISBN'] == 2, library))
print( filtered_books )
