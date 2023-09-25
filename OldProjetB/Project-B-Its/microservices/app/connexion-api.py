import requests
import pymysql

# Informations de la base de données MariaDB
MYSQL_HOST = 'localhost'
MYSQL_USER = 'test'
MYSQL_PASSWORD = 'stargatesg71'
MYSQL_DATABASE = 'prestashop'

# Informations de l'API PrestaShop
PRESTASHOP_API_URL = 'http://localhost:8080/api'
PRESTASHOP_API_KEY = 'FSZPDXM9FKCV1N5YD8XYP19RZ6DMPT16'

# Connexion à la base de données
db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DATABASE)

# Création d'un curseur
cursor = db.cursor()

# Exemple : récupération des produits depuis la base de données MariaDB
query = "SELECT * FROM produits"
cursor.execute(query)
products = cursor.fetchall()

# Fermeture du curseur et de la connexion à la base de données
cursor.close()
db.close()

# Envoi des données à l'API PrestaShop
for product in products:
    data = {
        "name": product[1],  # Supposons que le nom du produit se trouve à l'index 1
        "price": product[2]  # Supposons que le prix du produit se trouve à l'index 2
        # ... Autres données à envoyer
    }
    headers = {
        "Authorization": "Bearer " + PRESTASHOP_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(PRESTASHOP_API_URL + '/products', json=data, headers=headers)
    if response.status_code == 201:
        print(f"Produit {product[1]} envoyé avec succès.")
    else:
        print(f"Erreur lors de l'envoi du produit {product[1]} - Code {response.status_code}: {response.text}")
