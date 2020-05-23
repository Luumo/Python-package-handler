from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QLineEdit, QProgressBar, QListWidget

class MainWindow(QGroupBox):
    def __init__(self, handler):
        super().__init__("Main window")
        anpv = AddNewPackagesView()
        ipv = InstallPackagesView()
        pv = ProgressView()

        ppv = PreviousPackagesView(handler)


        vbox = QVBoxLayout()
        vbox.addStretch(1)

        vbox.addWidget(anpv)
        vbox.addWidget(ipv)
        vbox.addWidget(pv)


        hbox = QHBoxLayout()
        hbox.addWidget(ppv)
        
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        ppv.update_packages()

class AddNewPackagesView(QGroupBox):
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
        hbox.addStretch(1)

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
        hbox.addStretch(1)

        self.installProgressBar = QProgressBar()
        self.installProgressBar.setProperty("value", 65)

        self.removeButton = QPushButton("Install packages")

        hbox = QHBoxLayout()
        hbox.addStretch()

        hbox.addWidget(self.installProgressBar)
        hbox.addWidget(self.removeButton)

        self.setLayout(hbox)


class PreviousPackagesView(QGroupBox):
    def __init__(self, handler):
        super().__init__("Installed packages on system")
        self.handler = handler
        hbox = QHBoxLayout()
        hbox.addStretch(1)

        self.PackagesList = QListWidget()
        self.removeButton = QPushButton("Remove")

        hbox = QHBoxLayout()
        hbox.addStretch()

        hbox.addWidget(self.PackagesList)
        hbox.addWidget(self.removeButton)

        self.setLayout(hbox)

        self.update_packages()

    def update_packages(self):
        for package in self.handler.packages:
            self.PackagesList.addItem(package[0])