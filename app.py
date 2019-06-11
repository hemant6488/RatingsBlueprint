# app.py - a minimal flask api using flask_restful
import logging
from flask import Flask, render_template
from flask_restful import Api
from api.v1.urls import api_v1 as api_blueprint
from helpers.seedData import seedDatabase

app = Flask(__name__)
api = Api(app)
app.register_blueprint(api_blueprint, url_prefix='/ratings/v1')
logger = logging.getLogger("ratings")


def initializeLogging():
    logging.basicConfig(filename='logs/server.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)


@app.route('/')
def get():
    return render_template('template.html')


if __name__ == '__main__':
    initializeLogging()
    seedDatabase()
    app.run(debug=True, host='0.0.0.0')
