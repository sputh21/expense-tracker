from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt6.QtWidgets import QTableView, QApplication
import sys
import MySQLdb as mdb


SERVER_NAME = '<Server Name>'
DATABASE_NAME = '<Database Name>'
USERNAME = ''
PASSWORD = ''
db = mdb.connect('localhost', 'localhost', '1283', 'foodData')

def displayData(sqlStatement):
    print('processing query...')
    qry = QSqlQuery()
    qry.prepare(sqlStatement)
    qry.exec()

    model = QSqlQueryModel()
    model.setQuery(qry)

    view = QTableView()
    view.setModel(model)
    return view    

if __name__=='__main__':
    app = QApplication(sys.argv)

    
    SQL_STATEMENT = 'SELECT * FROM foodData'
    dataView = displayData(SQL_STATEMENT)
    dataView.show()
        
    app.exit()
    sys.exit(app.exec())