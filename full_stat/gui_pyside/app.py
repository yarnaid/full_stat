# -*- coding: utf-8 -*-
__author__ = 'yarnaid'


import sys
from PySide import QtGui
from window import MainWindow
from PySide import QtCore

TITLE = 'Full Statistics'

def main():

    translator = QtCore.QTranslator()
    translator.load(':/i18n/translations/ru_RU')
    app = QtGui.QApplication(sys.argv)
    app.installTranslator(translator)


    frame = MainWindow(title=TITLE)
    frame.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()