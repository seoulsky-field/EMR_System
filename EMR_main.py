import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import pandas as pd
import csv
from PySide2 import QtUiTools, QtGui, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QHeaderView
from pandas.io.parsers import read_csv
from SubMain import SubMain
from plus import Plus

class MainView(QMainWindow):   
    
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set
        global PATIENT_PATH
        
        self.patientID = "ID000001"
        
        PATIENT_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/patientData.csv"
        self.patientData2 = pd.read_csv(PATIENT_PATH)

        UI_set = QtUiTools.QUiLoader().load(resource_path("EMR_GUI.ui"))

        # 환자 찾기 관련 지정
        UI_set.resulttable.setColumnWidth(0, 100)
        UI_set.resulttable.setColumnWidth(1, 150)
        UI_set.resulttable.setColumnWidth(2, 200)
        UI_set.revise_add2.clicked.connect(self.revise_add)
        UI_set.BTN_addPatient.clicked.connect(Plus)

        UI_set.BTN_editPatient.clicked.connect(self.edit)

        UI_set.CB_ImageChoice.activated.connect(self.showImage)
        UI_set.BTN_choose.clicked.connect(self.clear)
        UI_set.BTN_choose.clicked.connect(self.showImageTitles)
        UI_set.BTN_newTab.clicked.connect(self.imageClicked)
        UI_set.BTN_choose.clicked.connect(self.showMedicine)
        UI_set.BTN_choose.clicked.connect(self.surgeryinfor)
        UI_set.BTN_choose.clicked.connect(self.visitinfor)
        UI_set.BTN_choose.clicked.connect(self.patientinfor)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System : v.beta")
        self.resize(1400,950)

        self.show()
    def clear(self):
        UI_set.surgeryInforWidget.setRowCount(0)
        UI_set.TW_medicine.setRowCount(0)
        UI_set.visitInforWidget.setRowCount(0)

    # 환자 찾기 관련 함수입니다.
    def revise_add(self):
        Fr = open(PATIENT_PATH,'r', encoding='UTF8')
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
        Fr = open(PATIENT_PATH,'r', encoding='UTF8')
        ReadF = csv.reader(Fr)

        keyword = UI_set.revise_add.text()
        list2 = 0 
        for line in ReadF:
            if(keyword==line[1]):
                if(list2!=line[0]):
                    item = self.cell(line[0])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    
                    item1 = self.cell(line[1])
                    item1.setFlags(QtCore.Qt.ItemIsEnabled)
                    item3 = self.cell(line[3])

                    UI_set.resulttable.setItem(row, 0, QTableWidgetItem(item))
    
                    UI_set.resulttable.setItem(row, 1, QTableWidgetItem(item1))
                    UI_set.resulttable.setItem(row, 2, QTableWidgetItem(item3))       
                    row += 1
                list2 = line[0]       
        UI_set.resulttable.doubleClicked.connect(self.treeMedia_doubleClicked)

    def treeMedia_doubleClicked(self):
        row = UI_set.resulttable.currentIndex().row()
        column = UI_set.resulttable.currentIndex().column()
        if(column==0):
            self.patientID = UI_set.resulttable.item(row,column).text()
            UI_set.revise_add.setText(self.patientID)
            # submain = SubMain()
            # submain.id(self.patientID)
            # submain.__init__()

    def edit(self):
        submain = SubMain()
        submain.id(self.patientID)
        submain.__init__()

    

    def cell(self,var=""):
            item = QTableWidgetItem()
            item.setText(var)
            return item


    # 의료 영상 관련 함수입니다.
    def showImageTitles(self):
        # 환자 데이터 경로 지정 및 데이터 읽기
        #PATIENT_PATH = "D:/workspace_python/univ_basic_sw/" + patientID + ".csv"
        try:
            OPEN_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/" + self.patientID + "_visit.csv"
            self.patientData = pd.read_csv(OPEN_PATH, encoding='cp949')

            # 이미지 정보 로드하기
            imageList = self.patientData['의료 영상'].dropna(axis=0).tolist()
            print(imageList)
            images = ''.join(imageList).split(', ')

            # 이미지 ComboBox에 추가하기
            UI_set.CB_ImageChoice.clear()
            UI_set.LABEL_imageShow.clear()

            if(len(imageList) == 0):
                UI_set.CB_ImageChoice.addItem("환자의 의료 이미지가 없습니다.")

            else:
                UI_set.CB_ImageChoice.addItem("의료 이미지를 선택하세요.")
                for image in images:
                    UI_set.CB_ImageChoice.addItem(image)
        except FileNotFoundError:
            UI_set.CB_ImageChoice.addItem("환자의 의료 이미지가 없습니다.")
    

    # 의료 영상 관련 함수입니다.
    def showImage(self):
        self.IMAGE_PATH= ''
        self.ImageName = UI_set.CB_ImageChoice.currentText()
        print(self.ImageName)
        if self.ImageName == "의료 이미지를 선택하세요." or self.ImageName == "환자의 의료 이미지가 없습니다.":
            # 창을 띄운다.
            UI_set.LABEL_imageShow.setText("의료 이미지를 선택해야 합니다.")
        else:
            self.IMAGE_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/Images/" + self.ImageName + ".png"
            UI_set.LABEL_imageShow.setPixmap(QtGui.QPixmap(self.IMAGE_PATH))
    

    # 의료 영상 관련 함수입니다.
    def imageClicked(self):
        try:
            if self.ImageName == "의료 이미지를 선택하세요." or self.ImageName == "환자의 의료 이미지가 없습니다." or self.ImageName == "":
                UI_set.LABEL_imageShow.setText("이미지가 존재하지 않아 새 창에서 열 수 없습니다.")
            else:
                image = img.imread(self.IMAGE_PATH)
                # image = image.resize((256, 256))
                plt.imshow(image)
                plt.show() 
            
        except FileNotFoundError:
            UI_set.LABEL_imageShow.setText("이미지가 존재하지 않아 새 창에서 열 수 없습니다.")

    # 투약 및 처방 정보 관련 함수입니다.
    def showMedicine(self):
        target_columns = ['처방 일자', '처방 과', '처방 의사', '처방 명', '용량', '일일 투약 횟수', '투약 일수']
        UI_set.TW_medicine.setColumnCount(len(target_columns))
        UI_set.TW_medicine.setHorizontalHeaderLabels(target_columns)

        try:
            DATA_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/" + self.patientID + "_pilldata.csv"
            pillData = pd.read_csv(DATA_PATH, encoding='cp949').dropna(axis=0)
            UI_set.TW_medicine.setRowCount(len(pillData.index))
            UI_set.TW_medicine.setColumnCount(len(pillData.columns))

            for row in range(0, len(pillData.index)):
                for column in range(0, len(target_columns)):
                    UI_set.TW_medicine.setItem(row, column, QTableWidgetItem(str(pillData.iloc[row, column])))

        except(FileNotFoundError):
            print("no exist")
        

        UI_set.TW_medicine.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        header = UI_set.TW_medicine.horizontalHeader()
        twidth = header.width()
        width = []
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.ResizeToContents)
            width.append(header.sectionSize(column))

        wfactor = twidth / sum(width)
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.Interactive)
            header.resizeSection(column, width[column]*wfactor)

    # 수술 정보 관련 함수입니다.
    def surgeryinfor(self):
        OPEN_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/" + self.patientID + "_surgery.csv"
        # 수술정보
        UI_set.surgeryInforWidget.setColumnCount(6)
        UI_set.surgeryInforWidget.setHorizontalHeaderLabels(['수술명','수술 코드','집도 과','수술 일자','담당 의사','수술 시간'])

        try:
            f = open(OPEN_PATH, "r", encoding='cp949')
            reader = csv.reader(f)
        except IOError: #수술정보가 없을 경우
            pass
        else:
            surgerylist = list(reader)
            headerList = []

            UI_set.surgeryInforWidget.setVerticalHeaderLabels(headerList)
            UI_set.surgeryInforWidget.setRowCount(len(surgerylist))

            for x in range(0, len(surgerylist)-1):
                for y in range(0, 6):
                    UI_set.surgeryInforWidget.setItem(x, y, QTableWidgetItem(str(surgerylist[x+1][y])))
            f.close()

    # 환자 정보 관련 함수입니다.
    def patientinfor(self):
        #환자정보
        f = open(PATIENT_PATH, "r", encoding='UTF8')
        reader = csv.reader(f)
        patientlist = list(reader)

        index = -1

        for idx in range(1, len(patientlist)):
            if patientlist[idx][0] == self.patientID:
                index = idx
                break
        if index == -1:
            print("ERROR")

        #LINEEDIT에 환자 정보 넣기
        UI_set.name.setText(str(patientlist[index][1]))
        UI_set.ID.setText(str(patientlist[index][0]))
        UI_set.personalNum.setText(str(patientlist[index][3]))
        UI_set.birth.setText(str(patientlist[index][2]))
        UI_set.lineEdit.setText(str(patientlist[index][7]))
        UI_set.weight.setText(str(patientlist[index][8]))
        UI_set.adress.setText(str(patientlist[index][5]))
        UI_set.bloodtype.setText(str(patientlist[index][6]))
        if patientlist[index][4] == "남":
            UI_set.man.setChecked(True)
        else:
            UI_set.woman.setChecked(True)


    # 내원정보
    def visitinfor(self):
        OPEN_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/" + self.patientID + "_visit.csv"
        
        UI_set.visitInforWidget.setColumnCount(7)
        UI_set.visitInforWidget.setHorizontalHeaderLabels(['진료날짜','내원 구분','진료 과','진료의','환자 통증','담당의 소견', '의료 영상'])

        f = open(OPEN_PATH, "r", encoding="cp949")
        reader = csv.reader(f)
        visitlist = list(reader)
        headerList2 = []

        UI_set.visitInforWidget.setVerticalHeaderLabels(headerList2)
        UI_set.visitInforWidget.setRowCount(len(visitlist)-1)
        for x in range(0, len(visitlist)-1):
            for y in range(0, 7):
                UI_set.visitInforWidget.setItem(x, y, QTableWidgetItem(str(visitlist[x+1][y])))

        f.close()


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
