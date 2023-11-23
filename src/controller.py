from flask import Blueprint, jsonify, request
from src.model import books, Book

books_bp = Blueprint('books', __name__)

# Get all books
@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': [book.__dict__ for book in books]})

# Get a specific book by ID
@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book.id == book_id), None)
    if book:
        return jsonify({'book': book.__dict__})
    else:
        return jsonify({'message': 'Book not found'}), 404

# Create a new book
@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(id=len(books) + 1, title=data['title'], author=data['author'])
    books.append(new_book)
    return jsonify({'book': new_book.__dict__}), 201

# Update a book
@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book.id == book_id), None)
    if book:
        data = request.get_json()
        book.title = data['title']
        book.author = data['author']
        return jsonify({'book': book.__dict__})
    else:
        return jsonify({'message': 'Book not found'}), 404

# Delete a book
@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book.id != book_id]
    return jsonify({'message': 'Book deleted'})