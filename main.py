import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

SIZE_X, SIZE_Y = 1000, 800

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.setStyleSheet('background: rgb(0,255,0);')
        self.setWindowTitle('Yellow circles')
        self.do_paint = False
        self.btn.clicked.connect(self.click)

    def click(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            # Начинаем процесс рисования
            qp.begin(self)
            self.circle(qp)
            # Завершаем рисование
            qp.end()

    def circle(self, qp):
        x = random.randint(100, SIZE_X - 100)
        y = random.randint(100, SIZE_Y - 150)
        d = random.randint(10, 50)
        color = random.choice([Qt.red, Qt.yellow, Qt.blue, Qt.green, Qt.black])
        qp.setBrush(QBrush(color, Qt.Dense3Pattern))
        qp.setPen(QPen(Qt.yellow, 3, Qt.DashLine))
        qp.drawEllipse(x - d, y - d, 2 * d, 2 * d)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())