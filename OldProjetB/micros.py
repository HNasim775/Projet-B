import requests

# Paramètres de configuration
base_url = 'http://localhost:8080/Mahdokht/api'
api_key = '88W9JLXX7T5FFALZD743B5QFS7DSTQFY'

# Authentification
def authenticate():
        response = requests.get(f'{base_url}/employees', headers={'Authorization': f'Basic {api_key}'})
        if response.status_code == 200:
                print('Authentification réussie')
        else:
                print('Échec de l\'authentification')

# Création d'un produit
def create_product():
        payload = {
                'name': 'Nouveau produit',
                'price': '10.00'
                }
        response = requests.post(f'{base_url}/products', json=payload, headers={'Authorization': f'Basic {api_key}'})
        if response.status_code == 201:
                print('Produit créé avec succès')
        else:
                print('Échec de la création du produit')

# ... D'autres fonctions pour la création d'utilisateurs, la validation du panier, les commandes, etc.

if __name__ == '__main__':
        authenticate()
        create_product()
        # ... Appels aux autres fonctions
