from PyQt6 import uic
from model.newUserModel import NewUserModel
from utils.validation import *


class NewUserWindow:
    def __init__(self):
        self.ui = uic.loadUi('view/newUserWindow.ui')
        self.ui.btn_register.clicked.connect(self.register_user)
        self.ui.show()

    def validate_fields(self):
        name = self.ui.txt_name.text()
        last_name = self.ui.txt_last_name.text()
        username = self.ui.txt_username.text()
        password = self.ui.txt_password.text()
        phone = self.ui.txt_phone.text()
        role = self.ui.cb_role.currentText()

        if not validate_text(name, 'Nombres: '):
            return False
        if not validate_text(last_name, 'Apellidos: '):
            return False
        if not validate_username(username):
            return False
        if not validate_password(password):
            return False
        if not validate_phone(phone):
            return False
        if not validate_role(role):
            return False
        return True

    def clean_fields(self):
        self.ui.txt_name.setText('')
        self.ui.txt_last_name.setText('')
        self.ui.txt_username.setText('')
        self.ui.txt_password.setText('')
        self.ui.txt_phone.setText('')
        self.ui.cb_role.setCurrentIndex(0)

    def register_user(self):
        if not self.validate_fields():
            print('No se pudo registrar al usuario')
            return False

        name = self.ui.txt_name.text()
        last_name = self.ui.txt_last_name.text()
        username = self.ui.txt_username.text()
        password = hash_password(self.ui.txt_password.text())
        phone = self.ui.txt_phone.text()
        role = self.ui.cb_role.currentText()
        
        newUserModel = NewUserModel(name, last_name, username, password, phone, role)
        self.clean_fields()
        print('Registro exitoso')