import time

import logging
from flask import jsonify

logger = logging.getLogger(__name__)


def get_api():
    """
     GET Demo API
     ---
    responses:
      200:
        description: Returns GET demo api response
    """
    logger.debug("in demo api")
    time.sleep(2)
    return jsonify({'message': "demo get api"}), 200


def post_api():
    """
     POST Demo API
     ---
    responses:
      200:
        description: Returns POST demo api response
    """
    return jsonify({'message': "demo post api"}), 200