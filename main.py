from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction

import sys



class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        QWidget.__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
class tabs(QWidget):
    def __init__(self):
        layout = QGridLayout()
        self.setLayout(layout)


        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())
        

