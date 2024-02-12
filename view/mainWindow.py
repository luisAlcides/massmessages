from PyQt6 import uic

from view.newUserWindow import NewUserWindow
from view.newPersonalWindow import NewPersonalWindow
from view.personalView import PersonalWindow
from view.userView import UserWindow


class MainWindow():
    def __init__(self):
        self.main_window = uic.loadUi('view/mainWindow.ui')
        self.main_window.showMaximized()
        
        self.main_window.btn_new_user.triggered.connect(self.openNewRegister)
        self.main_window.btn_new_personal.triggered.connect(self.openNewPersonal)
        #self.main_window.btn_user.triggered.connect(self.openUser)
        #self.main_window.btn_personal.triggered.connect(self.openPersonal)
        
    
    def openNewRegister(self):
        self.new_user_window = NewUserWindow()
        return self.new_user_window
    
    
    def openNewPersonal(self):
        self.new_personal_window = NewPersonalWindow()
        return self.new_personal_window
    
    def openUser(self):
        self.user_window = UserWindow()
        return self.user_window
    
    
    def openPersonal(self):
        self.personal_window = PersonalWindow()
        return self.personal_window