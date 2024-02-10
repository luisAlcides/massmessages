from PyQt6 import uic

from view.newUserWindow import NewUserWindow
from view.newPersonalWindow import NewPersonalWindow



class MainWindow():
    def __init__(self):
        self.main_window = uic.loadUi('view/mainWindow.ui')
        self.main_window.showMaximized()
        
        self.main_window.btn_new_user.triggered.connect(self.openNewRegister)
        self.main_window.btn_new_personal.triggered.connect(self.openNewPersonal)
        
    
    def openNewRegister(self):
        self.new_user_window = NewUserWindow()
        return self.new_user_window
    
    
    def openNewPersonal(self):
        self.new_personal_window = NewPersonalWindow()
        return self.new_personal_window