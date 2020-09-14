from PySide2.QtWidgets import QApplication, QMainWindow, QTextBrowser,QPushButton, QLabel, QPlainTextEdit,QMessageBox
from socket import *


result=''
def handleCalc():
    global result
    # 获取用户输入的IP,端口，超时
    ip = textEdit1.toPlainText()
    port = textEdit2.toPlainText()
    time = textEdit3.toPlainText()
    try:
        sock = socket(AF_INET, SOCK_STREAM)  # 实例化socket
        sock.settimeout(int(time))  # 限制重连时间
        sock.connect((ip, int(port)))  # 对对应主机的对应端口发起连接
        result = f'{port}端口开放'
        sock.close()  # 关闭连接
    except Exception as e:
        result = f'{port}端口关闭'
    win.append(result)
    #QMessageBox.about(window,'扫描结果',result)

app = QApplication([])

window = QMainWindow()
window.resize(500, 270)
window.move(300, 300)
window.setWindowTitle('端口扫描')

textEdit1 = QPlainTextEdit(window)
#textEdit1.setPlaceholderText("输入IP")
textEdit1.move(10,50)
textEdit1.resize(200,40)

textEdit2 = QPlainTextEdit(window)
#textEdit2.setPlaceholderText("输入端口")
textEdit2.move(10,130)
textEdit2.resize(200,40)

textEdit3 = QPlainTextEdit(window)
#textEdit3.setPlaceholderText("超时(毫秒)")
textEdit3.move(10,210)
textEdit3.resize(200,40)

label1 = QLabel(window)
label1.setText('输入IP')
label1.move(80, 0)
label1.resize(500,60)
label2 = QLabel(window)
label2.setText('输入端口')
label2.move(80, 80)
label2.resize(500,60)
label3 = QLabel(window)
label3.setText('超时(毫秒)')
label3.move(80, 160)
label3.resize(500,60)
label4 = QLabel(window)
label4.setText('扫描结果')
label4.move(320, 0)
label4.resize(500,60)


button = QPushButton('开始扫描', window)
button.move(300,220)
button.resize(100,40)
button.clicked.connect(handleCalc)

win= QTextBrowser(window)
win.move(230,50)
win.resize(250,160)



window.show()

app.exec_()
