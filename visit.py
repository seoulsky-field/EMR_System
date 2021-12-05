#-*- encoding: utf-8 -*-

import sys
import os
from PySide2 import QtUiTools, QtGui, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QDialog, QPushButton
from PySide2.QtWidgets import QFileDialog
import csv
import pickle
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader


class Naewon(QWidget):
    global ID
    ID = -10
    
    def id(self,c):
        global ID
        ID = c
        
    
    def __init__(self):
        self.setupUI()
        
    def cell(self,var=""):
            item = QTableWidgetItem()
            item.setText(var)
            return item
        
        
    def setupUI(self):
        global Sul
        global ID
        if(ID!=-10):
            Sul = QtUiTools.QUiLoader().load(resource_path("Visit.ui"))


            global KSD
            KSD = ID+ '_visit.csv'
            print(KSD)
            
        
            Sul.setWindowTitle(KSD)
            Sul.setGeometry(300, 700,1000, 400)
            Sul.plus.setMinimumHeight(50)
            Sul.plus.setMinimumWidth(50)
            Sul.plus.setMaximumHeight(50)
            Sul.plus.setMaximumWidth(50)
            Sul.plus.move(0,0)
        
            Sul.minus.setMinimumHeight(50)
            Sul.minus.setMinimumWidth(50)
            Sul.minus.setMaximumHeight(50)
            Sul.minus.setMaximumWidth(50)
            Sul.minus.move(110,0)
            
            Sul.save.setMinimumHeight(50)
            Sul.save.setMinimumWidth(50)
            Sul.save.setMaximumHeight(50)
            Sul.save.setMaximumWidth(50)
        
            Sul.resulttable.setColumnWidth(0, 100)
            Sul.resulttable.setColumnWidth(1, 80)
            Sul.resulttable.setColumnWidth(2, 80)
            Sul.resulttable.setColumnWidth(3, 130)
            Sul.resulttable.setColumnWidth(4, 200)
            Sul.resulttable.setColumnWidth(5, 200)


        
        
            
        
            Fr = open(KSD,'r', encoding='UTF8')
            ReadF = csv.reader(Fr)
          
            column = -1
        
            for line in ReadF:
                column += 1





            Sul.resulttable.setRowCount(column)

            Sul.show()
        
        
            self.showT()
        
        
        
        
            Sul.plus.clicked.connect(Naewon.plus2)
            Sul.minus.clicked.connect(Naewon.minus2)
            Sul.save.clicked.connect(Naewon.save2)
            
        
        

        

    
    def showT(self):
        global KSD
        
        
        
        self.row = 0 
        
        self.setTablewidgetdata()
    
        
        
        
    def setTablewidgetdata(self):
        Fr = open(KSD,'r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        
        row = 0


    
        for line in ReadF:
            
            item = Naewon.cell(self,line[0])
            item1 = Naewon.cell(self,line[1])
            item2 = Naewon.cell(self,line[2])
            item3 = Naewon.cell(self,line[3])
            item4 = Naewon.cell(self,line[4])
            item5 = Naewon.cell(self,line[5])

            

                
            Sul.resulttable.setItem(row-1, 0, QTableWidgetItem(item))
            Sul.resulttable.setItem(row-1, 1, QTableWidgetItem(item1))
            Sul.resulttable.setItem(row-1, 2, QTableWidgetItem(item2))
            Sul.resulttable.setItem(row-1, 3, QTableWidgetItem(item3))
            Sul.resulttable.setItem(row-1, 4, QTableWidgetItem(item4))
            Sul.resulttable.setItem(row-1, 5, QTableWidgetItem(item4))


            
            row+=1
        
        
        
                
        
        
    def plus2(self): 
        row_count = Sul.resulttable.rowCount() 
        Sul.resulttable.setRowCount(row_count+1)
        Naewon.setTablewidgetdata(self)
        
    def minus2(self): 
        row_count = Sul.resulttable.rowCount() 
        Sul.resulttable.setRowCount(row_count-1)
        Naewon.setTablewidgetdata(self)


    def save2(self):
        Fr = open(KSD,'w',newline="", encoding='UTF8')
        WriteF = csv.writer(Fr)
        
        row_count = Sul.resulttable.rowCount()
        
        WriteF.writerow(['진료 날짜','내원 구분','진료 과','진료의','환자 통증','담당의 소견'])
        
        for i in range(row_count):
            a = Sul.resulttable.item(i,0).text()
            b = Sul.resulttable.item(i,1).text()
            c = Sul.resulttable.item(i,2).text()
            d = Sul.resulttable.item(i,3).text()
            e = Sul.resulttable.item(i,4).text()
            f = Sul.resulttable.item(i,5).text()

            
            WriteF.writerow([a,b,c,d,e,f])

        
        
        
        
        



        



           
           
    def showModal(self):
        return super().exec_()
    
    
        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Naewon()
    

    sys.exit(app.exec_())       
     