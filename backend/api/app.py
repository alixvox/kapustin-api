from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from api.views import user_blueprint, crud_blueprint, get_blueprint, filter_blueprint
from flask_socketio import SocketIO
from .models import db
from api.extensions import db, cache  # Import from extensions.py

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/alix/Documents/holberton/kapustin-api/backend/kapustin.db'
app.config['SECRET_KEY'] = 'cabbagesounds'
db.init_app(app)
api = Api(app)

app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)

socketio = SocketIO(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(crud_blueprint)
app.register_blueprint(get_blueprint)
app.register_blueprint(filter_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
