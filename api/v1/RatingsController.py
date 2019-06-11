import time

import logging
from flask import jsonify, request
from flask_restful import abort

from config.Constants import Constants
from helpers.ApiHelper import validateAddRatingsRequest, getFailureResponse, getRecordedRating
from services.RatingService import RatingService

logger = logging.getLogger("ratings")
ratingService = RatingService()

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


def addRating():
    """
    Adds a product rating or updates the existing rating if a corresponding NON-DELETED rating entry already exists.

    Requires: userId, rating, productId in POST request.
    Note: User Authentication not implemented for the scope of the project.

    :return: HTTP Response containing corresponding rating entry from database.
    """
    request_dict = request.get_json()
    if validateAddRatingsRequest(request_dict):
        record = ratingService.addRating(request_dict['userId'], request_dict['rating'], request_dict['productId'])
        if record is not None:
            response = {Constants.STATUS_KEY: Constants.STATUS_SUCCESS, Constants.DATA_KEY: getRecordedRating(record)}
            return jsonify(response)
        else:
            return jsonify(getFailureResponse())
    else:
        return jsonify(getFailureResponse(400)), 400


def getRatingsBreakdown():
    request.get_json()
    pass


def removeRating():
    pass
