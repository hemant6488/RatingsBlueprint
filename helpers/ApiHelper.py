import logging

from config.Constants import Constants

logger = logging.getLogger("ratings")


def validateAddRatingsRequest(request):
    valid = True
    if not request or 'userId' not in request or 'rating' not in request or 'productId' not in request:
        valid = False
    if valid and not 0 < request['rating'] < 6:
        valid = False
    return valid


def validateRatingsBreakdownRequest(request):
    if not request or 'productId' not in request:
        return False
    else:
        return True


def validateRemoveRatingRequest(request):
    if not request or 'productId' not in request or 'userId' not in request:
        return False
    else:
        return True


def getFailureResponse(response_code=None):
    if response_code == 400:
        return {Constants.STATUS_KEY: Constants.STATUS_FAILURE, Constants.MESSAGE_KEY: Constants.REQUEST_ERROR}
    else:
        return {Constants.STATUS_KEY: Constants.STATUS_FAILURE, Constants.MESSAGE_KEY: Constants.GENERIC_ERROR}


def getRecordedRating(record):
    data = {
        'rating': {
            'productId': record.product_id,
            'rating': record.rating,
            'userId': record.user_id,
        }
    }
    return data
