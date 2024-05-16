# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 500)
        Dialog.setMinimumSize(QSize(400, 500))
        Dialog.setMaximumSize(QSize(400, 500))
        self.header = QWidget(Dialog)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 400, 80))
        self.header.setStyleSheet(u"QWidget{\n"
"	background-color: #f1d275;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border: nune;\n"
"	padding: 10%;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"}")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 7, 180, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self.header)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 40, 400, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_diagnostic = QPushButton(self.widget)
        self.choose_diagnostic.setObjectName(u"choose_diagnostic")
        font1 = QFont()
        font1.setPointSize(11)
        self.choose_diagnostic.setFont(font1)
        self.choose_diagnostic.setCheckable(True)
        self.choose_diagnostic.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.choose_diagnostic)

        self.choose_parrameters = QPushButton(self.widget)
        self.choose_parrameters.setObjectName(u"choose_parrameters")
        self.choose_parrameters.setFont(font1)
        self.choose_parrameters.setCheckable(True)
        self.choose_parrameters.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.choose_parrameters)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 110, 380, 380))
        self.chose_diagnostic = QWidget()
        self.chose_diagnostic.setObjectName(u"chose_diagnostic")
        self.chose_diagnostic.setStyleSheet(u"Line{\n"
"	background-color: #ffb146;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	background-color: #f1d275;\n"
"	border: 1px solid #ffad3d;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QTableView{\n"
"	border: 1px solid #ffad3d;\n"
"}\n"
"\n"
"QTableView::section{\n"
"	background-color: #f1d275;\n"
"	color: white;\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}")
        self.widget1 = QWidget(self.chose_diagnostic)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 380, 380))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choose_diagnostc = QComboBox(self.widget1)
        self.choose_diagnostc.setObjectName(u"choose_diagnostc")
        font2 = QFont()
        font2.setPointSize(14)
        self.choose_diagnostc.setFont(font2)
        self.choose_diagnostc.setEditable(False)

        self.verticalLayout.addWidget(self.choose_diagnostc)

        self.choose_repair_plan = QComboBox(self.widget1)
        self.choose_repair_plan.setObjectName(u"choose_repair_plan")
        self.choose_repair_plan.setFont(font2)

        self.verticalLayout.addWidget(self.choose_repair_plan)

        self.repairs_table = QTableView(self.widget1)
        self.repairs_table.setObjectName(u"repairs_table")

        self.verticalLayout.addWidget(self.repairs_table)

        self.stackedWidget.addWidget(self.chose_diagnostic)
        self.parameters_repair = QWidget()
        self.parameters_repair.setObjectName(u"parameters_repair")
        self.parameters_repair.setStyleSheet(u"Line{\n"
"	background-color: #ffb146;\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	background-color: #f1d275;\n"
"	border: 1px solid #ffad3d;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}\n"
"\n"
"QTableView{\n"
"	border: 1px solid #ffad3d;\n"
"}\n"
"\n"
"QTableView::section{\n"
"	background-color: #f1d275;\n"
"	color: white;\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}")
        self.buttons = QWidget(self.parameters_repair)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setGeometry(QRect(0, 340, 380, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.buttons)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_characteristic = QPushButton(self.buttons)
        self.add_characteristic.setObjectName(u"add_characteristic")
        self.add_characteristic.setCheckable(True)
        self.add_characteristic.setChecked(False)

        self.horizontalLayout_3.addWidget(self.add_characteristic)

        self.edit_characteristic = QPushButton(self.buttons)
        self.edit_characteristic.setObjectName(u"edit_characteristic")
        self.edit_characteristic.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.edit_characteristic)

        self.delite_characteristic = QPushButton(self.buttons)
        self.delite_characteristic.setObjectName(u"delite_characteristic")
        self.delite_characteristic.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.delite_characteristic)

        self.go_to_repair = QPushButton(self.buttons)
        self.go_to_repair.setObjectName(u"go_to_repair")

        self.horizontalLayout_3.addWidget(self.go_to_repair)

        self.widget2 = QWidget(self.parameters_repair)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 380, 330))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.choose_diagnostc_par = QComboBox(self.widget2)
        self.choose_diagnostc_par.setObjectName(u"choose_diagnostc_par")
        self.choose_diagnostc_par.setFont(font2)
        self.choose_diagnostc_par.setEditable(False)

        self.verticalLayout_2.addWidget(self.choose_diagnostc_par)

        self.choose_repair_plan_par = QComboBox(self.widget2)
        self.choose_repair_plan_par.setObjectName(u"choose_repair_plan_par")
        self.choose_repair_plan_par.setFont(font2)

        self.verticalLayout_2.addWidget(self.choose_repair_plan_par)

        self.chatacteristics_table = QTableView(self.widget2)
        self.chatacteristics_table.setObjectName(u"chatacteristics_table")

        self.verticalLayout_2.addWidget(self.chatacteristics_table)

        self.stackedWidget.addWidget(self.parameters_repair)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"User", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u0433\u0438\u0442\u0430\u0440", None))
        self.choose_diagnostic.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0443", None))
        self.choose_parrameters.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.choose_diagnostc.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.choose_repair_plan.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.add_characteristic.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_characteristic.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delite_characteristic.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.go_to_repair.setText(QCoreApplication.translate("Dialog", u"\u043f\u0435\u0440\u0435\u0439\u0442\u0438", None))
        self.choose_diagnostc_par.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.choose_repair_plan_par.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
    # retranslateUi

