#-*- encoding: utf-8 -*-
import sys
import os
import csv
import pandas as pd
import numpy as np
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow


class MainView(QMainWindow): 
    global ID
    ID = -10

    def __init__(self):
        self.setupUI()
        
    def id(self,C):
        global ID
        ID = C

    def setupUI(self):
        global UI_set
        global ID
        if(ID!=-10):
            UI_set = QtUiTools.QUiLoader().load(resource_path("MedicalImaging.ui"))

            KSD = str(ID)+ '님의 정보'
    
            UI_set.setGeometry(500,300, 1000, 400)
            UI_set.setWindowTitle(KSD)
            UI_set.resize(500,270)
            UI_set.show()
            
            UI_set.BTN_addImgInfo.clicked.connect(MainView.addImageInfo)
    

    def addImageInfo(self):
        patientId = ID
        patientTime = patientTime = UI_set.LE_specificDate.text()
        
        PATIENT_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/EMR_DATA/" + patientId + "_visit.csv"

        name = UI_set.LE_specific.text()
        
        if(patientTime==""):
            UI_set.LE_showInfo.setText("시간을 입력해주세요")
        else:
            patientInfo = pd.read_csv(PATIENT_PATH, encoding="euc-kr")
            specificDateInfo = patientInfo[patientInfo['진료날짜'] == patientTime]
            patientImgInfo = specificDateInfo['의료 영상']

            print(patientImgInfo)
            
            # 환자ID 문자열 가공
            patientId = patientId.replace(patientId[0], "")
            patientId = patientId.replace(patientId[0], "")
            
            # 진료날짜 문자열 가공
            timeEdit = patientTime.split("-")
            timeEdit[0] = timeEdit[0][2:]
            timeEdit = ''.join(timeEdit)
            
            # 입력받은 문자열이 공백이면
            if name == "":
                UI_set.LE_showInfo.setText("부위를 입력해주세요")
            else:
                # 진료날짜에 맞는 의료 영상 정보 문자열 가공
                if np.isnan(patientImgInfo.tolist()) == False:
                    patientImgData = patientImgInfo.tolist()
                    patientImgData = ''.join(patientImgData).split(', ')
                else:
                    patientImgData = []
                
                # 해당 부위 이미지 개수 체크            
                check = []
                print(patientImgData)
                if np.isnan(patientImgData) == False:
                    for idx, value in enumerate(patientImgData):
                        value = value.split("(")
                        value = value[0]
                        check.append(value)
                
                 # 번호 달기 전 추가될 의료 영상 정보 문자열
                fullName = patientId + "_" + timeEdit + "_" + name
    
                count = 1
                for value in check:
                    if value == fullName:
                        count += 1
                
                # 번호 단 후 추가될 의료 영상 정보 문자열
                addName = fullName + "(" + str(count) + ")"
                patientImgData.append(addName)
                UI_set.LE_showInfo.setText(addName + " 추가 완료")

                if len(patientImgData) != 1:
                    fullImgInfo = ', '.join(patientImgData)
                else:
                    fullImgInfo = patientImgData[0]
    
                # index = int(patientInfo.index[patientInfo['진료날짜'] == patientTime].tolist()[0])
    
                condition = patientInfo['진료날짜'] == patientTime
                patientInfo.loc[condition, ['의료 영상']] = fullImgInfo
                
                patientInfo.to_csv(PATIENT_PATH, index = False, encoding='cp949')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    sys.exit(app.exec_())