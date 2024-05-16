# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(260, 190)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
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
        self.incorect_input = QLabel(self.widget)
        self.incorect_input.setObjectName(u"incorect_input")
        self.incorect_input.setGeometry(QRect(10, 10, 211, 101))
        font = QFont()
        font.setPointSize(20)
        self.incorect_input.setFont(font)
        self.incorect_input.setLayoutDirection(Qt.LeftToRight)
        self.error_ok = QPushButton(self.widget)
        self.error_ok.setObjectName(u"error_ok")
        self.error_ok.setGeometry(QRect(10, 120, 220, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.incorect_input.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0435\n"
"\u0432\u0445\u043e\u0434\u043d\u044b\u0435\n"
"\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.error_ok.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

