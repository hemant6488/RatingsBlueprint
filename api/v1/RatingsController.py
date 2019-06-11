import time

import logging
from flask import jsonify, request

from config.Constants import Constants
from helpers.ApiHelper import validateAddRatingsRequest, getFailureResponse, getRecordedRating
from services.RatingService import RatingService

logger = logging.getLogger("ratings")
ratingService = RatingService()


def addRating():
    """
    Adds a product rating or updates the existing rating if a corresponding NON-DELETED rating entry already exists.

    Requires: userId, rating, productId in POST request.

    Note (not implemented for the scope of the project):
    - User Authentication
    - Check if the user has actually rented the furniture in the past that he/she is trying to rate.

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
    """
    Calculates the ratings breakdown for the given product.
    :return: Schema:
    {
        "productDetails":{},
        "averageRating":int,
        "totalRatings":int,
        "loggedInUserRating":int,
        "ratingsBreakdown":{
            //percentages of 5 stars, 4 stars and so on.
            "5": 60,
            "4": 20,
            "3": 5,
        }
    }
    """


def removeRating():
    pass
