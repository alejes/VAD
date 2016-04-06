#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frm import *

if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWin()
    ui = Win()

    ui.setupUi(MainWindow)
    ui.ui_prepare()
    MainWindow.show()
    sys.exit(app.exec_())

    #app = QApplication(sys.argv)
    #MainWindow = Win()
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    sys.exit(app.exec_())
    #ex = Win()
    #ex.show()
    #sys.exit(app.exec_())

    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Win()

    #ui.setupUi(MainWindow)
    #ui.ui_prepare()
    #MainWindow.show()

    # ui.connect(ui.pushButtonStart, SIGNAL("clicked()"), startButtonPress)
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    #sys.exit(app.exec_())
