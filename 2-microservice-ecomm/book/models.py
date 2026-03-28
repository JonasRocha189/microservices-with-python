from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
  db.app = app
  db.init_app(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True, nullable=False)
  slug = db.Column(db.String(255), unique=True, nullable=False)
  price = db.Column(db.Float, nullable=False)
  image = db.Column(db.String(255))

  def __repr__(self):
    f'<Book {self.id}: {self.name}>'

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'slug': self.slug,
      'price': self.price,
      'image': self.image
    }