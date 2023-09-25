import os
from app import limiter
from app import app, limiter
from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db'); SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configurations pour connexion l'API de PrestaShop
PRESTASHOP_API_URL = 'http://localhost:8080/api'
PRESTASHOP_API_KEY = 'FSZPDXM9FKCV1N5YD8XYP19RZ6DMPT16'

# app = Flask(__name__)
# MYSQL_HOST = app.config['MYSQL_HOST']
# MYSQL_USER = app.config['MYSQL_USER ']
# MYSQL_PASSWORD = app.config['MYSQL_PASSWORD']
# MYSQL_DB = app.config['MYSQL_DB']
# mysql = MySQL(app)

# ... autres configurations

CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 300 # 5 minutes, ajustez selon vos besoins
CACHE_REDIS_URL = 'redis://localhost:6379/0'


@app.route('/add_to_cart', methods=['POST'])
@limiter.limit("5 per minute") # Adaptez selon vos besoins
def add_to_cart():
# ... code de la route
   return 'todo'