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
        self.setupUI()
        
    def setupUI(self):
        global Plus3
        
        Plus3 = QtUiTools.QUiLoader().load(resource_path("plus.ui"))
        Plus3.setWindowTitle("환자 추가")
        
        Plus3.setGeometry(300, 100, 430, 205)
        Plus3.setFixedSize(430, 205)
        
        Plus3.show()
        Plus3.a.setChecked(True)

        Plus3.plus.clicked.connect(Plus.plus2)
 
    def plus2(self): 
        Fr = open("D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/patientData.csv",'r', encoding='utf-8')
        ReadF = csv.reader(Fr)
        keyword = Plus3.Name.text()
        Num = Plus3.Num.text()        
        
        alist = []
        aq = 0
        for line in ReadF:
            if(keyword==line[1]):
                if(Num == line[3]):
                    aq = 1
            alist.append(line[8])
                    
        rock = choice([i for i in range(0,999999) if i not in alist])       
        Fr.close()

        Ar = open("D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/patientData.csv",'a',newline="", encoding='utf-8')
        if(aq==0):
            a = Plus3.Name.text()
            if Plus3.man.isChecked() : b = "남"
            elif Plus3.woman.isChecked() : b = "여"
            else: b = '비공개'
            c = Plus3.Num.text()
            d1 = Plus3.key.text()
            d2 = Plus3.gram.text()
            if Plus3.a.isChecked() : e = "A"
            elif Plus3.b.isChecked() : e = "B"
            elif Plus3.ab.isChecked() : e = "AB"
            elif Plus3.o.isChecked() : e = "O"
            h = Plus3.home.text()
            rock = str(rock)
            rock = rock.zfill(6)
            i =  "ID"+rock
            Plus3.lock.setText(i)
            j = Plus3.day.text()
            
            
            Ar.write(i+','+a+','+j+','+c+','+b+',"'+h+'",'+e+','+d1+','+ d2 + "\n")
        

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)    
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Plus()
    sys.exit(app.exec_())        
        

