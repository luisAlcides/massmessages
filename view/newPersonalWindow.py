from PyQt6 import uic
from controller.newPersonalController import NewPersonalController
from model.NewPersonalModel import NewPersonalModel
from utils.validation import *

class NewPersonalWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/newPersonalWindow.ui')
        self.ui.btn_register.clicked.connect(self.register_personal)
        self.ui.show()
        
        
    
    def validate_fields(self):
        first_name = self.ui.txt_first_name
        second_name = self.ui.txt_second_name
        first_surname = self.ui.txt_first_surname
        second_surname = self.ui.txt_second_surname
        phone = self.ui.txt_phone
        salary = self.ui.txt_salary
        overtime = self.ui.txt_overtime
        travelers = self.ui.txt_travelers
        trips = self.ui.txt_trips
        productive_bonus = self.ui.txt_productive_bonus
        social_security = self.ui.txt_social_security
        IR = self.ui.txt_IR

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

    def clean_fields(self):
        self.ui.txt_first_name.setText('')
        self.ui.txt_second_name.setText('')
        self.ui.txt_first_surname.setText('')
        self.ui.txt_second_surname.setText('')
        self.ui.txt_phone.setText('')
        self.ui.txt_salary.setText('')
        self.ui.txt_overtime.setText('')
        self.ui.txt_travelers.setText('')
        self.ui.txt_trips.setText('')
        self.ui.txt_productive_bonus.setText('')
        self.ui.txt_social_security.setText('')
        self.ui.txt_IR.setText('')

    def register_personal(self):
        if not self.validate_fields():
            print('No se pudo registrar al personal')
            return False

        first_name = self.ui.txt_first_name.text()
        second_name = self.ui.txt_second_name.text()
        first_surname = self.ui.txt_first_surname.text()
        second_surname = self.ui.txt_second_surname.text()
        phone = self.ui.txt_phone.text()
        salary = float(self.ui.txt_salary.text())
        overtime = float(self.ui.txt_overtime.text())
        travelers = float(self.ui.txt_travelers.text())
        trips = float(self.ui.txt_trips.text())
        productive_bonus = float(self.ui.txt_productive_bonus.text())
        social_security = float(self.ui.txt_social_security.text())
        IR = float(self.ui.txt_IR.text())
        
        personal_model = NewPersonalModel(first_name, second_name,first_surname,second_surname ,phone, salary, overtime, travelers, trips, productive_bonus, social_security, IR)
        personal_controller = NewPersonalController(personal_model)
        messageError('Personal agregado exitosamente')
        
        self.clean_fields()
        print('Registro exitoso')