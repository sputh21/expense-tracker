from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtSql import *
import sqlite3 as sqlite

global db 

db = sqlite.connect("food.db")
cursor = db.cursor()

class foodTableWindow(QMainWindow):
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
        self.table.setColumnWidth(0,100)
        self.table.setColumnWidth(1,250)
        self.table.setColumnWidth(2,100)
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
        #TODO: fix display when removing data and add error messages
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
            



class streaming(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)           
        toolbar = QToolBar()
        addButton = QAction("Add Item", self)
        addButton.triggered.connect(self.popUpAdd)
        
        removeButton = QAction("Remove Item", self)
        removeButton.triggered.connect(self.popUpRemove)
    
        editButton = QAction("Edit Item", self)

        toolbar.addActions([addButton,removeButton,editButton])
        self.addToolBar(toolbar)
        ##########################################################
        self.tablerow=0
        self.rowCount=1
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0,100)
        self.table.setColumnWidth(1,100)
        self.table.setHorizontalHeaderLabels(["name", "Monthly Price"])
        self.table.setRowCount(self.rowCount)
        self.setCentralWidget(self.table)
        
        self.displayDataStart()
        #############################################################    
    def popUpAdd(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Add item")
        self.dlg.layout = QFormLayout()

        message1 = QLabel("Name of the streaming service")
        message2 = QLabel("What is the monthly price?")

        self.streamLine = QLineEdit()
        self.costLine = QLineEdit()

        button=QPushButton("Add")
        button.clicked.connect(lambda: self.setData())

        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.streamLine)
        self.dlg.layout.addRow(message2)
        self.dlg.layout.addRow(self.costLine)
        self.dlg.layout.addRow(button)
        
        self.dlg.setFixedWidth(250)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
        ############################################################
    def setData(self):
        string = self.streamLine.text()
        string2 = self.costLine.text()
        string = "'"+string+"'," 
        string2 = "'"+string2+"'"
        qry = """INSERT INTO streaming VALUES(""" + string + string2 + """)"""
        cursor.execute(qry)
        db.commit()
        res=cursor.execute("SELECT * FROM streaming")
        for row in res:
            print(row)
        self.refresh() 
        ###########################################################
    def popUpRemove(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Remove item")
        self.dlg.layout = QFormLayout()

        message1 = QLabel("Input the streaming service name")
        message3 = QLabel("Input the monthly cost")

        self.streamLine = QLineEdit()
        self.costLine = QLineEdit()

        button=QPushButton("Remove")
        button.clicked.connect(lambda: self.removeData())

        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.streamLine)
        self.dlg.layout.addRow(message3)
        self.dlg.layout.addRow(self.costLine)
        self.dlg.layout.addRow(button)

        self.dlg.setFixedWidth(300)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
        ###########################################################
    def removeItem(self):
        string1 = self.streamLine.text()
        string2 = self.costLine.text()
        string1 = "'"+string1+"'"
        qry = "DELETE FROM streaming WHERE service = "+string1 + " AND price = "+string2
        cursor.execute(qry)
        db.commit()
        ###########################################################
    def refresh(self):
        self.table.setRowCount(1)
        self.tablerow=0
        self.displayDataStart()
        ###########################################################
    def displayDataStart(self):       
        cursor.execute('create table if not exists streaming(service varchar(255), price varchar(4));')
        db.commit()
        res=cursor.execute("SELECT * from streaming")
        counter=0
        for row in res:
            self.table.setItem(self.tablerow,0, QTableWidgetItem(row[0]))
            self.table.setItem(self.tablerow,1, QTableWidgetItem(row[1]))
            self.tablerow=self.tablerow+1
            self.rowCount=self.rowCount+1
            counter+=1
            self.table.setRowCount(self.rowCount)

