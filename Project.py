#Amanda Christianson och Emelie Sandved
#2018-06


#Things to be done:
#Fix so that the program ends correctly when pressing the "Cancel" or red close button in open and save file
#Implement a warning when closing the window (without saving)
#The graph widget (figure) should not be opened/shown until a file is chosen in the drop down menu
#Reload the drop down menus, call it each time the menu is closed
#Add felkontrollering: exeption: "try:...exept:..." Inform user..."finally: f.close()"

#!/usr/in/python3 #Defines where the interpretor is located. Tells the operating system that it is a python script?
# -*- coding: utf-8 -*-

#Imports the necessary libraries
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QDockWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np
from numpy.fft import fft, fftshift, fftfreq

#For the graph
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

#For the creation of data
import random
from datetime import datetime
import math


class Window(QWidget):
    #Creates an init method. Constructor
    def __init__(self):
         #Super returns the parent object of the class. #Calls the constructor of the QWidget
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):

        #Dropdown test
        directorytestFiles = []
        self.dropDownTest = QComboBox()
        for index in os.listdir(): #Adds the files in the directory to a list
            directorytestFiles.append(index)
        for index in directorytestFiles:
            if index.find('.py') == -1:
                self.dropDownTest.addItem(index)
        self.dropDownTest.activated[str].connect(self.open_file) #Connects the user's choice in the dropdown menu
        self.dropDownTest.setToolTip('List over Testfiles')

        #Textbox
        self.text = QTextEdit(self)
        self.text.hide()

        #SaveButton
        self.saveButton = QPushButton('Save')
        self.saveButton.setToolTip('Press to save the changes')
        self.saveButton.clicked.connect(self.save_text)

        #RunButton
        self.runButton = QPushButton('Run')
        self.runButton.setToolTip('Press to run the testfile')
        self.runButton.clicked.connect(self.run_test)
        #FFT button
        self.fftButton = QCheckBox('FFT')
        self.fftButton.setToolTip('Fast Fourier Transform')

        #Dropdown analyse
        self.dropDownAnalyse = QComboBox()
        #Adds the files in the directory to a list
        directoryFiles = sorted(os.listdir())
        #Adds the text files in the directory to the drop down menu in alphabetical order
        for index in directoryFiles:
            #Ensures that only text files are displayed as options
            if index.find('.txt') != -1:
                self.dropDownAnalyse.addItem(index)
        self.dropDownAnalyse.activated[str].connect(self.plot)

        #For the graph. The figure is where the data is plotted and the canvas is where the figure is displayed.
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.toolbar.hide()

        #Titles and subtitles
        self.titleTest = QLabel('<b>TEST</b>')
        self.titleTest.setFont(QFont('SansSerif', 14))
        self.subtitleTest = QLabel('Test selection:')
        self.titleAnalyse = QLabel('<b>ANALYSE</b>')
        self.titleAnalyse.setFont(QFont('SansSerif', 14))
        self.subtitleAnalyse = QLabel('Load test data:')

        #Layout
        #Creates a vertical box layout
        v1Layout = QVBoxLayout()
        #Creates horisontal box layouts
        h1Layout = QHBoxLayout()
        h2Layout = QHBoxLayout()
        h3Layout = QHBoxLayout()

        #Adds the widget for the test title to the vertical box layout
        v1Layout.addWidget(self.titleTest)

        #Adds widgets to the first horisontal layout
        h1Layout.addWidget(self.subtitleTest)
        h1Layout.addWidget(self.dropDownTest)

        #Pushes the widgets to the left corner
        h1Layout.addStretch(1)

        #Adds the first horisontal layout to the vertical layout
        v1Layout.addLayout(h1Layout)
        v1Layout.addWidget(self.text)

        h2Layout.addWidget(self.saveButton)
        h2Layout.addWidget(self.runButton)

        v1Layout.addLayout(h2Layout)
        v1Layout.addWidget(self.titleAnalyse)

        h3Layout.addWidget(self.subtitleAnalyse)
        h3Layout.addWidget(self.dropDownAnalyse)
        h3Layout.addWidget(self.fftButton)
        h3Layout.addStretch(1)

        v1Layout.addLayout(h3Layout)

        #Layout for the graph
        v1Layout.addWidget(self.toolbar)
        v1Layout.addWidget(self.canvas)

        #Sets the font for the Tooltip elements
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setLayout(v1Layout)
        self.setWindowTitle('MIDAS')
        #Shows the window
        self.show()

    #Function for dropdownbox
    def open_file(self, fileName):
        textFile = open(fileName).read()
        self.text.setText(textFile)
        self.text.show()

    #Lets the user save a document in a chosen folder
    def save_text(self):
        #Accesses the file dialog
        filename = QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def run_test(self):
        pass

    #Plots the data (of the file passed as an argument) as a graph
    def plot(self, fileName):

        self.figure.clear()
        #self.canvas.show()

        #Creates lists for the x and y coordinates
        xList = []
        yList = []

        #Opens and reads the file with the name passed as an argument to the function
        text_file = open(fileName, "r")
        lines = text_file.readlines()
        #Adds the data for the x and y coordinates to the corresponding lists
        for line in lines:
            x,y = line.split(',')
            x = float(x)
            y = float(y)
            xList.append(x)
            yList.append(y)
        text_file.close()

        #Sets the label of the y axis
        plt.ylabel('Voltage(V)')

        #Plots line at y = 0
        plt.axhline(0, color ='black', linewidth = 0.5)

        #Sets the label of the x axis and plots either the "regular" graph or the graph after FFT
        if self.fftButton.isChecked():
            plt.xlabel('Frequency (Hz)')
            plt.plot(xList, fft(yList))

        else:
            plt.xlabel('Time (s)')
            plt.plot(xList, yList)

        plt.tight_layout()
        self.canvas.draw()

    def fft_function(self):
        pass

#The main function
def main():
    #Seeds random from the current time
    random.seed(datetime.now())

    """
    # Creates/overwrites a text file with randomized data for the graph
    text_file = open("sine2integer.txt", "w")
    #Creates data points accordingly: (start, stop, step)
    for index in np.arange(0, math.pi, 0.1):
        x = str(index)
        y = str(math.sin(2*float(x)))
        #Uniform is used to randomize floats. The floats are rounded to 3 decimals.
        #y = str(round(random.uniform(0,9), 3))
        text_file.write(x + ',' + y)
        text_file.write('\n')
    text_file.close()
    """
    #Constructs an application object. sys.argv is a list of command line arguments.
    app = QApplication(sys.argv)
    ex = Window()
    #Makes the program wait for user input/action
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
