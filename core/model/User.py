import datetime
from mongoengine import *


class User(Document):
    user_id = IntField(required=True)
    user_name = IntField(required=True)
    # -- additional user attributes come here --
    created_at = DateTimeField()
    modified_at = DateTimeField()

    # Overriding the save method to save created and modified times.
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)
