from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("SW Design Team")
        layout.addWidget(label, 0, 0)
        label = QLabel("1.Muruganandham")
        layout.addWidget(label, 1, 0)
        label = QLabel("2.Srinath")
        layout.addWidget(label, 2, 0)
        label = QLabel("3.Nanda")
        layout.addWidget(label, 3, 0)
        label = QLabel("4.AASAI")
        layout.addWidget(label,4,0)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
