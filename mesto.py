from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import psycopg2

# connectoin = psycopg2.connect(
#     host = "127.0.0.1",
#     user = "postgres",
#     password = "xkleeps123",
#     database = "postgres"
# )
# connectoin.autocommit = True
# # cursor = connectoin.cursor()

# with connectoin.cursor() as cursor:
#     cursor.execute(
#         "SELECT version();"
#     )
#     print(f"Версия сервера: {cursor.fetchone()}")
# with connectoin.cursor() as cursor:
#     cursor.execute(
#         """SELECT name_id, row, place, name FROM user_data ORDER BY name_id;"""
#     )
#     # print(cursor.fetchone())
#     mesto_user = cursor.fetchall()

class Ui_Window1(QMainWindow):
    def setupUi(self, Window1):
        Window1.setObjectName("Window1")
        # Window1.resize(1053, 741)
        Window1.setFixedWidth(1053)
        Window1.setFixedHeight(741)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Window1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Window1)
        self.centralwidget.setObjectName("centralwidget")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(20, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.but_back.setFont(font)
        self.but_back.setObjectName("but_back")
        self.but_back.clicked.connect(Window1.close)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1053, 21))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(184, 184, 184);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.But1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_1.setGeometry(QtCore.QRect(40, 170, 40, 40))
        self.But1_1.setText("")
        self.But1_1.setObjectName("But1_1")
        self.But1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_2.setGeometry(QtCore.QRect(90, 170, 40, 40))
        self.But1_2.setText("")
        self.But1_2.setObjectName("But1_2")
        self.But1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_3.setGeometry(QtCore.QRect(140, 170, 40, 40))
        self.But1_3.setText("")
        self.But1_3.setObjectName("But1_3")
        self.But1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_4.setGeometry(QtCore.QRect(190, 170, 40, 40))
        self.But1_4.setText("")
        self.But1_4.setObjectName("But1_4")
        self.But1_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_5.setGeometry(QtCore.QRect(240, 170, 40, 40))
        self.But1_5.setText("")
        self.But1_5.setObjectName("But1_5")
        self.But1_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_6.setGeometry(QtCore.QRect(290, 170, 40, 40))
        self.But1_6.setText("")
        self.But1_6.setObjectName("But1_6")
        self.But1_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_7.setGeometry(QtCore.QRect(340, 170, 40, 40))
        self.But1_7.setText("")
        self.But1_7.setObjectName("But1_7")
        self.But1_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_8.setGeometry(QtCore.QRect(390, 170, 40, 40))
        self.But1_8.setText("")
        self.But1_8.setObjectName("But1_8")
        self.But1_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_9.setGeometry(QtCore.QRect(440, 170, 40, 40))
        self.But1_9.setText("")
        self.But1_9.setObjectName("But1_9")
        self.But1_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But1_10.setGeometry(QtCore.QRect(490, 170, 40, 40))
        self.But1_10.setText("")
        self.But1_10.setObjectName("But1_10")
        self.But2_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_7.setGeometry(QtCore.QRect(340, 220, 40, 40))
        self.But2_7.setText("")
        self.But2_7.setObjectName("But2_7")
        self.But2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_2.setGeometry(QtCore.QRect(90, 220, 40, 40))
        self.But2_2.setText("")
        self.But2_2.setObjectName("But2_2")
        self.But2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_3.setGeometry(QtCore.QRect(140, 220, 40, 40))
        self.But2_3.setText("")
        self.But2_3.setObjectName("But2_3")
        self.But2_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_5.setGeometry(QtCore.QRect(240, 220, 40, 40))
        self.But2_5.setText("")
        self.But2_5.setObjectName("But2_5")
        self.But2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_4.setGeometry(QtCore.QRect(190, 220, 40, 40))
        self.But2_4.setText("")
        self.But2_4.setObjectName("But2_4")
        self.But2_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_9.setGeometry(QtCore.QRect(440, 220, 40, 40))
        self.But2_9.setText("")
        self.But2_9.setObjectName("But2_9")
        self.But2_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_10.setGeometry(QtCore.QRect(490, 220, 40, 40))
        self.But2_10.setText("")
        self.But2_10.setObjectName("But2_10")
        self.But2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_1.setGeometry(QtCore.QRect(40, 220, 40, 40))
        self.But2_1.setText("")
        self.But2_1.setObjectName("But2_1")
        self.But2_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_8.setGeometry(QtCore.QRect(390, 220, 40, 40))
        self.But2_8.setText("")
        self.But2_8.setObjectName("But2_8")
        self.But2_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But2_6.setGeometry(QtCore.QRect(290, 220, 40, 40))
        self.But2_6.setText("")
        self.But2_6.setObjectName("But2_6")
        self.But3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_3.setGeometry(QtCore.QRect(140, 270, 40, 40))
        self.But3_3.setText("")
        self.But3_3.setObjectName("But3_3")
        self.But3_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_6.setGeometry(QtCore.QRect(290, 270, 40, 40))
        self.But3_6.setText("")
        self.But3_6.setObjectName("But3_6")
        self.But3_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_9.setGeometry(QtCore.QRect(440, 270, 40, 40))
        self.But3_9.setText("")
        self.But3_9.setObjectName("But3_9")
        self.But4_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_8.setGeometry(QtCore.QRect(390, 320, 40, 40))
        self.But4_8.setText("")
        self.But4_8.setObjectName("But4_8")
        self.But3_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_7.setGeometry(QtCore.QRect(340, 270, 40, 40))
        self.But3_7.setText("")
        self.But3_7.setObjectName("But3_7")
        self.But4_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_10.setGeometry(QtCore.QRect(490, 320, 40, 40))
        self.But4_10.setText("")
        self.But4_10.setObjectName("But4_10")
        self.But4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_2.setGeometry(QtCore.QRect(90, 320, 40, 40))
        self.But4_2.setText("")
        self.But4_2.setObjectName("But4_2")
        self.But4_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_6.setGeometry(QtCore.QRect(290, 320, 40, 40))
        self.But4_6.setText("")
        self.But4_6.setObjectName("But4_6")
        self.But4_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_7.setGeometry(QtCore.QRect(340, 320, 40, 40))
        self.But4_7.setText("")
        self.But4_7.setObjectName("But4_7")
        self.But3_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_5.setGeometry(QtCore.QRect(240, 270, 40, 40))
        self.But3_5.setText("")
        self.But3_5.setObjectName("But3_5")
        self.But4_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_4.setGeometry(QtCore.QRect(190, 320, 40, 40))
        self.But4_4.setText("")
        self.But4_4.setObjectName("But4_4")
        self.But3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_2.setGeometry(QtCore.QRect(90, 270, 40, 40))
        self.But3_2.setText("")
        self.But3_2.setObjectName("But3_2")
        self.But4_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_3.setGeometry(QtCore.QRect(140, 320, 40, 40))
        self.But4_3.setText("")
        self.But4_3.setObjectName("But4_3")
        self.But4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_1.setGeometry(QtCore.QRect(40, 320, 40, 40))
        self.But4_1.setText("")
        self.But4_1.setObjectName("But4_1")
        self.But3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_1.setGeometry(QtCore.QRect(40, 270, 40, 40))
        self.But3_1.setText("")
        self.But3_1.setObjectName("But3_1")
        self.But3_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_4.setGeometry(QtCore.QRect(190, 270, 40, 40))
        self.But3_4.setText("")
        self.But3_4.setObjectName("But3_4")
        self.But4_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_5.setGeometry(QtCore.QRect(240, 320, 40, 40))
        self.But4_5.setText("")
        self.But4_5.setObjectName("But4_5")
        self.But3_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_8.setGeometry(QtCore.QRect(390, 270, 40, 40))
        self.But3_8.setText("")
        self.But3_8.setObjectName("But3_8")
        self.But4_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But4_9.setGeometry(QtCore.QRect(440, 320, 40, 40))
        self.But4_9.setText("")
        self.But4_9.setObjectName("But4_9")
        self.But3_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But3_10.setGeometry(QtCore.QRect(490, 270, 40, 40))
        self.But3_10.setText("")
        self.But3_10.setObjectName("But3_10")
        self.But8_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_3.setGeometry(QtCore.QRect(140, 520, 40, 40))
        self.But8_3.setText("")
        self.But8_3.setObjectName("But8_3")
        self.But8_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_8.setGeometry(QtCore.QRect(390, 520, 40, 40))
        self.But8_8.setText("")
        self.But8_8.setObjectName("But8_8")
        self.But5_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_5.setGeometry(QtCore.QRect(240, 370, 40, 40))
        self.But5_5.setText("")
        self.But5_5.setObjectName("But5_5")
        self.But7_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_7.setGeometry(QtCore.QRect(340, 470, 40, 40))
        self.But7_7.setText("")
        self.But7_7.setObjectName("But7_7")
        self.But6_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_6.setGeometry(QtCore.QRect(290, 420, 40, 40))
        self.But6_6.setText("")
        self.But6_6.setObjectName("But6_6")
        self.But7_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_2.setGeometry(QtCore.QRect(90, 470, 40, 40))
        self.But7_2.setText("")
        self.But7_2.setObjectName("But7_2")
        self.But6_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_10.setGeometry(QtCore.QRect(490, 420, 40, 40))
        self.But6_10.setText("")
        self.But6_10.setObjectName("But6_10")
        self.But7_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_5.setGeometry(QtCore.QRect(240, 470, 40, 40))
        self.But7_5.setText("")
        self.But7_5.setObjectName("But7_5")
        self.But5_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_7.setGeometry(QtCore.QRect(340, 370, 40, 40))
        self.But5_7.setText("")
        self.But5_7.setObjectName("But5_7")
        self.But5_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_3.setGeometry(QtCore.QRect(140, 370, 40, 40))
        self.But5_3.setText("")
        self.But5_3.setObjectName("But5_3")
        self.But7_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_8.setGeometry(QtCore.QRect(390, 470, 40, 40))
        self.But7_8.setText("")
        self.But7_8.setObjectName("But7_8")
        self.But6_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_1.setGeometry(QtCore.QRect(40, 420, 40, 40))
        self.But6_1.setText("")
        self.But6_1.setObjectName("But6_1")
        self.But8_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_2.setGeometry(QtCore.QRect(90, 520, 40, 40))
        self.But8_2.setText("")
        self.But8_2.setObjectName("But8_2")
        self.But5_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_4.setGeometry(QtCore.QRect(190, 370, 40, 40))
        self.But5_4.setText("")
        self.But5_4.setObjectName("But5_4")
        self.But8_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_1.setGeometry(QtCore.QRect(40, 520, 40, 40))
        self.But8_1.setText("")
        self.But8_1.setObjectName("But8_1")
        self.But5_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_8.setGeometry(QtCore.QRect(390, 370, 40, 40))
        self.But5_8.setText("")
        self.But5_8.setObjectName("But5_8")
        self.But6_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_3.setGeometry(QtCore.QRect(140, 420, 40, 40))
        self.But6_3.setText("")
        self.But6_3.setObjectName("But6_3")
        self.But6_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_9.setGeometry(QtCore.QRect(440, 420, 40, 40))
        self.But6_9.setText("")
        self.But6_9.setObjectName("But6_9")
        self.But7_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_1.setGeometry(QtCore.QRect(40, 470, 40, 40))
        self.But7_1.setText("")
        self.But7_1.setObjectName("But7_1")
        self.But6_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_5.setGeometry(QtCore.QRect(240, 420, 40, 40))
        self.But6_5.setText("")
        self.But6_5.setObjectName("But6_5")
        self.But7_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_3.setGeometry(QtCore.QRect(140, 470, 40, 40))
        self.But7_3.setText("")
        self.But7_3.setObjectName("But7_3")
        self.But7_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_10.setGeometry(QtCore.QRect(490, 470, 40, 40))
        self.But7_10.setText("")
        self.But7_10.setObjectName("But7_10")
        self.But8_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_5.setGeometry(QtCore.QRect(240, 520, 40, 40))
        self.But8_5.setText("")
        self.But8_5.setObjectName("But8_5")
        self.But8_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_6.setGeometry(QtCore.QRect(290, 520, 40, 40))
        self.But8_6.setText("")
        self.But8_6.setObjectName("But8_6")
        self.But5_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_1.setGeometry(QtCore.QRect(40, 370, 40, 40))
        self.But5_1.setText("")
        self.But5_1.setObjectName("But5_1")
        self.But8_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_9.setGeometry(QtCore.QRect(440, 520, 40, 40))
        self.But8_9.setText("")
        self.But8_9.setObjectName("But8_9")
        self.But5_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_2.setGeometry(QtCore.QRect(90, 370, 40, 40))
        self.But5_2.setText("")
        self.But5_2.setObjectName("But5_2")
        self.But8_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_4.setGeometry(QtCore.QRect(190, 520, 40, 40))
        self.But8_4.setText("")
        self.But8_4.setObjectName("But8_4")
        self.But7_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_4.setGeometry(QtCore.QRect(190, 470, 40, 40))
        self.But7_4.setText("")
        self.But7_4.setObjectName("But7_4")
        self.But6_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_8.setGeometry(QtCore.QRect(390, 420, 40, 40))
        self.But6_8.setText("")
        self.But6_8.setObjectName("But6_8")
        self.But7_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_9.setGeometry(QtCore.QRect(440, 470, 40, 40))
        self.But7_9.setText("")
        self.But7_9.setObjectName("But7_9")
        self.But8_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_10.setGeometry(QtCore.QRect(490, 520, 40, 40))
        self.But8_10.setText("")
        self.But8_10.setObjectName("But8_10")
        self.But7_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But7_6.setGeometry(QtCore.QRect(290, 470, 40, 40))
        self.But7_6.setText("")
        self.But7_6.setObjectName("But7_6")
        self.But8_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But8_7.setGeometry(QtCore.QRect(340, 520, 40, 40))
        self.But8_7.setText("")
        self.But8_7.setObjectName("But8_7")
        self.But6_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_4.setGeometry(QtCore.QRect(190, 420, 40, 40))
        self.But6_4.setText("")
        self.But6_4.setObjectName("But6_4")
        self.But5_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_10.setGeometry(QtCore.QRect(490, 370, 40, 40))
        self.But5_10.setText("")
        self.But5_10.setObjectName("But5_10")
        self.But6_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_2.setGeometry(QtCore.QRect(90, 420, 40, 40))
        self.But6_2.setText("")
        self.But6_2.setObjectName("But6_2")
        self.But6_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But6_7.setGeometry(QtCore.QRect(340, 420, 40, 40))
        self.But6_7.setText("")
        self.But6_7.setObjectName("But6_7")
        self.But5_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_9.setGeometry(QtCore.QRect(440, 370, 40, 40))
        self.But5_9.setText("")
        self.But5_9.setObjectName("But5_9")
        self.But5_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But5_6.setGeometry(QtCore.QRect(290, 370, 40, 40))
        self.But5_6.setText("")
        self.But5_6.setObjectName("But5_6")
        self.But9_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_1.setGeometry(QtCore.QRect(40, 570, 40, 40))
        self.But9_1.setText("")
        self.But9_1.setObjectName("But9_1")
        self.But9_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_9.setGeometry(QtCore.QRect(440, 570, 40, 40))
        self.But9_9.setText("")
        self.But9_9.setObjectName("But9_9")
        self.But10_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_10.setGeometry(QtCore.QRect(490, 620, 40, 40))
        self.But10_10.setText("")
        self.But10_10.setObjectName("But10_10")
        self.But9_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_8.setGeometry(QtCore.QRect(390, 570, 40, 40))
        self.But9_8.setText("")
        self.But9_8.setObjectName("But9_8")
        self.But9_10 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_10.setGeometry(QtCore.QRect(490, 570, 40, 40))
        self.But9_10.setText("")
        self.But9_10.setObjectName("But9_10")
        self.But10_8 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_8.setGeometry(QtCore.QRect(390, 620, 40, 40))
        self.But10_8.setText("")
        self.But10_8.setObjectName("But10_8")
        self.But10_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_4.setGeometry(QtCore.QRect(190, 620, 40, 40))
        self.But10_4.setText("")
        self.But10_4.setObjectName("But10_4")
        self.But10_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_6.setGeometry(QtCore.QRect(290, 620, 40, 40))
        self.But10_6.setText("")
        self.But10_6.setObjectName("But10_6")
        self.But10_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_7.setGeometry(QtCore.QRect(340, 620, 40, 40))
        self.But10_7.setText("")
        self.But10_7.setObjectName("But10_7")
        self.But10_9 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_9.setGeometry(QtCore.QRect(440, 620, 40, 40))
        self.But10_9.setText("")
        self.But10_9.setObjectName("But10_9")
        self.But9_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_5.setGeometry(QtCore.QRect(240, 570, 40, 40))
        self.But9_5.setText("")
        self.But9_5.setObjectName("But9_5")
        self.But10_5 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_5.setGeometry(QtCore.QRect(240, 620, 40, 40))
        self.But10_5.setText("")
        self.But10_5.setObjectName("But10_5")
        self.But10_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_2.setGeometry(QtCore.QRect(90, 620, 40, 40))
        self.But10_2.setText("")
        self.But10_2.setObjectName("But10_2")
        self.But10_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_3.setGeometry(QtCore.QRect(140, 620, 40, 40))
        self.But10_3.setText("")
        self.But10_3.setObjectName("But10_3")
        self.But9_4 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_4.setGeometry(QtCore.QRect(190, 570, 40, 40))
        self.But9_4.setText("")
        self.But9_4.setObjectName("But9_4")
        self.But9_7 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_7.setGeometry(QtCore.QRect(340, 570, 40, 40))
        self.But9_7.setText("")
        self.But9_7.setObjectName("But9_7")
        self.But10_1 = QtWidgets.QPushButton(self.centralwidget)
        self.But10_1.setGeometry(QtCore.QRect(40, 620, 40, 40))
        self.But10_1.setText("")
        self.But10_1.setObjectName("But10_1")
        self.But9_6 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_6.setGeometry(QtCore.QRect(290, 570, 40, 40))
        self.But9_6.setText("")
        self.But9_6.setObjectName("But9_6")
        self.But9_2 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_2.setGeometry(QtCore.QRect(90, 570, 40, 40))
        self.But9_2.setText("")
        self.But9_2.setObjectName("But9_2")
        self.But9_3 = QtWidgets.QPushButton(self.centralwidget)
        self.But9_3.setGeometry(QtCore.QRect(140, 570, 40, 40))
        self.But9_3.setText("")
        self.But9_3.setObjectName("But9_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(540, 80, 20, 651))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(52, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 280, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 430, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 480, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 580, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 530, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 630, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(100, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(198, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(150, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(252, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(300, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(400, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(498, 150, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(450, 150, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(550, 80, 522, 650))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.But_white = QtWidgets.QPushButton(self.centralwidget)
        self.But_white.setGeometry(QtCore.QRect(80, 680, 31, 31))
        self.But_white.setText("")
        self.But_white.setObjectName("But_white")
        self.But_red = QtWidgets.QPushButton(self.centralwidget)
        self.But_red.setGeometry(QtCore.QRect(360, 680, 31, 31))
        self.But_red.setStyleSheet("background-color:rgb(255, 0, 4)")
        self.But_red.setText("")
        self.But_red.setObjectName("But_red")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(110, 680, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(400, 680, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        Window1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window1)
        self.statusbar.setObjectName("statusbar")
        Window1.setStatusBar(self.statusbar)

        self.retranslateUi(Window1)
        QtCore.QMetaObject.connectSlotsByName(Window1)

        # self.add_function1()

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "Панель администратора"))
        self.but_back.setText(_translate("Window1", "Назад"))
        self.label.setText(_translate("Window1", "               Трибуна"))
        self.label_2.setText(_translate("Window1", "1"))
        self.label_3.setText(_translate("Window1", "1"))
        self.label_4.setText(_translate("Window1", "2"))
        self.label_5.setText(_translate("Window1", "3"))
        self.label_6.setText(_translate("Window1", "5"))
        self.label_7.setText(_translate("Window1", "4"))
        self.label_8.setText(_translate("Window1", "6"))
        self.label_9.setText(_translate("Window1", "7"))
        self.label_10.setText(_translate("Window1", "9"))
        self.label_11.setText(_translate("Window1", "8"))
        self.label_12.setText(_translate("Window1", "10"))
        self.label_13.setText(_translate("Window1", "2"))
        self.label_14.setText(_translate("Window1", "4"))
        self.label_15.setText(_translate("Window1", "3"))
        self.label_16.setText(_translate("Window1", "5"))
        self.label_17.setText(_translate("Window1", "6"))
        self.label_18.setText(_translate("Window1", "8"))
        self.label_19.setText(_translate("Window1", "7"))
        self.label_20.setText(_translate("Window1", "10"))
        self.label_21.setText(_translate("Window1", "9"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window1", "id"))        
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window1", "Ряд"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window1", "Место"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Window1", "Имя зрителя"))
        self.tableWidget.verticalHeader().setVisible(False)

        # for row_index, record in enumerate(mesto_user):
        #     self.tableWidget.insertRow(row_index)
        #     for col_index, value in enumerate(record):
        #         item = QTableWidgetItem(str(value))
        #         self.tableWidget.setItem(row_index, col_index, item)

        self.label_22.setText(_translate("Window1", "-свободное место"))
        self.label_23.setText(_translate("Window1", "-занятое место"))

    # def add_function1(self):
    #     print('')

    # def add_row(self):
    #     print('Кнопка')