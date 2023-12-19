from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import *
import sys
import psycopg2
from mesto import Ui_Window1


connection = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "xkleeps123",
    database = "postgres"
)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT version();"
    )
    print(f"Версия сервера: {cursor.fetchone()}")
with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, name, text_data, date_cinema, time FROM cinema ORDER BY id;"""
    )
    records = cursor.fetchall()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 607)
        MainWindow.setFixedWidth(800)
        MainWindow.setFixedHeight(607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_labl = QtWidgets.QLabel(self.centralwidget)
        self.main_labl.setGeometry(QtCore.QRect(210, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_labl.setFont(font)
        self.main_labl.setObjectName("main_labl")
        self.but_add = QtWidgets.QPushButton(self.centralwidget)
        self.but_add.setGeometry(QtCore.QRect(60, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.but_add.setFont(font)
        self.but_add.setObjectName("but_add")
        self.but_del = QtWidgets.QPushButton(self.centralwidget)
        self.but_del.setGeometry(QtCore.QRect(320, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.but_del.setFont(font)
        self.but_del.setObjectName("but_del")
        self.but_ed = QtWidgets.QPushButton(self.centralwidget)
        self.but_ed.setGeometry(QtCore.QRect(550, 420, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.but_ed.setFont(font)
        self.but_ed.setObjectName("but_ed")
        self.but_check = QtWidgets.QPushButton(self.centralwidget)
        self.but_check.setGeometry(QtCore.QRect(270, 490, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_check.setFont(font)
        self.but_check.setObjectName("but_check")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 801, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель администратора"))
        self.main_labl.setText(_translate("MainWindow", "Панель администратора"))
        self.but_add.setText(_translate("MainWindow", "Добавить"))
        self.but_del.setText(_translate("MainWindow", "Удалить"))
        self.but_ed.setText(_translate("MainWindow", "Сохранить"))
        self.but_check.setText(_translate("MainWindow", "Посмотреть места"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Время"))
        self.tableWidget.verticalHeader().setVisible(False)

        for row_index, record in enumerate(records):
            self.tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row_index, col_index, item)
# --------------------------------------------------------------------------------------------------------------------------------------
    def add_function(self):
        self.but_add.clicked.connect(self.add_record)
        self.but_ed.clicked.connect(self.save_record)
        self.but_check.clicked.connect(self.open_window1)  #open_window1
        self.but_del.clicked.connect(self.delete_records)

    def add_record(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)

        # Получение значения id из предыдущей записи
        previous_id_item = self.tableWidget.item(row_count - 1, 0)
        previous_id = int(previous_id_item.text()) if previous_id_item is not None else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Автозаполнение поля "id" в таблице
        id_item = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget.setItem(row_count, 0, id_item)

    def save_red(self):
        row_count = self.tableWidget.rowCount()
        if row_count > 0:
            for row in range(row_count):
                id_item = self.tableWidget.item(row, 0)
                name_item = self.tableWidget.item(row, 1)
                description_item = self.tableWidget.item(row, 2)
                date_item = self.tableWidget.item(row, 3)
                time_item = self.tableWidget.item(row, 4)

                id = id_item.text()
                name = name_item.text() if name_item else ''
                description = description_item.text() if description_item else ''
                date = date_item.text() if date_item else ''
                time = time_item.text() if time_item else ''

                if name or description or date or time:
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT id FROM cinema WHERE id = %s;", (id,))
                        existing_id = cursor.fetchone()

                    if existing_id:
                        with connection.cursor() as cursor:
                            cursor.execute("UPDATE cinema SET name = %s, text_data = %s, date_cinema = %s, time = %s WHERE id = %s;",
                                        (name, description, date, time, id))
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO cinema (id, name, text_data, date_cinema, time) VALUES (%s, %s, %s, %s, %s);",
                                        (id, name, description, date, time))
                else:
                    print(f"Пустая запись не сохранена")
        else:
            print("Нет записей для сохранения")

    def save_record(self):
        row_count = self.tableWidget.rowCount()
        if row_count > 0:
            # Получение значений из добавленной строки
            id_item = self.tableWidget.item(row_count - 1, 0)
            name_item = self.tableWidget.item(row_count - 1, 1)
            description_item = self.tableWidget.item(row_count - 1, 2)
            date_item = self.tableWidget.item(row_count - 1, 3)
            time_item = self.tableWidget.item(row_count - 1, 4)

            if name_item and description_item and date_item and time_item:
                name = name_item.text()
                description = description_item.text()
                date = date_item.text()
                time = time_item.text()
                id = id_item.text()

                # Проверка существования записи с таким же id
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id FROM cinema WHERE id = %s;", (id,))
                    existing_id = cursor.fetchone()

                if existing_id:
                    # Запись с таким id уже существует, обработать это как необходимо
                    pass
                else:
                    # Вставка новой записи в базу данных
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO cinema (id, name, text_data, date_cinema, time) VALUES (%s, %s, %s, %s, %s);",
                                    (id, name, description, date, time))
                        print("Новая запись сохранена")
            else:
                print("Новая запись содержит пустые значения")
        else:
            print("Новая запись не сохранена")

    def delete_records(self):
        selected_row = self.tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM cinema WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.tableWidget.removeRow(selected_row)
    
    def close_con(self):
        connection.close()
        print("Соединение закрыто")
# ------------------------------------------------------------------------------------------------------------------------------------------------
    def open_window1(self):
        global idt
        connection1 = psycopg2.connect(
            host = "127.0.0.1",
            user = "postgres",
            password = "xkleeps123",
            database = "postgres"
        )
        connection1.autocommit = True
        # cursor = connectoin.cursor()

        selected_row = self.tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            idt = item.text()  # Получение текста из элемента

            with connection1.cursor() as cursor1:
                cursor1.execute(
                    "SELECT version();"
                )
                print(f"Версия сервера: {cursor1.fetchone()}")
            with connection1.cursor() as cursor1:
                cursor1.execute(
                        """SELECT ud.name_id, ud.place, ud.row, ud.name
                    FROM user_data ud
                    LEFT JOIN cinema c ON ud.cinemas = c.id 
                    WHERE c.id = %s ORDER BY ud.place, ud.row;""", (idt,))

                # print(cursor.fetchone())
                mesto_user = cursor1.fetchall()

            self.window1 = QMainWindow()
            self.ui_window1 = Ui_Window1()
            self.ui_window1.setupUi(self.window1)
            

            # Проверка кнопки but1_1 
            with connection1.cursor() as cursor1:
                for place in range(1, 11):
                    for row in range(1, 11):
                        cursor1.execute(
                            """SELECT 1 
                            FROM user_data ud
                            LEFT JOIN cinema c ON ud.cinemas = c.id 
                            WHERE ud.place = %s AND ud.row = %s AND c.id = %s""",
                            (str(place), str(row), idt)
                        )
                        record_exists = cursor1.fetchone()

                        button_name = f"But{place}_{row}"
                        button = getattr(self.ui_window1, button_name)
                        if record_exists:
                            button.setStyleSheet("background-color: red;")
                            button.setEnabled(False)

            self.ui_window1.But1_1.clicked.connect(self.add_row)
            self.ui_window1.But1_2.clicked.connect(self.btn1_2)
            self.ui_window1.But1_3.clicked.connect(self.btn1_3)
            self.ui_window1.But1_4.clicked.connect(self.btn1_4)
            self.ui_window1.But1_5.clicked.connect(self.btn1_5)
            self.ui_window1.But1_6.clicked.connect(self.btn1_6)
            self.ui_window1.But1_7.clicked.connect(self.btn1_7)
            self.ui_window1.But1_8.clicked.connect(self.btn1_8)
            self.ui_window1.But1_9.clicked.connect(self.btn1_9)
            self.ui_window1.But1_10.clicked.connect(self.btn1_10)

            self.ui_window1.But2_1.clicked.connect(self.btn2_1)
            self.ui_window1.But2_2.clicked.connect(self.btn2_2)
            self.ui_window1.But2_3.clicked.connect(self.btn2_3)
            self.ui_window1.But2_4.clicked.connect(self.btn2_4)
            self.ui_window1.But2_5.clicked.connect(self.btn2_5)
            self.ui_window1.But2_6.clicked.connect(self.btn2_6)
            self.ui_window1.But2_7.clicked.connect(self.btn2_7)
            self.ui_window1.But2_8.clicked.connect(self.btn2_8)
            self.ui_window1.But2_9.clicked.connect(self.btn2_9)
            self.ui_window1.But2_10.clicked.connect(self.btn2_10)

            self.ui_window1.But3_1.clicked.connect(self.btn3_1)
            self.ui_window1.But3_2.clicked.connect(self.btn3_2)
            self.ui_window1.But3_3.clicked.connect(self.btn3_3)
            self.ui_window1.But3_4.clicked.connect(self.btn3_4)
            self.ui_window1.But3_5.clicked.connect(self.btn3_5)
            self.ui_window1.But3_6.clicked.connect(self.btn3_6)
            self.ui_window1.But3_7.clicked.connect(self.btn3_7)
            self.ui_window1.But3_8.clicked.connect(self.btn3_8)
            self.ui_window1.But3_9.clicked.connect(self.btn3_9)
            self.ui_window1.But3_10.clicked.connect(self.btn3_10)

            self.ui_window1.But4_1.clicked.connect(self.btn4_1)
            self.ui_window1.But4_2.clicked.connect(self.btn4_2)
            self.ui_window1.But4_3.clicked.connect(self.btn4_3)
            self.ui_window1.But4_4.clicked.connect(self.btn4_4)
            self.ui_window1.But4_5.clicked.connect(self.btn4_5)
            self.ui_window1.But4_6.clicked.connect(self.btn4_6)
            self.ui_window1.But4_7.clicked.connect(self.btn4_7)
            self.ui_window1.But4_8.clicked.connect(self.btn4_8)
            self.ui_window1.But4_9.clicked.connect(self.btn4_9)
            self.ui_window1.But4_10.clicked.connect(self.btn4_10)

            self.ui_window1.But5_1.clicked.connect(self.btn5_1)
            self.ui_window1.But5_2.clicked.connect(self.btn5_2)
            self.ui_window1.But5_3.clicked.connect(self.btn5_3)
            self.ui_window1.But5_4.clicked.connect(self.btn5_4)
            self.ui_window1.But5_5.clicked.connect(self.btn5_5)
            self.ui_window1.But5_6.clicked.connect(self.btn5_6)
            self.ui_window1.But5_7.clicked.connect(self.btn5_7)
            self.ui_window1.But5_8.clicked.connect(self.btn5_8)
            self.ui_window1.But5_9.clicked.connect(self.btn5_9)
            self.ui_window1.But5_10.clicked.connect(self.btn5_10)

            self.ui_window1.But6_1.clicked.connect(self.btn6_1)
            self.ui_window1.But6_2.clicked.connect(self.btn6_2)
            self.ui_window1.But6_3.clicked.connect(self.btn6_3)
            self.ui_window1.But6_4.clicked.connect(self.btn6_4)
            self.ui_window1.But6_5.clicked.connect(self.btn6_5)
            self.ui_window1.But6_6.clicked.connect(self.btn6_6)
            self.ui_window1.But6_7.clicked.connect(self.btn6_7)
            self.ui_window1.But6_8.clicked.connect(self.btn6_8)
            self.ui_window1.But6_9.clicked.connect(self.btn6_9)
            self.ui_window1.But6_10.clicked.connect(self.btn6_10)

            self.ui_window1.But7_1.clicked.connect(self.btn7_1)
            self.ui_window1.But7_2.clicked.connect(self.btn7_2)
            self.ui_window1.But7_3.clicked.connect(self.btn7_3)
            self.ui_window1.But7_4.clicked.connect(self.btn7_4)
            self.ui_window1.But7_5.clicked.connect(self.btn7_5)
            self.ui_window1.But7_6.clicked.connect(self.btn7_6)
            self.ui_window1.But7_7.clicked.connect(self.btn7_7)
            self.ui_window1.But7_8.clicked.connect(self.btn7_8)
            self.ui_window1.But7_9.clicked.connect(self.btn7_9)
            self.ui_window1.But7_10.clicked.connect(self.btn7_10)

            self.ui_window1.But8_1.clicked.connect(self.btn8_1)
            self.ui_window1.But8_2.clicked.connect(self.btn8_2)
            self.ui_window1.But8_3.clicked.connect(self.btn8_3)
            self.ui_window1.But8_4.clicked.connect(self.btn8_4)
            self.ui_window1.But8_5.clicked.connect(self.btn8_5)
            self.ui_window1.But8_6.clicked.connect(self.btn8_6)
            self.ui_window1.But8_7.clicked.connect(self.btn8_7)
            self.ui_window1.But8_8.clicked.connect(self.btn8_8)
            self.ui_window1.But8_9.clicked.connect(self.btn8_9)
            self.ui_window1.But8_10.clicked.connect(self.btn8_10)

            self.ui_window1.But9_1.clicked.connect(self.btn9_1)
            self.ui_window1.But9_2.clicked.connect(self.btn9_2)
            self.ui_window1.But9_3.clicked.connect(self.btn9_3)
            self.ui_window1.But9_4.clicked.connect(self.btn9_4)
            self.ui_window1.But9_5.clicked.connect(self.btn9_5)
            self.ui_window1.But9_6.clicked.connect(self.btn9_6)
            self.ui_window1.But9_7.clicked.connect(self.btn9_7)
            self.ui_window1.But9_8.clicked.connect(self.btn9_8)
            self.ui_window1.But9_9.clicked.connect(self.btn9_9)
            self.ui_window1.But9_10.clicked.connect(self.btn9_10)

            self.ui_window1.But10_1.clicked.connect(self.btn10_1) 
            self.ui_window1.But10_2.clicked.connect(self.btn10_2)
            self.ui_window1.But10_3.clicked.connect(self.btn10_3)
            self.ui_window1.But10_4.clicked.connect(self.btn10_4)
            self.ui_window1.But10_5.clicked.connect(self.btn10_5)
            self.ui_window1.But10_6.clicked.connect(self.btn10_6)
            self.ui_window1.But10_7.clicked.connect(self.btn10_7)
            self.ui_window1.But10_8.clicked.connect(self.btn10_8)
            self.ui_window1.But10_9.clicked.connect(self.btn10_9)
            self.ui_window1.But10_10.clicked.connect(self.btn10_10)

            self.ui_window1.but_back.clicked.connect(self.save_red1)
            # Установка tableWidget основного окна равным tableWidget из Ui_Window1
            self.tableWidget1 = self.ui_window1.tableWidget
            self.window1.show()

            for row_index, record in enumerate(mesto_user):
                self.tableWidget1.insertRow(row_index)
                for col_index, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget1.setItem(row_index, col_index, item)
        
    # Функция для добавления новой строки
# -----------------------------------------------------------------------------------------------------------------------------------------                    
    def add_row(self):
        self.ui_window1.But1_1.setStyleSheet("background-color: red;")
        self.ui_window1.But1_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_2(self):
        self.ui_window1.But1_2.setStyleSheet("background-color: red;")
        self.ui_window1.But1_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_3(self):
        self.ui_window1.But1_3.setStyleSheet("background-color: red;")
        self.ui_window1.But1_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_4(self):
        self.ui_window1.But1_4.setStyleSheet("background-color: red;")
        self.ui_window1.But1_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_5(self):
        self.ui_window1.But1_5.setStyleSheet("background-color: red;")
        self.ui_window1.But1_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_6(self):
        self.ui_window1.But1_6.setStyleSheet("background-color: red;")
        self.ui_window1.But1_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_7(self):
        self.ui_window1.But1_7.setStyleSheet("background-color: red;")
        self.ui_window1.But1_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_8(self):
        self.ui_window1.But1_8.setStyleSheet("background-color: red;")
        self.ui_window1.But1_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_9(self):
        self.ui_window1.But1_9.setStyleSheet("background-color: red;")
        self.ui_window1.But1_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn1_10(self):
        self.ui_window1.But1_10.setStyleSheet("background-color: red;")
        self.ui_window1.But1_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("1")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_1(self):
        self.ui_window1.But2_1.setStyleSheet("background-color: red;")
        self.ui_window1.But2_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_2(self):
        self.ui_window1.But2_2.setStyleSheet("background-color: red;")
        self.ui_window1.But2_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_3(self):
        self.ui_window1.But2_3.setStyleSheet("background-color: red;")
        self.ui_window1.But2_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_4(self):
        self.ui_window1.But2_4.setStyleSheet("background-color: red;")
        self.ui_window1.But2_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_5(self):
        self.ui_window1.But2_5.setStyleSheet("background-color: red;")
        self.ui_window1.But2_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_6(self):
        self.ui_window1.But2_6.setStyleSheet("background-color: red;")
        self.ui_window1.But2_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_7(self):
        self.ui_window1.But2_7.setStyleSheet("background-color: red;")
        self.ui_window1.But2_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_8(self):
        self.ui_window1.But2_8.setStyleSheet("background-color: red;")
        self.ui_window1.But2_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_9(self):
        self.ui_window1.But2_9.setStyleSheet("background-color: red;")
        self.ui_window1.But2_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn2_10(self):
        self.ui_window1.But2_10.setStyleSheet("background-color: red;")
        self.ui_window1.But2_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("2")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_1(self):
        self.ui_window1.But3_1.setStyleSheet("background-color: red;")
        self.ui_window1.But3_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_2(self):
        self.ui_window1.But3_2.setStyleSheet("background-color: red;")
        self.ui_window1.But3_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_3(self):
        self.ui_window1.But3_3.setStyleSheet("background-color: red;")
        self.ui_window1.But3_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_4(self):
        self.ui_window1.But3_4.setStyleSheet("background-color: red;")
        self.ui_window1.But3_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_5(self):
        self.ui_window1.But3_5.setStyleSheet("background-color: red;")
        self.ui_window1.But3_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_6(self):
        self.ui_window1.But3_6.setStyleSheet("background-color: red;")
        self.ui_window1.But3_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_7(self):
        self.ui_window1.But3_7.setStyleSheet("background-color: red;")
        self.ui_window1.But3_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_8(self):
        self.ui_window1.But3_8.setStyleSheet("background-color: red;")
        self.ui_window1.But3_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_9(self):
        self.ui_window1.But3_9.setStyleSheet("background-color: red;")
        self.ui_window1.But3_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn3_10(self):
        self.ui_window1.But3_10.setStyleSheet("background-color: red;")
        self.ui_window1.But3_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("3")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_1(self):
        self.ui_window1.But4_1.setStyleSheet("background-color: red;")
        self.ui_window1.But4_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_2(self):
        self.ui_window1.But4_2.setStyleSheet("background-color: red;")
        self.ui_window1.But4_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_3(self):
        self.ui_window1.But4_3.setStyleSheet("background-color: red;")
        self.ui_window1.But4_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_4(self):
        self.ui_window1.But4_4.setStyleSheet("background-color: red;")
        self.ui_window1.But4_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_5(self):
        self.ui_window1.But4_5.setStyleSheet("background-color: red;")
        self.ui_window1.But4_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_6(self):
        self.ui_window1.But4_6.setStyleSheet("background-color: red;")
        self.ui_window1.But4_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_7(self):
        self.ui_window1.But4_7.setStyleSheet("background-color: red;")
        self.ui_window1.But4_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_8(self):
        self.ui_window1.But4_8.setStyleSheet("background-color: red;")
        self.ui_window1.But4_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_9(self):
        self.ui_window1.But4_9.setStyleSheet("background-color: red;")
        self.ui_window1.But4_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn4_10(self):
        self.ui_window1.But4_10.setStyleSheet("background-color: red;")
        self.ui_window1.But4_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("4")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_1(self):
        self.ui_window1.But5_1.setStyleSheet("background-color: red;")
        self.ui_window1.But5_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_2(self):
        self.ui_window1.But5_2.setStyleSheet("background-color: red;")
        self.ui_window1.But5_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_3(self):
        self.ui_window1.But5_3.setStyleSheet("background-color: red;")
        self.ui_window1.But5_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_4(self):
        self.ui_window1.But5_4.setStyleSheet("background-color: red;")
        self.ui_window1.But5_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_5(self):
        self.ui_window1.But5_5.setStyleSheet("background-color: red;")
        self.ui_window1.But5_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_6(self):
        self.ui_window1.But5_6.setStyleSheet("background-color: red;")
        self.ui_window1.But5_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_7(self):
        self.ui_window1.But5_7.setStyleSheet("background-color: red;")
        self.ui_window1.But5_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_8(self):
        self.ui_window1.But5_8.setStyleSheet("background-color: red;")
        self.ui_window1.But5_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_9(self):
        self.ui_window1.But5_9.setStyleSheet("background-color: red;")
        self.ui_window1.But5_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn5_10(self):
        self.ui_window1.But5_10.setStyleSheet("background-color: red;")
        self.ui_window1.But5_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("5")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_1(self):
        self.ui_window1.But6_1.setStyleSheet("background-color: red;")
        self.ui_window1.But6_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_2(self):
        self.ui_window1.But6_2.setStyleSheet("background-color: red;")
        self.ui_window1.But6_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_3(self):
        self.ui_window1.But6_3.setStyleSheet("background-color: red;")
        self.ui_window1.But6_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_4(self):
        self.ui_window1.But6_4.setStyleSheet("background-color: red;")
        self.ui_window1.But6_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_5(self):
        self.ui_window1.But6_5.setStyleSheet("background-color: red;")
        self.ui_window1.But6_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_6(self):
        self.ui_window1.But6_6.setStyleSheet("background-color: red;")
        self.ui_window1.But6_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_7(self):
        self.ui_window1.But6_7.setStyleSheet("background-color: red;")
        self.ui_window1.But6_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_8(self):
        self.ui_window1.But6_8.setStyleSheet("background-color: red;")
        self.ui_window1.But6_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_9(self):
        self.ui_window1.But6_9.setStyleSheet("background-color: red;")
        self.ui_window1.But6_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn6_10(self):
        self.ui_window1.But6_10.setStyleSheet("background-color: red;")
        self.ui_window1.But6_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("6")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_1(self):
        self.ui_window1.But7_1.setStyleSheet("background-color: red;")
        self.ui_window1.But7_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_2(self):
        self.ui_window1.But7_2.setStyleSheet("background-color: red;")
        self.ui_window1.But7_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_3(self):
        self.ui_window1.But7_3.setStyleSheet("background-color: red;")
        self.ui_window1.But7_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_4(self):
        self.ui_window1.But7_4.setStyleSheet("background-color: red;")
        self.ui_window1.But7_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_5(self):
        self.ui_window1.But7_5.setStyleSheet("background-color: red;")
        self.ui_window1.But7_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_6(self):
        self.ui_window1.But7_6.setStyleSheet("background-color: red;")
        self.ui_window1.But7_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_7(self):
        self.ui_window1.But7_7.setStyleSheet("background-color: red;")
        self.ui_window1.But7_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_8(self):
        self.ui_window1.But7_8.setStyleSheet("background-color: red;")
        self.ui_window1.But7_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_9(self):
        self.ui_window1.But7_9.setStyleSheet("background-color: red;")
        self.ui_window1.But7_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn7_10(self):
        self.ui_window1.But7_10.setStyleSheet("background-color: red;")
        self.ui_window1.But7_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("7")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_1(self):
        self.ui_window1.But8_1.setStyleSheet("background-color: red;")
        self.ui_window1.But8_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_2(self):
        self.ui_window1.But8_2.setStyleSheet("background-color: red;")
        self.ui_window1.But8_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_3(self):
        self.ui_window1.But8_3.setStyleSheet("background-color: red;")
        self.ui_window1.But8_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_4(self):
        self.ui_window1.But8_4.setStyleSheet("background-color: red;")
        self.ui_window1.But8_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_5(self):
        self.ui_window1.But8_5.setStyleSheet("background-color: red;")
        self.ui_window1.But8_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_6(self):
        self.ui_window1.But8_6.setStyleSheet("background-color: red;")
        self.ui_window1.But8_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_7(self):
        self.ui_window1.But8_7.setStyleSheet("background-color: red;")
        self.ui_window1.But8_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_8(self):
        self.ui_window1.But8_8.setStyleSheet("background-color: red;")
        self.ui_window1.But8_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_9(self):
        self.ui_window1.But8_9.setStyleSheet("background-color: red;")
        self.ui_window1.But8_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn8_10(self):
        self.ui_window1.But8_10.setStyleSheet("background-color: red;")
        self.ui_window1.But8_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("8")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_1(self):
        self.ui_window1.But9_1.setStyleSheet("background-color: red;")
        self.ui_window1.But9_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_2(self):
        self.ui_window1.But9_2.setStyleSheet("background-color: red;")
        self.ui_window1.But9_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_3(self):
        self.ui_window1.But9_3.setStyleSheet("background-color: red;")
        self.ui_window1.But9_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_4(self):
        self.ui_window1.But9_4.setStyleSheet("background-color: red;")
        self.ui_window1.But9_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_5(self):
        self.ui_window1.But9_5.setStyleSheet("background-color: red;")
        self.ui_window1.But9_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_6(self):
        self.ui_window1.But9_6.setStyleSheet("background-color: red;")
        self.ui_window1.But9_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_7(self):
        self.ui_window1.But9_7.setStyleSheet("background-color: red;")
        self.ui_window1.But9_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_8(self):
        self.ui_window1.But9_8.setStyleSheet("background-color: red;")
        self.ui_window1.But9_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_9(self):
        self.ui_window1.But9_9.setStyleSheet("background-color: red;")
        self.ui_window1.But9_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn9_10(self):
        self.ui_window1.But9_10.setStyleSheet("background-color: red;")
        self.ui_window1.But9_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("9")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_1(self):
        self.ui_window1.But10_1.setStyleSheet("background-color: red;")
        self.ui_window1.But10_1.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("1")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_2(self):
        self.ui_window1.But10_2.setStyleSheet("background-color: red;")
        self.ui_window1.But10_2.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("2")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_3(self):
        self.ui_window1.But10_3.setStyleSheet("background-color: red;")
        self.ui_window1.But10_3.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("3")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_4(self):
        self.ui_window1.But10_4.setStyleSheet("background-color: red;")
        self.ui_window1.But10_4.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("4")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_5(self):
        self.ui_window1.But10_5.setStyleSheet("background-color: red;")
        self.ui_window1.But10_5.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("5")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_6(self):
        self.ui_window1.But10_6.setStyleSheet("background-color: red;")
        self.ui_window1.But10_6.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("6")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_7(self):
        self.ui_window1.But10_7.setStyleSheet("background-color: red;")
        self.ui_window1.But10_7.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("7")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_8(self):
        self.ui_window1.But10_8.setStyleSheet("background-color: red;")
        self.ui_window1.But10_8.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("8")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_9(self):
        self.ui_window1.But10_9.setStyleSheet("background-color: red;")
        self.ui_window1.But10_9.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("9")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def btn10_10(self):
        self.ui_window1.But10_10.setStyleSheet("background-color: red;")
        self.ui_window1.But10_10.setEnabled(False)
        
        row_count1 = self.tableWidget1.rowCount()
        self.tableWidget1.insertRow(row_count1)

        # Подключение к базе данных
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection.autocommit = True

        # Получение значения id из последней записи в таблице "user_data"
        with connection.cursor() as cursor:
            cursor.execute("SELECT name_id FROM user_data ORDER BY name_id DESC LIMIT 1;")
            result = cursor.fetchone()
            previous_id = int(result[0]) if result else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Закрытие соединения с базой данных
        connection.close()

        # Автозаполнение поля "id" в таблице
        id_item1 = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.tableWidget1.setItem(row_count1, 0, id_item1)

        row_item = QTableWidgetItem("10")
        seat_item = QTableWidgetItem("10")
        name_item = QTableWidgetItem("Имя зрителя")

        self.tableWidget1.setItem(row_count1, 1, row_item)
        self.tableWidget1.setItem(row_count1, 2, seat_item)
        self.tableWidget1.setItem(row_count1, 3, name_item)
        self.save_red1()

    def save_red1(self):
        connection1 = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="xkleeps123",
            database="postgres"
        )
        connection1.autocommit = True

        with connection1.cursor() as cursor1:
            cursor1.execute("SELECT version();")
            print(f"Версия сервера: {cursor1.fetchone()}")

        with connection1.cursor() as cursor1:
            cursor1.execute("SELECT name_id, row, place, name FROM user_data ORDER BY cinemas;")
            mesto_user = cursor1.fetchall()

        row_count = self.tableWidget1.rowCount()

        if row_count > 0:
            for row in range(row_count):
                id_item = self.tableWidget1.item(row, 0)
                name_item = self.tableWidget1.item(row, 1)
                description_item = self.tableWidget1.item(row, 2)
                date_item = self.tableWidget1.item(row, 3)

                id1 = id_item.text()
                row_red = description_item.text() if description_item else ''
                col_red = date_item.text() if date_item else ''
                name = name_item.text() if name_item else ''

                if name or row_red or col_red or name:
                    with connection1.cursor() as cursor1:
                        cursor1.execute("SELECT name_id FROM user_data WHERE name_id = %s;", (id1,))
                        existing_id = cursor1.fetchone()

                    cinemas = idt  # Значение столбца "cinemas" равно id

                    if existing_id:
                        with connection1.cursor() as cursor1:
                            cursor1.execute("UPDATE user_data SET place = %s, row = %s, name = %s, cinemas = %s WHERE name_id = %s;",
                                            (name, row_red, col_red, cinemas, id1))
                    else:
                        with connection1.cursor() as cursor1:
                            cursor1.execute("INSERT INTO user_data (name_id, place, row, name, cinemas) VALUES (%s, %s, %s, %s, %s);",
                                            (id1, name, row_red, col_red, cinemas))
                else:
                    print(f"Пустая запись не сохранена")
        else:
            print("Нет записей для сохранения")

        connection1.close()
        print("Соединение закрыто")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.aboutToQuit.connect(ui.save_red)
    app.aboutToQuit.connect(ui.close_con)
    MainWindow.show()
    sys.exit(app.exec_())