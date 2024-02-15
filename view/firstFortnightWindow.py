from PyQt6 import uic
from PyQt6.QtCore import Qt

from controller.firstFortnightController import FirstFortnightController

from sms.sms import sms


class FirstFortnightWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/firstFortnightWindow.ui')
        self.ui.showMaximized()
        self.load_users()
        self.ui.btn_selectAll.clicked.connect(self.select_all)
        self.ui.btn_deselectAll.clicked.connect(self.deselect_all)
        self.ui.btn_send.clicked.connect(self.send_messages)
        
        
    
    def load_users(self):
        controller = FirstFortnightController(self.ui)
        controller.load()
        
        
    def select_all(self):
        for row in range(self.ui.table_fortnight.rowCount()):
            item = self.ui.table_fortnight.item(row, self.ui.table_fortnight.columnCount()-1)
            item.setCheckState(Qt.CheckState.Checked)
            
    
    def deselect_all(self):
        for row in range(self.ui.table_fortnight.rowCount()):
            item = self.ui.table_fortnight.item(row, self.ui.table_fortnight.columnCount()-1)
            item.setCheckState(Qt.CheckState.Unchecked)
            
            
    def send_messages(self):
        controller = FirstFortnightController(self.ui)
        numbers = controller.get_numbers()
        sms(numbers)
        
        self.ui.close()