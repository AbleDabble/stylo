import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QDialogButtonBox,
    QLabel,
    QSizePolicy,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QRadioButton,
    QHBoxLayout,
    QSpinBox,
    QGridLayout,
    QTextEdit,
)

from PyQt5.QtGui import QFont

from PersonalityModel import start_personality_reddit, start_personality_twitter
from verifModel import start_verification_reddit, start_verification_twitter
from IdentModel import start_identification_reddit, start_identification_twitter


class PrimaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self._new_window = None
        self.initUI()
    
    def initUI(self):
        self.verificationButton = QPushButton("Authorship Verification")
        self.setFont(QFont('Arial', 14))
        self.verificationButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.identificationButton = QPushButton("Authorship Identification")
        self.identificationButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.profileButton = QPushButton("Authorship Profiling")
        self.profileButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # set up Events
        self.verificationButton.clicked.connect(self.verification)
        self.identificationButton.clicked.connect(self.identification)
        self.profileButton.clicked.connect(self.profile)

        # Setting Layout
        layout = QVBoxLayout()
        layout.addWidget(self.verificationButton)
        layout.addWidget(self.identificationButton)
        layout.addWidget(self.profileButton)
        self.setLayout(layout)
        self.setWindowTitle("Stylo")
        self.show()
    
    def verification(self):
        self._new_window = Verification()
        self._new_window.show()

    def identification(self):
        self._new_window = Identification()
        self._new_window.show()
    def profile(self):
        self._new_window = Profiling()
        self._new_window.show()

class Identification(QWidget):
    def __init__(self):
        super().__init__()
        self.site = "reddit"
        self.resize(500, 800)
        self.initUI()

    def initUI(self):
        self.setFont(QFont('Arial', 14))
        outerLayout = QVBoxLayout()
        self.topLayout = QFormLayout()
        self.users = []
        for i in range(1, 3):
            self.users.append(QLineEdit())
            self.topLayout.addRow(f'User', self.users[i-1])
        textLayout = QFormLayout()
        self.textInput = QTextEdit()
        textLayout.addRow('Text', self.textInput)
        self.textInput.textChanged.connect(self.count)
        
        botLayout = QGridLayout()
        spinLabel = QLabel("Number of Users")
        botLayout.addWidget(spinLabel, 0,0)
        spinBox = QSpinBox()
        spinBox.setValue(2)
        spinBox.valueChanged.connect(self.set_users)
        botLayout.addWidget(spinBox, 0, 1)

        redditBtn = QRadioButton("Reddit")
        redditBtn.setChecked(True)
        redditBtn.toggled.connect(self.toggle)
        botLayout.addWidget(redditBtn, 0, 2)
        twitterBtn = QRadioButton("Twitter")

        twitterBtn.toggled.connect(self.toggle)
        botLayout.addWidget(twitterBtn, 0, 3)
        
        self.charCount = QLabel("Character Count: 0")
        botLayout.addWidget(self.charCount, 1, 0)
        
        testBtn = QPushButton("Start Test")
        testBtn.clicked.connect(self.start)
        botLayout.addWidget(testBtn, 2, 0)
        
        outerLayout.addLayout(self.topLayout)
        outerLayout.addLayout(textLayout)
        outerLayout.addLayout(botLayout)

        self.setLayout(outerLayout)

    def toggle(self):
        self.site = self.sender().text().lower()
        print(f'Set Site to {self.site}')

    def start(self):
        usernames = [u.text().strip() for u in self.users if len(u.text().strip()) > 0]
        r = -1
        if self.site == 'reddit':
            r = start_identification_reddit(usernames, self.textInput.toPlainText().strip())
        if self.site == 'twitter':
            r = start_identification_twitter(usernames, self.textInput.toPlainText().strip())
        if type(r) == int:
            self._new_window = Results("Error downloading users")
            self._new_window.show()
        else:
            self._new_window = Results(f"The Most Likely User is: {r}")
            self._new_window.show()

    def count(self):
        sender = self.sender()
        self.charCount.setText("Character Count " + str(len(sender.toPlainText())))

    def set_users(self):
        sender = self.sender()
        if sender.value() > len(self.users):
            new_name = QLineEdit()
            self.topLayout.addRow("User", new_name)
            self.users.append(new_name)
        else:
            self.topLayout.itemAt(len(self.users) * 2 - 1).widget().deleteLater()
            self.topLayout.itemAt(len(self.users) * 2 - 2).widget().deleteLater()
            self.users.pop()

