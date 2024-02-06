from PySide6.QtWidgets import QApplication,QFormLayout, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Inicio de sesión')
        self.setFixedSize(500, 500)
        primary_screen = QApplication.screens()[0]
        self.move(primary_screen.availableGeometry().center() - self.rect().center())
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        self.username_label = QLabel('Nombre de usuario: ')
        self.username_input = QLineEdit()
        form_layout.addRow(self.username_label, self.username_input)
        
        self.password_label = QLabel('Password: ')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addRow(self.password_label, self.password_input)
        
        layout.addLayout(form_layout)
        
        self.login_button = QPushButton('Iniciar')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)
        
        self.central_widget.setLayout(layout)
        
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        print(f'Username: {username}, Password: {password}')