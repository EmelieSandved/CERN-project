#Amanda Christianson och Emelie Sandved
#2018-06


#Things to be done:
#Fix so that the program ends correctly when pressing the "Cancel" or red close button in open and save file
#Implement a warning when closing the window (without saving)


#!/usr/in/python3 #Defines where the interpretor is located. Tells the operating system that it is a python script?
# -*- coding: utf-8 -*- #Necessary?

import sys #Necessary?
import os #Enables the use of the file dialoge
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont


class Window(QWidget):

    def __init__(self): #Creates an init method. Constructor
        super(Window, self).__init__() #Super return the parent object of the class. #Calls the constructor of the QWidget

        self.initUI() #Could be called externally in the if__name__ == '__main__': part

    def initUI(self):

        self.text = QTextEdit(self) #To enable the text editor

        #Open button
        self.openButton = QPushButton('Open') #Opens a text file
        self.openButton.setToolTip('Press to open text file') #Sets the tooltip for the button (what will happen when hovered over)
        self.openButton.clicked.connect(self.open_text) #Connects the button to a defined function

        #Clear button
        self.clearButton = QPushButton('Clear') #Clears a text file
        self.clearButton.setToolTip('Press to clear the text file')
        self.clearButton.clicked.connect(self.clear_text)

        #Save button
        self.saveButton = QPushButton('Save') #Saves the text file
        self.saveButton.setToolTip('Press to save the changes')
        self.saveButton.clicked.connect(self.save_text)

        #Run button
        self.runButton = QPushButton('Run') #Runs the hypothetical test
        self.runButton.setToolTip('Press to run the test')
        self.runButton.clicked.connect(self.run_test)

        #Dropdown test
        self.dropDownTest = QComboBox() #Creates a dropdown menu
        self.dropDownTest.addItem('File 1') #Adds items to the dropdown menu
        self.dropDownTest.addItem('File 2')
        self.dropDownTest.addItem('File 3')

        #Dropdown analyse
        self.dropDownAnalyse = QComboBox() #Creates a dropdown menu
        self.dropDownAnalyse.addItem('Data 1')
        self.dropDownAnalyse.addItem('Data 2')
        self.dropDownAnalyse.addItem('Data 3')

        #Titles and subtitles
        self.titleTest = QLabel('<b>TEST</b>') #Creates a label for the testing part of the interface
        self.titleTest.setFont(QFont('SansSerif', 14)) #Sets the size of the test label
        self.subtitleTest = QLabel('Test selection:')
        self.titleAnalyse = QLabel('<b>ANALYSE</b>')
        self.titleAnalyse.setFont(QFont('SansSerif', 14))
        self.subtitleAnalyse = QLabel('Load test data:')

        #Layout
        v1Layout = QVBoxLayout() #Creates a vertical box layout
        h1Layout = QHBoxLayout() #Creates a horisontal box layout
        h2Layout = QHBoxLayout()
        h3Layout = QHBoxLayout()

        v1Layout.addWidget(self.titleTest) #Adds the widget for the test title to the vertical box layout
        h1Layout.addWidget(self.subtitleTest) #Adds the widget for the test subtitle to the first horisontal layout
        h1Layout.addWidget(self.dropDownTest)

        v1Layout.addLayout(h1Layout) #Adds the first horisontal layout to the vertical layout
        v1Layout.addWidget(self.openButton)
        v1Layout.addWidget(self.text) #Places the text editor

        h2Layout.addWidget(self.clearButton)
        h2Layout.addWidget(self.saveButton)
        h2Layout.addWidget(self.runButton)

        v1Layout.addLayout(h2Layout)
        v1Layout.addWidget(self.titleAnalyse)

        h3Layout.addWidget(self.subtitleAnalyse)
        h3Layout.addWidget(self.dropDownAnalyse)

        v1Layout.addLayout(h3Layout)

        QToolTip.setFont(QFont('SansSerif', 10)) #Sets the font for the Tooltip elements (the text explaining the function of a widget by popping up when hovered over)

        self.setLayout(v1Layout)
        self.setWindowTitle('MIDAS') #Sets the window title
        self.show() #Shows the window

    def clear_text(self): #Clears a text document
        self.text.clear()

    def save_text(self): #Lets the user save a document in a chosen folder
        filename = QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME')) #The os.getenv accesses the file dialog (finder)
        with open(filename[0], 'w') as f: #What does this part mean?
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self): #Lets the user choose a file by opening the file dialoge (finder)
        filename = QFileDialog.getOpenFileName(self, 'Open file', os.getenv('HOME')) #The os.getenv accesses the file dialog (finder)
        with open(filename[0], 'r') as f: #What does this part mean?
            file_text = f.read()
            self.text.setText(file_text)

    def run_test(self):
        pass

def main(): #The main function

    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_()) #Enters the main loop (?) Ensures that the program ends correctly (?)

if __name__ == '__main__' :
    main()
