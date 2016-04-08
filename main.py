#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frm import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ApplicationWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    ui.ui_prepare()
    MainWindow.show()
    sys.exit(app.exec_())
