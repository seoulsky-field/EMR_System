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


class patient(QWidget):
    global ID
    ID = -10
    
    
    def id(self,C):
        global ID
        
        ID = C
    
        
    
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
            Sul = QtUiTools.QUiLoader().load(resource_path("patient.ui"))


            global KSD
            KSD = str(ID)+ '.csv'
            
            
        
            Sul.setWindowTitle(KSD+"환자 정보")
            Sul.setGeometry(0, 0, 1100, 100)
            
            
            Sul.save.setMinimumHeight(50)
            Sul.save.setMinimumWidth(50)
            Sul.save.setMaximumHeight(50)
            Sul.save.setMaximumWidth(50)
        
            Sul.resulttable.setColumnWidth(0, 70)
            Sul.resulttable.setColumnWidth(1, 100)
            Sul.resulttable.setColumnWidth(2, 100)
            Sul.resulttable.setColumnWidth(3, 150)
            Sul.resulttable.setColumnWidth(4, 50)
            Sul.resulttable.setColumnWidth(5, 350)
            Sul.resulttable.setColumnWidth(6, 50)
            Sul.resulttable.setColumnWidth(7, 70)
            Sul.resulttable.setColumnWidth(8, 70)
            
            
            Sul.resulttable.setRowCount(1)


        
    

            Sul.show()
        
        
            self.showT()
        
        
        
        
          
            Sul.save.clicked.connect(patient.save2)
            
        
        

        

    
    def showT(self):
        global KSD
        
        
        
        self.row = 0 
        
        self.setTablewidgetdata()
    
        
        
        
    def setTablewidgetdata(self):
        Fr = open('patientData.csv','r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        
        row = 0


    
        for line in ReadF:
            
            if(str(ID) == line[1]):
                
            
                item = patient.cell(self,line[0])
                item1 = patient.cell(self,line[1])
                item2 = patient.cell(self,line[2])
                item3 = patient.cell(self,line[3])
                item4 = patient.cell(self,line[4])
                item5 = patient.cell(self,line[5])
                item6 = patient.cell(self,line[6])
                item7 = patient.cell(self,line[7])
                item8 = patient.cell(self,line[8])
            

                
                Sul.resulttable.setItem(row, 0, QTableWidgetItem(item))
                Sul.resulttable.setItem(row, 1, QTableWidgetItem(item1))
                Sul.resulttable.setItem(row, 2, QTableWidgetItem(item2))
                Sul.resulttable.setItem(row, 3, QTableWidgetItem(item3))
                Sul.resulttable.setItem(row, 4, QTableWidgetItem(item4))
                Sul.resulttable.setItem(row, 5, QTableWidgetItem(item5))
                Sul.resulttable.setItem(row, 6, QTableWidgetItem(item6))
                Sul.resulttable.setItem(row, 7, QTableWidgetItem(item7))
                Sul.resulttable.setItem(row, 8, QTableWidgetItem(item8))

            
                row+=1
        
        
        
                
        
        
    


    def save2(self):
        
        
        with open('patientData.csv', 'r', encoding='UTF8') as file:
            data = file.readlines() 
        
        roA = 0
        
        
        
        Fr = open('patientData.csv','r',newline="", encoding='UTF8')
        WriteF = csv.reader(Fr)
        
        for line in WriteF:
            if(str(ID) == line[1]):
                
                k = roA
                a = data[k].replace(line[0],Sul.resulttable.item(0,0).text())
                data[k] = a
                b = data[k].replace(line[1],Sul.resulttable.item(0,1).text())
                data[k] = b
                c = data[k].replace(line[2],Sul.resulttable.item(0,2).text())
                data[k] = c
                d = data[k].replace(line[3],Sul.resulttable.item(0,3).text())
                data[k] = d
                e = data[k].replace(line[4],Sul.resulttable.item(0,4).text())
                data[k] = e
                f = data[k].replace(line[5],Sul.resulttable.item(0,5).text())
                data[k] = f
                g = data[k].replace(line[6],Sul.resulttable.item(0,6).text())
                data[k] = g
                h = data[k].replace(line[7],Sul.resulttable.item(0,7).text())
                data[k] = h
                l = data[k].replace(line[8],Sul.resulttable.item(0,8).text())
                data[k] = l
                
                
            roA+=1

        
        print(data)
        
        with open('patientData.csv', 'w', encoding='UTF8') as file:
            file.writelines( data )



        



           
           
    def showModal(self):
        return super().exec_()
    
    
        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = patient()
    

    sys.exit(app.exec_())       
