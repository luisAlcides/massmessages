from PyQt6.QtWidgets import QApplication

from view.LoginWindow import LoginWindow, MainWindow


class MassMessages():
    def __init__(self):
        self.app = QApplication([])
        self.login_window = LoginWindow()
        self.app.exec()