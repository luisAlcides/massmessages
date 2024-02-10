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
                name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                role TEXT
            )
        '''
        sql_create_table_worksheet = '''
                CREATE TABLE IF NOT EXISTS worksheet(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                salary NUMERIC,
                overtime NUMERIC,
                travelers NUMERIC,
                trips NUMERIC,
                productive_bonus NUMERIC,
                social_security NUMERIC,
                IR NUMERIC
                
            )
        '''
        
        with self as cursor:  # Maneja la conexión dentro del bloque 'with' 
            try:
                cursor.execute(sql_create_table_users)
                cursor.execute(sql_create_table_worksheet)
            except sqlite3.OperationalError as e:
                print('Error creating tables: ', e)

    def create_admin(self):
        sql_insert_admin = '''
                INSERT INTO users(name, last_name, username, password, phone, role)
                            VALUES (?, ?, ?, ?, ?, ?)
            '''
        values = ('Alvaro Antonio', 'Quezada Quintanilla', 'alvaroQuezada', 'admin.alvaro.23$', '+50584355878', 'admin')
        with self as cursor:
            try:
                cursor.execute(sql_insert_admin, values)
                self.con.commit()
            except sqlite3.IntegrityError as e:
                print('Error creating admin: ', e)

    def setup_database(self):
        with self as cursor:  # Usa el context manager
            self.create_tables()
            self.create_admin() 

