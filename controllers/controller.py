from models.database import Database


def connect():
    db = Database('db_mass_messages.db')

    db.create_tables()
    db.cursor.execute('''
                    INSERT INTO users_system(username, name, lastname, password, level, phone)
                    VALUES (?,?,?,?,?,?)
                    ''', ('alvaroq', 'Alvaro', 'Quezada', 'alvaroq1919$', 'admin', '84355878'))

    db.conn.commit()
    db.close()