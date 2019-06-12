# Product Rating Management System with Flask

### Features
- Made very Light weight using [Flask](http://flask.pocoo.org/) and Python3.
- Scalable [MongoDb](https://www.mongodb.com/) integration.
- Cross platform deployment using [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
- Minimal setup and ready to be deployed in a matter of minutes.
- Automatic database seeding with test data.

### Setup
- [Install docker](https://docs.docker.com/install/) for the operating system.
- Build using docker-compose.


```bash
# This will download all the required images and build the container.
docker-compose build

# This command will start the container
docker-compose up

```
- Verify server has successfully started using `logs/server.log`.
- Go to `localhost:5000/casaone/product/{productId}?userId={userId}` for rating the product.

#### Further: [API Documentation](https://github.com/hemant6488/RatingsBlueprint/blob/master/docs/README.md)