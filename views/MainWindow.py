from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mass Messages')
        button = QPushButton('Press Me')
        
        self.setCentralWidget(button)
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()