import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
# 引入图标库
from PyQt5.QtGui import QIcon

# 引入py ui 组件（差不多是这个意思）
import login_model_test

# 弹窗的ui结构
ui = login_model_test.Ui_MainWindow()

class initMain():
    # 定义点击事件
    def click_success():
        # input = ui.loginForm.loginName.text()
        loginNameText = ui.loginName.text().strip()
        loginPasswordText = ui.loginPassword.text().strip()
        # 先判断输入框是否都为空，或全部输入的都是空格
        if not loginNameText or not loginPasswordText:
            print('if ')
            return
        else:
            print(loginNameText, loginPasswordText)

    # 定义UI方法
    def initUI(MainWindow):
        # 获得窗口
        qr = MainWindow.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

        # 显示窗口
        MainWindow.show()

    def closeEvent(MainWindow, event):

        reply = QMessageBox.warning(MainWindow, '更新提示',
                                    '请更新为最新版软件后再启动！',
                                    QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    # 创建应用程序和对象#创建应用程序和对象
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui.setupUi(MainWindow)

    # 调用设置窗口位置的函数
    initMain.initUI(MainWindow)
    # ul.loginButton是id 触发id的clicked事件
    ui.loginButton.clicked.connect(initMain.click_success)
    # ui.pushButton.clicked.connect(partial(convert, ui))

    sys.exit(app.exec_())
