import os  # Importation du module os pour accéder aux variables d'environnement

# Classe de configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Clé secrète pour Flask
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'  # URI de la base de données
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')  # Clé secrète pour JWT
