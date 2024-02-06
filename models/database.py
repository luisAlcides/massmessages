import sqlite3

class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f'Erro al conectarse a la base de datos: {e}')
        
    def create_tables(self):
        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS users_system(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL UNIQUE,
                                    name TEXT NOT NULL,
                                    lastname TEXT NOT NULL,
                                    password TEXT NOT NULL,
                                    level TEXT NOT NULL
                                )
                                
                                CREATE TABLE IF NOT EXISTS users(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    lastname TEXT NOT NULL,
                                    phone TEXT,
                                    mail TEXT,
                                    salary INTEGER,
                                    age INTEGER,
                                    area TEXT
                                    
                                )
                                ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Erro al crear la tabla: {e}')
    
    
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except sqlite3.Error as e:
            print(f'Error al cerrar la conextion: {e}')