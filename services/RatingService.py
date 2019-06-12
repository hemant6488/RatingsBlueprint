import logging
from collections import Counter

from services.DatabaseService import database
from services.ProductService import ProductService
from services.UserService import UserService

logger = logging.getLogger("ratings")


class RatingService:
    def __init__(self):
        self.database = database
        self.product = ProductService()
        self.user = UserService()

    def addRating(self, user_id, rating, product_id):
        if self.productAndUserExist(user_id, product_id):
            logger.info("Adding rating for user: {}, product: {}, rating: {}".format(user_id, product_id, rating))
            saved_record = self.database.addRating(user_id, rating, product_id)
            return saved_record
        else:
            logger.error("Product/User does not exist.")
            return None

    def productAndUserExist(self, user_id, product_id):
        product = self.database.getProduct(product_id)
        user = self.database.getUser(user_id)
        if product is not None and user is not None:
            return True
        else:
            return False

    def getRatingsDetailsForProduct(self, params):
        response = {}
        product_id = params['productId']
        response['averageRating'] = self.database.getAverageRating(product_id)
        response['totalRatings'] = self.database.getRatingsCount(product_id)
        response['productDetails'] = self.product.getProductById(product_id)
        if 'userId' in params:
            response['userDetails'] = self.user.getUserById(params['userId'])
            response['loggedInUserRating'] = self.database.getProductRatingForUser(product_id, params['userId'])

        if response['loggedInUserRating'] is None:
            response['loggedInUserRating'] = 0

        ratings = self.database.getRatings(product_id)
        response['ratingsBreakdown'] = self.computeRatingsBreakdown(ratings)
        return response

    def removeRating(self, params):
        return self.database.removeRating(params['userId'], params['productId'])

    @staticmethod
    def computeRatingsBreakdown(ratings):
        c = Counter(ratings)
        ratings_percentages = dict((i, round(c[i] / len(ratings) * 100, 1)) for i in ratings)
        for i in range(1, 5):
            if i not in ratings_percentages:
                ratings_percentages[i] = 0
        return ratings_percentages
