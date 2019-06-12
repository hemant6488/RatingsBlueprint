import logging
import os

from mongoengine import *

from core.model.Product import Product
from core.model.Rating import Rating
from core.model.User import User

logger = logging.getLogger("ratings")


class DatabaseService:
    def __init__(self):
        try:
            self.connection = connect("casaone", host=os.environ['DB_PORT_27017_TCP_ADDR'], port=27017)
            # self.connection = connect("casaone", host='127.0.0.1', port=27017)
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
    def removeRating(user_id, product_id):
        try:
            dropped = Rating.objects(user_id=user_id, product_id=product_id, deleted=False).update_one(
                set__deleted=True)
            return dropped
        except Exception:
            logger.exception("Error occurred while saving record")
            return None

    @staticmethod
    def getProduct(product_id):
        try:
            product = Product.objects(product_id=product_id).first()
            return product
        except Exception:
            logger.exception("Error while fetching product: {}".format(product_id))
            return None

    @staticmethod
    def getUser(user_id):
        try:
            user = User.objects(user_id=user_id).first()
            return user
        except Exception:
            logger.exception("Error while fetching user: {}".format(user_id))
            return None

    @staticmethod
    def getAverageRating(product_id):
        try:
            average_rating = Rating.objects(product_id=product_id, deleted=False).average('rating')
            return round(average_rating, 2)
        except Exception:
            logger.exception("Error while fetching average rating for product: {}".format(product_id))
            return None

    @staticmethod
    def getRatingsCount(product_id):
        try:
            ratings_count = Rating.objects(product_id=product_id, deleted=False).count()
            return ratings_count
        except Exception:
            logger.exception("Error while fetching ratings count for product: {}".format(product_id))
            return None

    @staticmethod
    def getProductRatingForUser(product_id, user_id):
        try:
            user_rating = Rating.objects(product_id=product_id, user_id=user_id, deleted=False).first()
            return user_rating.rating
        except Exception:
            logger.exception("Error while fetching ratings count: {}".format(product_id))
            return None

    @staticmethod
    def getRatings(product_id):
        try:
            ratings = []
            for entry in Rating.objects(product_id=product_id, deleted=False):
                ratings.append(entry.rating)
            return ratings
        except Exception:
            logger.exception("Error while fetching ratings: {}".format(product_id))
            return None


# Initializing a singleton instance
database = DatabaseService()
