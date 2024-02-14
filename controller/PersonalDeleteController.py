from connection import Connection


class PersonalDeleteController:
    @staticmethod
    def delete_personal(personal_id):
        db_connection = Connection()
        with db_connection as cursor:
            query = 'DELETE FROM worksheet WHERE id=? LIMIT 1'
            value = (personal_id,)
            cursor.execute(query, value)
            db_connection.con.commit()
    