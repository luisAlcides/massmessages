from PyQt6 import QtWidgets

from connection import Connection
from utils.validation import *
from PyQt6 import QtWidgets, uic



class EditUserController(QtWidgets.QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        uic.loadUi('view/updateUserWindow.ui', self)
        self.txt_first_name.setText(user_data[1])
        self.txt_second_name.setText(user_data[2])
        self.txt_first_surname.setText(user_data[3])
        self.txt_second_surname.setText(user_data[4])
        self.txt_username.setText(user_data[5])
        phone = user_data[7]
        phone_without_prefix = phone.replace('+505', '')
        self.txt_phone.setText(phone_without_prefix)
        self.cb_role.setCurrentText(user_data[8])
        self.user_data = user_data
        
        self.btn_update = self.findChild(QtWidgets.QPushButton, 'btn_update')
        self.btn_update.clicked.connect(self.update_user)
        
        
    
    def validate_fields(self, first_name, second_name, first_surname, second_surname,
                        username,phone, role, password=None):
        

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
        if not validate_phone(phone):
            return False
        if not validate_role(role):
            return False
        if password and not validate_password(password):
            return False
        return True
    
    
    def update_user(self):
        new_first_name = self.txt_first_name
        new_second_name = self.txt_second_name
        new_first_surname = self.txt_first_surname
        new_second_surname = self.txt_second_surname
        new_username = self.txt_username
        new_password = self.txt_password
        new_phone = self.txt_phone
        new_role = self.cb_role.currentText()
        
        if not self.validate_fields(new_first_name, new_second_name, new_first_surname, 
                                 new_second_surname, new_username,new_phone , new_role,  new_password):
            return 
        
        
        db_connection = Connection()
        with db_connection as cursor:
            if new_password:
                sql_update_password_changed = '''
                            UPDATE users 
                            SET first_name=?,
                            second_name=?,
                            first_surname=?,
                            second_surname=?,
                            username=?,
                            password=?,
                            phone=?,
                            role=?
                            WHERE id=?
                            '''
                values_changed_password = (
                new_first_name.text(), 
                new_second_name.text(),
                new_first_surname.text(),
                new_second_surname.text(),
                new_username.text(),
                hash_password(new_password.text()),
                f'+505{new_phone.text()}',
                new_role, 
                self.user_data[0]
                )
                cursor.execute(sql_update_password_changed, values_changed_password)
                db_connection.con.commit()
            else:
                sql_update= '''
                            UPDATE users 
                            SET first_name=?,
                            second_name=?,
                            first_surname=?,
                            second_surname=?,
                            username=?,
                            phone=?,
                            role=?
                            WHERE id=?
                            '''
                values_changed = (
                new_first_name.text(), 
                new_second_name.text(),
                new_first_surname.text(),
                new_second_surname.text(),
                new_username.text(),
                f'+505{new_phone}',
                new_role, 
                self.user_data[0]
                )
                cursor.execute(sql_update, values_changed)
                db_connection.con.commit()
            self.accept()
                
            
