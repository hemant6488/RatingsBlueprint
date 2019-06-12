import logging

from services.DatabaseService import database

logger = logging.getLogger("ratings")


class ProductService:
    def __init__(self):
        self.database = database

    def getProductById(self, product_id):
        if not product_id:
            return None
        else:
            product_entry = self.database.getProduct(product_id)
            product = None
            if product_entry is not None:
                product = {'id': product_entry.product_id, 'name': product_entry.product_name}
            return product

