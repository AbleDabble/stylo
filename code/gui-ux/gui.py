try:
    import os
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import pyqtSlot
    from PyQt5.QtWidgets import QWidget, QMainWindow
except Exception as e:
    print("Some modules are missing  {}", format(e))

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 30, 331, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 110, 331, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 190, 331, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.id_click)
        self.pushButton_2.clicked.connect(self.ver_click)
        self.pushButton_3.clicked.connect(self.prof_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #set up the 3 buttons to take user to the proper pane
        self.pushButton.setText(_translate("MainWindow", "Authorship Identification"))
        self.pushButton_2.setText(_translate("MainWindow", "Authorship Verification"))
        self.pushButton_3.setText(_translate("MainWindow", "Authorship Profiling"))
        
    #opens the identification pane
    def id_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_identificationForm()
        self.ui.setupUi(self.window)
        self.window.show()
        print("ID Clicked")

    #opens the profiling pane
    def prof_click(self):
        prof_window = profiling()
        prof_window.show()

    #opens the verification pane
    def ver_click(self):
        ver_window = verification()
        ver_window.show()
        
class Ui_identificationForm(QWidget):
    def setupUi(self, identificationForm):
        identificationForm.setObjectName("identificationForm")
        identificationForm.resize(604, 363)
        self.numUsers = QtWidgets.QSpinBox(identificationForm)
        self.numUsers.setGeometry(QtCore.QRect(270, 100, 41, 21))
        self.numUsers.setObjectName("numUsers")
        self.user1 = QtWidgets.QLineEdit(identificationForm)
        self.user1.setGeometry(QtCore.QRect(20, 100, 241, 21))
        self.user1.setObjectName("user1")
        self.user2 = QtWidgets.QLineEdit(identificationForm)
        self.user2.setGeometry(QtCore.QRect(20, 130, 241, 21))
        self.user2.setObjectName("user2")
        self.user3 = QtWidgets.QLineEdit(identificationForm)
        self.user3.setGeometry(QtCore.QRect(20, 160, 241, 21))
        self.user3.setObjectName("user3")
        self.user4 = QtWidgets.QLineEdit(identificationForm)
        self.user4.setGeometry(QtCore.QRect(20, 190, 241, 21))
        self.user4.setObjectName("user4")
        self.user5 = QtWidgets.QLineEdit(identificationForm)
        self.user5.setGeometry(QtCore.QRect(20, 220, 241, 21))
        self.user5.setObjectName("user5")
        self.user6 = QtWidgets.QLineEdit(identificationForm)
        self.user6.setGeometry(QtCore.QRect(20, 250, 241, 21))
        self.user6.setObjectName("user6")
        self.user7 = QtWidgets.QLineEdit(identificationForm)
        self.user7.setGeometry(QtCore.QRect(20, 280, 241, 21))
        self.user7.setObjectName("user7")
        self.mainUser = QtWidgets.QLineEdit(identificationForm)
        self.mainUser.setGeometry(QtCore.QRect(330, 100, 241, 21))
        self.mainUser.setObjectName("mainUser")
        self.cValue = QtWidgets.QLineEdit(identificationForm)
        self.cValue.setGeometry(QtCore.QRect(330, 160, 71, 31))
        self.cValue.setObjectName("cValue")
        self.cReset = QtWidgets.QPushButton(identificationForm)
        self.cReset.setGeometry(QtCore.QRect(420, 160, 61, 31))
        self.cReset.setObjectName("cReset")
        self.redditChecked = QtWidgets.QCheckBox(identificationForm)
        self.redditChecked.setGeometry(QtCore.QRect(330, 220, 111, 17))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(identificationForm)
        self.twitterChecked.setGeometry(QtCore.QRect(330, 240, 111, 17))
        self.twitterChecked.setObjectName("twitterChecked")
        self.testButton = QtWidgets.QPushButton(identificationForm)
        self.testButton.setGeometry(QtCore.QRect(330, 260, 241, 41))
        self.testButton.setObjectName("testButton")

        self.retranslateUi(identificationForm)
        QtCore.QMetaObject.connectSlotsByName(identificationForm)

        #connect the buttons to their functions
        self.testButton.clicked.connect(self.testClicked)
        self.cReset.clicked.connect(self.cResetClicked)


    def retranslateUi(self, identificationForm):
        _translate = QtCore.QCoreApplication.translate
        identificationForm.setWindowTitle(_translate("identificationForm", "Stylometric Identification"))
        self.cReset.setText(_translate("identificationForm", "Reset C"))
        self.redditChecked.setText(_translate("identificationForm", "Download Reddit"))
        self.twitterChecked.setText(_translate("identificationForm", "Download Twitter"))
        self.testButton.setText(_translate("identificationForm", "Test"))

    def testClicked(self):
        print("testClicked")
        #check if reddit and twitter are set to download
        if self.redditChecked.isChecked() == True:
            print("Downloading usernames from reddit")
        if self.twitterChecked.isChecked() == True:
            print("Downloading usernames from twitter")

    def cResetClicked(self):
        print("cReset Clicked")
        self.cValue.setText("1")

    def pullUsernames(self):
        Users = []
        Users.append(self.user1.text())
        Users.append(self.user2.text())
        Users.append(self.user3.text())
        Users.append(self.user4.text())
        Users.append(self.user5.text())
        Users.append(self.user6.text())
        Users.append(self.user7.text())

class profiling(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.returnButton.setObjectName("returnButton")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 50, 281, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 281, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 160, 141, 16))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
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
        self.returnButton.setText(_translate("MainWindow", "< Return"))
        self.lineEdit_8.setText(_translate("MainWindow", "Username"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate Profile"))
        self.checkBox_2.setText(_translate("MainWindow", "Dowload Twitter"))
        self.checkBox.setText(_translate("MainWindow", "Download Reddit"))

class verification(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 160, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 160, 81, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 210, 231, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 160, 111, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
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
        self.pushButton.setText(_translate("MainWindow", "< Return"))
        self.lineEdit.setText(_translate("MainWindow", "Compare User One"))
        self.lineEdit_2.setText(_translate("MainWindow", "Compare User Two"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset C"))
        self.lineEdit_9.setText(_translate("MainWindow", "C Value"))
        self.pushButton_3.setText(_translate("MainWindow", "Test"))
        self.checkBox.setText(_translate("MainWindow", "Download Reddit"))
        self.checkBox_2.setText(_translate("MainWindow", "Dowload Twitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
