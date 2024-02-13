import sqlite3
from connection import Connection

class NewPersonalController():
    def __init__(self, user):
        con = Connection()
        sql_insert_new_personal = '''
            INSERT INTO worksheet(first_name, second_name,first_surname, second_surname,phone, salary, overtime, travelers, trips, productive_bonus, social_security, IR) 
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
        '''
        phone = f'+505{user._phone}'
        values = (user._first_name, user._second_name,user._first_surname,
                  user._second_surname,phone, user._salary, user._overtime, user._travelers,user._trips, user._productive_bonus, user._social_security, user._IR)
        with con as cursor:
            try:
                cursor.execute(sql_insert_new_personal, values)
                con.con.commit()
            except sqlite3.IntegrityError as e:
                print('Error al insertar al personal: ', e)
            except sqlite3.Error as e:
                print('Error inesperado: ', e)
            
        