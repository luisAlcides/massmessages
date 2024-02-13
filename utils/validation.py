import re
import hashlib
from PyQt6.QtWidgets import QMessageBox

def messageError(message):
    mBox = QMessageBox()
    mBox.setText(message)
    mBox.exec()


### validation

def validate_text(text, campo):
    if (campo == 'Primer Nombre:' or campo == 'Primer Apellido:'):
        if not text.text():
            messageError(f"El campo {campo} no pueden estar vacios")
            text.setFocus()
            return False
        if not re.match(r"^[a-zA-Z]+$", text.text()):
            messageError(f"El campo {campo} solo permite letras")
            text.setFocus()
            return False
    return True


def validate_username(username):
    if not username.text():
        messageError("El usuario no puede estar vacio")
        username.setFocus()
        return False
    if len(username.text()) < 4:
        messageError("El usuario debe contener al menos 4 letras")
        username.setFocus()
        return False
    return True

def validate_password(password):
    if not password.text():
        messageError("Debe ingresar la contraseña")
        password.setFocus()
        return False
    if len(password.text()) < 8:
        messageError("La contraseñan debe contener al menos 8 caracteres")
        password.setFocus()
        return False
    if not re.search(r"\d", password.text()):
        messageError("La contraseña debe contener al menos 1 número")
        password.setFocus()
        return False
    if not re.search(r"[A-Z]", password.text()):
        messageError("La contraseña debe contener al menos una mayúscula")
        password.setFocus()
        return False
    if not re.search(r"[a-z]", password.text()):
        messageError("La contraseña debe contener al menos un caracter")
        password.setFocus()
        return False
    return True

def validate_phone(phone):
    if not phone.text():
        messageError("Debe ingresar el teléfono")
        phone.setFocus()
        return False
    if not re.match(r"^\d{8}$", phone.text()):
        messageError("Este número no es válido. Debe tener 8 dígitos.")
        phone.setFocus()
        return False
    return True

def validate_role(role):
    if role not in ["admin", "user"]:
        messageError("El rol debe ser 'admin' o 'user'")
        return False
    return True

def validate_salary(salary):
    if not salary:
        messageError("Salario no puede estar vacio")
        return False
    if not isinstance(salary, (int, float)):
        messageError("Salario debe ser un número")
        return False
    return True

def validate_number(over):
    if not float(over.text()):
        messageError("No puede estar vacio")
        over.setFocus()
        return False
    if not isinstance(float(over.text()), (int, float)):
        messageError("Debe ser un número")
        over.setFocus()
        return False
    return True
        
### security
def hash_password(password):
    password_bytes = password.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(password_bytes)
    hashed_password = sha256.hexdigest()
    return hashed_password
        

def validate_password_hash(input_password, stored_hash):
    hashed_input_password = hash_password(input_password)
    
    if hashed_input_password == stored_hash:
        return True
    else:
        return False
    
    
'''
alvaro.quezada
Quezada$alvaro23
84355878
'''