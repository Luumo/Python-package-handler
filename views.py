from PyQt5.QtWidgets import QLineEdit, QApplication, QLabel, QMainWindow, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Python Handler"
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)

        #textbox
        self.textbox = QLineEdit(self)
        self.show()
        self.button = QPushButton('Show text', self)

        self.button.clicked.connect(self.button_clicked)
        self.show()

    @pyqtSlot()
    def button_clicked(self):
        print("hello")
