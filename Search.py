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

from SubMain import SubMain



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
        UI_set.setGeometry(300, 100, 500, 400)
        UI_set.resulttable.setColumnWidth(0, 100)
        UI_set.resulttable.setColumnWidth(1, 150)
        UI_set.resulttable.setColumnWidth(2, 200)
        
        UI_set.show()
        UI_set.revise_add2.clicked.connect(Fileread.revise_add)

    def revise_add(self):
        Fr = open("D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/patientData.csv",'r', encoding='UTF8')
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
        Fr = open("D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/patientData.csv",'r', encoding='UTF8')
        ReadF = csv.reader(Fr)
        
        keyword = UI_set.revise_add.text()

        list2 = 0
    
        for line in ReadF:
            if(keyword==line[1]):
                if(list2!=line[0]):
                    item = Fileread.cell(self,line[0])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    
                    item1 = Fileread.cell(self,line[1])
                    item1.setFlags(QtCore.Qt.ItemIsEnabled)
                    item3 = Fileread.cell(self,line[3])
                    
        
                    
                    UI_set.resulttable.setItem(row, 0, QTableWidgetItem(item))
    
                    UI_set.resulttable.setItem(row, 1, QTableWidgetItem(item1))
                    UI_set.resulttable.setItem(row, 2, QTableWidgetItem(item3))
                   
                    
                    row += 1
                list2 = line[0]
                
                
        UI_set.resulttable.doubleClicked.connect(Fileread.treeMedia_doubleClicked)
 
    def treeMedia_doubleClicked(self):
        row = UI_set.resulttable.currentIndex().row()
        column = UI_set.resulttable.currentIndex().column()
        if(column==0):
            k = UI_set.resulttable.item(row,column).text()
            UI_set.revise_add.setText(k)
            
            submain = SubMain()
            submain.id(k)
            submain.__init__()
           
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
        