import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow

class Tracker(QMainWindow): #создание класса приложения c наследованием функционала класса QMainWindow
    def __init__(self):
        super(Tracker, self).__init__() #вызов конструктора родительского класса QMainWindow
        self.ui = Ui_MainWindow() #создание экземпляра родительского класса
        self.ui.setupUi(self) #настройка

if __name__ == "__main__": #определение точки входа в программу
    app = QApplication(sys.argv) #объявления приложения "приложением"
    window = Tracker()
    window.show() #отображение окна программы
    sys.exit(app.exec()) #закрытие по окончании цикла событий в приложении


