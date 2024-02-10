from PyQt6 import uic

class NewPersonalWindow():
    def __init__(self):
        self.new_personal_window = uic.loadUi('view/newPersonalWindow.ui')
        self.new_personal_window.show()