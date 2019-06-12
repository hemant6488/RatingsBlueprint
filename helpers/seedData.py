import logging
import random

from core.model.Product import Product
from core.model.Rating import Rating
from core.model.User import User
import numpy as np

logger = logging.getLogger("ratings")

good_words = ["Awesome", "Amazing", "Good", "Perfect", "Fabulous", "Genuine", "Handsome", "Compassionate", "Beautiful",
              "Great", "Fantastic", "Marvelous"]
furniture = ["Sofas", "Tables", "Chairs", "Beds", "Desks", "Mattresses", "Dressers", "Ottomans", "Dining Tables",
             "Dining Chairs", "Sectional Sofas", "TV Stands", "Bookcases", "Futons", "Bunk Beds", "Coffee Tables",
             "Stools", "End Tables", "Mini-Bars", "Mini Kitchen Islands", "Mudroom Lockers", "Storage Benches",
             "Toy Organizers", "Hall Trees"]
names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin",
         "Charlotte", "Elijah", "Mia", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Evelyn", "Alexander", "Abigail",
         "Ethan", "Emily", "Jacob", "Elizabeth", "Michael", "Mila", "Daniel", "Ella", "Henry", "Avery", "Jackson",
         "Sofia", "Sebastian", "Camila", "Aiden", "Aria", "Matthew", "Scarlett", "Samuel", "Victoria", "David",
         "Madison", "Joseph", "Luna", "Carter", "Grace", "Owen", "Chloe", "Wyatt", "Penelope", "John", "Layla", "Jack",
         "Riley", "Luke", "Zoey", "Jayden", "Nora", "Dylan", "Lily", "Grayson", "Eleanor", "Levi", "Hannah", "Isaac",
         "Lillian", "Gabriel", "Addison", "Julian", "Aubrey", "Mateo", "Ellie", "Anthony", "Stella", "Jaxon", "Natalie",
         "Lincoln", "Zoe"]


def seedDatabase():
    if User.objects.count() == 0:
        logger.info("Seeding users data")
        for i in range(1, 30):
            User(
                user_id=i,
                user_name=random.choice(names)
            ).save()

    if Product.objects.count() == 0:
        logger.info("Seeding products data.")
        for i in range(1, 10):
            Product(
                product_id=i,
                product_name=random.choice(good_words) + " " + random.choice(furniture)
            ).save()

    rating_count = Rating.objects.count()
    if rating_count < 20:
        logger.info("Seeding random ratings.")
        while rating_count < 200:
            for i in range(1, 10):
                try:
                    Rating(
                        product_id=i,
                        rating=np.random.choice([1, 2, 3, 4, 5], p=[0.10, 0.10, 0.10, 0.15, 0.55]),
                        user_id=random.randint(10, 30)
                    ).save()
                    rating_count += 1
                except Exception:
                    pass
