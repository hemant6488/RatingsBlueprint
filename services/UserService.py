import logging

from services.DatabaseService import database

logger = logging.getLogger("ratings")


class UserService:
    def __init__(self):
        self.database = database

    def getUserById(self, user_id):
        if not user_id:
            return None
        else:
            user_entry = self.database.getUser(user_id)
            user = None
            if user_entry is not None:
                user = {'id': user_entry.user_id, 'name': user_entry.user_name}
            return user
