try:
    import io
    import os
    import sys
    import nltk
    sys.path.append( './' )
    import tweepy
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import pyqtSlot
    from PyQt5.QtWidgets import QWidget, QMainWindow
    from EntropyDiscretization import EntropyDiscretization
except Exception as e:
    print("Some modules are missing  {}", format(e))
from Twitterscrape import twitScrape
from reddit_Scrape import redditScraper
from verifModel import start_verification_reddit, start_verification_twitter
from IdentModel import start_identification_reddit

class Ui_MainWindow(QMainWindow):
    #initialize main window
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
        #Form configuration
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
        
        #Link 3 buttons to their respective functions to open the panels
        self.pushButton.clicked.connect(self.id_click)
        self.pushButton_2.clicked.connect(self.ver_click)
        self.pushButton_3.clicked.connect(self.prof_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stylometry - Team Stylo"))
        self.pushButton.setText(_translate("MainWindow", "Authorship Identification"))
        self.pushButton_2.setText(_translate("MainWindow", "Authorship Verification"))
        self.pushButton_3.setText(_translate("MainWindow", "Authorship Profiling"))
        
    #opens the identification pane
    def id_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = identification()
        self.ui.setupUi(self.window)
        self.window.show()
        print("ID Clicked")

    #opens the profiling pane
    def prof_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = profiling()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Profiling Clicked")

    #opens the verification pane
    def ver_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = verification()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Verification Clicked")
        
class identification(QWidget):
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

        self.TestButton.clicked.connect(self.testClicked)

    def retranslateUi(self, Identification):
        _translate = QtCore.QCoreApplication.translate
        Identification.setWindowTitle(_translate("Identification", "Form"))
        self.label.setText(_translate("Identification", "Enter Text to Identify Here (>350 Characters Only"))
        self.label_2.setText(_translate("Identification", "Enter Probable Users Here"))
        self.TestButton.setText(_translate("Identification", "Test"))
        self.redditChecked.setText(_translate("Identification", "Download Usernames via Reddit"))
        self.twitterChecked.setText(_translate("Identification", "Download Usernames via Twitter"))
        #connect the buttons to their functions

    def testClicked(self):
        print("testClicked")
        #check if reddit and twitter are set to download
        if self.redditChecked.isChecked() == True:
            print("Downloading usernames from reddit")
            self.usersList = self.pullUsernames()
            self.textToCompare = self.identificationText.toPlainText()
            if (self.countWords(self.textToCompare) < 350):
                self.showDialogue("Must have >350 words")
            return 0
            print(self.textToCompare)
            print(self.usersList)
            self.stringMatch = start_identification_reddit(self.usersList, self.textToCompare)
            self.showResults(self.stringMatch)
            # change to twitter self.stringMatch = start_identification_reddit(self.usersList, self.textToCompare)
            #use william's function that takes array of users and a text
        if self.twitterChecked.isChecked() == True:
            #take username from input and run the function for reddit or twitter, download and save into text file by name, perform feature extraction with profile class.
            self.usersList = self.pullUsernames()
            self.textToCompare = self.identificationText.toPlainText()
            if (self.countWords(self.textToCompare) < 350):
                self.showDialogue("Must have >350 words")
            return 0
            print("Downloading usernames from twitter")
        elif (self.redditChecked.isChecked() == False and self.twitterChecked.isChecked() == False):
            self.showDialogue("Select Twitter/Reddit")
        

        #dowload main user and user one through seven, train the model on all seven users and the main user and try to predict which user has the greatest number out of each cycle.

    def pullUsernames(self):
        Users = []
        Users.append(self.user1.toPlainText())
        Users.append(self.user2.toPlainText())
        Users.append(self.user3.toPlainText())
        Users.append(self.user4.toPlainText())
        Users.append(self.user5.toPlainText())
        Users.append(self.user6.toPlainText())
        Users.append(self.user7.toPlainText())
        print(Users)
        return Users
        #handle edge case of missing/blank users

    def countWords(self, words):
        count = 0
        for word in words:
            count += 1
        return count


    def showResults(self, userArray):
        self.window = QtWidgets.QMainWindow()
        self.ui = ResultsMenu(userArray, 1)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def showDialogue(self, message):
        self.window = QtWidgets.QMainWindow()
        self.ui = dialogue(message)
        self.ui.setupUi(self.window)
        self.window.show()

class verification(QWidget):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(361, 253)
        self.cUserOne = QtWidgets.QLineEdit(Form)
        self.cUserOne.setGeometry(QtCore.QRect(10, 20, 241, 31))
        self.cUserOne.setObjectName("cUserOne")
        self.cUserTwo = QtWidgets.QLineEdit(Form)
        self.cUserTwo.setGeometry(QtCore.QRect(10, 60, 241, 31))
        self.cUserTwo.setObjectName("cUserTwo")
        self.redditChecked = QtWidgets.QCheckBox(Form)
        self.redditChecked.setGeometry(QtCore.QRect(10, 100, 200, 16))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(Form)
        self.twitterChecked.setGeometry(QtCore.QRect(10, 120, 200, 17))
        self.twitterChecked.setObjectName("twitterChecked")
        self.testButton = QtWidgets.QPushButton(Form)
        self.testButton.setGeometry(QtCore.QRect(10, 150, 241, 31))
        self.testButton.setObjectName("testButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.testButton.clicked.connect(self.testClicked)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stylometric Verification"))
        self.cUserOne.setText(_translate("Form", ""))
        self.cUserTwo.setText(_translate("Form", ""))
        self.redditChecked.setText(_translate("Form", "Download Reddit Users"))
        self.twitterChecked.setText(_translate("Form", "Download Twitter Users"))
        self.testButton.setText(_translate("Form", "Test"))
    

    def testClicked(self):
        self.userArray = []
        if (len(self.cUserOne.text()) == 0 or len(self.cUserTwo.text()) == 0):
            self.showDialogue("Enter Two Usernames")
            return 0

        if(self.redditChecked.isChecked() and self.twitterChecked.isChecked()):
            self.showDialogue("Select Reddit or Twitter")
            return 0

        if (self.redditChecked.isChecked()):
            print("downloading reddit")
            nltk.download("punkt")
            self.result = start_verification_reddit(self.cUserOne.text(), self.cUserTwo.text())
        
        if (self.twitterChecked.isChecked()):
            print("downloading twitter")
            self.result = start_verification_twitter(self.cUserOne.text(), self.cUserTwo.text())
            #todo start verification from twitter

        self.userArray.append(self.cUserOne.text())
        self.userArray.append(self.cUserTwo.text())
        if type(self.result) == int:
            self.userArray.append("The user doesn't exist, or there is not enough data for the user")
        elif (self.result == True):
            self.userArray.append("Users Match")
        elif (self.result == False):
            self.userArray.append("Users do not Match")
        print(self.userArray)

        #verify reddit
        self.showResults(self.userArray)
        print("Test Clicked")

    def showResults(self, userArray):
        self.window = QtWidgets.QMainWindow()
        self.ui = ResultsMenu(self.userArray, 2)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def showDialogue(self, message):
        self.window = QtWidgets.QMainWindow()
        self.ui = dialogue(message)
        self.ui.setupUi(self.window)
        self.window.show()

