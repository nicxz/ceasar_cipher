# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ceasar/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 571)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.encryptButton = QtWidgets.QRadioButton(self.centralWidget)
        self.encryptButton.setGeometry(QtCore.QRect(20, 20, 100, 20))
        self.encryptButton.setChecked(True)
        self.encryptButton.setObjectName("encryptButton")
        self.decryptButton = QtWidgets.QRadioButton(self.centralWidget)
        self.decryptButton.setGeometry(QtCore.QRect(20, 40, 100, 20))
        self.decryptButton.setObjectName("decryptButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 371, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.inputText = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.inputText.setGeometry(QtCore.QRect(0, 0, 371, 171))
        self.inputText.setObjectName("inputText")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 280, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 60, 16))
        self.label_2.setObjectName("label_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 320, 371, 171))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 369, 169))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.outputText = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.outputText.setGeometry(QtCore.QRect(0, 0, 371, 171))
        self.outputText.setObjectName("outputText")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.switchButton = QtWidgets.QPushButton(self.centralWidget)
        self.switchButton.setGeometry(QtCore.QRect(0, 500, 113, 32))
        self.switchButton.setObjectName("switchButton")
        self.clearButton = QtWidgets.QPushButton(self.centralWidget)
        self.clearButton.setGeometry(QtCore.QRect(270, 500, 113, 32))
        self.clearButton.setObjectName("clearButton")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(130, 0, 121, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.keyInput = QtWidgets.QSpinBox(self.centralWidget)
        self.keyInput.setGeometry(QtCore.QRect(320, 30, 48, 24))
        self.keyInput.setMinimum(1)
        self.keyInput.setMaximum(25)
        self.keyInput.setProperty("value", 13)
        self.keyInput.setObjectName("keyInput")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 31, 20))
        self.label_4.setObjectName("label_4")
        self.scrollArea_2.raise_()
        self.encryptButton.raise_()
        self.decryptButton.raise_()
        self.scrollArea.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.switchButton.raise_()
        self.clearButton.raise_()
        self.label_3.raise_()
        self.keyInput.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ceasar"))
        self.encryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.label.setText(_translate("MainWindow", "Input"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.switchButton.setText(_translate("MainWindow", "Switch in/out"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Ceasar crypto tool"))
        self.keyInput.setToolTip(_translate("MainWindow", "<html><head/><body><p>How many places in the alphabet to shift (1-25)</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Key:"))

