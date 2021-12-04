import sys
import os

import pandas
import pandas as pd
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        # 환자 데이터 경로 지정 및 데이터 읽기
        DATA_PATH = "D:/장혜림/Desktop/장혜림/pythonProject/patientData.csv"
        self.patientData = pd.read_csv(DATA_PATH)

        # GUI 로드
        UI_set = QtUiTools.QUiLoader().load(resource_path("D:/장혜림/Desktop/장혜림/pythonProject/emr.ui"))

        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System")
        self.resize(500,400)
        self.show()


        UI_set.BTN_find.clicked.connect(self.nameCorrespond)
        UI_set.BTN_del.clicked.connect(self.nameDiscordance)

    def nameCorrespond(self):
        target_columns = ['환자ID', '환자명', '주민번호']
        needData = self.patientData[target_columns]
        nameData = needData['환자명']

        global a
        a = UI_set.LE_name.text()

        def nameIN(self):
            UI_set.patientCombo.clear()
            personData = needData['환자명'].str.contains(a)
            savePersonData = needData.loc[personData]
            strSPD = str(savePersonData)
            UI_set.patientCombo.addItem(strSPD)      # str로 저장해야 combobox에 들어가는데, 한꺼번에 표시됨. 열 별로 나누는 방법?

        def nameOUT(self):
            UI_set.patientCombo.clear()
            allPatientData = needData.loc[:]
            strAPD = str(allPatientData)
            UI_set.patientCombo.addItem(strAPD)

        for idx in range(0, 1):         # range(0, len(needData))로 하면, 4번(환자데이터개수) 반복돼서 4개의 똑같은 데이터 출력됨.
            if a in str(nameData):
                nameIN(self)
                UI_set.L_name.setText(a + " 환자가 존재합니다.")
            elif a not in str(nameData):
                nameOUT(self)
                UI_set.L_name.setText(a + " 환자가 존재하지 않습니다.")
                continue


    def nameDiscordance(self):
        target_columns = ['환자ID', '환자명', '주민번호']
        needData = self.patientData[target_columns]
        nameData = needData['환자명']

        global a
        a = UI_set.LE_name.text()

        def nameIN(self):
            UI_set.patientCombo.clear()
            personData = needData['환자명'].str.contains(a)
            savePersonData = needData.loc[personData]
            strSPD = str(savePersonData)
            UI_set.patientCombo.addItem(strSPD)      # str로 저장해야 combobox에 들어가는데, 한꺼번에 표시됨. 열 별로 나누는 방법?

        def nameOUT(self):
            UI_set.patientCombo.clear()
            allPatientData = needData.loc[:]
            strAPD = str(allPatientData)
            UI_set.patientCombo.addItem(strAPD)

        def patientDelete(self):
            UI_set.patientCombo.clear()
            allPatientData = needData.loc[:]
            modifiedData = allPatientData[~allPatientData['환자명'].str.contains(a)]
            strMD = str(modifiedData)
            UI_set.patientCombo.addItem(strMD)

        for idx in range(0, 1):         # range(0, len(needData))로 하면, 4번(환자데이터개수) 반복돼서 4개의 똑같은 데이터 출력됨.
            if a in str(nameData):
                patientDelete(self)
                UI_set.L_name.setText(a + " 환자를 삭제합니다.")
            elif a not in str(nameData):
                nameOUT(self)
                UI_set.L_name.setText(a + " 환자가 존재하지 않습니다.")
                continue


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