# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'identification2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Identification(object):
    def setupUi(self, Identification):
        Identification.setObjectName("Identification")
        Identification.resize(469, 559)
        self.label = QtWidgets.QLabel(Identification)
        self.label.setGeometry(QtCore.QRect(20, 330, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Identification)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.identificationText = QtWidgets.QPlainTextEdit(Identification)
        self.identificationText.setGeometry(QtCore.QRect(20, 360, 431, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.identificationText.setFont(font)
        self.identificationText.setObjectName("identificationText")
        self.user1 = QtWidgets.QTextEdit(Identification)
        self.user1.setGeometry(QtCore.QRect(20, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user1.setFont(font)
        self.user1.setObjectName("user1")
        self.user2 = QtWidgets.QTextEdit(Identification)
        self.user2.setGeometry(QtCore.QRect(20, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user2.setFont(font)
        self.user2.setObjectName("user2")
        self.user3 = QtWidgets.QTextEdit(Identification)
        self.user3.setGeometry(QtCore.QRect(20, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user3.setFont(font)
        self.user3.setObjectName("user3")
        self.user4 = QtWidgets.QTextEdit(Identification)
        self.user4.setGeometry(QtCore.QRect(20, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user4.setFont(font)
        self.user4.setObjectName("user4")
        self.user5 = QtWidgets.QTextEdit(Identification)
        self.user5.setGeometry(QtCore.QRect(20, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user5.setFont(font)
        self.user5.setObjectName("user5")
        self.user6 = QtWidgets.QTextEdit(Identification)
        self.user6.setGeometry(QtCore.QRect(20, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user6.setFont(font)
        self.user6.setObjectName("user6")
        self.user7 = QtWidgets.QTextEdit(Identification)
        self.user7.setGeometry(QtCore.QRect(20, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user7.setFont(font)
        self.user7.setObjectName("user7")
        self.TestButton = QtWidgets.QPushButton(Identification)
        self.TestButton.setGeometry(QtCore.QRect(330, 40, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TestButton.setFont(font)
        self.TestButton.setObjectName("TestButton")
        self.redditChecked = QtWidgets.QCheckBox(Identification)
        self.redditChecked.setGeometry(QtCore.QRect(280, 270, 181, 17))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(Identification)
        self.twitterChecked.setGeometry(QtCore.QRect(280, 290, 181, 17))
        self.twitterChecked.setObjectName("twitterChecked")

        self.retranslateUi(Identification)
        QtCore.QMetaObject.connectSlotsByName(Identification)

    def retranslateUi(self, Identification):
        _translate = QtCore.QCoreApplication.translate
        Identification.setWindowTitle(_translate("Identification", "Form"))
        self.label.setText(_translate("Identification", "Enter Text to Identify Here"))
        self.label_2.setText(_translate("Identification", "Enter Probable Users Here"))
        self.TestButton.setText(_translate("Identification", "Test"))
        self.redditChecked.setText(_translate("Identification", "Download Usernames via Reddit"))
        self.twitterChecked.setText(_translate("Identification", "Download Usernames via Twitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Identification = QtWidgets.QWidget()
    ui = Ui_Identification()
    ui.setupUi(Identification)
    Identification.show()
    sys.exit(app.exec_())

