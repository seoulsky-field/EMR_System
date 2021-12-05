#-*- encoding: utf-8 -*-
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
from lib2to3.fixer_util import Newline
from random import choice




class Plus(QWidget):
    
    global count
    count = 0
    
    
    def __init__(self):
        super().__init__()
        
        self.setupUI()
        
    
        
        
    def setupUI(self):
        global Plus
        
        
        

        Plus = QtUiTools.QUiLoader().load(resource_path("plus.ui"))
        Plus.setWindowTitle("plus")
        
        
        Plus.setGeometry(300, 100, 430, 205)
        Plus.setFixedSize(430, 205)
        
        
        Plus.show()
        Plus.yang.setChecked(True)
        
        
        
        
        
        
        Plus.plus.clicked.connect(self.plus)
        



        
                
        
        
    def plus(self): 
        
        global count
        
        
        Fr = open('example.csv','r',newline="")
        ReadF = csv.reader(Fr)
        keyword = Plus.Name.text()
        Num = Plus.Num.text()        
        
        alist = []
        aq = 0
        for line in ReadF:
            if(keyword==line[0]):
                if(Num == line[2]):
                    aq = 1
            alist.append(line[8])
                    
        rock = choice([i for i in range(0,999999) if i not in alist])
                    
        Fr.close()
        
        Ar = open('example(plus).csv','a',newline="")
        WriteF = csv.writer(Ar)


        if(aq==0):
            if(count==0):
                WriteF.writerow("")
            a = Plus.Name.text()
            if Plus.man.isChecked() : b = "남"
            elif Plus.woman.isChecked() : b = "여"
            else: b = '비공개'
            c = Plus.Num.text()
            d = Plus.birth.text()
            if Plus.yang.isChecked() : e = "양"
            elif Plus.um.isChecked() : e = "음"
            f = Plus.Ph.text()
            g = Plus.Ph2.text()
            h = Plus.home.text()
            i =  rock
            Plus.lock.setText(str(rock))
            
            WriteF.writerow([a,b,c,d,e,f,g,h,i])
            count += 1
            
            
        
        



           
           
    
    
    
        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Plus()
    main.show()

    app.exec_()       
        

