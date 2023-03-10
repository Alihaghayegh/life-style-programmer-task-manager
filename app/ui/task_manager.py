# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 619)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "    background-color: #3a424f;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.head_label = QtWidgets.QLabel(self.centralwidget)
        self.head_label.setGeometry(QtCore.QRect(200, 20, 341, 51))
        self.head_label.setStyleSheet("#head_label{\n"
                                      "    font: 16pt \"Arial\";\n"
                                      "    padding: 5px;\n"
                                      "    color: white;\n"
                                      "}")
        self.head_label.setObjectName("head_label")
        self.task_list = QtWidgets.QListWidget(self.centralwidget)
        self.task_list.setGeometry(QtCore.QRect(390, 120, 381, 461))
        self.task_list.setStyleSheet("#task_list {\n"
                                     "    background-color: darkgrey;\n"
                                     "    padding: 5px;\n"
                                     "}")
        self.task_list.setObjectName("task_list")
        self.task_input = QtWidgets.QLineEdit(self.centralwidget)
        self.task_input.setGeometry(QtCore.QRect(20, 120, 251, 41))
        self.task_input.setStyleSheet("#task_input {\n"
                                      "    font: 16px \"Arial\";\n"
                                      "    padding: 10px;\n"
                                      "}")
        self.task_input.setObjectName("task_input")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 70, 751, 20))
        self.line.setStyleSheet("#line{\n"
                                "    color: white;\n"
                                "}")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 220, 341, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Add = QtWidgets.QPushButton(self.layoutWidget)
        self.Add.setStyleSheet("#Add {\n"
                               "    background-color: #9bc1eb;\n"
                               "}\n"
                               "\n"
                               "#Add:hover {\n"
                               "    background-color: #5da2f0;\n"
                               "    color: white;\n"
                               "}")
        self.Add.setObjectName("Add")
        self.horizontalLayout_2.addWidget(self.Add)
        self.Edit = QtWidgets.QPushButton(self.layoutWidget)
        self.Edit.setStyleSheet("#Edit {\n"
                                "    background-color: #f0d999;\n"
                                "}\n"
                                "\n"
                                "#Edit:hover {\n"
                                "    background-color: #f0cb65;\n"
                                "    color: white;\n"
                                "}")
        self.Edit.setObjectName("Edit")
        self.horizontalLayout_2.addWidget(self.Edit)
        self.Delete = QtWidgets.QPushButton(self.layoutWidget)
        self.Delete.setStyleSheet("#Delete    {\n"
                                  "    background-color: #ed9595;\n"
                                  "}\n"
                                  "\n"
                                  "#Delete:hover {\n"
                                  "    background-color: #eb5959;\n"
                                  "    color: white;\n"
                                  "}")
        self.Delete.setObjectName("Delete")
        self.horizontalLayout_2.addWidget(self.Delete)
        self.task_datetime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.task_datetime.setGeometry(QtCore.QRect(20, 180, 341, 22))
        self.task_datetime.setObjectName("task_datetime")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 270, 341, 251))
        self.calendarWidget.setObjectName("calendarWidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 550, 341, 30))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.to_excel = QtWidgets.QPushButton(self.layoutWidget_2)
        self.to_excel.setStyleSheet("#to_excel {\n"
                                    "    background-color: #a2eba6;\n"
                                    "}\n"
                                    "\n"
                                    "#to_excel:hover {\n"
                                    "    background-color: #477a4a;\n"
                                    "    color: white;\n"
                                    "}")
        self.to_excel.setObjectName("to_excel")
        self.horizontalLayout_3.addWidget(self.to_excel)
        self.delete_all = QtWidgets.QPushButton(self.layoutWidget_2)
        self.delete_all.setStyleSheet("#delete_all {\n"
                                      "    background-color: #ed9595;\n"
                                      "}\n"
                                      "\n"
                                      "#delete_all:hover {\n"
                                      "    background-color: #eb5959;\n"
                                      "    color: white;\n"
                                      "}")
        self.delete_all.setObjectName("delete_all")
        self.horizontalLayout_3.addWidget(self.delete_all)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(282, 120, 81, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.footer = QtWidgets.QLabel(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(20, 590, 341, 16))
        self.footer.setStyleSheet("#footer {\n"
                                  "    color: white;\n"
                                  "    padding-left: 5px;\n"
                                  "}")
        self.footer.setObjectName("footer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task Manager"))
        self.head_label.setText(_translate(
            "MainWindow", "Programmer Task Manager"))
        self.task_input.setPlaceholderText(
            _translate("MainWindow", "Add Some Tasks..."))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.Edit.setText(_translate("MainWindow", "Edit"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.to_excel.setText(_translate("MainWindow", "Export to Excel"))
        self.delete_all.setText(_translate("MainWindow", "Delete All"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Done"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Done"))
        self.comboBox.setItemText(1, _translate("MainWindow", "In Progress"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Testing"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Failed"))
        self.footer.setText(_translate(
            "MainWindow", "Created by Ali Haghayegh 2023  github.com/Alihaghayegh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
