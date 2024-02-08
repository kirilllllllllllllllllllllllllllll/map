from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi('design.ui', self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    app.exec_()
