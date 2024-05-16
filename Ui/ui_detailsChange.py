# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datails_change.ui'
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
        Dialog.setStyleSheet(u"")
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
        self.fill_detail = QLineEdit(self.widget)
        self.fill_detail.setObjectName(u"fill_detail")
        self.fill_detail.setGeometry(QRect(10, 70, 220, 31))
        font = QFont()
        font.setPointSize(14)
        self.fill_detail.setFont(font)
        self.fill_detail.setDragEnabled(False)
        self.details = QLabel(self.widget)
        self.details.setObjectName(u"details")
        self.details.setGeometry(QRect(10, 10, 220, 40))
        font1 = QFont()
        font1.setPointSize(24)
        self.details.setFont(font1)
        self.details.setLayoutDirection(Qt.LeftToRight)
        self.save_detail = QPushButton(self.widget)
        self.save_detail.setObjectName(u"save_detail")
        self.save_detail.setGeometry(QRect(10, 120, 220, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0442\u0430\u043b\u0438", None))
        self.fill_detail.setText("")
        self.fill_detail.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.details.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0442\u0430\u043b\u0438", None))
        self.save_detail.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

