from kirana_store.models.product_model import add_product, update_product, delete_product, get_all_products

def add_new_product(name, stock, price):
    add_product(name, stock, price)

def update_existing_product(product_id, name, stock, price):
    update_product(product_id, name, stock, price)

def remove_product(product_id):
    delete_product(product_id)

def fetch_products():
    return get_all_products()
