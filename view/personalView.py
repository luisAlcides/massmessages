from PyQt6 import uic


class PersonalWindow():
    def __init__(self):
        self.personal_window = uic.loadUi('view/personalWindow.ui')
        self.personal_window.show()