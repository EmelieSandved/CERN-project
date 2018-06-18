#Amanda Christianson och Emelie Sandved
#2018-06


#Things to be done:
#Fix so that the program ends correctly when pressing the "Cancel" or red close button in open and save file
#Implement a warning when closing the window (without saving)
#The graph widget (figure) should not be opened/shown until a file is chosen in the drop down menu


#!/usr/in/python3 #Defines where the interpretor is located. Tells the operating system that it is a python script?
# -*- coding: utf-8 -*- #Necessary?

import sys #Necessary?
import os #Enables the use of the file dialoge
import math #Enables the use of sinus and cosinus for the creation of data
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QComboBox, QTextEdit, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import numpy as np #To use floats as x values
from numpy.fft import fft, fftshift

#For the graph
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random #To create data to plot (should be removed later on)
from datetime import datetime #Datetime is used to seed random (should be removed later on)


class Window(QWidget):

    def __init__(self): #Creates an init method. Constructor
        super(Window, self).__init__() #Super return the parent object of the class. #Calls the constructor of the QWidget

        self.initUI() #Could be called externally in the if__name__ == '__main__': part

    def initUI(self):

        self.text = QTextEdit(self) #To enable the text editor

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

        #FFT button
        self.fftButton = QCheckBox('FFT')
        self.fftButton.stateChanged.connect(self.fft_function)
        self.fftButton.setToolTip('Fast Fourier Transform')

        #Dropdown analyse
        directoryFiles = []
        self.dropDownAnalyse = QComboBox() #Creates a dropdown menu
        for index in os.listdir(): #Adds the files in the directory to a list
            directoryFiles.append(index)
        directoryFiles.sort() #Sorts the list with the files in the directory
        for index in directoryFiles: #Adds the text files in the directory to the drop down menu in alphabetic order
            if index.find('.txt') != -1: #Ensures that only text files are displayed as options (change so that it corresponds to the actual file type that we will use later on (if it is not .txt)
                self.dropDownAnalyse.addItem(index)
        self.dropDownAnalyse.activated[str].connect(self.plot)

        #Titles and subtitles
        self.titleTest = QLabel('<b>TEST</b>') #Creates a label for the testing part of the interface
        self.titleTest.setFont(QFont('SansSerif', 14)) #Sets the size of the test label
        self.subtitleTest = QLabel('Test selection:')
        self.titleAnalyse = QLabel('<b>ANALYSE</b>')
        self.titleAnalyse.setFont(QFont('SansSerif', 14))
        self.subtitleAnalyse = QLabel('Load test data:')

        #Diagram
        self.figure = plt.figure() #A figure to plot on
        self.canvas = FigureCanvas(self.figure) #Displays the figure
        self.toolbar = NavigationToolbar(self.canvas, self)

        #Layout
        v1Layout = QVBoxLayout() #Creates a vertical box layout
        h1Layout = QHBoxLayout() #Creates a horisontal box layout
        h2Layout = QHBoxLayout()
        h3Layout = QHBoxLayout()

        v1Layout.addWidget(self.titleTest) #Adds the widget for the test title to the vertical box layout
        h1Layout.addWidget(self.subtitleTest) #Adds the widget for the test subtitle to the first horisontal layout
        h1Layout.addWidget(self.dropDownTest)
        h1Layout.addStretch(1)

        v1Layout.addLayout(h1Layout) #Adds the first horisontal layout to the vertical layout
        v1Layout.addWidget(self.text) #Places the text editor

        h2Layout.addWidget(self.saveButton)
        h2Layout.addWidget(self.runButton)

        v1Layout.addLayout(h2Layout)
        v1Layout.addWidget(self.titleAnalyse)

        h3Layout.addWidget(self.subtitleAnalyse)
        h3Layout.addWidget(self.dropDownAnalyse)
<<<<<<< HEAD
        h3Layout.addWidget(self.fftButton)
=======
        h3Layout.addStretch(1)
>>>>>>> 488f1ffb9a88f9c74db54c4795e92157fdb10f04

        v1Layout.addLayout(h3Layout)

        #Layout for the graph
        v1Layout.addWidget(self.toolbar)
        v1Layout.addWidget(self.canvas)

        QToolTip.setFont(QFont('SansSerif', 10)) #Sets the font for the Tooltip elements (the text explaining the function of a widget by popping up when hovered over)

        self.setLayout(v1Layout)
        self.setWindowTitle('MIDAS') #Sets the window title
        self.show() #Shows the window

    def save_text(self): #Lets the user save a document in a chosen folder
        filename = QFileDialog.getSaveFileName(self, 'Save file', os.getenv('HOME')) #The os.getenv accesses the file dialog (finder)
        with open(filename[0], 'w') as f: #What does this part mean?
            my_text = self.text.toPlainText()
            f.write(my_text)

    def run_test(self):
        pass

    def plot(self, fileName): #Plots the data as a graph

        self.figure.clear() #Clears the figure. May be good to use if we decide to keep the plot button

        xList = [] #Creates lists for the x and y coordinates
        yList = []

        text_file = open(fileName, "r") #Opens and reads the file with the name passed as an argument to the function (the file chosen in the dropdown menu)
        lines = text_file.readlines()
        for line in lines: #Adds the x and y coordinates to the corresponding lists
            x,y = line.split(',')
            x = float(x)
            y = float(y)
            xList.append(x)
            yList.append(y)
        text_file.close()

        plt.xlabel('Time (s)')
        plt.ylabel('Voltage(V)')
        plt.plot(xList, yList)
        plt.axhline(0, color ='black', linewidth = 0.5) #Plots line at y = 0

        self.canvas.draw() #Draws the graph

    def fft_function(self, state):
        pass

def main(): #The main function


    random.seed(datetime.now()) #Seeds random from the current time

    """
    text_file = open("sine2.txt", "w")  # Creates/overwrites a text file with randomized data for the graph
    for index in np.arange(0.0, math.pi, 0.1): #(start, stop, step)
        x = str(index)
        y = str(math.sin(2*float(x)))
        #y = str(round(random.uniform(0,9), 3)) #Uniform is used to randomize floats. The floats are rounded to 3 decimals.
        text_file.write(x + ',' + y)
        text_file.write('\n')
    text_file.close()
    """

    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_()) #Enters the main loop (?) Ensures that the program ends correctly (?)

if __name__ == '__main__' :
    main()
