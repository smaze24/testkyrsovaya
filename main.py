import datetime
import sqlite3
import time
import threading
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
import auto_generation

conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 273)
        Form.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/User/Desktop/pic1.jpg"))
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(139, 139, 209);\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(32, 32))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/User/Desktop/pic2.jpg"))
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit_2.setStyleSheet("background-color: rgb(139, 139, 209);\n"
                                      "color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 32))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 14pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.go)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Пароль"))
        self.pushButton.setText(_translate("Form", "Войти"))

    def go(self):

        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(login)
        print(password)

        c.execute("SELECT * FROM admins WHERE login = ? and password = ?", (login, password))
        result = c.fetchall()
        print(result)
        if result == []:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Логин или пароль введён не правильно')
            error.exec()
        else:
            Form.close()
            MainWindow.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 684)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.tabWidget.setToolTip("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-color: black;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-color: black;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-color: black;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-color: black;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border-style: solid;\n"
                                   "border-width: 1px;\n"
                                   "border-color: black;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.tab_6)
        self.label_25.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.tab_6)
        self.label_26.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_3.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.tab_6)
        self.label_27.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_3.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.tab_6)
        self.label_28.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.tab_6)
        self.label_29.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_30.setObjectName("label_30")
        self.verticalLayout_3.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.tab_6)
        self.label_31.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_3.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.tab_6)
        self.label_32.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_3.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.tab_6)
        self.label_33.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_3.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.tab_6)
        self.label_34.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: black;")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_3.addWidget(self.label_34)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.widget = QtWidgets.QWidget(self.tab_7)
        self.widget.setGeometry(QtCore.QRect(10, 10, 154, 112))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_7, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Звонки"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Клиенты"))
        self.label_25.setText(_translate("MainWindow", "TextLabel"))
        self.label_26.setText(_translate("MainWindow", "TextLabel"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "TextLabel"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Устройства"))
        self.label.setText(_translate("MainWindow", "Генерация звонков"))
        self.label_2.setText(_translate("MainWindow", "Генерация клиентов"))
        self.label_3.setText(_translate("MainWindow", "Генерация устройств"))
        self.label_4.setText(_translate("MainWindow", "Частота генерации"))
        self.pushButton.setText(_translate("MainWindow", "Применить частоту"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Генератор"))

    def pr(self):
        prohod = 1
        while True:
            box1 = self.checkBox.isChecked()
            box2 = self.checkBox_2.isChecked()
            box3 = self.checkBox_3.isChecked()
            if prohod == 1:
                box1 = True
                box2 = True
                box3 = True
                prohod = 0
            if box1 == True:
                auto_generation.gen_calls()
                c.execute("SELECT * FROM calls ORDER BY gen_time DESC")
                result = c.fetchall()
                self.label_5.setText(f'Звонит: {str(result[0][0])}\nОтвечает: {str(result[0][1])}\nВремя разговора: {str(result[0][2])}')
                self.label_6.setText(f'Звонит: {str(result[1][0])}\nОтвечает: {str(result[1][1])}\nВремя разговора: {str(result[1][2])}')
                self.label_7.setText(f'Звонит: {str(result[2][0])}\nОтвечает: {str(result[2][1])}\nВремя разговора: {str(result[2][2])}')
                self.label_8.setText(f'Звонит: {str(result[3][0])}\nОтвечает: {str(result[3][1])}\nВремя разговора: {str(result[3][2])}')
                self.label_9.setText(f'Звонит: {str(result[4][0])}\nОтвечает: {str(result[4][1])}\nВремя разговора: {str(result[4][2])}')
                self.label_10.setText(f'Звонит: {str(result[5][0])}\nОтвечает: {str(result[5][1])}\nВремя разговора: {str(result[5][2])}')
                self.label_11.setText(f'Звонит: {str(result[6][0])}\nОтвечает: {str(result[6][1])}\nВремя разговора: {str(result[6][2])}')
                self.label_12.setText(f'Звонит: {str(result[7][0])}\nОтвечает: {str(result[7][1])}\nВремя разговора: {str(result[7][2])}')
                self.label_13.setText(f'Звонит: {str(result[8][0])}\nОтвечает: {str(result[8][1])}\nВремя разговора: {str(result[8][2])}')
                self.label_14.setText(f'Звонит: {str(result[9][0])}\nОтвечает: {str(result[9][1])}\nВремя разговора: {str(result[9][2])}')
            if box2 == True:
                auto_generation.gen_clients()
                c.execute("SELECT * FROM clients ORDER BY gen_time DESC")
                result = c.fetchall()
                self.label_15.setText(f'Идентификатор: {str(result[0][0])}\nНомер паспорта: {str(result[0][1])}\nФИО: {str(result[0][2])}\nДата рождения: {str(result[0][3])}')
                self.label_16.setText(f'Идентификатор: {str(result[1][0])}\nНомер паспорта: {str(result[1][1])}\nФИО: {str(result[1][2])}\nДата рождения: {str(result[1][3])}')
                self.label_17.setText(f'Идентификатор: {str(result[2][0])}\nНомер паспорта: {str(result[2][1])}\nФИО: {str(result[2][2])}\nДата рождения: {str(result[2][3])}')
                self.label_18.setText(f'Идентификатор: {str(result[3][0])}\nНомер паспорта: {str(result[3][1])}\nФИО: {str(result[3][2])}\nДата рождения: {str(result[3][3])}')
                self.label_19.setText(f'Идентификатор: {str(result[4][0])}\nНомер паспорта: {str(result[4][1])}\nФИО: {str(result[4][2])}\nДата рождения: {str(result[4][3])}')
                self.label_20.setText(f'Идентификатор: {str(result[5][0])}\nНомер паспорта: {str(result[5][1])}\nФИО: {str(result[5][2])}\nДата рождения: {str(result[5][3])}')
                self.label_21.setText(f'Идентификатор: {str(result[6][0])}\nНомер паспорта: {str(result[6][1])}\nФИО: {str(result[6][2])}\nДата рождения: {str(result[6][3])}')
                self.label_22.setText(f'Идентификатор: {str(result[7][0])}\nНомер паспорта: {str(result[7][1])}\nФИО: {str(result[7][2])}\nДата рождения: {str(result[7][3])}')
                self.label_23.setText(f'Идентификатор: {str(result[8][0])}\nНомер паспорта: {str(result[8][1])}\nФИО: {str(result[8][2])}\nДата рождения: {str(result[8][3])}')
                self.label_24.setText(f'Идентификатор: {str(result[9][0])}\nНомер паспорта: {str(result[9][1])}\nФИО: {str(result[9][2])}\nДата рождения: {str(result[9][3])}')
            if box3 == True:
                auto_generation.gen_devices()
                c.execute("SELECT * FROM devices ORDER BY gen_time DESC")
                result = c.fetchall()
                self.label_25.setText(f'Идентификатор: {str(result[0][0])}\nНомер телефона: {str(result[0][1])}\nТип телефона: {str(result[0][2])}\nБаланс: {str(result[0][3])}\nАйди подписки{str(result[0][4])}')
                self.label_26.setText(f'Идентификатор: {str(result[1][0])}\nНомер телефона: {str(result[1][1])}\nТип телефона: {str(result[1][2])}\nБаланс: {str(result[1][3])}\nАйди подписки{str(result[1][4])}')
                self.label_27.setText(f'Идентификатор: {str(result[2][0])}\nНомер телефона: {str(result[2][1])}\nТип телефона: {str(result[2][2])}\nБаланс: {str(result[2][3])}\nАйди подписки{str(result[2][4])}')
                self.label_28.setText(f'Идентификатор: {str(result[3][0])}\nНомер телефона: {str(result[3][1])}\nТип телефона: {str(result[3][2])}\nБаланс: {str(result[3][3])}\nАйди подписки{str(result[3][4])}')
                self.label_29.setText(f'Идентификатор: {str(result[4][0])}\nНомер телефона: {str(result[4][1])}\nТип телефона: {str(result[4][2])}\nБаланс: {str(result[4][3])}\nАйди подписки{str(result[4][4])}')
                self.label_30.setText(f'Идентификатор: {str(result[5][0])}\nНомер телефона: {str(result[5][1])}\nТип телефона: {str(result[5][2])}\nБаланс: {str(result[5][3])}\nАйди подписки{str(result[5][4])}')
                self.label_31.setText(f'Идентификатор: {str(result[6][0])}\nНомер телефона: {str(result[6][1])}\nТип телефона: {str(result[6][2])}\nБаланс: {str(result[6][3])}\nАйди подписки{str(result[6][4])}')
                self.label_32.setText(f'Идентификатор: {str(result[7][0])}\nНомер телефона: {str(result[7][1])}\nТип телефона: {str(result[7][2])}\nБаланс: {str(result[7][3])}\nАйди подписки{str(result[7][4])}')
                self.label_33.setText(f'Идентификатор: {str(result[8][0])}\nНомер телефона: {str(result[8][1])}\nТип телефона: {str(result[8][2])}\nБаланс: {str(result[8][3])}\nАйди подписки{str(result[8][4])}')
                self.label_34.setText(f'Идентификатор: {str(result[9][0])}\nНомер телефона: {str(result[9][1])}\nТип телефона: {str(result[9][2])}\nБаланс: {str(result[9][3])}\nАйди подписки{str(result[9][4])}')
            time.sleep(self.spinBox.value())

print(datetime.datetime.now())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    x = threading.Thread(target=ui.pr)
    x.setDaemon(True)
    x.start()
    Form = QtWidgets.QWidget()
    ui2 = Ui_Form()
    ui2.setupUi(Form)
    Form.show()
    sys.exit(app.exec())