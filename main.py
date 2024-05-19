import sys
from PySide6.QtCore import Qt, QModelIndex

import PySide6.QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
from connection import Data
from addwindow import Ui_Dialog
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
class Tracker(QMainWindow): #создание класса приложения c наследованием функционала класса QMainWindow
    def __init__(self):
        super(Tracker, self).__init__() #вызов конструктора родительского класса QMainWindow
        self.ui = Ui_MainWindow() #создание экземпляра родительского класса
        self.ui.setupUi(self) #настройка
        self.connect = Data()

        self.view_data()
        self.refresh()

        self.ui.pb_add.clicked.connect(self.openAddWindow)
        self.ui.pb_edit.clicked.connect(self.openAddWindow)

        self.ui.pushButton_3.clicked.connect(self.delete)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('data')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        if self.ui.tableView.model().rowCount() < 1:
            self.ui.pushButton_3.setStyleSheet("QPushButton {font-color: black;background-color: rgba(0,0,0,30);border: 1px solid rgba(0,0,0,40);border-radius: 7px;width: 230px;height: 50px;}")

        else:
            self.ui.pushButton_3.setStyleSheet("QPushButton {font-color: white;background-color: rgba(255,255,255,30);border: 1px solid rgba(255,255,255,40);border-radius: 7px;width: 230px;height: 50px;} "
                                               "QPushButton:hover {background-color: rgba(255,255,255,50);} QPushButton:pressed {background-color: rgba(255,255,255,80);}")
    def refresh(self):
        self.ui.lb_valuern.setText(self.connect.totalBalance())
        self.ui.lb_textupmain.setText(self.connect.totalIncome())
        self.ui.lb_textdownmain.setText(self.connect.totalOutcome())
        self.ui.lb_foodvalue.setText(self.connect.totalFood())
        self.ui.lb_entervalue.setText(self.connect.totalEnter())
        self.ui.lb_subscrvalue.setText(self.connect.totalSubs())
        self.view_data()

    def openAddWindow(self):
        self.newWindow = QtWidgets.QDialog()
        self.uiNewWindow = Ui_Dialog()
        self.uiNewWindow.setupUi(self.newWindow)
        self.newWindow.show()
        sender = self.sender()
        if sender.text() == "Новая запись":
            self.uiNewWindow.btn_.clicked.connect(self.addNew)
        else:
            self.uiNewWindow.btn_.clicked.connect(self.edit)

    def addNew(self):
        date = self.uiNewWindow.dateEdit.text()
        cat = self.uiNewWindow.cb_categories.currentText()
        descr = self.uiNewWindow.le_descr.text()
        status = self.uiNewWindow.le_type.currentText()
        balance = self.uiNewWindow.le_balance.text()
        if balance == "" or balance == "-":
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка ввода")
            error.setStyleSheet(
                "QMessageBox{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9,112,121,1), stop:1 rgba(60,147,59,1))}")
            error.setText("Введите сумму операции")
            error.show()
            error.exec()
        else:
            self.connect.addQuery(date, cat, descr, balance, status)
            self.view_data()
            self.refresh()
            self.newWindow.close()

    # def valueCatcher(self):
    #     index = self.ui.tableView.selectedIndexes()[0]
    #     id = index.row()
    #     self.uiNewWindow.dateEdit.setText(str(self.ui.tableView.model().data(self.ui.tableView.model().index(id, 1))))
    #     self.uiNewWindow.cb_categories.setCurrentText(
    #         str(self.ui.tableView.model().data(self.ui.tableView.model().index(id, 2))))
    #     self.uiNewWindow.le_descr.setText(str(self.ui.tableView.model().data(self.ui.tableView.model().index(id, 3))))
    #     self.uiNewWindow.le_balance.setText(str(self.ui.tableView.model().data(self.ui.tableView.model().index(id, 4))))
    #     self.uiNewWindow.le_type.setCurrentText(
    #         str(self.ui.tableView.model().data(self.ui.tableView.model().index(id, 5))))

    def edit(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        date = self.uiNewWindow.dateEdit.text()
        cat = self.uiNewWindow.cb_categories.currentText()
        descr = self.uiNewWindow.le_descr.text()
        balance = self.uiNewWindow.le_balance.text()
        status = self.uiNewWindow.le_type.currentText()

        if balance == "" or balance == "-":
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка ввода")
            error.setStyleSheet(
                "QMessageBox{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9,112,121,1), stop:1 rgba(60,147,59,1))}")
            error.setText("Введите сумму операции")
            error.show()
            error.exec()
        else:
            self.connect.updateQuery(date, cat, descr, balance, status, id)
            self.newWindow.close()
            self.view_data()
            self.refresh()


    def delete(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.connect.deleteQuery(id)
        self.view_data()
        self.refresh()


if __name__ == "__main__": #определение точки входа в программу
    app = QApplication(sys.argv) #объявления приложения "приложением"
    window = Tracker()
    window.show() #отображение окна программы
    sys.exit(app.exec()) #закрытие по окончании цикла событий в приложении