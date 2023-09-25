from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

cache = Cache(app)
limiter = Limiter(get_remote_address, app=app,  default_limits=["200 per day", "50 per hour"])

#.....Configuration Flask-CORS
#CORS(app)