class personal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)           
        toolbar = QToolBar()
        addButton = QAction("Add Item", self)
        addButton.triggered.connect(self.popUpAdd)
        
        removeButton = QAction("Remove Item", self)
        removeButton.triggered.connect(self.popUpRemove)
    
        editButton = QAction("Edit Item", self)

        toolbar.addActions([addButton,removeButton,editButton])
        self.addToolBar(toolbar)
        ##########################################################
        self.tablerow=0
        self.rowCount=1
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0,100)
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,100)
        self.table.setHorizontalHeaderLabels(["name", "Total Price", "Date of Purchase"])
        self.table.setRowCount(self.rowCount)
        self.setCentralWidget(self.table)
        
        self.displayDataStart()
        #############################################################    
    def popUpAdd(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Add item")
        self.dlg.layout = QFormLayout()

        message1 = QLabel("What was the purchase")
        message2 = QLabel("What is the total price?")
        message3 = QLabel("What is the date of purchase?")

        self.nameLine = QLineEdit()
        self.costLine = QLineEdit()
        self.dateLine = QLineEdit()


        button=QPushButton("Add")
        button.clicked.connect(lambda: self.setData())

        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.streamLine)
        self.dlg.layout.addRow(message2)
        self.dlg.layout.addRow(self.costLine)
        self.dlg.layout.addRow(message3)
        self.dlg.layout.addRow(self.dateLine)
        self.dlg.layout.addRow(button)
        
        self.dlg.setFixedWidth(250)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
        ############################################################
    def setData(self):
        string = self.streamLine.text()
        string2 = self.costLine.text()
        string3 = self.dateLine.text()
        string = "'"+string+"',"
        string2 = "'"+string2+"'," 
        string3 = "'"+string3+"'"
        qry = """INSERT INTO personalItems VALUES(""" + string + string2 + string3 + """)"""
        cursor.execute(qry)
        db.commit()
        res=cursor.execute("SELECT * FROM personalItems")
        for row in res:
            print(row)
        self.refresh() 
        ###########################################################
    def popUpRemove(self):
        self.dlg = QDialog()
        self.dlg.setWindowTitle("Remove item")
        self.dlg.layout = QFormLayout()

        message1 = QLabel("Input the name of the item you want to remove")
        message3 = QLabel("Input the date of purchase of the item you want to remove")
        message2 = QLabel("Input the total price of the item you want to remove")


        self.streamLine = QLineEdit()
        self.dateLine = QLineEdit()
        self.costLine = QLineEdit()


        button=QPushButton("Remove")
        button.clicked.connect(lambda: self.removeData())

        self.dlg.layout.addRow(message1)
        self.dlg.layout.addRow(self.streamLine)
        self.dlg.layout.addRow(message3)
        self.dlg.layout.addRow(self.costLine)
        self.dlg.layout.addRow(message2)
        self.dlg.layout.addRow(self.dateLine)
        self.dlg.layout.addRow(button)

        self.dlg.setFixedWidth(300)
        self.dlg.setLayout(self.dlg.layout)
        self.dlg.exec()
        ###########################################################
    def removeItem(self):
        string1 = self.streamLine.text()
        string2 = self.costLine.text()
        string3 = self.dateLine.text()

        string1 = "'"+string1+"'"
        string2 = "'"+string2+"'"
        string3 = "'"+string3+"'"

        qry = "DELETE FROM personalItems WHERE name = "+string1 + " AND price = "+string2 + "AND date = "+string3  

        cursor.execute(qry)
        db.commit()
        ###########################################################
    def refresh(self):
        self.table.setRowCount(1)
        self.tablerow=0
        self.displayDataStart()
        ###########################################################
    def displayDataStart(self):       
        cursor.execute('create table if not exists personalItems(name varchar(255), price varchar(4), date varchar(10));')
        db.commit()
        res=cursor.execute("SELECT * from personalItems")
        counter=0
        for row in res:
            self.table.setItem(self.tablerow,0, QTableWidgetItem(row[0]))
            self.table.setItem(self.tablerow,1, QTableWidgetItem(row[1]))
            self.table.setItem(self.tablerow,2, QTableWidgetItem(row[2]))
            self.tablerow=self.tablerow+1
            self.rowCount=self.rowCount+1
            counter+=1
            self.table.setRowCount(self.rowCount)