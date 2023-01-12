class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.books = []

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.id}, {self.username}, {self.books}"
