import logging
import os

from mongoengine import *

from core.model.Product import Product
from core.model.Rating import Rating

logger = logging.getLogger("ratings")


class DatabaseService:
    def __init__(self):
        try:
            self.connection = connect("ratings", host=os.environ['DB_PORT_27017_TCP_ADDR'], port=27017)
        except MongoEngineConnectionError:
            logger.exception("Fatal Error. Connection to the database can not be established.")

    @staticmethod
    def addRating(user_id, rating, product_id):
        try:
            record = Rating.objects(user_id=user_id, product_id=product_id, deleted=False)
            record.update_one(set__rating=rating, upsert=True)
            return record.first()
        except Exception:
            logger.exception("Error occurred while saving record")
            return None

    @staticmethod
    def getProduct(product_id):
        try:
            product = Product.objects(product_id=product_id).first()
            return product
        except Exception:
            logger.error("Error while fetching product: {}".format(product_id))
