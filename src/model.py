class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

# Sample data (in-memory storage)
books = [
    Book(id=1, title="Book 1", author="Author 1"),
    Book(id=2, title="Book 2", author="Author 2")
]
