# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repair_plan_change.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(260, 190)
        Dialog.setMinimumSize(QSize(260, 190))
        Dialog.setMaximumSize(QSize(260, 190))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 240, 170))
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
        self.fill_repair_plan = QLineEdit(self.widget)
        self.fill_repair_plan.setObjectName(u"fill_repair_plan")
        self.fill_repair_plan.setGeometry(QRect(10, 70, 220, 31))
        font = QFont()
        font.setPointSize(14)
        self.fill_repair_plan.setFont(font)
        self.repair_plan = QLabel(self.widget)
        self.repair_plan.setObjectName(u"repair_plan")
        self.repair_plan.setGeometry(QRect(10, 10, 220, 40))
        font1 = QFont()
        font1.setPointSize(19)
        self.repair_plan.setFont(font1)
        self.repair_plan.setLayoutDirection(Qt.LeftToRight)
        self.save_repair_plan = QPushButton(self.widget)
        self.save_repair_plan.setObjectName(u"save_repair_plan")
        self.save_repair_plan.setGeometry(QRect(10, 120, 220, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.fill_repair_plan.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043f\u043e\u0441\u043e\u0431\u0430", None))
        self.repair_plan.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u0441\u043e\u0431\u044b \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.save_repair_plan.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

