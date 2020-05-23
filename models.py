import os
from PyQt5.QtCore import QObject, pyqtSignal
import handlerlib

class PackageHandler(QObject):   
    def __init__(self):
        super().__init__()

        self.packages = []

        self.get_system_packages()
    
    def get_system_packages(self):
        self.packages = handlerlib.installed_packages()            
        #installed_packages()
        