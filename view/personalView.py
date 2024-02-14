from PyQt6 import uic
from PyQt6 import QtWidgets

from controller.PersonalDeleteController import PersonalDeleteController
from controller.personalViewController import PersonalViewController
from controller.editPersonalController import EditPersonalController

class PersonalWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/personalWindow.ui')
        self.ui.showMaximized()
        self.load_workers()
        self.ui.btn_delete.clicked.connect(self.delete_personal)
        self.ui.btn_refresh.clicked.connect(self.refresh_personal)
        self.ui.btn_edit.clicked.connect(self.edit_personal)
        
        
    
    def load_workers(self):
        personal_view = PersonalViewController(self.ui)
        personal_view.load()
        
    
    def delete_personal(self):
        selected_rows = self.ui.table_personal.selectionModel().selectedRows()
        for row in selected_rows:
            personal_id = self.ui.table_personal.item(row.row(), 0).text()
            PersonalDeleteController.delete_personal(personal_id)
            self.ui.table_personal.removeRow(row.row())
            
    
    def refresh_personal(self):
        self.ui.table_personal.clearContents()
        self.ui.table_personal.setRowCount(0)
        self.load_workers()
        
    
    def edit_personal(self):
        selected_indexes = self.ui.table_personal.selectionModel().selectedRows()
        if len(selected_indexes) == 1:
            row = selected_indexes[0].row()
            personal_data = [self.ui.table_personal.item(row, col).text() for col in range(self.ui.table_personal.columnCount())]
            edit_window = EditPersonalController(personal_data)
            if edit_window.exec() == QtWidgets.QDialog.accepted:
                edit_window.close()