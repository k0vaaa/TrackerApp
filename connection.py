from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data,self).__init__()
        self.createConnection()

    def createConnection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None,"Не удается установить соединение с базой данных.",QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS data (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True

    def executeQueryWithParams(self, sql_query, query_values = None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def addQuery(self, date, category, description, balance, status):
        sql_query = "INSERT INTO data (Date, Category, Description, Balance, Status) VALUES (?,?,?,?,?)"
        self.executeQueryWithParams(sql_query,[date,category,description,balance,status])

    def updateQuery(self, date, category, description, balance, status, id):
        sql_query = "UPDATE data SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.executeQueryWithParams(sql_query,[date,category,description, balance,status,id])

    def deleteQuery(self,id):
        sql_query = "DELETE FROM data  WHERE ID=?"
        self.executeQueryWithParams(sql_query,[id])

    # def selectQuery(self,id):
    #     sql_query = "SELECT * FROM data WHERE ID=?"
    #     self.executeQueryWithParams(sql_query, [id])


    def getTotal(self, column, filter=None, value=None, case_when = None):
        # Инициализация SQL запроса
        if case_when:
            sql_query = f"SELECT SUM(CASE WHEN {case_when['filter']} = '{case_when['value1']}' THEN {column} ELSE 0 END) - SUM(CASE WHEN {case_when['filter']} = '{case_when['value2']}' THEN {column} ELSE 0 END) AS total_balance FROM data"
        else:
            sql_query = f"SELECT SUM({column}) FROM data"

        query_values = []

        if filter and value is not None:
            sql_query += f" WHERE {filter} = ?"
            query_values.append(value)

        # Выполнение запроса
        query = self.executeQueryWithParams(sql_query, query_values)
        
        if query.next():
            return str(query.value(0)) + " ₽"
        return '0 ₽'

    def totalBalance(self):
        return self.getTotal(column="Balance", case_when={"filter": "Status", "value1": "Поступление", "value2": "Списание"})

    def totalIncome(self):
        return self.getTotal(column="Balance",filter="Status", value="Поступление")

    def totalOutcome(self):
        return self.getTotal(column="Balance",filter="Status", value="Списание")

    def totalFood(self):
        return self.getTotal(column="Balance",filter="Category", value="Еда", case_when={"filter": "Status", "value1": "Поступление", "value2": "Списание"})

    def totalEnter(self):
        return self.getTotal(column="Balance",filter="Category", value="Развлечения", case_when={"filter": "Status", "value1": "Поступление", "value2": "Списание"})

    def totalSubs(self):
        return self.getTotal(column="Balance",filter="Category", value="Подписки", case_when={"filter": "Status", "value1": "Поступление", "value2": "Списание"})