class Profiling(QWidget):
    def __init__(self):
        super().__init__()
        self.site = "reddit"
        self.initUI()
    
    def initUI(self):
        self.setFont(QFont('Arial', 14))
        outerLayout = QVBoxLayout()
        formLayout = QFormLayout()

        self.user = QLineEdit()
        formLayout.addRow("User", self.user)

        redditBtn = QRadioButton("Reddit")
        redditBtn.setChecked(True)
        redditBtn.toggled.connect(self.toggle)
        twitterBtn = QRadioButton("Twitter")
        twitterBtn.toggled.connect(self.toggle)

        botLayout = QHBoxLayout()
        botLayout.addWidget(redditBtn)
        botLayout.addWidget(twitterBtn)

        startBtn = QPushButton("Start Test")
        startBtn.clicked.connect(self.start)
        botLayout.addWidget(startBtn)
        outerLayout.addLayout(formLayout)
        outerLayout.addLayout(botLayout)

        self.setLayout(outerLayout)

    def toggle(self):
        sender = self.sender()
        self.site = sender.text().lower()

    def start(self):
        r = -1
        if self.site == 'reddit':
            r = start_personality_reddit(self.user.text().strip())
        if self.site == 'twitter':
            r = start_personality_twitter(self.user.text().strip())
        if type(r) == int:
            self._new_window = Results(f"The users predicted personality is {r}")
            self._new_window.show()
        # Results Dialog
        

class Verification(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.site = "reddit"

    def initUI(self):
        self.setFont(QFont('Arial', 14))
        outerLayout = QVBoxLayout()
        topLayout = QFormLayout()
        self.userOne = QLineEdit()
        self.userTwo = QLineEdit()

        # Add username inputs to top layout
        topLayout.addRow("User One:", self.userOne)
        topLayout.addRow("User Two:", self.userTwo)

        # Add Radio Buttons for Reddit or Twitter
        botLayout = QGridLayout()
        redditButton = QRadioButton("Reddit")
        redditButton.setChecked(True)
        redditButton.toggled.connect(self.toggle)
        botLayout.addWidget(redditButton, 0, 1)

        twitterButton = QRadioButton("Twitter")
        twitterButton.toggled.connect(self.toggle)
        botLayout.addWidget(twitterButton, 0, 0)

        testButton = QPushButton("Start Test")
        testButton.clicked.connect(self.start)
        botLayout.addWidget(testButton, 1, 0)

        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(botLayout)
        
        self.setLayout(outerLayout)
        
    def toggle(self):
        sender = self.sender()
        self.site = sender.text().lower()
        print(f'Button {sender.text()} was clicked')
    
    def start(self):
        r = -1
        if self.site == 'twitter':
            r = start_verification_twitter(self.userOne.text().strip(), self.usertwo.text().strip())
        if self.site == 'reddit':
            r = start_verification_reddit(self.userOne.text().strip(), self.userTwo.text().strip())
        if type(r) == int:
            self._new_window = Results("Error: Downloading User")
            self._new_window.show()
        else:
            if r == True:
                self._new_window = Results("These Two users match")
                self._new_window.show()
            elif r == False:
                self._new_window = Results("These two users do not match")
                self._new_window.show()
        #TODO add error dialog on case where it doesn't return boolean

class Results(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setFont(QFont('Arial', 14))
        layout = QVBoxLayout()
        label = QLabel(message)
        layout.addWidget(QLabel(message))
        self.setLayout(layout)

def main():
    print('Opening')
    app = QApplication(sys.argv)
    ex = PrimaryWindow()
    app.exec()
    #window = QWidget()
    #layout = QVBoxLayout()
    #layout.addWidget(QPushButton("Test"))
    #layout.addWidget(QPushButton("Test 2"))
    #window.setLayout(layout)
    #window.show()
    #app.exec()


if __name__ == "__main__":
    main()
        
        
        

