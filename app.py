import sys
from views import *


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()



if __name__ == "__main__":
    main()