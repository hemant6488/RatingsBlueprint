import datetime
from mongoengine import *


class Product(Document):
    product_id = IntField(required=True)
    product_name = StringField(required=True)
    # -- other product attributes come here--
    created_at = DateTimeField()
    modified_at = DateTimeField()

    # Overriding the save method to save created and modified times.
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        return super(Product, self).save(*args, **kwargs)
