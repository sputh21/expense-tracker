from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
import sqlite3 as sqlite

global db 

db = sqlite.connect("food.db")

class tableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #TOOLBAR SETUP
        toolbar = QToolBar("New Bar")


        addButton = QAction("Add Item", self)
        addButton.triggered.connect(self.addItem)
    

        removeButton = QAction("Remove Item", self)
        

        editButton = QAction("Edit Item", self)

        
        
        
        
        toolbar.addActions([addButton,removeButton,editButton])
        self.addToolBar(toolbar)


        #TABLE SETUP
        self.tablerow=0
        self.rowCount=1
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setColumnWidth(0,250)
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,350)
        self.table.setHorizontalHeaderLabels(["restaurant"])
        self.table.setRowCount(self.rowCount)
        self.setCentralWidget(self.table)



        self.displayDataStart()

    def addItem(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Add item to list")
        self.dlg.layout = QFormLayout()

        message1 = QLabel("Input the restaurant name")
        message2 = QLabel("Separate the dishes by commas")
        message3 = QLabel("Input the price")

        self.resLine = QLineEdit()
        self.dishLine = QLineEdit()
        self.priceLine = QLineEdit()

        button=QPushButton("Add")
               
        
        
        
        
        
        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.resLine)
        self.dlg.layout.addRow(message2)
        self.dlg.layout.addRow(self.dishLine)
        self.dlg.layout.addRow(message3)
        self.dlg.layout.addRow(self.priceLine)
        self.dlg.layout.addRow(button)
        button.clicked.connect(lambda: self.printData())
        self.dlg.setFixedWidth(300)

        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()


    def refresh(self):
        #self.tablerow=0
        
        self.table.setRowCount(1)
        self.tablerow=0
        self.displayDataStart()
        

    def printData(self):
        string = self.resLine.text()
        string = "'"+string+"'"
        #print(string)  
        
        cursor=db.cursor()    
        cursor.execute("""INSERT INTO food VALUES(""" + string + """)""")
        db.commit()
        res=cursor.execute("SELECT * FROM food")
        for row in res:
            print(row)
        self.refresh()
        


        
        

        
      
        
    #TABLE DISPLAY DATA
    def displayDataStart(self):       
        cursor = db.cursor()
        cursor.execute('create table if not exists food(name varchar(255));')
        #cursor.execute("""INSERT INTO food VALUES('ford')""")
        db.commit()
        res=cursor.execute("SELECT * from food")
        counter=0
        for row in res:
            #print(row)
            self.table.setItem(self.tablerow,0, QTableWidgetItem(row[0]))
            self.tablerow=self.tablerow+1
            self.rowCount=self.rowCount+1
            counter+=1
            self.table.setRowCount(self.rowCount)
            
            
            
            

            
  