# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 322)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9,121,109,1), stop:1 rgba(0,255,185,1));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_add = QLabel(self.frame)
        self.lbl_add.setObjectName(u"lbl_add")
        self.lbl_add.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_add.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_add)

        self.cb_categories = QComboBox(self.frame)
        self.cb_categories.addItem("")
        self.cb_categories.addItem("")
        self.cb_categories.addItem("")
        self.cb_categories.setObjectName(u"cb_categories")
        self.cb_categories.setAutoFillBackground(False)
        self.cb_categories.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"font-size: 16pt;\n"
"}")

        self.verticalLayout.addWidget(self.cb_categories)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 5px;")
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.verticalLayout.addWidget(self.dateEdit)

        self.le_descr = QLineEdit(self.frame)
        self.le_descr.setObjectName(u"le_descr")
        self.le_descr.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 5px;")

        self.verticalLayout.addWidget(self.le_descr)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 5px;")

        self.verticalLayout.addWidget(self.le_balance)

        self.le_type = QComboBox(self.frame)
        self.le_type.addItem("")
        self.le_type.addItem("")
        self.le_type.setObjectName(u"le_type")
        self.le_type.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"font-size: 16pt;\n"
"}")

        self.verticalLayout.addWidget(self.le_type)

        self.btn_ = QPushButton(self.frame)
        self.btn_.setObjectName(u"btn_")
        self.btn_.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_.setIcon(icon)

        self.verticalLayout.addWidget(self.btn_)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_categories.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_add.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.cb_categories.setItemText(0, QCoreApplication.translate("Dialog", u"\u0415\u0434\u0430", None))
        self.cb_categories.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.cb_categories.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438", None))

        self.cb_categories.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e...", None))
        self.le_descr.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439...", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430...", None))
        self.le_type.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.le_type.setItemText(1, QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))

        self.btn_.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

