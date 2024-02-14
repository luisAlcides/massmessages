from connection import Connection
from PyQt6 import QtWidgets

class PersonalViewController():
    def __init__(self, ui):
        self.db_connection = Connection()
        self.ui = ui
        
    
    def load(self):
        with self.db_connection as cursor:
            cursor.execute('SELECT * FROM worksheet')
            personals = cursor.fetchall()
            for personal in personals:
                self.add_personal_to_table(personal)
                
    
    def add_personal_to_table(self, personal):
        row_position = self.ui.table_personal.rowCount()
        self.ui.table_personal.insertRow(row_position)
        for i, field in enumerate(personal):
            item = QtWidgets.QTableWidgetItem(str(field))
            self.ui.table_personal.setItem(row_position, i, item)