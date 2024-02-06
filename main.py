import sys, os

from PySide6.QtWidgets import QApplication
from views.LoginWindow import LoginWindow
from controllers.LoginController import LoginController
from controllers.controller import connect
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #styles_file = os.path.join(os.path.dirname(__file__), 'styles.qss')
    connect()
    app.setStyleSheet(open('./styles/styles.qss').read())
    
    window = LoginWindow()
    controller = LoginController(window)
    window.show()
    sys.exit(app.exec())