class profiling(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 180)
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.username.setObjectName("username")
        self.redditChecked = QtWidgets.QCheckBox(Form)
        self.redditChecked.setGeometry(QtCore.QRect(10, 70, 211, 17))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(Form)
        self.twitterChecked.setGeometry(QtCore.QRect(10, 90, 211, 17))
        self.twitterChecked.setObjectName("twitterChecked")
        self.profileButton = QtWidgets.QPushButton(Form)
        self.profileButton.setGeometry(QtCore.QRect(10, 120, 211, 31))
        self.profileButton.setObjectName("profileButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.profileButton.clicked.connect(self.profilingTestClicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Styolometric Profiling"))
        self.username.setText(_translate("Form", "Username"))
        self.redditChecked.setText(_translate("Form", "Download Reddit Users"))
        self.twitterChecked.setText(_translate("Form", "Download Twitter Users"))
        self.profileButton.setText(_translate("Form", "Generate Profile"))
    
    def profilingTestClicked(self):
        if(self.twitterChecked.isChecked()):
            print(self.username.text())
            twitScrape().getIndivTweets(self.username.text())
            #todo run entropy discretization on downloaded corpus
        if(self.redditChecked.isChecked()):
            print(self.username.text())
            redditScraper().getUserComments(self.username.text())
        #data = get data from model trainer
        self.profiling = []
        self.profiling.append(self.username.text())



        self.showResults(self.profiling)
            #todo: run entropy discretization on corpus based on reddit comments

        #Open display window for results
    def showResults(self, userArray):
        self.window = QtWidgets.QMainWindow()
        self.ui = ResultsMenu(userArray, 3)
        self.ui.setupUi(self.window)
        self.window.show()

    def showDialogue(self, message):
        self.window = QtWidgets.QMainWindow()
        self.ui = dialogue(message)
        self.ui.setupUi(self.window)
        self.window.show()

        #eventually, created window for results new test button should be able to close using a function here
    
class ResultsMenu(QWidget):
    def __init__(self, userArray, useCase):
        print("Constructed Results Menu")
        self.array = userArray
        self.useCase = useCase

    def setupUi(self, ResultsMenu):
        ResultsMenu.setObjectName("ResultsMenu")
        ResultsMenu.resize(433, 569)

        self.textEdit = QtWidgets.QTextEdit(ResultsMenu)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 391, 500))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ResultsMenu)
        QtCore.QMetaObject.connectSlotsByName(ResultsMenu)
        if(self.useCase == 1):
            self.printDataIdentification(self.array)
        elif(self.useCase == 2):
            self.printDataVerification(self.array)
        elif(self.useCase == 3):
            self.printDataProfiling(self.array)
        else:
            print("Improper model input to print function")

    def retranslateUi(self, ResultsMenu):
        _translate = QtCore.QCoreApplication.translate
        ResultsMenu.setWindowTitle(_translate("ResultsMenu", "Results Menu"))

    def printDataIdentification(self, dataArray):
        for user in dataArray:
            self.textEdit.append(user)
            print(user)
    
    def printDataVerification(self, dataArray):
        for user in dataArray:
            self.textEdit.append(user)

    def printDataProfiling(self, dataArray):
        statement = "User profile added to corpus folder for: "
        for user in dataArray:
            print(statement + user)
        self.textEdit.append(statement + user)
        

        
        #Probably add an integer input for case switch to differentiate ident/verif/prof outputs

class dialogue(object):
    def __init__(self, message):
        print("Constructed Dialogue")
        self.text = message
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 162)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.printMessage(self.text)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))

    def printMessage(self, message):
        self.text = message
        self.label.setText(self.text)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
