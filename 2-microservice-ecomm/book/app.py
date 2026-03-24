from flask import Flask
from routes import book_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '0Di-n1GgnMMa8OpdG3shdQ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(book_blueprint)

if __name__ == '__main__':
  app.run(debug=True, port=5502)