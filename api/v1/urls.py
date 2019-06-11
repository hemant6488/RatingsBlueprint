from flask import Blueprint
from api.v1.RatingsController import get_api, post_api

api_v1 = Blueprint('api.v1', __name__)

api_v1.add_url_rule('/demo-api/', view_func=get_api, methods=['GET'])
api_v1.add_url_rule('/demo-api/', view_func=post_api, methods=['POST'])