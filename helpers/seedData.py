import logging
import random

from core.model.Product import Product
from core.model.User import User
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
         "Lincoln", "Zoe", "Joshua", "Leah", "Christopher", "Hazel", "Andrew", "Violet", "Theodore", "Aurora", "Caleb",
         "Savannah", "Ryan", "Audrey", "Asher", "Brooklyn", "Nathan", "Bella", "Thomas", "Claire", "Leo", "Skylar",
         "Isaiah", "Lucy", "Charles", "Paisley", "Josiah", "Everly", "Hudson", "Anna", "Christian", "Caroline",
         "Hunter", "Nova", "Connor", "Genesis", "Eli", "Emilia", "Ezra", "Kennedy", "Aaron", "Samantha", "Landon",
         "Maya", "Adrian", "Willow", "Jonathan", "Kinsley", "Nolan", "Naomi", "Jeremiah", "Aaliyah", "Easton", "Elena",
         "Elias", "Sarah", "Colton", "Ariana", "Cameron", "Allison", "Carson", "Gabriella", "Robert", "Alice", "Angel",
         "Madelyn", "Maverick", "Cora", "Nicholas", "Ruby", "Dominic", "Eva", "Jaxson", "Serenity", "Greyson", "Autumn",
         "Adam", "Adeline", "Ian", "Hailey", "Austin", "Gianna", "Santiago", "Valentina", "Jordan", "Isla", "Cooper",
         "Eliana", "Brayden", "Quinn", "Roman", "Nevaeh", "Evan", "Ivy", "Ezekiel", "Sadie", "Xavier", "Piper", "Jose",
         "Lydia", "Jace", "Alexa", "Jameson", "Josephine", "Leonardo", "Emery", "Bryson", "Julia", "Axel", "Delilah",
         "Everett", "Arianna", "Parker", "Vivian", "Kayden", "Kaylee", "Miles", "Sophie", "Sawyer", "Brielle", "Jason",
         "Madeline"]


def seedDatabase():
    if User.objects.count() == 0:
        logger.info("Seeding users data.")
        for i in range(1, 100):
            User(
                user_id=i,
                user_name=random.choice(names)
            ).save()

    if Product.objects.count() == 0:
        logger.info("Seeding products data.")
        for i in range(1, 100):
            Product(
                product_id=i,
                product_name=random.choice(good_words) + " " + random.choice(furniture)
            ).save()
