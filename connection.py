from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data,self).__init__()
        self.createConnection()

    def createConnection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        # db.databaseName()

        if not db.open():
            QtWidgets.QMessageBox.critical(None,"Не удается установить соединение с базой данных.",QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS data (ID integer primary key AUTOINCREMENT, Date VARCHAR(20),"
                   "Category VARCHAR(20), Description VARCHAR(20), Balance MONEY, Status VARCHAR(20))")
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
        self.executeQueryWithParams(sql_query,[date,category,description, balance,status])

    def updateQuery(self, date, category, description, balance, status, id):
        sql_query = "UPDATE data SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.executeQueryWithParams(sql_query,[date,category,description, balance,status,id])

    def deleteQuery(self,id):
        sql_query = "DELETE * FROM data  WHERE ID=?"
        self.executeQueryWithParams(sql_query,[id])

    # def getTotal(self, column, filter = None, value = None):
    #     sql_query= f"SELECT SUM({column}) FROM data"
    #     if filter is not None and value is not None:
    #         sql_query += f"WHERE {filter} = ?"
    #
    #     query_values = []
    #
    #     if value is not None:
    #         query_values.append(value)
    #
    #     query = self.executeQueryWithParams(sql_query, query_values)
    #
    #     if query.next():
    #         return str(query.value(0)) + " ₽"
    #     return '0 ₽'

    def getTotal(self, column, filter=None, value=None, fortotal = None):
        # Инициализация SQL запроса
        sql_query = f"SELECT SUM({column}) FROM data"
        query_values = []

        # Добавление условия фильтрации, если задано
        if filter and value is not None:
            sql_query += f" WHERE {filter} = ?"
            query_values.append(value)

        # Выполнение запроса
        query = self.executeQueryWithParams(sql_query, query_values)

        # Проверка и возврат результата
        if query.next():
            # if fortotal != None:

            return str(query.value(0)) + " ₽"
        return '0 ₽'

    def totalBalance(self):
        return self.getTotal(column="Balance")

    def totalIncome(self):
        return self.getTotal(column="Balance",filter="Status", value="Поступление")

    def totalOutcome(self):
        return self.getTotal(column="Balance",filter="Status", value="Списание")

    def totalFood(self):
        return self.getTotal(column="Balance",filter="Category", value="Еда")

    def totalEnter(self):
        return self.getTotal(column="Balance",filter="Category", value="Развлечения")

    def totalSubs(self):
        return self.getTotal(column="Balance",filter="Category", value="Подписки")
