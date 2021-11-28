import sys
import os
import csv
import pandas as pd
import numpy as np
from PySide2 import QtUiTools, QtGui,QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog,QHeaderView,QTableWidgetItem


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("EMR.ui"))
        self.setCentralWidget(UI_set)
        self.setWindowTitle("정보")
        self.resize(800,600)
        self.show()
        UI_set.filefinder.clicked.connect(self.FileOpen)
        

        # 수술정보
        UI_set.surgeryInforWidget.setColumnCount(5)
        UI_set.surgeryInforWidget.setRowCount(3)
        UI_set.surgeryInforWidget.setHorizontalHeaderLabels(['수술 명', '수술 코드', '집도 과', '수술 일자', '담당 의사', '수술에 걸린 시간'])
        UI_set.surgeryInforWidget.setVerticalHeaderLabels(['1', '2', '3'])

        # 내원정보
        UI_set.visitInforWidget.setColumnCount(5)
        UI_set.visitInforWidget.setRowCount(3)
        UI_set.visitInforWidget.setHorizontalHeaderLabels(['내원 구분', '진료 과','진료의','환자 통증','소견'])
        UI_set.visitInforWidget.setVerticalHeaderLabels(['1', '2', '3'])

    def FileOpen(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter(self.tr("Data Files (*.csv *.xls *.xlsx);; Images (*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            data = pd.read_csv(fileName)
        #for x in range(3):
        #    for y in range(5):
        #        UI_set.visitInforWidget.setItem(x, y, QTableWidgetItem(""))

        '''
UI_set.name.setText(str(patientlist[0])
UI_set.ID.setText(str(patientlist[1])
UI_set.personalNum.setText(str(patientlist[3])
UI_set.birth.setText(str(patientlist[4])
UI_set.height.setText(str(patientlist[6])
UI_set.weight.setText(str(patientlist[7])
UI_set.date.setText(str(patientlist[8])
UI_set.adress.setText(str(patientlist[9])
if patientlist[2] == "남":
UI_set.man.setAttribute(str('checked',true)
else
UI_set.woman.setAttribute(str('checked',true)


'''

    #파일 경로
#pyinstaller로 원파일로 압축할때 경로 필요함
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()

    #main.show()
    sys.exit(app.exec_())
