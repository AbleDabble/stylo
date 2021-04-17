try:
    import io
    import os
    import sys
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
# begin twitter scraping code, unable to import from file so far, added here for testing purposes

#end of twitter scraping code

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Stylometry - Team Stylo"))
        #set up the 3 buttons to take user to the proper pane
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
    def setupUi(self, identification):
        identification.setObjectName("identification")
        identification.resize(604, 363)
        self.numUsers = QtWidgets.QSpinBox(identification)
        self.numUsers.setGeometry(QtCore.QRect(270, 100, 41, 21))
        self.numUsers.setObjectName("numUsers")
        self.user1 = QtWidgets.QLineEdit(identification)
        self.user1.setGeometry(QtCore.QRect(20, 100, 241, 21))
        self.user1.setObjectName("user1")
        self.user2 = QtWidgets.QLineEdit(identification)
        self.user2.setGeometry(QtCore.QRect(20, 130, 241, 21))
        self.user2.setObjectName("user2")
        self.user3 = QtWidgets.QLineEdit(identification)
        self.user3.setGeometry(QtCore.QRect(20, 160, 241, 21))
        self.user3.setObjectName("user3")
        self.user4 = QtWidgets.QLineEdit(identification)
        self.user4.setGeometry(QtCore.QRect(20, 190, 241, 21))
        self.user4.setObjectName("user4")
        self.user5 = QtWidgets.QLineEdit(identification)
        self.user5.setGeometry(QtCore.QRect(20, 220, 241, 21))
        self.user5.setObjectName("user5")
        self.user6 = QtWidgets.QLineEdit(identification)
        self.user6.setGeometry(QtCore.QRect(20, 250, 241, 21))
        self.user6.setObjectName("user6")
        self.user7 = QtWidgets.QLineEdit(identification)
        self.user7.setGeometry(QtCore.QRect(20, 280, 241, 21))
        self.user7.setObjectName("user7")
        self.mainUser = QtWidgets.QLineEdit(identification)
        self.mainUser.setGeometry(QtCore.QRect(330, 100, 241, 21))
        self.mainUser.setObjectName("mainUser")
        self.redditChecked = QtWidgets.QCheckBox(identification)
        self.redditChecked.setGeometry(QtCore.QRect(330, 220, 111, 17))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(identification)
        self.twitterChecked.setGeometry(QtCore.QRect(330, 240, 111, 17))
        self.twitterChecked.setObjectName("twitterChecked")
        self.testButton = QtWidgets.QPushButton(identification)
        self.testButton.setGeometry(QtCore.QRect(330, 260, 241, 41))
        self.testButton.setObjectName("testButton")

        self.retranslateUi(identification)
        QtCore.QMetaObject.connectSlotsByName(identification)

        #connect the buttons to their functions
        self.testButton.clicked.connect(self.testClicked)


    def retranslateUi(self, identification):
        _translate = QtCore.QCoreApplication.translate
        identification.setWindowTitle(_translate("identification", "Stylometric Identification"))
        self.redditChecked.setText(_translate("identification", "Download Reddit"))
        self.twitterChecked.setText(_translate("identification", "Download Twitter"))
        self.testButton.setText(_translate("identification", "Test"))

    def testClicked(self):
        print("testClicked")
        #check if reddit and twitter are set to download
        if self.redditChecked.isChecked() == True:
            print("Downloading usernames from reddit")
        if self.twitterChecked.isChecked() == True:
            #take username from input and run the function for reddit or twitter, download and save into text file by name, perform feature extraction with profile class.

            print("Downloading usernames from twitter")
        #dowload main user and user one through seven, train the model on all seven users and the main user and try to predict which user has the greatest number out of each cycle.
        #startIdent(user, pullUsernames(), topMatches: int = 3, cVal: float = tbd, source: int = 1)

    def pullUsernames(self):
        Users = []
        Users.append(self.user1.text())
        Users.append(self.user2.text())
        Users.append(self.user3.text())
        Users.append(self.user4.text())
        Users.append(self.user5.text())
        Users.append(self.user6.text())
        Users.append(self.user7.text())
        return Users

    def countUsers(usernames):
        count = []
        for names in usernames:
            if(names.text() != ""):
                count.append(True)
            else:
                count.append(False)
        return count

class profiling(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(234, 191)
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
            #todo run entropy discrretization on downloaded corpus
        if(self.redditChecked.isChecked()):
            print(self.username.text())
            redditScraper().getUserComments(self.username.text())
            #todo: run entropy discretization on 

class verification(object):
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
        self.redditChecked.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.redditChecked.setObjectName("redditChecked")
        self.twitterChecked = QtWidgets.QCheckBox(Form)
        self.twitterChecked.setGeometry(QtCore.QRect(10, 120, 141, 17))
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
        self.cUserOne.setText(_translate("Form", "Compare User One"))
        self.cUserTwo.setText(_translate("Form", "Compare User Two"))
        self.redditChecked.setText(_translate("Form", "Download Reddit Users"))
        self.twitterChecked.setText(_translate("Form", "Download Twitter Users"))
        self.testButton.setText(_translate("Form", "Test"))

    def testClicked(self):
        if (self.redditChecked.isChecked()):
            print("downloading reddit")
            #todo search files for reddit profile, if not notify user of missing profile; and/or download from reddit
        if (self.twitterChecked.isChecked()):
            print("downloading twitter")
            #todo search files for reddit profile, if not notify user of missing profile; and/or download from twitter
        print("Test Clicked")
        #todo grab username1 and username2 files from ../corpora/reddit_corpus/ and ../corpora/twitter_corpus
        #todo compare two profiles (with entropy discretization?) and display value to user


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
