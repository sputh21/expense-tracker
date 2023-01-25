from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
import MySQLdb as mdb
import sys


class tableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        toolbar = QToolBar("New Bar")
        addButton = QToolButton()
        addButton.setText("Add Item")
        removeButton = QToolButton()
        removeButton.setText("Remove Item")
        editButton = QToolButton()
        editButton.setText("Edit Item")
        toolbar.addWidget(addButton)
        toolbar.addWidget(removeButton)
        toolbar.addWidget(editButton)
        self.addToolBar(toolbar)
        table = sqlTable()
  
class sqlTable(QSqlTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            db = mdb.connect('localhost', 'localhost', '1283', 'foodData')
        except:
            print("didn't connect")
        print("connected")
        # db.setHostName("localhost")
        # db.setDatabaseName("foodData")
        # db.setUserName("localhost")
        # db.setPassword("1283")
        # ok=db.open()
        # print(ok)
        # print(db.lastError())
        
        

        

class tabs(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        restaurants = QWidget()
        restaurants.layout = QHBoxLayout()
        left = QFrame()
        left.setFrameShape(QFrame.Shape.StyledPanel)
        left.layout=QHBoxLayout()
        newTool = tableWindow()
        left.layout.addWidget(newTool)
        left.setLayout(left.layout)
        
        right = QFrame()
        right.setFrameShape(QFrame.Shape.StyledPanel)
        right.layout=QHBoxLayout()
        right.setLayout(right.layout)


        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(left)
        splitter1.addWidget(right)
       
        restaurants.setLayout(restaurants.layout)
        restaurants.layout.addWidget(splitter1)

        streamingServices= QWidget()
        personalItems = QWidget()
        groceries = QWidget()
        bills = QWidget() 
        summary = QWidget()
        tabWidget = QTabWidget()

        widgetArr=[restaurants, streamingServices, personalItems, groceries, bills]
        strArr = ["Restaurants", "Streaming", "Personal Items", "Groceries", "Bills"]
        #add tabs
        for i in range(len(strArr)):
            tabWidget.addTab(widgetArr[i],strArr[i])
        tabWidget.addTab(summary, "Summary")
        layout.addWidget(tabWidget, 0, 0)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("Example")
        tabsWidget = tabs()
        self.setCentralWidget(tabsWidget)







app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec())
        

