import requests
from config import PRESTASHOP_API_URL, PRESTASHOP_API_KEY
from app import cache

headers = {
        'Authorization': f'Basic {PRESTASHOP_API_KEY}'
}

def fetch_product(product_id):
        response = requests.get(f'{PRESTASHOP_API_URL}/Products/{product_id}', headers=headers)
        if response.status_code == 200:
                return response.json()
        return None


@cache.memoize(timeout=300)
def fetch_product(product_id):
# ... le reste de la fonction reste inchangé