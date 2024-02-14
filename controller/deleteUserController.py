from connection import Connection

class UserDelete:
    @staticmethod
    def delete_user(user_id):
        db_connection = Connection()
        with db_connection as cursor:
            query = 'Delete FROM users WHERE id=?'
            value = (user_id,)
            cursor.execute(query, value)
            db_connection.con.commit()