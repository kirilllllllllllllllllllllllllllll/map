from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtGui import QPixmap, QImage
import sys
from load_map import load_map


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi('design.ui', self)

        self.start_spn = 1.0
        self.start_index = False
        self.start_mode = "map"

        self.search_btn.clicked.connect(
            lambda: self.search_button_click(self.get_user_search()))
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            self.start_spn += 0.003
            self.search_button_click(self.get_user_search())
        elif e.key() == Qt.Key_PageDown:
            pass
        elif e.key() == Qt.Key_Up:
            pass
        elif e.key() == Qt.Key_Left:
            pass
        elif e.key() == Qt.Key_Right:
            pass
        elif e.key() == Qt.Key_Down:
            pass

    def get_user_search(self):
        return self.to_search.text()

    def search_button_click(self, toponym):
        image, address = load_map(toponym, self.start_spn, self.start_index, self.start_mode)
        img = QImage()
        img.loadFromData(image)
        self.pixmap_label.setPixmap(QPixmap.fromImage(img))
        self.statusBar().showMessage(address)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
