class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Book title: {self.title}\n" \
               f"Book author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_title):
        try:
            self.books.remove([book for book in self.books if book.title == book_title][0])
        except IndexError:
            return 'Book not found'

    def find_book(self, book_title):
        try:
            return [book for book in self.books if book.title == book_title][0]
        except IndexError:
            return 'Book not found'


book_1 = Book('Peter Pan', 'Haho')
book_2 = Book('Harry Potter', 'JK Rowling')
book_3 = Book('Pod igoto', 'Ivan Vazov')
book_4 = Book('Lord of the rings', 'Bai Huy')

library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
library.add_book(book_2)

print(library.find_book('Harry Potters'))
print(library.find_book('Harry Potter'))
print(library.find_book('Peter Pan'))
