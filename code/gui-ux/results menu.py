# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultsMenu(object):
    def setupUi(self, ResultsMenu):
        ResultsMenu.setObjectName("ResultsMenu")
        ResultsMenu.resize(433, 569)
        self.newTestButton = QtWidgets.QPushButton(ResultsMenu)
        self.newTestButton.setGeometry(QtCore.QRect(90, 490, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newTestButton.setFont(font)
        self.newTestButton.setObjectName("newTestButton")
        self.textEdit = QtWidgets.QTextEdit(ResultsMenu)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 391, 451))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ResultsMenu)
        QtCore.QMetaObject.connectSlotsByName(ResultsMenu)

    def retranslateUi(self, ResultsMenu):
        _translate = QtCore.QCoreApplication.translate
        ResultsMenu.setWindowTitle(_translate("ResultsMenu", "Results Menu"))
        self.newTestButton.setText(_translate("ResultsMenu", "New Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsMenu = QtWidgets.QWidget()
    ui = Ui_ResultsMenu()
    ui.setupUi(ResultsMenu)
    ResultsMenu.show()
    sys.exit(app.exec_())

