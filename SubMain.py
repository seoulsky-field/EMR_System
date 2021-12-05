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

from Surgery import Susul
from Prescription import Cheobang
from visit import Naewon
from patient import patient
from MedicalImaging import MainView


class SubMain(QWidget):
    global ID
    ID = -10
    def id(self,C):
        global ID
        
        ID = C
    
    def __init__(self):
        self.setupUI()
        
    
    
    
    
        
    def setupUI(self):
        global Sub
        global ID
        if(ID!=-10):
        
            Sub = QtUiTools.QUiLoader().load(resource_path("SubMain.ui"))

            KSD = str(ID)+ '님의 정보'
            
            Sub.setWindowTitle(KSD)
            Sub.setGeometry(500,300, 1000, 400)
            
            Sub.patient.setMinimumHeight(150)
            Sub.patient.setMinimumWidth(150)
            Sub.patient.setMaximumHeight(150)
            Sub.patient.setMaximumWidth(150)
            
            Sub.Prescription.setMinimumHeight(150)
            Sub.Prescription.setMinimumWidth(150)
            Sub.Prescription.setMaximumHeight(150)
            Sub.Prescription.setMaximumWidth(150)
            
            Sub.MedicalImaging.setMinimumHeight(150)
            Sub.MedicalImaging.setMinimumWidth(150)
            Sub.MedicalImaging.setMaximumHeight(150)
            Sub.MedicalImaging.setMaximumWidth(150)
            
            Sub.visit.setMinimumHeight(150)
            Sub.visit.setMinimumWidth(150)
            Sub.visit.setMaximumHeight(150)
            Sub.visit.setMaximumWidth(150)
            
            Sub.surgery.setMinimumHeight(150)
            Sub.surgery.setMinimumHeight(150)
            Sub.surgery.setMinimumHeight(150)
            Sub.surgery.setMinimumHeight(150)
            
            Sub.show()
            
            
            Sub.patient.clicked.connect(SubMain.patient)
            Sub.Prescription.clicked.connect(SubMain.Prescriptionpatient)
            Sub.MedicalImaging.clicked.connect(SubMain.MedicalImagingpatient)
            Sub.visit.clicked.connect(SubMain.visit)
            Sub.surgery.clicked.connect(SubMain.surgery)

            
            
            
            
    def patient(self):
        patient1 = patient()
        patient1.id(ID)
        patient1.__init__()
        
    def Prescriptionpatient(self):
        prescription = Cheobang()
        prescription.id(ID)
        prescription.__init__()
        
    def MedicalImagingpatient(self):
        mainview = MainView()
        mainview.id(ID)
        mainview.__init__()
        
    def visit(self):
        visit1 = Naewon()
        visit1.id(ID)
        visit1.__init__()
        
    def surgery(self):
        surgery = Susul()
        surgery.id(ID)
        surgery.__init__()
        
        
   



def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)    
    
       
if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = SubMain()
    
    sys.exit(app.exec_())       
