# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
# 'C:\Users\orhan\PycharmProjects\imageProcessingPixelation\ui_desing_file\design_file_pixelation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphics_view_input = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphics_view_input.setObjectName("graphics_view_input")
        self.gridLayout.addWidget(self.graphics_view_input, 0, 0, 1, 1)
        self.graphics_view_output = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphics_view_output.setObjectName("graphics_view_output")
        self.gridLayout.addWidget(self.graphics_view_output, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_edit_vertical = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_vertical.setObjectName("line_edit_vertical")
        self.verticalLayout.addWidget(self.line_edit_vertical)
        self.line_edit_horizontal = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_horizontal.setObjectName("line_edit_horizontal")
        self.verticalLayout.addWidget(self.line_edit_horizontal)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.push_button_update = QtWidgets.QPushButton(self.centralwidget)
        self.push_button_update.setObjectName("push_button_update")
        self.verticalLayout_3.addWidget(self.push_button_update)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CHOOSE FILE"))
        self.label_3.setText(_translate("MainWindow", "Window Pixel Size"))
        self.label.setText(_translate("MainWindow", "Vertical"))
        self.label_2.setText(_translate("MainWindow", "Horizontal"))
        self.push_button_update.setText(_translate("MainWindow", "UPDATE"))

