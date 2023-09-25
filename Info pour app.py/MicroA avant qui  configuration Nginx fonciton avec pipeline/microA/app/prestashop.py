import requests
from my_config import PRESTASHOP_API_URL, PRESTASHOP_API_KEY
import base64
import xmltodict

presta_key = base64.b64encode(
    PRESTASHOP_API_KEY.encode("utf-8")).decode("utf-8")
headers = {
    'Authorization': f'basic {presta_key}'
}
def fetch_product(product_id):
    response = requests.get(f'{PRESTASHOP_API_URL}/products/{product_id}', headers=headers)
    if response.status_code == 200:
        try:
            product_data_xml = response.content.decode("utf-8")
            product_data_dict = xmltodict.parse(product_data_xml)
            return product_data_dict
        except Exception as e:
            return {"error": f"Failed to parse XML: {e}"}
    return {"error": "Failed to fetch product data from PrestaShop"}

def fetch_product_qty(product_id):
    response = requests.get(f'{PRESTASHOP_API_URL}/stock_availables/{product_id}', headers=headers)
    if response.status_code == 200:
        try:
            product_data_xml = response.content.decode("utf-8")
            product_data_dict = xmltodict.parse(product_data_xml)
            return product_data_dict
        except Exception as e:
            return {"error": f"Failed to parse XML: {e}"}
    return {"error": "Failed to fetch product quantity from PrestaShop"}
