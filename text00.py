
import sys
import os
from PySide2 import QtUiTools, QtGui, QtCore
from PySide2.QtWidgets import QApplication,QMainWindow, QWidget, QDialog
from PySide2.QtWidgets import QFileDialog
import csv
import pickle
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from test.test_decimal import file
from text01 import Susul
from text02 import Fileread





class Mainwindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUI()
        
    def setupUI(self):
        global Main
        global UI_set
        
        Main = QtUiTools.QUiLoader().load(resource_path("main.ui"))
        

        Main.SEA.clicked.connect(self.clicked_option)
        
        self.setWindowTitle("main")
        self.resize(500,400)
        
        self.setCentralWidget(Main)
        
        
        
        
        
        
        
        self.show()
        
        
        

    def clicked_option(self):
        fileread = Fileread()
        
        
        
        
        
        

        
        






    

        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Mainwindow()
    

    sys.exit(app.exec_())       
        