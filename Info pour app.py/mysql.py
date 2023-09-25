from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'votre_utilisateur_mysql'
app.config['MYSQL_DATABASE_PASSWORD'] = 'votre_mot_de_passe_mysql'
app.config['MYSQL_DATABASE_DB'] = 'nom_de_votre_base_de_donnees'
app.config['MYSQL_DATABASE_PORT'] = 3306  # Port par défaut pour MySQL

# Initialisation de l'extension MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    # Exemple de requête à la base de données
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM ma_table")
    data = cursor.fetchall()
    cursor.close()
    
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)
