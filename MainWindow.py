from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtWidgets
import sys
from Ui.ui_main import Ui_MainWindow
from Ui.ui_detailsChange import Ui_Dialog as Details_Change
from Ui.ui_actionsChange import Ui_Dialog as Actions_Change
from Ui.ui_diagnosticsChange import Ui_Dialog as Diagnostic_Change
from Ui.ui_diagnosticsCharacteristicsChange import Ui_Dialog as Diagnostic_Values_Change
from Ui.ui_characteristicsChange import Ui_Dialog as Characteristic_Change
from connection import Data

class MainWindow(QMainWindow, Ui_MainWindow, Data):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi(self)
        self.conn = Data()

        #Sidebar
        self.details_button.clicked.connect(self.to_details_page)
        self.characteristics_button.clicked.connect(self.to_characteristic_page)
        self.diagnostic_button.clicked.connect(self.to_diagnostic_page)
        self.actions_button.clicked.connect(self.to_actions_page)
        self.repairs_button.clicked.connect(self.to_repairs_page)

        #Details page        
        self.add_detail.clicked.connect(self.open_add_detail_window)
        self.edit__detail.clicked.connect(self.open_add_detail_window)
        self.delite_detail.clicked.connect(self.delete_detail_click)

        #Actions page 
        self.add_action.clicked.connect(self.open_add_action_window)
        self.edit__action.clicked.connect(self.open_add_action_window)
        self.delite_action.clicked.connect(self.delete_action_click)

        #Characteristics page 
        self.add_characteristic.clicked.connect(self.open_add_characteristic_window)
        self.delite_characteristic.clicked.connect(self.delete_characteristic_click)

        #Diagnostic page
        self.update_diagnostic.clicked.connect(self.update_diagnostic_table)
        self.add_diagnostic.clicked.connect(self.open_add_diagnostic_window)
        self.delite_diagnostic.clicked.connect(self.delete_diagnostic_click)
        self.add_diagnostic_characteristic.clicked.connect(self.open_values_diagnostic_window)
        self.delite_diagnostic_characteristic.clicked.connect(self.delete_diagnostic_value_click)

        self.view_characteristics()
        # Updating tablices
        if self.stackedWidget.currentIndex == 2:
            self.view_actions()
        elif self.stackedWidget.currentIndex == 4:
            self.view_characteristics()
        elif self.stackedWidget.currentIndex == 1:
            self.view_diagnostic()
        else:
            self.view_detail()


    #Sidebar functions
    def to_details_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.view_detail()

    def to_characteristic_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def to_diagnostic_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.view_diagnostic()
        
    def to_actions_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.view_actions()

    def to_repairs_page(self):
        self.stackedWidget.setCurrentIndex(3)

    #Details page functions
    def view_detail(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Detail')
        self.model.select()
        self.detaild_table.setModel(self.model)

    def open_add_detail_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_detail = Details_Change()
        self.ui_detail.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        if sender.objectName() == "add_detail":
            self.ui_detail.save_detail.clicked.connect(self.add_detail_click)
        else:
            self.ui_detail.save_detail.clicked.connect(self.edit_detail_click)

    def add_detail_click(self):
        data = self.ui_detail.fill_detail.text()

        self.conn.add_detail_bd(data)
        self.view_detail()
        self.new_window.close()

    def edit_detail_click(self):
        index = self.detaild_table.selectedIndexes()[0]
        print(self.detaild_table.model().data(index))
        id = str(self.detaild_table.model().data(index))

        data = self.ui_detail.fill_detail.text()

        self.conn.update_detail_bd(data, id)
        self.view_detail()
        
        
        self.new_window.close()

    def delete_detail_click(self):
        index = self.detaild_table.selectedIndexes()[0]
        id = str(self.detaild_table.model().data(index))

        self.conn.delite_detail_bd(id)
        self.view_detail()

    #Actions page functions
    def view_actions(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Action')
        self.model.select()
        self.actions_table.setModel(self.model)

    def open_add_action_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_action = Actions_Change()
        self.ui_action.setupUi(self.new_window)
        self.new_window.show()

        sender = self.sender()
        if sender.objectName() == "add_action":
            self.ui_action.save_action.clicked.connect(self.add_action_click)
        else:
            self.ui_action.save_action.clicked.connect(self.edit_action_click)

    def add_action_click(self):
        data = self.ui_action.fill_action.toPlainText()

        self.conn.add_actions_bd(data)
        self.view_actions()
        self.new_window.close()

    def edit_action_click(self):
        index = self.actions_table.selectedIndexes()[0]
        id = str(self.actions_table.model().data(index))

        action = self.ui_action.fill_action.toPlainText()

        self.conn.update_detail_bd(action, id)
        self.view_actions()
        
        
        self.new_window.close()

    def delete_action_click(self):
        index = self.actions_table.selectedIndexes()[0]
        id = str(self.actions_table.model().data(index))

        self.conn.delite_actions_bd(id)
        self.view_actions()

    #Characteristics page functions
    def view_characteristics(self):
        self.model = QSqlTableModel(self)
        self.model.setQuery('''SELECT c.*, cv.value_name
        FROM Characteristic c
        LEFT JOIN (
            SELECT cd.characteristic_id, cv.value_name
            FROM Characteristic_Diagnostic cd
            JOIN Characteristic_Value cv ON cd.characteristics_value_id = cv.characteristics_value_id
        ) AS cv ON c.characteristic_id = cv.characteristic_id;''')
        self.model.select()
        self.chatacteristics_table.setModel(self.model)

    def open_add_characteristic_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_characteristic = Characteristic_Change()
        self.ui_characteristic.setupUi(self.new_window)
        self.new_window.show()
        self.ui_characteristic.save_characteristic.clicked.connect(self.add_characteristic_click)

    def add_characteristic_click(self):
        name = self.ui_characteristic.fill_characteristic.text()
        minimum = self.ui_characteristic.min_acceptable_vavue.text()
        maximum = self.ui_characteristic.nax_acceptable_value.text()
        values = self.ui_characteristic.fill_acceptable_values.text()

        self.conn.add_characteristic_bd(name, minimum, maximum, values)
        self.view_characteristics()
        self.new_window.close()

    # def edit_characteristic_click(self):
    #     index = self.chatacteristics_table.selectedIndexes()[0]
    #     id = str(self.chatacteristics_table.model().data(index))

    #     name = self.ui_characteristic.fill_characteristic.text()
    #     minimum = self.ui_characteristic.min_acceptable_vavue.text()
    #     maximum = self.ui_characteristic.nax_acceptable_value.text()
    #     values = self.ui_characteristic.fill_acceptable_values.text()

    #     self.conn.update_characteristic_bd(name, minimum, maximum, values, id)
    #     self.view_characteristics()
    #     self.new_window.close()

    def delete_characteristic_click(self):
        index = self.chatacteristics_table.selectedIndexes()[0]
        id = str(self.chatacteristics_table.model().data(index))

        self.conn.delite_characteristic_bd(id)
        self.view_characteristics()


    def view_diagnostic(self):
        self.choose_diagnostic.clear()
        self.choose_diagnostic.addItems(self.get_diagnostic())   

    def update_diagnostic_table(self):
        curent_diagnostic = self.choose_diagnostic.currentText()
        self.model = QSqlTableModel(self)
        sql_query = '''SELECT dv.diagnostic_characteristic_value, dv.diagnostic_value, dv.min_value, dv.max_value
                    FROM Diagnostic_Values dv
                    JOIN Diagnostic d ON dv.diagnostic_id = d.diagnostic_id
                    WHERE d.diagnostic_name = "''' + curent_diagnostic + '";'
        self.model.setQuery(sql_query)
        self.model.select()
        self.diagnostic_characteristic_table.setModel(self.model)

    def open_add_diagnostic_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_diagnostic = Diagnostic_Change()
        self.ui_diagnostic.setupUi(self.new_window)
        self.new_window.show()

        self.ui_diagnostic.save_diagnostic.clicked.connect(self.add_diagnostic_click)

    
    def add_diagnostic_click(self):
        data = self.ui_diagnostic.fill_diagnostic.text()

        self.conn.add_diagnostic_bd(data)
        self.view_diagnostic()
        self.new_window.close()

    def delete_diagnostic_click(self):
        data = self.choose_diagnostic.currentText()

        self.conn.delite_diagnostic_bd(data)
        self.view_diagnostic()

    def open_values_diagnostic_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_diagnosti_values = Diagnostic_Values_Change()
        self.ui_diagnosti_values.setupUi(self.new_window)
        self.new_window.show()

        self.ui_diagnosti_values.save_diagnostic_characteristic.clicked.connect(self.add_diagnostic_value_click)

    def add_diagnostic_value_click(self):
        diagnostic = self.choose_diagnostic.currentText()
        characteristic = self.ui_diagnosti_values.fill_diagnostic_characteristic.text()
        value = self.ui_diagnosti_values.fill_value.text()
        min_value = self.ui_diagnosti_values.min_vavue.text()
        max_value = self.ui_diagnosti_values.max_value.text()


        self.conn.add_diagnostic_value_bd(diagnostic, characteristic, value, min_value, max_value)
        self.update_diagnostic_table()
        self.new_window.close()

    def delete_diagnostic_value_click(self):
        index = self.diagnostic_characteristic_table.selectedIndexes()[0]
        name = str(self.diagnostic_characteristic_table.model().data(index))

        self.conn.delite_diagnostic_values_bd(name)
        self.update_diagnostic_table()
        
        