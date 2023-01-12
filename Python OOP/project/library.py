from project.user import User


class Library:
    def __init__(self):
        self.user_records = []      # [users objects]
        self.books_available = {}   # {author : [available books for this author]}
        self.rented_books = {}      # {username: {book name: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            if book_name not in self.rented_books[user.username]:
                self.rented_books[user.username][book_name] = 0
            self.rented_books[user.username][book_name] += days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, data in self.rented_books.items():
            if book_name in data:
                days_to_return_by_other_user = data[book_name]
                return f"""The book "{book_name}" is already rented and will be available in {days_to_return_by_other_user} days!"""

    def return_book(self, author, book_name, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
