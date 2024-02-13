import sqlite3
from connection import Connection

class NewUserController():
    def __init__(self, user):
        con = Connection()
        sql_insert_new_user = '''
            INSERT INTO users(first_name, second_name,first_surname, second_surname,username,password,phone, role) 
            VALUES(?,?,?,?,?,?,?,?)
        '''
        phone = f'+505{user._phone}'
        values = (user._first_name, user._second_name,user._first_surname,
                  user._second_surname,user._username, user._password,phone, user._role)
        with con as cursor:
            try:
                cursor.execute(sql_insert_new_user, values)
                con.con.commit()
            except sqlite3.IntegrityError as e:
                print('Error al insertar al usuario: ', e)
            except sqlite3.Error as e:
                print('Error inesperado: ', e)
            
        