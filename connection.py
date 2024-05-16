from PySide6 import QtWidgets, QtSql


class Data:    
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('guitar.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
            "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        

        query.exec('''CREATE TABLE IF NOT EXISTS Characteristic (
        characteristic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        characteristic_name TEXT,
        min_acceptable_val REAL,
        max_acceptable_val REAL
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Detail (
        detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        detail_name TEXT
        )''')
        
        query.exec('''CREATE TABLE IF NOT EXISTS Characteristic_Diagnostic (
        chara_diag_id INTEGER PRIMARY KEY AUTOINCREMENT,
        characteristic_id INTEGER,
        diagnostic_id INTEGER,
        repair_id INTEGER,
        characteristics_value_id INTEGER,
        FOREIGN KEY (characteristic_id) REFERENCES Characteristic(characteristic_id),
        FOREIGN KEY (characteristics_value_id) REFERENCES Characteristic_Value(characteristics_value_id),
        FOREIGN KEY (diagnostic_id) REFERENCES Diagnostic(diagnostic_id),
        FOREIGN KEY (repair_id) REFERENCES Repair(repair_id)
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Diagnostic (
        diagnostic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        diagnostic_name TEXT,
        min_value REAL,
        max_value REAL
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Repair (
        repair_id INTEGER PRIMARY KEY AUTOINCREMENT,
        repair_name TEXT,
        action_id INTEGER,
        FOREIGN KEY (action_id) REFERENCES Action(action_id)
        )''')

        query.exec('''CREATE TABLE IF NOT EXISTS Action (
        action_id INTEGER PRIMARY KEY AUTOINCREMENT,
        action_name TEXT
        )''')
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query
    
    #Detail tasks
    def add_detail_bd(self, name):
        sql_query = "INSERT INTO Detail (detail_name) VALUES (?)"
        self.execute_query_with_params(sql_query, [name])

    def update_detail_bd(self, name, id):
        sql_query = "UPDATE Detail SET detail_name=? WHERE detail_id=?"
        self.execute_query_with_params(sql_query, [name, id])

    def delite_detail_bd(self, id):
        sql_query = "DELETE FROM Detail WHERE detail_id=?"
        self.execute_query_with_params(sql_query, [id])

    #Action tasks
    def add_actions_bd(self, action):
        sql_query = "INSERT INTO Action (action_name) VALUES (?)"
        self.execute_query_with_params(sql_query, [action])

    def update_actions_bd(self, action, id):
        sql_query = "UPDATE Action SET action_name=? WHERE action_id=?"
        self.execute_query_with_params(sql_query, [action, id])

    def delite_actions_bd(self, id):
        sql_query = "DELETE FROM Action WHERE action_id=?"
        self.execute_query_with_params(sql_query, [id])

    # Characteristic tasks
    def add_characteristic_bd(self, name, min, max, values):
        sql_query = "INSERT INTO Characteristic (characteristic_name, min_acceptable_val, max_acceptable_val) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, min, max])

        values = values.split(', ')
        for value in values:
            sql_query = "INSERT INTO Characteristic_Value (value_name) VALUES (?)"
            self.execute_query_with_params(sql_query, [value])

            sql_query = '''INSERT INTO Characteristic_Diagnostic (characteristics_value_id)
                            SELECT cv.characteristics_value_id
                            FROM Characteristic_Value cv
                            WHERE cv.value_name = ?'''
            self.execute_query_with_params(sql_query, [value])

            sql_query = '''UPDATE Characteristic_Diagnostic SET (characteristic_id)
                            SELECT c.characteristic_id
                            FROM Characteristic c
                            WHERE cv.value_name = ?'''
            self.execute_query_with_params(sql_query, [value])

            sql_query = '''
                        INSERT INTO Characteristic_Diagnostic (characteristic_id, characteristics_value_id)
                        SELECT c.characteristic_id, cv.characteristics_value_id
                        FROM Characteristic c
                        JOIN Characteristic_Value AS cv
                        WHERE c.characteristic_name = ? AND cv.value_name = ?
                        '''
            self.execute_query_with_params(sql_query, [name, value])
            print(value + ' ' + name)

    # def update_characteristic_bd(self, name, min, max, values):
    #     sql_query = "UPDATE Characteristic (characteristic_name, min_acceptable_val, max_acceptable_val) VALUES (?, ?, ?)"
    #     self.execute_query_with_params(sql_query, [name, min, max])

    #     values = values.split(', ')
    #     for value in values:
    #         sql_query = "INSERT INTO Characteristic_Value (value_name) VALUES (?)"
    #         self.execute_query_with_params(sql_query, [value])

    #         sql_query = '''INSERT INTO Characteristic_Diagnostic (characteristics_value_id)
    #                         SELECT cv.characteristics_value_id
    #                         FROM Characteristic_Value cv
    #                         WHERE cv.value_name = ?'''
    #         self.execute_query_with_params(sql_query, [value])

    #         sql_query = '''UPDATE Characteristic_Diagnostic SET (characteristic_id)
    #                         SELECT c.characteristic_id
    #                         FROM Characteristic c
    #                         WHERE cv.value_name = ?'''
    #         self.execute_query_with_params(sql_query, [value])

    #         sql_query = '''
    #                     INSERT INTO Characteristic_Diagnostic (characteristic_id, characteristics_value_id)
    #                     SELECT c.characteristic_id, cv.characteristics_value_id
    #                     FROM Characteristic c
    #                     JOIN Characteristic_Value AS cv
    #                     WHERE c.characteristic_name = ? AND cv.value_name = ?
    #                     '''
    #         self.execute_query_with_params(sql_query, [name, value])
    #         print(value + ' ' + name)

    def delite_characteristic_bd(self, id):
        sql_query = "DELETE FROM Characteristic_Diagnostic WHERE characteristic_id = ?"
        self.execute_query_with_params(sql_query, [id])

        sql_query = """DELETE FROM Characteristic_Value
                    WHERE characteristics_value_id IN (
                        SELECT characteristics_value_id
                        FROM Characteristic_Diagnostic
                        WHERE characteristic_id = ?"""
        self.execute_query_with_params(sql_query, [id])

        sql_query = """DELETE FROM Characteristic
            WHERE characteristic_id = ?"""
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, tablice):
        sql_query = f"SELECT {column} FROM {tablice}"


        query = self.execute_query_with_params(sql_query, [])

        result_list = []
        query.first()
        result_list.append(query.value(0))
        while query.next():
            result_list.append(query.value(0))

        # if query.next():
        #     return str(query.value(0)) + '$'

        # print(query.value(0))

        return result_list

    #Diagnosric tasks
    def get_diagnostic(self):
        return self.get_total(column="diagnostic_name", tablice="Diagnostic")
    
    def add_diagnostic_bd(self, diagnostic):
        sql_query = "INSERT INTO Diagnostic (diagnostic_name) VALUES (?)"
        self.execute_query_with_params(sql_query, [diagnostic])


    def delite_diagnostic_bd(self, name):
        sql_query = "DELETE FROM Diagnostic WHERE diagnostic_name=?"
        self.execute_query_with_params(sql_query, [name])

    def add_diagnostic_value_bd(self, diagnostic, characteristic, value, min_value, max_value):
        sql_query = '''INSERT INTO Diagnostic_Values (diagnostic_characteristic_value, diagnostic_value, min_value, max_value, diagnostic_id)
                SELECT ?, ?, ?, ?, d.diagnostic_id
                FROM Diagnostic d
                WHERE d.diagnostic_name = ?;'''
        self.execute_query_with_params(sql_query, [characteristic, value, min_value, max_value, diagnostic])

    def delite_diagnostic_values_bd(self, name):
        sql_query = "DELETE FROM Diagnostic_Values WHERE diagnostic_characteristic_value=?"
        self.execute_query_with_params(sql_query, [name])
