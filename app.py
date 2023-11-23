from flask import Flask
from src.controller import books_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(books_bp)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)