from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
import sqlite3 as sqlite

global db 

db = sqlite.connect("food.db")
cursor = db.cursor()

class tableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #TOOLBAR SETUP
        toolbar = QToolBar("New Bar")

        addButton = QAction("Add Item", self)
        addButton.triggered.connect(self.popUpAdd)
    
        removeButton = QAction("Remove Item", self)
        removeButton.triggered.connect(self.popUpRemove)

        editButton = QAction("Edit Item", self)

        toolbar.addActions([addButton,removeButton,editButton])
        self.addToolBar(toolbar)
        #TABLE SETUP###############################################
        self.tablerow=0
        self.rowCount=1
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0,250)
        self.table.setColumnWidth(1,250)
        self.table.setColumnWidth(2,250)
        self.table.setHorizontalHeaderLabels(["restaurant", "dishes", "price"])
        self.table.setRowCount(self.rowCount)
        self.setCentralWidget(self.table)
        self.displayDataStart()
    ##############################################################
    def popUpAdd(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Add item")
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
        button.clicked.connect(lambda: self.setData())
        self.dlg.setFixedWidth(300)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
    ############################################################
    def setData(self):
        string = self.resLine.text()
        string2 = self.dishLine.text()
        string3 = self.priceLine.text()

        string = "'"+string+"'," 
        string2 = "'"+string2+"',"
        qry = """INSERT INTO food VALUES(""" + string + string2 + string3 + """)"""
        cursor.execute(qry)
        db.commit()
        res=cursor.execute("SELECT * FROM food")
        for row in res:
            print(row)
        self.refresh()
    ############################################################
    def popUpRemove(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Remove item")
        self.dlg.layout = QFormLayout()
        message1 = QLabel("Input the restaurant name")
        message3 = QLabel("Input the price")
        self.resLine = QLineEdit()
        self.dishLine = QLineEdit()
        self.priceLine = QLineEdit()
        button=QPushButton("Remove")
        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.resLine)
        self.dlg.layout.addRow(message3)
        self.dlg.layout.addRow(self.priceLine)
        self.dlg.layout.addRow(button)
        button.clicked.connect(lambda: self.removeData())
        self.dlg.setFixedWidth(300)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
    ############################################################
    def removeData(self):
        string1 = self.resLine.text()
        string2 = self.priceLine.text()
        string1 = "'"+string1+"'"
        qry = "DELETE FROM food WHERE restaurant = "+string1 + " AND price = "+string2
        cursor.execute(qry)
        db.commit()
        


    ###########################################################
    def refresh(self):
        self.table.setRowCount(1)
        self.tablerow=0
        self.displayDataStart() 
    #TABLE DISPLAY DATA###########################################################
    def displayDataStart(self):       
        cursor = db.cursor()
        cursor.execute('create table if not exists food(restaurant varchar(255), dishes varchar(1024), price varchar(5));')
        #cursor.execute("""INSERT INTO food VALUES('ford')""")
        db.commit()
        res=cursor.execute("SELECT * from food")
        counter=0
        for row in res:
            #print(row)
            self.table.setItem(self.tablerow,0, QTableWidgetItem(row[0]))
            self.table.setItem(self.tablerow,1, QTableWidgetItem(row[1]))
            self.table.setItem(self.tablerow,2, QTableWidgetItem(row[2]))
            self.tablerow=self.tablerow+1
            self.rowCount=self.rowCount+1
            counter+=1
            self.table.setRowCount(self.rowCount)
            
            
            
            

            
  