# Utilisez une version appropriée de Python
FROM python:3.9

# Créez et définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY app.py models.py config.py requirements.txt /app/

# Installez les dépendances de votre application
RUN pip install -r requirements.txt

# Définissez la variable d'environnement pour le Flask en mode de production
ENV FLASK_ENV=production

# Exposez le port sur lequel votre application Flask s'exécute (par exemple, 5000)
EXPOSE 5000

# Commande pour créer la base de données SQLite et démarrer l'application Flask
CMD ["flask", "db", "upgrade", "&&", "flask", "run", "--host=0.0.0.0"]
