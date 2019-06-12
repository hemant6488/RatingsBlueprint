from flask import Blueprint
from api.v1.RatingsController import addRating, getRatingsBreakdown, removeRating
from config.Endpoints import Endpoints

api_v1 = Blueprint('api.v1', __name__)

api_v1.add_url_rule(Endpoints.ADD_RATING, view_func=addRating, methods=['POST'])
api_v1.add_url_rule(Endpoints.RATINGS_BREAKDOWN, view_func=getRatingsBreakdown, methods=['POST'])
api_v1.add_url_rule(Endpoints.REMOVE_RATING, view_func=removeRating, methods=['POST'])
