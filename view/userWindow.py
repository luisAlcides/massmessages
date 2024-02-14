from PyQt6 import uic

from connection import Connection
from controller.EditUserController import EditUserController
from controller.deleteUserController import UserDelete
from controller.userViewController import userViewController
from PyQt6 import QtWidgets


class UserWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/userWindow.ui')
        self.ui.show()
        self.load_users()
        self.ui.btn_delete.clicked.connect(self.delete_user)
        self.ui.btn_edit.clicked.connect(self.edit_user)
        self.ui.btn_refresh.clicked.connect(self.refresh_users)
        
    
    def load_users(self):
        user_view = userViewController(self.ui)
        user_view.load()


    def delete_user(self):
        selected_rows = self.ui.table_users.selectionModel().selectedRows()
        for row in selected_rows:
            user_id = self.ui.table_users.item(row.row(),0).text()
            UserDelete.delete_user(user_id)
            self.ui.table_users.removeRow(row.row())


    def edit_user(self):
        selected_indexes = self.ui.table_users.selectionModel().selectedRows()
        if len(selected_indexes) == 1:
            row = selected_indexes[0].row()
            user_data = [self.ui.table_users.item(row, col).text() for col in range(self.ui.table_users.columnCount())]
            edit_window = EditUserController(user_data)
            if edit_window.exec() == QtWidgets.QDialog.accepted:
                for i in range(self.ui.table_users.columnCount()):
                    item = self.ui.table.users.item(row, i)
                    if item is None:
                        item = QtWidgets.QTableWidgetItem()
                        self.ui.table_users.setItem(row, i, item)
                    item.setText(str(user_data[i]))
                edit_window.close()

    def refresh_users(self):
        self.ui.table_users.clearContents()
        self.ui.table_users.setRowCount(0)
        self.load_users()