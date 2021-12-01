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
        DATA_PATH = "D:\장혜림\Desktop\장혜림\pythonProject\emr.csv"
        self.patientData = pd.read_csv(DATA_PATH)

        # GUI 로드
        UI_set = QtUiTools.QUiLoader().load(resource_path("D:\장혜림\Desktop\장혜림\pythonProject\emr.ui"))

        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System")
        self.resize(500,400)
        self.show()

        UI_set.BTN_find.clicked.connect(self.nameCorrespond)
        UI_set.BTN_del.clicked.connect(self.nameDiscordance)

    def nameCorrespond(self):
        # 환자ID, 진료날짜, 의료 영상 열들을 target으로 하고, 의료 영상이 공백인 경우 모두 제거
        target_columns = ['환자ID', '환자명', '진료 날짜', '주민번호', '성별', '주소', '혈액형', '키', '몸무게']
        needData = self.patientData[target_columns]

        global a
        a = UI_set.LE_name.text()                        #환자 아이디 입력 받기
        patientID = target_columns.loc[ ["환자ID"] : ]    #csv파일의 컬럼 중 "환자ID" 부분을 변수로 지정

        if a in patientID:                               #만약 입력 받은 아이디가 patientID에 있다면
            UI_set.L_name.setText(a.needData(self))      #밑의 라벨에 a의 데이터 출력
        else:
            UI_set.L_name.setText(a + "ID의 환자가 존재하지 않습니다.")

    def nameDiscordance(self):

        target_columns = ['환자ID', '환자명', '진료 날짜', '주민번호', '성별', '주소', '혈액형', '키', '몸무게']
        needData = self.patientData[target_columns]

        # a = UI_set.LE_name.text()                           #환자 아이디 입력 받기
        patientID = target_columns.loc[["환자ID"]:]          #csv파일의 컬럼 중 "환자ID" 부분을 변수로 지정

        if a in patientID:                                  #만약 입력받은 아이디가 patientID에 있으면
            UI_set.L_name.setText(a.target_columns.loc[["환자명"]:] + "님을 삭제하시겠습니까?")
                                                            #a의 데이터 중 환자명 추출+삭제할 것이냐고 묻기
            UI_set.patientDelete(self)
        else:
            UI_set.L_name.setText("해당 환자가 존재하지 않습니다.")

    def patientDelete(self):
        target_columns = ['환자ID', '환자명', '진료 날짜', '주민번호', '성별', '주소', '혈액형', '키', '몸무게']
        needData = self.patientData[target_columns]

        dataframe = target_columns[target_columns["환자ID"] != a]     #환자ID가 a(입력받은환자아이디, 전역변수)가 아닌 리스트만 dataframe에 저장
        print(dataframe)


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