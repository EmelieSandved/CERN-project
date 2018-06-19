import sys #Necessary?
import os #Enables the use of the file dialoge
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QAction
from PyQt5.QtGui import QFont

class Window(QWidget):

    def __init__(self): #Creates an init method. Constructor
        super(Window, self).__init__() #Super return the parent object of the class. #Calls the constructor of the QWidget

        self.initUI() #Could be called externally in the if__name__ == '__main__': part

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def initUI(self):

        self.text = QTextEdit(self)

        #Dropdown test
        directorytestFiles = []
        self.dropDowntest = QComboBox()
        for index in os.listdir(): #Adds the files in the directory to a list
            directorytestFiles.append(index)
        for index in directorytestFiles: #Adds the text files in the directory to the drop down menu in alphabetic order
            self.dropDowntest.addItem(index)
        self.dropDowntest.activated[str].connect(self.open_file) #Connects the user's choice in the dropdown menu
        self.dropDowntest.setToolTip('List over Testfiles')

        #Titlar och underrubriker
        self.titleTest = QLabel('<b>TEST</b>')
        self.titleTest.setFont(QFont('SansSerif', 14))
        self.subtitleTest = QLabel('Test Selection')

        #Layout
        v1Layout = QVBoxLayout()
        h1Layout = QHBoxLayout()

        v1Layout.addWidget(self.titleTest)
        h1Layout.addWidget(self.subtitleTest)
        h1Layout.addWidget(self.dropDowntest)
        h1Layout.addStretch(1)

        v1Layout.addLayout(h1Layout)
        v1Layout.addWidget(self.text)

        QToolTip.setFont(QFont('SansSerif', 10))

        #Skapar förstert
        self.setLayout(v1Layout)
        self.setWindowTitle('MIDAS')
        self.show()

def main():

    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_()) #Enters the main loop (?) Ensures that the program ends correctly (?)

if __name__ == '__main__' :
    main()
