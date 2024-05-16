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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sideMenu = QWidget(self.centralwidget)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setGeometry(QRect(0, 0, 200, 500))
        self.sideMenu.setStyleSheet(u"QWidget{\n"
"	background-color: #f1d275;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border: nune;\n"
"	padding: 10%;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding-left: 15%;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #ff9d16;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #ff9d16;\n"
"}")
        self.label = QLabel(self.sideMenu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.layoutWidget = QWidget(self.sideMenu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 201, 272))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.details_button = QPushButton(self.layoutWidget)
        self.details_button.setObjectName(u"details_button")
        self.details_button.setEnabled(True)
        self.details_button.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(16)
        self.details_button.setFont(font1)
        self.details_button.setMouseTracking(True)
        self.details_button.setAutoFillBackground(False)
        self.details_button.setStyleSheet(u"")
        self.details_button.setCheckable(True)
        self.details_button.setChecked(True)
        self.details_button.setAutoRepeat(False)
        self.details_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.details_button)

        self.characteristics_button = QPushButton(self.layoutWidget)
        self.characteristics_button.setObjectName(u"characteristics_button")
        self.characteristics_button.setEnabled(True)
        self.characteristics_button.setMinimumSize(QSize(0, 0))
        self.characteristics_button.setFont(font1)
        self.characteristics_button.setMouseTracking(True)
        self.characteristics_button.setAutoFillBackground(False)
        self.characteristics_button.setStyleSheet(u"")
        self.characteristics_button.setCheckable(True)
        self.characteristics_button.setAutoRepeat(False)
        self.characteristics_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.characteristics_button)

        self.diagnostic_button = QPushButton(self.layoutWidget)
        self.diagnostic_button.setObjectName(u"diagnostic_button")
        self.diagnostic_button.setEnabled(True)
        self.diagnostic_button.setMinimumSize(QSize(0, 0))
        self.diagnostic_button.setFont(font1)
        self.diagnostic_button.setMouseTracking(True)
        self.diagnostic_button.setStyleSheet(u"")
        self.diagnostic_button.setCheckable(True)
        self.diagnostic_button.setAutoRepeat(False)
        self.diagnostic_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.diagnostic_button)

        self.actions_button = QPushButton(self.layoutWidget)
        self.actions_button.setObjectName(u"actions_button")
        self.actions_button.setEnabled(True)
        self.actions_button.setMinimumSize(QSize(0, 0))
        self.actions_button.setFont(font1)
        self.actions_button.setMouseTracking(True)
        self.actions_button.setAutoFillBackground(False)
        self.actions_button.setStyleSheet(u"")
        self.actions_button.setCheckable(True)
        self.actions_button.setAutoRepeat(False)
        self.actions_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.actions_button)

        self.repairs_button = QPushButton(self.layoutWidget)
        self.repairs_button.setObjectName(u"repairs_button")
        self.repairs_button.setEnabled(True)
        self.repairs_button.setMinimumSize(QSize(0, 0))
        self.repairs_button.setFont(font1)
        self.repairs_button.setMouseTracking(True)
        self.repairs_button.setStyleSheet(u"")
        self.repairs_button.setCheckable(True)
        self.repairs_button.setAutoRepeat(False)
        self.repairs_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.repairs_button)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(220, 20, 560, 460))
        self.details_page = QWidget()
        self.details_page.setObjectName(u"details_page")
        self.details_page.setAutoFillBackground(False)
        self.details_page.setStyleSheet(u"Line{\n"
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
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.line_2 = QFrame(self.details_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 45, 560, 2))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_2 = QLabel(self.details_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 560, 40))
        font2 = QFont()
        font2.setPointSize(24)
        self.label_2.setFont(font2)
        self.details_data = QWidget(self.details_page)
        self.details_data.setObjectName(u"details_data")
        self.details_data.setGeometry(QRect(0, 60, 560, 400))
        self.verticalLayout_2 = QVBoxLayout(self.details_data)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.detaild_table = QTableView(self.details_data)
        self.detaild_table.setObjectName(u"detaild_table")
        self.detaild_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.detaild_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.detaild_table.setDragDropOverwriteMode(False)
        self.detaild_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.detaild_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.detaild_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.detaild_table.horizontalHeader().setCascadingSectionResizes(True)
        self.detaild_table.horizontalHeader().setStretchLastSection(True)
        self.detaild_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.detaild_table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_detail = QPushButton(self.details_data)
        self.add_detail.setObjectName(u"add_detail")
        self.add_detail.setCheckable(True)
        self.add_detail.setChecked(False)

        self.horizontalLayout.addWidget(self.add_detail)

        self.edit__detail = QPushButton(self.details_data)
        self.edit__detail.setObjectName(u"edit__detail")
        self.edit__detail.setCheckable(True)

        self.horizontalLayout.addWidget(self.edit__detail)

        self.delite_detail = QPushButton(self.details_data)
        self.delite_detail.setObjectName(u"delite_detail")
        self.delite_detail.setCheckable(True)

        self.horizontalLayout.addWidget(self.delite_detail)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.details_page)
        self.diagnistic_page = QWidget()
        self.diagnistic_page.setObjectName(u"diagnistic_page")
        self.diagnistic_page.setStyleSheet(u"Line{\n"
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
"QComboBox {\n"
"	border: 1px solid #ffad3d;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableView{\n"
"	border: 1px solid #ffad3d;\n"
"}\n"
"\n"
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.diagnistic_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 560, 40))
        self.label_3.setFont(font2)
        self.line_4 = QFrame(self.diagnistic_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 45, 560, 2))
        self.line_4.setAutoFillBackground(False)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.choose_diagnostic = QComboBox(self.diagnistic_page)
        self.choose_diagnostic.setObjectName(u"choose_diagnostic")
        self.choose_diagnostic.setGeometry(QRect(0, 60, 560, 26))
        font3 = QFont()
        font3.setPointSize(14)
        self.choose_diagnostic.setFont(font3)
        self.choose_diagnostic.setEditable(False)
        self.actions_data_1 = QWidget(self.diagnistic_page)
        self.actions_data_1.setObjectName(u"actions_data_1")
        self.actions_data_1.setGeometry(QRect(0, 130, 560, 320))
        self.verticalLayout_8 = QVBoxLayout(self.actions_data_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.diagnostic_characteristic_table = QTableView(self.actions_data_1)
        self.diagnostic_characteristic_table.setObjectName(u"diagnostic_characteristic_table")
        self.diagnostic_characteristic_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.diagnostic_characteristic_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.diagnostic_characteristic_table.setDragDropOverwriteMode(False)
        self.diagnostic_characteristic_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.diagnostic_characteristic_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.diagnostic_characteristic_table.horizontalHeader().setCascadingSectionResizes(True)
        self.diagnostic_characteristic_table.horizontalHeader().setStretchLastSection(True)
        self.diagnostic_characteristic_table.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.diagnostic_characteristic_table)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.add_diagnostic_characteristic = QPushButton(self.actions_data_1)
        self.add_diagnostic_characteristic.setObjectName(u"add_diagnostic_characteristic")
        self.add_diagnostic_characteristic.setCheckable(True)
        self.add_diagnostic_characteristic.setChecked(False)

        self.horizontalLayout_7.addWidget(self.add_diagnostic_characteristic)

        self.delite_diagnostic_characteristic = QPushButton(self.actions_data_1)
        self.delite_diagnostic_characteristic.setObjectName(u"delite_diagnostic_characteristic")
        self.delite_diagnostic_characteristic.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.delite_diagnostic_characteristic)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.widget_2 = QWidget(self.diagnistic_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 90, 560, 34))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(560, 34))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.update_diagnostic = QPushButton(self.widget_2)
        self.update_diagnostic.setObjectName(u"update_diagnostic")
        self.update_diagnostic.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.update_diagnostic)

        self.add_diagnostic = QPushButton(self.widget_2)
        self.add_diagnostic.setObjectName(u"add_diagnostic")
        self.add_diagnostic.setCheckable(True)
        self.add_diagnostic.setChecked(False)

        self.horizontalLayout_9.addWidget(self.add_diagnostic)

        self.delite_diagnostic = QPushButton(self.widget_2)
        self.delite_diagnostic.setObjectName(u"delite_diagnostic")
        self.delite_diagnostic.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.delite_diagnostic)

        self.stackedWidget.addWidget(self.diagnistic_page)
        self.actions_page = QWidget()
        self.actions_page.setObjectName(u"actions_page")
        self.actions_page.setStyleSheet(u"Line{\n"
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
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.label_6 = QLabel(self.actions_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 560, 40))
        self.label_6.setFont(font2)
        self.line_6 = QFrame(self.actions_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 45, 560, 2))
        self.line_6.setAutoFillBackground(False)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.actions_data_ = QWidget(self.actions_page)
        self.actions_data_.setObjectName(u"actions_data_")
        self.actions_data_.setGeometry(QRect(0, 60, 560, 400))
        self.verticalLayout_7 = QVBoxLayout(self.actions_data_)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.actions_table = QTableView(self.actions_data_)
        self.actions_table.setObjectName(u"actions_table")
        self.actions_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.actions_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.actions_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.actions_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.actions_table.horizontalHeader().setCascadingSectionResizes(True)
        self.actions_table.horizontalHeader().setStretchLastSection(True)
        self.actions_table.verticalHeader().setVisible(False)
        self.actions_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_7.addWidget(self.actions_table)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_action = QPushButton(self.actions_data_)
        self.add_action.setObjectName(u"add_action")
        self.add_action.setCheckable(True)
        self.add_action.setChecked(False)

        self.horizontalLayout_6.addWidget(self.add_action)

        self.edit__action = QPushButton(self.actions_data_)
        self.edit__action.setObjectName(u"edit__action")
        self.edit__action.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.edit__action)

        self.delite_action = QPushButton(self.actions_data_)
        self.delite_action.setObjectName(u"delite_action")
        self.delite_action.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.delite_action)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.actions_page)
        self.repair_page = QWidget()
        self.repair_page.setObjectName(u"repair_page")
        self.repair_page.setStyleSheet(u"Line{\n"
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
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.label_4 = QLabel(self.repair_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 560, 40))
        self.label_4.setFont(font2)
        self.line_3 = QFrame(self.repair_page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 45, 560, 2))
        self.line_3.setAutoFillBackground(False)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.choose_diagnostic_repair = QComboBox(self.repair_page)
        self.choose_diagnostic_repair.setObjectName(u"choose_diagnostic_repair")
        self.choose_diagnostic_repair.setGeometry(QRect(0, 60, 560, 26))
        self.choose_diagnostic_repair.setFont(font3)
        self.choose_repair_plan = QComboBox(self.repair_page)
        self.choose_repair_plan.setObjectName(u"choose_repair_plan")
        self.choose_repair_plan.setGeometry(QRect(0, 90, 560, 26))
        self.choose_repair_plan.setFont(font3)
        self.widget_3 = QWidget(self.repair_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 120, 560, 34))
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(560, 34))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.add_repair_plan = QPushButton(self.widget_3)
        self.add_repair_plan.setObjectName(u"add_repair_plan")
        self.add_repair_plan.setCheckable(True)
        self.add_repair_plan.setChecked(False)

        self.horizontalLayout_10.addWidget(self.add_repair_plan)

        self.edit_repair_plan = QPushButton(self.widget_3)
        self.edit_repair_plan.setObjectName(u"edit_repair_plan")
        self.edit_repair_plan.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.edit_repair_plan)

        self.delite_repair_plan = QPushButton(self.widget_3)
        self.delite_repair_plan.setObjectName(u"delite_repair_plan")
        self.delite_repair_plan.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.delite_repair_plan)

        self.actions_data_2 = QWidget(self.repair_page)
        self.actions_data_2.setObjectName(u"actions_data_2")
        self.actions_data_2.setGeometry(QRect(0, 160, 560, 290))
        self.verticalLayout_9 = QVBoxLayout(self.actions_data_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.repairs_table = QTableView(self.actions_data_2)
        self.repairs_table.setObjectName(u"repairs_table")
        self.repairs_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.repairs_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.repairs_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.repairs_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.repairs_table.horizontalHeader().setCascadingSectionResizes(True)
        self.repairs_table.horizontalHeader().setStretchLastSection(True)
        self.repairs_table.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.repairs_table)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.add_repair = QPushButton(self.actions_data_2)
        self.add_repair.setObjectName(u"add_repair")
        self.add_repair.setCheckable(True)
        self.add_repair.setChecked(False)

        self.horizontalLayout_11.addWidget(self.add_repair)

        self.edit_repair = QPushButton(self.actions_data_2)
        self.edit_repair.setObjectName(u"edit_repair")
        self.edit_repair.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.edit_repair)

        self.delite_repair = QPushButton(self.actions_data_2)
        self.delite_repair.setObjectName(u"delite_repair")
        self.delite_repair.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.delite_repair)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.repair_page)
        self.characteristics_page = QWidget()
        self.characteristics_page.setObjectName(u"characteristics_page")
        self.characteristics_page.setStyleSheet(u"Line{\n"
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
"QTableView::item{\n"
"	border: 1px solid #ffad3d;\n"
"	color: #ffa120;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	background-color: #ffad3d;\n"
"	color: white;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	width:100%;\n"
"	background-color: #ffa120;\n"
"	color: white;\n"
"	border: none;\n"
"	font-weight: bold;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"")
        self.label_5 = QLabel(self.characteristics_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 560, 40))
        self.label_5.setFont(font2)
        self.line_5 = QFrame(self.characteristics_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 45, 560, 2))
        self.line_5.setAutoFillBackground(False)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.characteristics_data = QWidget(self.characteristics_page)
        self.characteristics_data.setObjectName(u"characteristics_data")
        self.characteristics_data.setGeometry(QRect(0, 60, 560, 400))
        self.verticalLayout_4 = QVBoxLayout(self.characteristics_data)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chatacteristics_table = QTableView(self.characteristics_data)
        self.chatacteristics_table.setObjectName(u"chatacteristics_table")
        self.chatacteristics_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.chatacteristics_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chatacteristics_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.chatacteristics_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chatacteristics_table.horizontalHeader().setCascadingSectionResizes(True)
        self.chatacteristics_table.horizontalHeader().setStretchLastSection(True)
        self.chatacteristics_table.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.chatacteristics_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_characteristic = QPushButton(self.characteristics_data)
        self.add_characteristic.setObjectName(u"add_characteristic")
        self.add_characteristic.setCheckable(True)
        self.add_characteristic.setChecked(False)

        self.horizontalLayout_3.addWidget(self.add_characteristic)

        self.delite_characteristic = QPushButton(self.characteristics_data)
        self.delite_characteristic.setObjectName(u"delite_characteristic")
        self.delite_characteristic.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.delite_characteristic)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.characteristics_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u0433\u0438\u0442\u0430\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Service\n"
"Steps", None))
        self.details_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438", None))
        self.characteristics_button.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.diagnostic_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437\u044b", None))
        self.actions_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.repairs_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438", None))
        self.add_detail.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit__detail.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delite_detail.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437\u044b", None))
        self.choose_diagnostic.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.add_diagnostic_characteristic.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.delite_diagnostic_characteristic.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.update_diagnostic.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.add_diagnostic.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.delite_diagnostic.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.add_action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit__action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delite_action.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\u044b", None))
        self.choose_diagnostic_repair.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.choose_repair_plan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.add_repair_plan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.edit_repair_plan.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.delite_repair_plan.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.add_repair.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0448\u0430\u0433", None))
        self.edit_repair.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0448\u0430\u0433", None))
        self.delite_repair.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0448\u0430\u0433", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.add_characteristic.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delite_characteristic.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

