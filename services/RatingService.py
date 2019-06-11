import logging

from services.DatabaseService import DatabaseService

logger = logging.getLogger("ratings")


class RatingService:
    def __init__(self):
        self.database = DatabaseService()

    def addRating(self, user_id, rating, product_id):
        if self.productAndUserExist(user_id, product_id):
            logger.info("Adding rating for user: {}, product: {}, rating: {}".format(user_id, product_id, rating))
            saved_record = self.database.addRating(user_id, rating, product_id)
            return saved_record
        else:
            return None

    def productAndUserExist(self, user_id, product_id):
        product = self.database.getProduct(product_id)
        user = self.database.getUser(user_id)
        if product is not None and user is not None:
            return True
        else:
            return False
