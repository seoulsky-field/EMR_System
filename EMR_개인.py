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
        DATA_PATH = "D:/workspace_python/univ_basic_sw/EMR_System/patientData.csv"
        self.patientData = pd.read_csv(DATA_PATH)

        # GUI 로드
        UI_set = QtUiTools.QUiLoader().load(resource_path("D:/workspace_python/UNIV_BASIC_SW/EMR_System/e.ui"))

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
        
        # 환자 찾기를 통해서 얻은 환자의 ID를 바탕으로 출력 예정입니다.
        # 파일 합치기 전에 환자 ID를 임의의 데이터로 설정하였습니다.
        patientID = "1"

        personData = needData["환자ID" == patientID]

        # personData의 형태는 DataFrame 형태입니다.
        # Google에서 pandas dataframe 관련 행과 열 추출하는 방법을 검색하여 아래의 코드를 수정하시면 됩니다.
        # 환자 데이터 삭제의 경우 하나의 행이 아닌 여러 행이 존재할 수 있습니다.
        # 이 경우 환자의 ID가 일치할 경우 해당 행을 모두 삭제해주세요.
        # ex. personData['환자ID'] => 환자ID 열만 추출
        # 자세한 것은 loc과 iloc 관련해서 검색해보시면 바로 나올 것입니다.
        # 데이터 삭제는 "csv파일의 해당 행"을 삭제하는 것입니다.

        a = UI_set.LE_name.text()
        if a in name:
            text = UI_set.LE_name.text()
            UI_set.L_name.setText(text)
        else:
            UI_set.L_name.setText(a + " 환자가 존재하지 않습니다.")

    def nameDiscordance(self):
        name = ['김가나', '이다라', '최마바', '정사아', '박자차']
        a = UI_set.LE_name.text()
        if a in name:
            UI_set.L_name.setText(a + "님을 삭제하시겠습니까?")
        else:
            UI_set.L_name.setText("해당 환자가 존재하지 않습니다.")

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
