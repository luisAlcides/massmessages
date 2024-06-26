import sqlite3


class Connection:
    def __init__(self):
        self.con = None

    def __enter__(self):
        try:
            self.con = sqlite3.connect('db_massmessages.db')
            return self.con.cursor()
        except sqlite3.Error as e:
            print('Database connection error, ', e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con:
            self.con.close()

    def create_tables(self):
        sql_create_table_users = '''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                second_name TEXT,
                first_surname TEXT NOT NULL,
                second_surname TEXT, 
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                role TEXT,
                created DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        '''
        sql_create_table_worksheet = '''
                CREATE TABLE IF NOT EXISTS worksheet(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                second_name TEXT,
                first_surname TEXT NOT NULL,
                second_surname TEXT,
                phone TEXT NOT NULL UNIQUE,
                salary REAL,
                overtime REAL,
                travelers REAL,
                trips REAL,
                productive_bonus REAL,
                social_security REAL,
                IR REAL,
                created DATETIME DEFAULT CURRENT_TIMESTAMP
                
            )
        '''
        
        with self as cursor:  # Maneja la conexión dentro del bloque 'with' 
            try:
                cursor.execute(sql_create_table_users)
                cursor.execute(sql_create_table_worksheet)
            except sqlite3.OperationalError as e:
                print('Error creating tables: ', e)
    def setup_database(self):
        with self as cursor:  # Usa el context manager
            self.create_tables()
            



    

