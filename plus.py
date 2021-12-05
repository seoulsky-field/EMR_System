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
        Plus.setWindowTitle("환자 추가")
        
        
        Plus.setGeometry(300, 100, 430, 205)
        Plus.setFixedSize(430, 205)
        
        
        Plus.show()
        Plus.a.setChecked(True)
        
        
        
        
        
        
        Plus.plus.clicked.connect(self.plus)
        



        
                
        
        
    def plus(self): 
        
        
        
        
        Fr = open('patientData.csv','r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        keyword = Plus.Name.text()
        Num = Plus.Num.text()        
        
        alist = []
        aq = 0
        for line in ReadF:
            if(keyword==line[1]):
                if(Num == line[3]):
                    aq = 1
            alist.append(line[8])
                    
        rock = choice([i for i in range(0,999999) if i not in alist])
                    
        Fr.close()
        
        Ar = open('patientData.csv','a',newline="", encoding='UTF8')


        if(aq==0):
            a = Plus.Name.text()
            if Plus.man.isChecked() : b = "남"
            elif Plus.woman.isChecked() : b = "여"
            else: b = '비공개'
            c = Plus.Num.text()
            d1 = Plus.key.text()
            d2 = Plus.gram.text()
            if Plus.a.isChecked() : e = "A"
            elif Plus.b.isChecked() : e = "B"
            elif Plus.ab.isChecked() : e = "AB"
            elif Plus.o.isChecked() : e = "O"
            h = Plus.home.text()
            rock = str(rock)
            rock = rock.zfill(6)
            i =  "ID"+rock
            Plus.lock.setText(i)
            j = Plus.day.text()
            
            
            Ar.write('\n'+i+','+a+','+j+','+c+','+b+',"'+h+'",'+e+','+d1+','+d2)
            
            
            
            
        
        



           
           
    
    
    
        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Plus()
    main.show()

    app.exec_()       
        

