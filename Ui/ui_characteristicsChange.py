# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'characteristic_change.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 290)
        Dialog.setMinimumSize(QSize(400, 290))
        Dialog.setMaximumSize(QSize(400, 290))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 380, 270))
        self.widget.setStyleSheet(u"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #ffad3d;\n"
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
"}")
        self.characteristics = QLabel(self.widget)
        self.characteristics.setObjectName(u"characteristics")
        self.characteristics.setGeometry(QRect(10, 10, 360, 40))
        font = QFont()
        font.setPointSize(24)
        self.characteristics.setFont(font)
        self.fill_characteristic = QLineEdit(self.widget)
        self.fill_characteristic.setObjectName(u"fill_characteristic")
        self.fill_characteristic.setGeometry(QRect(10, 70, 360, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.fill_characteristic.setFont(font1)
        self.fill_acceptable_values = QLineEdit(self.widget)
        self.fill_acceptable_values.setObjectName(u"fill_acceptable_values")
        self.fill_acceptable_values.setGeometry(QRect(10, 120, 360, 31))
        self.fill_acceptable_values.setFont(font1)
        self.save_characteristic = QPushButton(self.widget)
        self.save_characteristic.setObjectName(u"save_characteristic")
        self.save_characteristic.setGeometry(QRect(80, 220, 220, 32))
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 170, 361, 29))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.min_acceptable_vavue = QLineEdit(self.widget1)
        self.min_acceptable_vavue.setObjectName(u"min_acceptable_vavue")
        self.min_acceptable_vavue.setFont(font1)

        self.horizontalLayout.addWidget(self.min_acceptable_vavue)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.nax_acceptable_value = QLineEdit(self.widget1)
        self.nax_acceptable_value.setObjectName(u"nax_acceptable_value")
        self.nax_acceptable_value.setFont(font1)

        self.horizontalLayout.addWidget(self.nax_acceptable_value)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.characteristics.setText(QCoreApplication.translate("Dialog", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.fill_characteristic.setText("")
        self.fill_characteristic.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.fill_acceptable_values.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.save_characteristic.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.min_acceptable_vavue.setText("")
        self.min_acceptable_vavue.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043d \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u2014", None))
        self.nax_acceptable_value.setText("")
        self.nax_acceptable_value.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u043a\u0441 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
    # retranslateUi

