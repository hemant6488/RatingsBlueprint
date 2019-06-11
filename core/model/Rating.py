import datetime
from mongoengine import *


class Rating(Document):
    user_id = IntField(required=True)
    product_id = IntField(required=True)
    rating = IntField(required=True, min_value=1, max_value=5)
    deleted = BooleanField(default=False)
    created_at = DateTimeField()
    modified_at = DateTimeField()
    meta = {"indexes": [
        {'fields': ('+user_id', '+product_id', '+deleted'), 'unique': True}
    ]}

    # Overriding the save method to save created and modified times.
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        return super(Rating, self).save(*args, **kwargs)
