import sys, os

from PySide6.QtWidgets import QApplication
from views.LoginWindow import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #styles_file = os.path.join(os.path.dirname(__file__), 'styles.qss')
    app.setStyleSheet(open('./styles/styles.qss').read())
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())