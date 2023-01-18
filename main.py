from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)


        #set up first tab
        restaurants = QWidget()
        restaurants.layout = QVBoxLayout()
        label1 = QPushButton("This is a widget")
        restaurants.layout.addWidget(label1)
        restaurants.setLayout(restaurants.layout)
        

        
        streamingServices= QWidget()
        personalItems = QWidget()
        groceries = QWidget()
        bills = QWidget()
        summary = QWidget()
        tabwidget = QTabWidget()



        tabwidget.addTab(restaurants, "Restaurants")
        tabwidget.addTab(streamingServices, "Streaming")
        tabwidget.addTab(personalItems, "Personal Items")
        tabwidget.addTab(groceries, "Groceries")
        tabwidget.addTab(bills, "Bills")
        tabwidget.addTab(summary, "Summary")


        layout.addWidget(tabwidget, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())