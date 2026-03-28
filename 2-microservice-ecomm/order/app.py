from flask import Flask, request, jsonify
from routes import order_blueprint
from models import init_app, db
from flask_migrate import Migrate

import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_dir = os.path.join(basedir, "database")
os.makedirs(db_dir, exist_ok=True)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mmJglNo4D3qw0Wqs2Q88zA'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_dir, "order.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(order_blueprint)

init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, host=5003)