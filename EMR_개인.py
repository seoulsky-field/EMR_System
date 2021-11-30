import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("e.ui"))

        self.setCentralWidget(UI_set)
        self.setWindowTitle("EMR System")
        self.resize(500,400)
        self.show()

        UI_set.BTN_find.clicked.connect(self.nameCorrespond)
        UI_set.BTN_del.clicked.connect(self.nameDiscordance)

    def nameCorrespond(self):
        name = ['김가나', '이다라', '최마바', '정사아', '박자차']
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