import sqlite3

class LoginController:
    def __init__(self, view):
        self.view = view
        self.view.login_button.clicked.connect(self.login)
        self.db_connection = sqlite3.connect('db_mass_messages.db')
        self.db_cursor = self.db_connection.cursor()
        
    
    def login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        
        query = 'SELECT * FROM users_system WHERE username=? AND password=?'
        self.db_cursor.execute(query, (username, password))
        user = self.db_cursor.fetchone()
        
        if user:
            print('Inicio de sesion exitoso')
        else:
            print('Credenciales incorrectas')
        
    def __del__(self):
        self.db_connection.close()