from PyQt6 import uic


class UserWindow():
    def __init__(self):
        self.user_window = uic.loadUi('view/userWindow.ui')
        self.user_window.show()