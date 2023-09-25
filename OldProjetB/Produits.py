import requests

class PrestaShopProductService:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_product(self, product_id):
        endpoint = f"{self.base_url}&id_product={product_id}"
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def create_product(self, product_data):
        endpoint = self.base_url
        response = requests.post(endpoint, data=product_data)
        
        if response.status_code == 200:
            print("Product created successfully!")
        else:
            print(f"Error: {response.status_code}")

    def update_product(self, product_id, product_data):
        endpoint = f"{self.base_url}&id_product={product_id}"
        response = requests.post(endpoint, data=product_data)
        
        if response.status_code == 200:
            print("Product updated successfully!")
        else:
            print(f"Error: {response.status_code}")

    def delete_product(self, product_id):
        endpoint = f"{self.base_url}&id_product={product_id}"
        response = requests.delete(endpoint)
        
        if response.status_code == 200:
            print("Product deleted successfully!")
        else:
            print(f"Error: {response.status_code}")

if __name__ == "__main__":
    base_url = "http://localhost:8080/Mahdokht/index.php?controller=AdminProducts&token=cad3892205fc6e2757379e6bf9640544&action=edit"
    api_key = "88W9JLXX7T5FFALZD743B5QFS7DSTQFY"
    
    product_service = PrestaShopProductService(base_url, api_key)
    
    # Example: Get product information
    product_id = 1
    product_info = product_service.get_product(product_id)
    if product_info:
        print("Product Information:")
        print(product_info)

    # Example: Create a new product
    new_product_data = {
        "name": "New Product",
        "price": "19.99",
        "description": "This is a new product",
    }
    product_service.create_product(new_product_data)

    # Example: Update product information
    product_id_to_update = 2
    updated_product_data = {
        "name": "Updated Product Name",
        "price": "24.99",
    }
    product_service.update_product(product_id_to_update, updated_product_data)

    # Example: Delete a product
    product_id_to_delete = 3
    product_service.delete_product(product_id_to_delete)
