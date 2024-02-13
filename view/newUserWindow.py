from PyQt6 import uic
from controller.newUserController import NewUserController
from model.newUserModel import NewUserModel
from utils.validation import *


class NewUserWindow:
    def __init__(self):
        self.ui = uic.loadUi('view/newUserWindow.ui')
        self.ui.btn_register.clicked.connect(self.register_user)
        self.ui.show()

    def validate_fields(self):
        first_name = self.ui.txt_first_name.text()
        second_name = self.ui.txt_second_name.text()
        first_surname = self.ui.txt_first_surname.text()
        second_surname = self.ui.txt_second_surname.text()
        username = self.ui.txt_username.text()
        password = self.ui.txt_password.text()
        phone = self.ui.txt_phone.text()
        role = self.ui.cb_role.currentText()

        if not validate_text(first_name, 'Primer Nombre:'):
            return False
        if not validate_text(second_name, 'Segundo Nombre: '):
            return False
        if not validate_text(first_surname, 'Primer Apellido:'):
            return False
        if not validate_text(second_surname, 'Segundo Apellido: '):
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
        self.ui.txt_first_name.setText('')
        self.ui.txt_second_name.setText('')
        self.ui.txt_first_surname.setText('')
        self.ui.txt_second_surname.setText('')
        self.ui.txt_username.setText('')
        self.ui.txt_password.setText('')
        self.ui.txt_phone.setText('')
        self.ui.cb_role.setCurrentIndex(0)

    def register_user(self):
        if not self.validate_fields():
            print('No se pudo registrar al usuario')
            return False

        first_name = self.ui.txt_first_name.text()
        second_name = self.ui.txt_second_name.text()
        first_surname = self.ui.txt_first_surname.text()
        second_surname = self.ui.txt_second_surname.text()
        username = self.ui.txt_username.text()
        password = hash_password(self.ui.txt_password.text())
        phone = self.ui.txt_phone.text()
        role = self.ui.cb_role.currentText()
        
        user_model = NewUserModel(first_name, second_name,first_surname,second_surname ,username, password, phone, role)
        user_controller = NewUserController(user_model)
        messageError('usuario agregado exitosamente')
        
        self.clean_fields()
        print('Registro exitoso')