from connection import Connection 
from model.userModel import UserModel
from utils.validation import *

class UserController():
    def login(self, user):
        db_connection = Connection()
        with db_connection as cursor:
            res = cursor.execute('''
                                        SELECT * FROM users 
                                        WHERE username=?
                                      ''', (user._username,))
            row = res.fetchone()
            if validate_password_hash(user._password, row[6]):
                if row:
                    username = UserModel(username=row[5], password=row[6])
                    return username
                else:
                    return None