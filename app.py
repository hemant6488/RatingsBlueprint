# app.py - a minimal flask api using flask_restful
import logging
from flask import Flask, render_template, request
from flask_restful import Api
from api.v1.urlMappings import api_v1 as api_blueprint
from config.Config import Config
from helpers.seedData import seedDatabase
from services.RatingService import RatingService

app = Flask(__name__)
api = Api(app)
app.register_blueprint(api_blueprint, url_prefix=Config.RATINGS_URL_PREFIX)
logger = logging.getLogger("ratings")

ratingService = RatingService()


def initializeLogging():
    logging.basicConfig(filename=Config.LOG_FILE, level=logging.DEBUG,
                        format=Config.LOG_PATTERN)
    logger.setLevel(logging.INFO)


@app.route('/product/<product_id>')
def getProductPage(product_id):
    rating_request = {'userId': request.args.get('userId'), 'productId': product_id}
    data = ratingService.getRatingsDetailsForProduct(rating_request)
    logger.info(data)
    return render_template('template.html', data=data)


if __name__ == '__main__':
    initializeLogging()
    seedDatabase()
    app.run(debug=True, host='0.0.0.0')
