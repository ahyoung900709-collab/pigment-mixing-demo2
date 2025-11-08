# qt_check.py
# (위에서처럼 환경변수 우회 코드가 필요하면 이 파일 맨 위에 동일하게 추가해도 됩니다)
from PyQt5 import QtWidgets
app = QtWidgets.QApplication([])
w = QtWidgets.QWidget()
w.setWindowTitle("Qt OK Test")
w.resize(300, 200)
w.show()
app.exec_()
