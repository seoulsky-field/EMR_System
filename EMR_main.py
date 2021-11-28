import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QHeaderView


class MainView(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("D:/workspace_python/univ_basic_sw/EMR_System/EMR_GUI.ui"))
        
        self.showImageTitles()

        UI_set.CB_ImageChoice.activated.connect(self.showImage)
        UI_set.BTN_newTab.clicked.connect(self.imageClicked)
        UI_set.BTN_choose.clicked.connect(self.showMedicine)

        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System : v.beta")
        self.resize(2000,1000)
        self.show()
    
    def showImageTitles(self):
        # 환자 데이터 경로 지정 및 데이터 읽기
        DATA_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/patientData.csv"
        self.patientData = pd.read_csv(DATA_PATH)

        # 환자ID, 진료날짜, 의료 영상 열들을 target으로 하고, 의료 영상이 공백인 경우 모두 제거
        target_columns = ['환자ID', '진료날짜', '의료 영상']
        ImageExist = self.patientData[target_columns].dropna(axis=0)

        # 환자의 의료 영상 정보 이미지 이름은 "환자ID_날짜_부위(번호)"로 되어 있다.
        # 아래의 ID와 DateTime은 임의의 데이터이다.
        patientID = "2"
        patientDateTime = "2021-11-11"

        # 현재 차트에 띄운 환자의 ID에 해당하는 행만 저장.
        patient = ImageExist[ImageExist['환자ID'] == int(patientID)]
        imageList = patient['의료 영상'].tolist()
        images = ''.join(imageList).split(', ')
        UI_set.CB_ImageChoice.addItem("의료 이미지를 선택하세요.")
        for image in images:
            UI_set.CB_ImageChoice.addItem(image)
    
    def showImage(self):
        ImageName = UI_set.CB_ImageChoice.currentText()
        if ImageName == "의료 이미지를 선택하세요.":
            # 창을 띄운다.
            UI_set.LABEL_imageShow.setText("의료 이미지를 선택해야 합니다.")
        else:
            self.IMAGE_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/Images/" + ImageName + ".png"
            UI_set.LABEL_imageShow.setPixmap(QtGui.QPixmap(self.IMAGE_PATH))
        
    def imageClicked(self):
        try:
            image = img.imread(self.IMAGE_PATH)
            plt.imshow(image)
            plt.show()
        except FileNotFoundError:
            UI_set.LABEL_imageShow.setText("이미지가 존재하지 않아 새 창에서 열 수 없습니다.")

    def showMedicine(self):
        patientID = "2"
        target_columns = ['환자ID', '처방 일자', '처방 과', '처방 의사', '처방 명', '용량', '일일 투약 횟수', '투약 일수']
        pillData = self.patientData[target_columns].dropna(axis=0)
        patient = pillData[pillData['환자ID'] == int(patientID)]

        UI_set.TW_medicine.setRowCount(len(patient.index))
        UI_set.TW_medicine.setColumnCount(len(patient.columns)-1)
        UI_set.TW_medicine.setEditTriggers(QAbstractItemView.NoEditTriggers)
        UI_set.TW_medicine.setHorizontalHeaderLabels(target_columns[1:])

        for row in range(0, len(patient.index)):
            for column in range(1, len(target_columns)):
                UI_set.TW_medicine.setItem(row, column-1, QTableWidgetItem(str(patient.iloc[row, column])))
        
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