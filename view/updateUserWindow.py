from PyQt6 import uic


class UpdateUserWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/updateUserWindow.ui')
        self.ui.show()