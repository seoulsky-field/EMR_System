import sys
import os
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

        global a
        a = UI_set.LE_name.text()

        id_list = []

        personData = needData['환자명'].str.contains(a)
        savePersonData = needData[personData]
        print(savePersonData)

        for a in range(0, len(personData)):

            if a in personData and a not in id_list:
                id_list.append(a)
                UI_set.L_name.setText(str(a)+" 환자가 존재합니다.")     #str(a)로 하지 않으면 에러 발생, str(a)로 하면 숫자로 출력됨.
                comboboxPersonData = "/".join(savePersonData)       #"환자ID/환자명/주민번호"가 14개 출력됨. 14개는 환자데이터 개수인듯
                UI_set.patientCombo.addItem(comboboxPersonData)
            elif a in personData and a in id_list:
                continue
            else:
                UI_set.L_name.setText(a + " 환자가 존재하지 않습니다.")

    def nameDiscordance(self):
        target_columns = ['환자ID', '환자명', '주민번호']
        needData = self.patientData[target_columns]

        a = UI_set.LE_name.text()

        id_list = []

        personData = needData['환자명'].str.contains(a)
        savePersonData = needData[personData]
        print(savePersonData)

        for a in range(0, len(personData)):

            if a in personData and a not in id_list:
                id_list.append(a)
                UI_set.L_name.setText(str(a) + " 환자를 삭제합니다.")
                self.patientDelete
            elif a in personData and a in id_list:
                continue
            else:
                UI_set.L_name.setText(a + " 환자가 존재하지 않습니다.")

    def patientDelete(self):
        target_columns = ['환자ID', '환자명', '주민번호']
        needData = self.patientData[target_columns]

        dataframe = target_columns[target_columns["환자명"] != a]
        UI_set.patientCombo.addItem(dataframe)


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