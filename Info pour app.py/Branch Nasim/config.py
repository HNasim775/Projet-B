import os
from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
PRESTASHOP_API_URL = config('PRESTASHOP_API_URL')
PRESTASHOP_API_KEY = config('PRESTASHOP_API_KEY')

CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 300 # 5 minutes, ajustez selon vos besoins
CACHE_REDIS_URL = 'redis://localhost:6379/0'
