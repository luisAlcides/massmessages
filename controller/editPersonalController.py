from connection import Connection
from PyQt6 import QtWidgets, uic
from utils.validation import *

class EditPersonalController(QtWidgets.QDialog):
    def __init__(self, personal_data, parent=None):
        super().__init__(parent)
        uic.loadUi('view/updatePersonalWindow.ui', self)
        self.txt_first_name.setText(personal_data[1])
        self.txt_second_name.setText(personal_data[2])
        self.txt_first_surname.setText(personal_data[3])
        self.txt_second_surname.setText(personal_data[4])
        phone = personal_data[5]
        phone_without_prefix = phone.replace('+505', '')
        self.txt_phone.setText(phone_without_prefix)
        self.txt_salary.setText(personal_data[6])
        self.txt_overtime.setText(personal_data[7])
        self.txt_travelers.setText(personal_data[8])
        self.txt_trips.setText(personal_data[9])
        self.txt_productive_bonus.setText(personal_data[10])
        self.txt_social_security.setText(personal_data[11])
        self.txt_IR.setText(personal_data[12])
        self.personal_data = personal_data
        
        self.btn_update = self.findChild(QtWidgets.QPushButton, 'btn_update')
        self.btn_update.clicked.connect(self.update_personal)
        
    
    def validate_fields(self,first_name, second_name, first_surname, second_surname, phone, salary, overtime, travelers, trips, productive_bonus, social_security, IR):
        
        if not validate_text(first_name, 'Primer Nombre:'):
            return False
        if not validate_text(second_name, 'Segundo Nombre: '):
            return False
        if not validate_text(first_surname, 'Primer Apellido:'):
            return False
        if not validate_text(second_surname, 'Segundo Apellido: '):
            return False
        if not validate_phone(phone):
            return False
        if not validate_number(salary):
            return False
        if not validate_number(overtime):
            return False
        if not validate_number(travelers):
            return False
        if not validate_number(trips):
            return False
        if not validate_number(productive_bonus):
            return False
        if not validate_number(social_security):
            return False
        if not validate_number(IR):
            return False
        return True
    
    
    
    def update_personal(self):
        new_first_name = self.txt_first_name
        new_second_name = self.txt_second_name
        new_first_surname = self.txt_first_surname
        new_second_surname = self.txt_second_surname
        new_phone = self.txt_phone
        new_salary = self.txt_salary
        new_overtime = self.txt_overtime
        new_travelers = self.txt_travelers
        new_trips = self.txt_trips
        new_productive_bonus = self.txt_productive_bonus
        new_social_security = self.txt_social_security
        new_IR = self.txt_IR
        
        
        if not self.validate_fields(new_first_name, new_second_name, new_first_surname, new_second_surname, new_phone, new_salary, new_overtime, new_travelers, new_trips, new_productive_bonus, new_social_security, new_IR):
            return 
        
        db = Connection()
        with db as cursor:
            sql_update_personal = '''
                UPDATE worksheet
                SET first_name=?,
                second_name=?,
                first_surname=?,
                second_surname=?,
                phone=?,
                salary=?,
                overtime=?,
                travelers=?,
                trips=?,
                productive_bonus=?,
                social_security=?,
                IR=?
                WHERE id=?
            '''
            phone = f'+505{new_phone.text()}'
            values = (
                new_first_name.text(),
                new_second_name.text(),
                new_first_surname.text(),
                new_second_surname.text(),
                phone,
                float(new_salary.text()),
                float(new_overtime.text()),
                float(new_travelers.text()),
                float(new_trips.text()),
                float(new_productive_bonus.text()),
                float(new_social_security.text()),
                float(new_IR.text()),
                self.personal_data[0]
            )
            cursor.execute(sql_update_personal, values)
            db.con.commit()
            self.accept()