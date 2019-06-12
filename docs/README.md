### Product Webpage
Once the application has started successfully and database has been seeded with test data, open up your favorite web browser and go to http://127.0.0.1:5000/casaone/product/6?userId=2.

Url path params and query params:
http://127.0.0.1:5000/casaone/product/{productId}?userId={userId}

Notes
- The database has been seeded with 10 products, 30 users and 200 random ratings.
- No ratings have been created for first 5 users (1-5) for testing 1st time rating creation.
- If the query param `userId` is passed, the web page will display user details as well (only name for now).


Screenshot
![Screenshot of Product Page](https://www.terminalbytes.com/wp-content/uploads/2019/06/Screenshot-2019-06-12-at-10.35.43-PM.jpg "Screenshot of Product Page")

You can rate the product on this webpage. All the rating details will be re-rendered via XHR calls in the following cases:
- User adds a rating.
- User removes a rating.
- User updates an existing rating.

------------
------------



### API Documentation
There are 3 APIs (contentType: application/json):
- /casaone/ratings/v1/add
- /casaone/ratings/v1/remove
- /casaone/ratings/v1/getDetailed


###### Add Rating API:
Checks if user exists and product exists, if yes then adds a rating for an existing product.
Endpoint: `/casaone/ratings/v1/add`

Request Structure
```json
    {
        	"userId": 22, // Mandatory
        	"rating": 5, // Mandatory
        	"productId": 50 // Mandatory
     }
```

Response Structure
Success

```json
    {
      "data": {
        "rating": {
          "productId": 9,
          "rating": 3,
          "userId": 8
        }
      },
      "status": "success"
    }
```

Failure
```json
    {
      "message": "Sorry something went wrong, please try again later.",
      "status": "failure"
    }
```
------------
------------

###### Remove Rating API:

Checks if a corresponding rating exists in db, if yes, soft deletes the entry.
Endpoint: `/casaone/ratings/v1/remove`

Request Structure

```json
    {
    	"userId": 19, // Mandatory
    	"productId": 1 // Mandatory
    }
```
Response Structure
Success

```json
    {
      "message": "Rating removed successfully.",
      "status": "success"
    }
```
Failure


```json
    {
      "message": "Error removing rating.",
      "status": "failure"
    }
```

------------
------------

###### Get Detailed Ratings Breakdown

Fetches all ratings and computes ratings breakup for diplaying on the frontend.
Optional field: `userId`, if passed in request, this API will also fetch user details and user rating for the product.

Endpoint: `/casaone/ratings/v1/getDetailed`

Request Structure

```json
    {
    	"productId": 1, //Mandatory
    	"userId": 19 //Optional
    }
```
Response Structure
Success

```json
    {
      "data": {
        "averageRating": 4.22,
        "loggedInUserRating": 4,
        "productDetails": {
          "id": 1,
          "name": "Awesome Desks"
        },
        "ratingsBreakdown": { // Percentages corresponding to ratings.
          "1": 4.3,
          "2": 17.4,
          "3": 0,
          "4": 8.7,
          "5": 69.6
        },
        "totalRatings": 23,
        "userDetails": {
          "id": 19,
          "name": "Isaac"
        }
      },
      "status": "success"
    }
```
Failure

```json
     {
          "message": "Sorry something went wrong, please try again later.",
          "status": "failure"
    }
```

------------
------------

