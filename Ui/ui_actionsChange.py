# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actions_change.ui'
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
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 260)
        Dialog.setMinimumSize(QSize(300, 260))
        Dialog.setMaximumSize(QSize(300, 260))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 280, 220))
        self.widget.setStyleSheet(u"QLabel{\n"
"	color: #ff9f1b;\n"
"}\n"
"\n"
"QTextEdit{\n"
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
        self.steps = QLabel(self.widget)
        self.steps.setObjectName(u"steps")
        self.steps.setGeometry(QRect(10, 10, 220, 40))
        font = QFont()
        font.setPointSize(24)
        self.steps.setFont(font)
        self.steps.setLayoutDirection(Qt.LeftToRight)
        self.save_action = QPushButton(self.widget)
        self.save_action.setObjectName(u"save_action")
        self.save_action.setGeometry(QRect(10, 170, 260, 32))
        self.fill_action = QTextEdit(self.widget)
        self.fill_action.setObjectName(u"fill_action")
        self.fill_action.setGeometry(QRect(10, 60, 260, 101))
        self.fill_action.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.fill_action.setOverwriteMode(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Action", None))
        self.steps.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.save_action.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.fill_action.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.fill_action.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
    # retranslateUi

