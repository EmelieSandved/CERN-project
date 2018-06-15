#Amanda Christianson
#2018-06


#Things to be done:
#Fix so that the program ends correctly when pressing the "Cancel" button in open and save file
#Implement a warning when closing the window (without saving)


#!/usr/in/python3 #Defines where the interpretor is located. Tells the operating system that it is a python script?
# -*- coding: utf-8 -*- #Necessary?

import sys #Necessary?
import os #Enables the use of the file dialoge
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont

def small_window():
    class Window(QWidget):

        def __init__(self): #Creates an init method. Constructor
            super(Window, self).__init__() #Super return the parent object of the class. #Calls the constructor of the QWidget

            self.text = QTextEdit(self) #To enable the text editor

            #Creates buttons
            self.openButton = QPushButton('Open') #Opens a text file
            self.clearButton = QPushButton('Clear') #Clears a text file
            self.saveButton = QPushButton('Save') #Saves the text file
            self.runButton = QPushButton('Run') #Runs the hypothetical test

            self.dropDown = QComboBox() #Creates a dropdown menu

            self.titleTest = QLabel('<b>TEST</b>') #Creates a label for the testing part of the interface
            self.titleTestSelection = QLabel('Test selection')

            #Declares what will be shown when the button is hovered over
            self.runButton.setToolTip('Press to run the test')
            self.saveButton.setToolTip('Press to save the changes')
            self.openButton.setToolTip('Press to open text file')
            self.clearButton.setToolTip('Press to clear the text file')

            self.initUI() #Could be called externally in the if__name__ == '__main__': part

        def initUI(self):
            vLayout = QVBoxLayout() #Creates a vertical box layout
            hLayout = QHBoxLayout() #Creates a horisontal box layout

            #Places a dropdown menu (not get fully functioning)
            vLayout.addWidget(self.titleTest)
            self.titleTest.setFont(QFont('SansSerif', 14)) #Sets the size of the test label
            vLayout.addWidget(self.titleTestSelection)

            vLayout.addWidget(self.dropDown)
            self.dropDown.addItem('File 1')
            self.dropDown.addItem('File 2')
            self.dropDown.addItem('File 3')

            vLayout.addWidget(self.openButton) #Places the open button

            vLayout.addWidget(self.text) #Places the text editor

            #Places buttons in the window
            hLayout.addWidget(self.clearButton)
            hLayout.addWidget(self.saveButton)
            hLayout.addWidget(self.runButton)

            #Assignes what will happen when the buttons are clicked on
            self.openButton.clicked.connect(self.open_text)
            self.clearButton.clicked.connect(self.clear_text)
            self.saveButton.clicked.connect(self.save_text)

            vLayout.addLayout(hLayout) #Adds the horisontal layout within the vertical layout

            QToolTip.setFont(QFont('SansSerif', 10)) #Sets the font for the Tooltip elements (the text explaining the function of a widget by popping up when hovered over)

            self.setLayout(vLayout)
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


    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_()) #Enters the main loop (?) Ensures that the program ends correctly (?)

def main(): #The main function

    small_window() #Runs the function that opens the window

if __name__ == '__main__' :
    main()
