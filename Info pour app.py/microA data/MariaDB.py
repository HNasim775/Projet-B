import mysql.connector

# Remplacez ces valeurs par vos informations de connexion
db_config = {
    'host': 'localhost',
    'user': 'test',
    'password': 'stargatesg71'
}

# Nom de la base de données à créer
database_name = 'nom_de_la_base_de_données'

# Connexion au serveur MariaDB
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Création de la base de données
create_db_query = f"CREATE DATABASE {database_name};"
cursor.execute(create_db_query)

print(f"Base de données '{database_name}' créée avec succès.")

# Fermeture de la connexion
cursor.close()
conn.close()
