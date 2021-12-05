
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
from Surgery import Susul
from Prescription import Cheobang
from visit import Naewon
from patient import patient




class Fileread(QWidget):
    
    def __init__(self,parent=None):
        super().__init__()
        
        self.setupUI()
        
    def cell(self,var=""):
            item = QTableWidgetItem()
            item.setText(var)
            return item
        
        
    def setupUI(self):
        global UI_set
        
        UI_set = QtUiTools.QUiLoader().load(resource_path("search.ui"))



        UI_set.setWindowTitle("Medical")
        
        UI_set.setGeometry(300, 100, 1100, 400)
        
        UI_set.resulttable.setColumnWidth(0, 80)
        UI_set.resulttable.setColumnWidth(1, 70)
        UI_set.resulttable.setColumnWidth(2, 100)
        UI_set.resulttable.setColumnWidth(3, 120)
        UI_set.resulttable.setColumnWidth(4, 50)
        UI_set.resulttable.setColumnWidth(5, 400)
        UI_set.resulttable.setColumnWidth(6, 50)
        UI_set.resulttable.setColumnWidth(7, 70)
        UI_set.resulttable.setColumnWidth(8, 70)
        
        
        
        UI_set.show()
        
        UI_set.revise_add2.clicked.connect(Fileread.revise_add)

        
    def revise_add(self):

        
        Fr = open('patientData1.csv','r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        
        
        
        keyword = UI_set.revise_add.text()
        
        row = 0    
        column = 0
        list = 0
        
        for line in ReadF:
            if(keyword==line[1]):
                if(list!=line[0]):
                    column += 1
                list = line[0]
                
                
    
        UI_set.resulttable.setRowCount(column)
        
        Fr.close()
        
        Fr = open('patientData1.csv','r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        
        keyword = UI_set.revise_add.text()

        list2 = 0
    
        for line in ReadF:
            if(keyword==line[1]):
                if(list2!=line[0]):
                    item = Fileread.cell(self,line[0])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    search1 = Fileread.cell(self,line[2])
                    search1.setFlags(QtCore.Qt.ItemIsEnabled)
                    item1 = Fileread.cell(self,line[1])
                    item1.setFlags(QtCore.Qt.ItemIsEnabled)
                    item3 = Fileread.cell(self,line[3])
                    item3.setFlags(QtCore.Qt.ItemIsEnabled)
                    item4 = Fileread.cell(self,line[4])
                    item4.setFlags(QtCore.Qt.ItemIsEnabled)
                    item5 = Fileread.cell(self,line[5])
                    item5.setFlags(QtCore.Qt.ItemIsEnabled)
                    item6 = Fileread.cell(self,line[6])
                    item6.setFlags(QtCore.Qt.ItemIsEnabled)
                    item7 = Fileread.cell(self,line[7])
                    item7.setFlags(QtCore.Qt.ItemIsEnabled)
                    item8 = Fileread.cell(self,line[8])
                    item8.setFlags(QtCore.Qt.ItemIsEnabled)
                    
    
                    
                    UI_set.resulttable.setItem(row, 0, QTableWidgetItem(line[0]))
                    UI_set.resulttable.setItem(row, 0, QTableWidgetItem(item))
    
                    UI_set.resulttable.setItem(row, 1, QTableWidgetItem(item1))
                    UI_set.resulttable.setItem(row, 2, QTableWidgetItem(search1))
                    UI_set.resulttable.setItem(row, 3, QTableWidgetItem(item3))
                    UI_set.resulttable.setItem(row, 4, QTableWidgetItem(item4))
                    UI_set.resulttable.setItem(row, 5, QTableWidgetItem(item5))
                    UI_set.resulttable.setItem(row, 6, QTableWidgetItem(item6))
                    UI_set.resulttable.setItem(row, 7, QTableWidgetItem(item7))
                    UI_set.resulttable.setItem(row, 8, QTableWidgetItem(item8))
                    
                    row += 1
                list2 = line[0]
                
                
        UI_set.resulttable.doubleClicked.connect(Fileread.treeMedia_doubleClicked)
 
    def treeMedia_doubleClicked(self):
        row = UI_set.resulttable.currentIndex().row()
        column = UI_set.resulttable.currentIndex().column()
        if(column==0):
            k = UI_set.resulttable.item(row,column).text()
            UI_set.revise_add.setText(k)
            susul = Susul()
            
            susul.id(k)
            susul.__init__()
            
            cheobang = Cheobang()
            cheobang.id(k)
            cheobang.__init__()
            
            naewon = Naewon()
            naewon.id(k)
            naewon.__init__()

            Patient = patient()
            Patient.id(k)
            Patient.__init__()


           
           
    def showModal(self):
        return super().exec_()
    
    

        


    
    
    
        

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Fileread()
    

    sys.exit(app.exec_())       
        