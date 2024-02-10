from connection import Connection 
from model.userModel import UserModel


class UserController():
    def login(self, user):
        db_connection = Connection()
        with db_connection as cursor:
            res = cursor.execute('''
                                        SELECT * FROM users 
                                        WHERE username=? 
                                        AND password=?
                                      ''', (user._username, user._password))
            row = res.fetchone()
            if row:
                username = UserModel(username=row[3], password=row[4])
                return username
            else:
                return None