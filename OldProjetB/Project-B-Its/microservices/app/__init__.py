from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# ... autres initialisations
cache = Cache(app)

# ... autres initialisations
limiter = Limiter(app, key_func=get_remote_address)

#.....Configuration Flask-CORS
CORS(app)