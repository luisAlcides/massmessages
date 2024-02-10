from PyQt6 import uic


class NewUserWindow():
    def __init__(self):
        self.new_user_window = uic.loadUi('view/newUserWindow.ui')
        self.new_user_window.show()