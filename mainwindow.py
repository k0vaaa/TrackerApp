# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(778, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9,121,109,1), stop:1 rgba(0,255,185,1));\n"
"font-family: Montserrat;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.status = QFrame(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.status)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lb_balancern = QLabel(self.status)
        self.lb_balancern.setObjectName(u"lb_balancern")
        self.lb_balancern.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_balancern)

        self.lb_valuern = QLabel(self.status)
        self.lb_valuern.setObjectName(u"lb_valuern")
        self.lb_valuern.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_valuern)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_iconup = QLabel(self.status)
        self.lb_iconup.setObjectName(u"lb_iconup")
        self.lb_iconup.setMaximumSize(QSize(50, 16777215))
        self.lb_iconup.setStyleSheet(u"background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.lb_iconup.setPixmap(QPixmap(u":/icons/icons/up.svg"))

        self.horizontalLayout.addWidget(self.lb_iconup)

        self.lb_textup = QLabel(self.status)
        self.lb_textup.setObjectName(u"lb_textup")
        self.lb_textup.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.lb_textup)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_textupmain = QLabel(self.status)
        self.lb_textupmain.setObjectName(u"lb_textupmain")
        self.lb_textupmain.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_textupmain)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_icondown = QLabel(self.status)
        self.lb_icondown.setObjectName(u"lb_icondown")
        self.lb_icondown.setMaximumSize(QSize(50, 16777215))
        self.lb_icondown.setStyleSheet(u"background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.lb_icondown.setPixmap(QPixmap(u":/icons/icons/down.svg"))

        self.horizontalLayout_2.addWidget(self.lb_icondown)

        self.lb_textdown = QLabel(self.status)
        self.lb_textdown.setObjectName(u"lb_textdown")
        self.lb_textdown.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.lb_textdown)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_textdownmain = QLabel(self.status)
        self.lb_textdownmain.setObjectName(u"lb_textdownmain")
        self.lb_textdownmain.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lb_textdownmain)


        self.horizontalLayout_6.addWidget(self.status)

        self.categories = QFrame(self.centralwidget)
        self.categories.setObjectName(u"categories")
        self.categories.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.lb_cattitle = QLabel(self.categories)
        self.lb_cattitle.setObjectName(u"lb_cattitle")
        self.lb_cattitle.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.lb_cattitle)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_iconfood = QLabel(self.categories)
        self.lb_iconfood.setObjectName(u"lb_iconfood")
        self.lb_iconfood.setMaximumSize(QSize(50, 16777215))
        self.lb_iconfood.setStyleSheet(u"background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.lb_iconfood.setPixmap(QPixmap(u":/icons/icons/food.svg"))

        self.horizontalLayout_5.addWidget(self.lb_iconfood)

        self.lb_foodname = QLabel(self.categories)
        self.lb_foodname.setObjectName(u"lb_foodname")
        self.lb_foodname.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lb_foodname)

        self.lb_foodvalue = QLabel(self.categories)
        self.lb_foodvalue.setObjectName(u"lb_foodvalue")
        self.lb_foodvalue.setStyleSheet(u"color: white;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lb_foodvalue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_iconenter = QLabel(self.categories)
        self.lb_iconenter.setObjectName(u"lb_iconenter")
        self.lb_iconenter.setMaximumSize(QSize(50, 16777215))
        self.lb_iconenter.setStyleSheet(u"background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.lb_iconenter.setPixmap(QPixmap(u":/icons/icons/enter.svg"))

        self.horizontalLayout_4.addWidget(self.lb_iconenter)

        self.lb_entername = QLabel(self.categories)
        self.lb_entername.setObjectName(u"lb_entername")
        self.lb_entername.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lb_entername)

        self.lb_entervalue = QLabel(self.categories)
        self.lb_entervalue.setObjectName(u"lb_entervalue")
        self.lb_entervalue.setStyleSheet(u"color: white;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lb_entervalue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_icon_subscr = QLabel(self.categories)
        self.lb_icon_subscr.setObjectName(u"lb_icon_subscr")
        self.lb_icon_subscr.setMaximumSize(QSize(50, 16777215))
        self.lb_icon_subscr.setStyleSheet(u"background-color: none;\n"
"padding-top: 10px;\n"
"border: none;")
        self.lb_icon_subscr.setPixmap(QPixmap(u":/icons/icons/sub.svg"))

        self.horizontalLayout_3.addWidget(self.lb_icon_subscr)

        self.lb_subscrname = QLabel(self.categories)
        self.lb_subscrname.setObjectName(u"lb_subscrname")
        self.lb_subscrname.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lb_subscrname)

        self.lb_subscrvalue = QLabel(self.categories)
        self.lb_subscrvalue.setObjectName(u"lb_subscrvalue")
        self.lb_subscrvalue.setStyleSheet(u"color: white;\n"
"font-size: 16px;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lb_subscrvalue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addWidget(self.categories)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pb_add = QPushButton(self.centralwidget)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setStyleSheet(u"QPushButton {\n"
"font-color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"};\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_add.setIcon(icon)
        self.pb_add.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pb_add)

        self.pb_edit = QPushButton(self.centralwidget)
        self.pb_edit.setObjectName(u"pb_edit")
        self.pb_edit.setStyleSheet(u"QPushButton {\n"
"font-color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"};\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_edit.setIcon(icon1)
        self.pb_edit.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pb_edit)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"font-color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"};\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color:  rgb(53,53,53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: 1px solid rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MyTracker", None))
        self.lb_balancern.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0431\u0430\u043b\u0430\u043d\u0441:", None))
        self.lb_valuern.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_iconup.setText("")
        self.lb_textup.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.lb_textupmain.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_icondown.setText("")
        self.lb_textdown.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.lb_textdownmain.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_cattitle.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u0440\u0430\u0442", None))
        self.lb_iconfood.setText("")
        self.lb_foodname.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0434\u0430", None))
        self.lb_foodvalue.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_iconenter.setText("")
        self.lb_entername.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.lb_entervalue.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lb_icon_subscr.setText("")
        self.lb_subscrname.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438", None))
        self.lb_subscrvalue.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.pb_add.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pb_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

