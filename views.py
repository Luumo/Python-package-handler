
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QLineEdit, QProgressBar, QListWidget

class MainWindow(QGroupBox):
    def __init__(self):
        super().__init__("Main window")

        npv = NewPackagesView()
        ipv = InstallPackagesView()
        pv = ProgressView()
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        vbox.addWidget(npv)
        vbox.addWidget(ipv)
        vbox.addWidget(pv)

        self.setLayout(vbox)



class NewPackagesView(QGroupBox):
    def __init__(self):
        super().__init__("New Packages")

        self.addPackage = QLineEdit()
        self.addButton = QPushButton("Add")

        # add clicked.connect to buttons

        hbox = QHBoxLayout()
        hbox.addStretch(1)

        hbox.addWidget(self.addPackage)
        hbox.addWidget(self.addButton)     

        self.setLayout(hbox)

class InstallPackagesView(QGroupBox):
    def __init__(self):
        super().__init__("Chosen Packages")

        hbox = QHBoxLayout()
        hbox.addStretch()

        self.chosenPackagesList = QListWidget()
        self.removeButton = QPushButton("Remove")

        hbox = QHBoxLayout()
        hbox.addStretch()

        hbox.addWidget(self.chosenPackagesList)
        hbox.addWidget(self.removeButton)

        self.setLayout(hbox)


class ProgressView(QGroupBox):
    def __init__(self):
        super().__init__("Install")

        hbox = QHBoxLayout()
        hbox.addStretch()

        self.installProgressBar = QProgressBar()
        self.installProgressBar.setProperty("value", 65)

        self.removeButton = QPushButton("Install packages")

        hbox = QHBoxLayout()
        hbox.addStretch()

        hbox.addWidget(self.installProgressBar)
        hbox.addWidget(self.removeButton)

        self.setLayout(hbox)
        

