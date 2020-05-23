  
import sys
from views import *
from models import *

def main():
    app = QApplication(sys.argv)
    win = MainWindow(PackageHandler())
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()