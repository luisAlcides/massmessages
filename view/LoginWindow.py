from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from connection import Connection

from controller.userController import UserController
from model.userModel import UserModel
from view.mainWindow import MainWindow

from utils.validation import validate_password, validate_username


class LoginWindow():
    def __init__(self):
        con = Connection()
        con.setup_database()
        self.login_window = uic.loadUi('view/Login.ui')
        self.initGUI()
        self.login_window.lbl_message.setText('')
        self.login_window.show()
        
    
    def initGUI(self):
        self.login_window.btn_login.clicked.connect(self.login)
        self.login_window.lbl_message.setVisible(False)
        
    
    def login(self):
        username = self.login_window.txt_username.text()
        password = self.login_window.txt_password.text()
        
        if not validate_username(username):
            self.showErrorMessage('El nombre de usuario debe tener almenos dos caracteres')
            return
        
        if not validate_password(password):
            self.showErrorMessage('La contrasena debe tener al menos 5 caracteres')
            return  
        
        user = UserModel(username=self.login_window.txt_username.text(), password=self.login_window.txt_password.text())
        controller = UserController()
        res = controller.login(user)
        if res:
            self.main_window = MainWindow()
            self.login_window.close()
        else:
            self.login_window.lbl_message.setText('Datos de usuario y contrasena incorrectos')
    
    
    def showErrorMessage(self, message):
        self.login_window.lbl_message.setText(message)
        self.login_window.lbl_message.setVisible(True)