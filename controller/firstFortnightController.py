from PyQt6 import QtWidgets
from connection import Connection
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt


class FirstFortnightController:
    def __init__(self, ui):
        self.db = Connection()
        self.ui = ui
        
    
    def load(self):
        with self.db as cursor:
            sql_select = 'SELECT first_name, second_name, first_surname, second_surname, phone FROM worksheet LIMIT 5'
            cursor.execute(sql_select)
            personals = cursor.fetchall()
            for personal in personals:
                self.add_personal_to_table(personal)
                
    
    def add_personal_to_table(self, personal):
        row_position = self.ui.table_fortnight.rowCount()
        self.ui.table_fortnight.insertRow(row_position)
        
        for i, field in enumerate(personal):
            if i ==4:
                phone_number = field.lstrip('+505')    # Quitar el prefijo "+505"
                item = QtWidgets.QTableWidgetItem(phone_number)
            else:
                item = QtWidgets.QTableWidgetItem(str(field))
            self.ui.table_fortnight.setItem(row_position, i, item)
            
        # Agregar checkbox para seleccionar
        checkbox_item = QtWidgets.QTableWidgetItem()
        checkbox_item.setFlags(checkbox_item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
        checkbox_item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.ui.table_fortnight.setItem(row_position, len(personal), checkbox_item)
        
    
    def get_numbers(self):
        numbers = []
        for row in range(self.ui.table_fortnight.rowCount()):
            checkbox_item = self.ui.table_fortnight.item(row, self.ui.table_fortnight.columnCount()-1)
            if checkbox_item.checkState() == Qt.CheckState.Checked:
                phone_item = self.ui.table_fortnight.item(row, 4)
                phone_more_505= f'+505{phone_item.text()}'
                numbers.append(phone_more_505)
        return numbers
