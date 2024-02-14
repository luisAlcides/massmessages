
from connection import Connection
from PyQt6 import QtWidgets


class userViewController():
    def __init__(self, ui):
        self.db_connection = Connection()
        self.ui = ui
    
    
    def load(self):
        with self.db_connection as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            for user in users:
                self.add_user_to_table(user)
    
    def add_user_to_table(self, user):
        row_position = self.ui.table_users.rowCount()
        self.ui.table_users.insertRow(row_position)
        for i, field in enumerate(user):
            item = QtWidgets.QTableWidgetItem(str(field))
            self.ui.table_users.setItem(row_position, i, item)

        
    
    
    