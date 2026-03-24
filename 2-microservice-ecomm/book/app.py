from flask import Flask
from routes import book_blueprint
from models import db, Book, init_app
from flask_migrate import Migrate

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '0Di-n1GgnMMa8OpdG3shdQ'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "database", "book.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(book_blueprint)
init_app(app)

migrate = Migrate(app, db)
if __name__ == '__main__':
  app.run(debug=True, port=5502)