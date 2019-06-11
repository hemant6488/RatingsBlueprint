from flask import Blueprint
from api.v1.RatingsController import post_api, addRating

api_v1 = Blueprint('api.v1', __name__)

api_v1.add_url_rule('/add', view_func=addRating, methods=['POST'])
api_v1.add_url_rule('/demo-api/', view_func=post_api, methods=['POST'])