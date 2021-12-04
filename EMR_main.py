import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
import csv
from PySide2 import QtUiTools, QtGui, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QHeaderView


class MainView(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("EMR_GUI.ui"))
        
        self.showImageTitles()

        UI_set.CB_ImageChoice.activated.connect(self.showImage)
        UI_set.BTN_newTab.clicked.connect(self.imageClicked)
        UI_set.BTN_choose.clicked.connect(self.showMedicine)
        UI_set.BTN_choose.clicked.connect(self.surgeryinfor)
        UI_set.BTN_choose.clicked.connect(self.visitinfor)
        UI_set.BTN_choose.clicked.connect(self.patientinfor)


        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System : v.beta")
        self.resize(2000,1000)
        self.show()


    def showImageTitles(self):
        # 환자의 의료 영상 정보 이미지 이름은 "환자ID_날짜_부위(번호)"로 되어 있다.
        # 아래의 patientID는 임의의 데이터입니다.
        patientID = "ID000002"

        # 환자 데이터 경로 지정 및 데이터 읽기
        #PATIENT_PATH = "D:/workspace_python/univ_basic_sw/" + patientID + ".csv"
        PATIENT_PATH = patientID + ".csv"
        self.patientData = pd.read_csv(PATIENT_PATH)

        # 이미지 정보 로드하기
        imageList = self.patientData['의료 영상'].dropna(axis=0).tolist()
        print(imageList)
        images = ''.join(imageList).split(', ')

        # 이미지 ComboBox에 추가하기
        if(len(imageList) == 0):
            UI_set.CB_ImageChoice.addItem("환자의 의료 이미지가 없습니다.")

        else:
            UI_set.CB_ImageChoice.addItem("의료 이미지를 선택하세요.")
            for image in images:
                UI_set.CB_ImageChoice.addItem(image)
        
    
    def showImage(self):
        self.ImageName = UI_set.CB_ImageChoice.currentText()
        if self.ImageName == "의료 이미지를 선택하세요.":
            # 창을 띄운다.
            UI_set.LABEL_imageShow.setText("의료 이미지를 선택해야 합니다.")
        else:
            self.IMAGE_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/Images/" + self.ImageName + ".png"
            UI_set.LABEL_imageShow.setPixmap(QtGui.QPixmap(self.IMAGE_PATH))
        

    def imageClicked(self):
        try:
            if self.ImageName == "의료 이미지를 선택하세요." or self.ImageName == "환자의 의료 이미지가 없습니다.":
                UI_set.LABEL_imageShow.setText("이미지가 존재하지 않아 새 창에서 열 수 없습니다.")
            else:
                image = img.imread(self.IMAGE_PATH)
                image = img.resize((160, 240), image.ANTIALIAS)
                plt.imshow(image)
                plt.show() 
            
        except FileNotFoundError:
            UI_set.LABEL_imageShow.setText("이미지가 존재하지 않아 새 창에서 열 수 없습니다.")


    def showMedicine(self):
        # 아래의 patientID는 임의의 데이터입니다.
        patientID = "ID000002"

        target_columns = ['처방 일자', '처방 과', '처방 의사', '처방 명', '용량', '일일 투약 횟수', '투약 일수']
        pillData = self.patientData[target_columns].dropna(axis=0)

        UI_set.TW_medicine.setRowCount(len(pillData.index))
        UI_set.TW_medicine.setColumnCount(len(pillData.columns))
        UI_set.TW_medicine.setEditTriggers(QAbstractItemView.NoEditTriggers)
        UI_set.TW_medicine.setHorizontalHeaderLabels(target_columns)

        for row in range(0, len(pillData.index)):
            for column in range(0, len(target_columns)):
                UI_set.TW_medicine.setItem(row, column, QTableWidgetItem(str(pillData.iloc[row, column])))
        
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


    def surgeryinfor(self):
        patientID = "ID000002" #임의
        PATIENT_PATH = patientID + "_surgery.csv"
        # 수술정보
        UI_set.surgeryInforWidget.setColumnCount(7)
        UI_set.surgeryInforWidget.setHorizontalHeaderLabels(['진료날짜','수술명','수술 코드','집도 과','수술 일자','담당 의사','수술 시간'])

        try:
            f = open(PATIENT_PATH, "r")
            reader = csv.reader(f)
        except IOError: #수술정보가 없을 경우
            pass
        else:
            surgerylist = list(reader)
            headerList = []

            for idx in range(1, len(surgerylist)):
                headerList.append(str(idx))

            UI_set.surgeryInforWidget.setVerticalHeaderLabels(headerList)
            UI_set.surgeryInforWidget.setRowCount(len(surgerylist))

            for x in range(0,len(surgerylist)):
                for y in range(0, 6):
                    UI_set.surgeryInforWidget.setItem(x, y,QTableWidgetItem(str(surgerylist[x][y])))
            f.close()


    def patientinfor(self):
        patientID = "ID000002" #임의
        PATIENT_PATH = patientID + "_patient.csv"
        #환자정보
        f = open(PATIENT_PATH, "r")
        reader = csv.reader(f)
        patientlist = list(reader)
        #LINEEDIT에 환자 정보 넣기
        UI_set.name.setText(str(patientlist[0][1]))
        UI_set.ID.setText(str(patientlist[0][0]))
        UI_set.personalNum.setText(str(patientlist[0][3]))
        UI_set.birth.setText(str(patientlist[0][2]))
        UI_set.lineEdit.setText(str(patientlist[0][7]))
        UI_set.weight.setText(str(patientlist[0][8]))
        UI_set.adress.setText(str(patientlist[0][5]))
        UI_set.bloodtype.setText(str(patientlist[0][6]))
        if patientlist[0][4] == "남":
            UI_set.man.setChecked(True)
        else:
            UI_set.woman.setChecked(True)

        f.close()

    def visitinfor(self):
        patientID = "ID000002" #임의
        PATIENT_PATH = patientID + "_visit.csv"
        # 내원정보
        UI_set.visitInforWidget.setColumnCount(5)
        UI_set.visitInforWidget.setHorizontalHeaderLabels(['내원 구분','진료 과','진료의','환자 통증','담당의 소견'])

        f = open(PATIENT_PATH, "r")
        reader = csv.reader(f)
        visitlist = list(reader)
        headerList2 = []

        for idx in range(1, len(visitlist)):
            visitlist.append(str(idx))

        UI_set.visitInforWidget.setVerticalHeaderLabels(headerList2)
        UI_set.visitInforWidget.setRowCount(len(visitlist))
        for x in range(0, len(visitlist) ):
            for y in range(0, 4):
                UI_set.visitInforWidget.setItem(x, y,QTableWidgetItem(str(visitlist[x][y])))

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
