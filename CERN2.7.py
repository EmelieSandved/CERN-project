import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QAction
from PyQt5.QtGui import QFont

class Window(QWidget):

    def __init__(self): #Creates an init method. Constructor
        super(Window, self).__init__() #Super return the parent object of the class. #Calls the constructor of the QWidget

        self.initUI() #Could be called externally in the if__name__ == '__main__': part

    def initUI(self):

        #Titlar och underrubriker
        self.titleTest = QLabel('<b>TEST</b>')
        self.titleTest.setFont(QFont('SansSerif', 14))
        self.subtitleTest = QLabel('Test Selection')

        #Dropdown test
        directorytestFiles = []
        self.dropDowntest = QComboBox()
        for index in os.listdir(): #Adds the files in the directory to a list
            directorytestFiles.append(index)
        for index in directorytestFiles: #Adds the text files in the directory to the drop down menu in alphabetic order
            self.dropDowntest.addItem(index)
        self.dropDowntest.activated[str].connect(self.open_file) #Connects the user's choice in the dropdown menu
        self.dropDowntest.setToolTip('List over Testfiles')

        #Textbox
        self.text = QTextEdit(self)

        #SaveButton
        self.saveButton = QPushButton('Save')
        self.saveButton.setToolTip('Press to save the changes')
        self.saveButton.clicked.connect(self.save_text)

        #RunButton
        self.runButton = QPushButton('Run')
        self.runButton.setToolTip('Press to run the testfile')
        self.runButton.clicked.connect(self.run_test)

        #Layout
        v1Layout = QVBoxLayout()
        h1Layout = QHBoxLayout()
        h2Layout = QHBoxLayout()

        v1Layout.addWidget(self.titleTest)
        h1Layout.addWidget(self.subtitleTest)
        h1Layout.addWidget(self.dropDowntest)
        h1Layout.addStretch(1)

        v1Layout.addLayout(h1Layout)
        v1Layout.addWidget(self.text)

        h2Layout.addWidget(self.saveButton)
        h2Layout.addWidget(self.runButton)

        v1Layout.addLayout(h2Layout)

        QToolTip.setFont(QFont('SansSerif', 10))

        #Creates the window's layout
        self.setLayout(v1Layout)
        self.setWindowTitle('MIDAS')
        self.show()

    #Function for dropdownbox
    def open_file(self, fileName):
        textFile = open(fileName).read()
        self.text.setText(textFile)

    #Function for SaveButton
    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME')) #The os.getenv accesses the file dialog (finder)
        with open(filename[0], 'w') as f: #What does this part mean?
            my_text = self.text.toPlainText()
            f.write(my_text)

    #Function for RunButton
    def run_test(self):
        pass

def main():

    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_()) #Enters the main loop (?) Ensures that the program ends correctly (?)

if __name__ == '__main__' :
    main()
