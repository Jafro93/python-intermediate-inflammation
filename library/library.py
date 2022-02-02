class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books
    
    def __len__(self):
        return len(self.books)

    def __getitem__(self, i):
        return self.books[i]

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def by_author(self, author):
        matches = []
        for book in self.books:
            if book.author == author:
                matches.append(book)
        
        if not matches:
            raise KeyError("Author does not exist")
        
        return matches

    @property
    def titles(self):
        return [book.title for book in self.books]

    @property
    def authors(self):
        return list(set([book.author for book in self.books]))

    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)
        
        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)


library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

print(library.titles)
print(library.authors)
