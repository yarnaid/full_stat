__author__ = 'yarnaid'


import sys
import platform
from PySide import QtGui
from PySide.QtGui import QApplication, QMainWindow, QMessageBox
import PySide

__version__ = '0.0.0'

class MainWindow(QMainWindow):
    def init_layout(self):
        self.cw = QtGui.QWidget()
        self.layout = QtGui.QHBoxLayout()
        self.left_layout = QtGui.QVBoxLayout()
        self.right_layout = QtGui.QVBoxLayout()
        self.cw.setLayout(self.layout)
        self.setCentralWidget(self.cw)

    def init_buttons(self):
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setText('Test')
        self.pushButton.clicked.connect(self.buttonTest)
        self.pushButton1 = QtGui.QPushButton()
        self.pushButton1.setText('Test')
        self.pushButton1.clicked.connect(self.buttonTest)

    def fill_layout(self):
        self.left_layout.addWidget(self.pushButton)
        self.left_layout.addWidget(self.pushButton1)

        self.right_layout.addWidget(self.tabs)
        self.layout.addLayout(self.left_layout)
        self.layout.stretch(1)
        self.layout.addLayout(self.right_layout)
        self.setLayout(self.layout)

    def init_ui(self, title):
        self.init_menus()
        self.init_toolbar()
        self.init_tabs()
        self.setWindowTitle(title)
        # self.resize(300, 200)

        self.init_layout()
        self.init_buttons()

        self.statusBar().showMessage('Ready')

        self.fill_layout()

    def __init__(self, parent=None, title=''):
        super(MainWindow, self).__init__(parent)
        self.init_ui(title)

    def buttonTest(self):
        print 'Test OK'

    def init_actions(self):
        exit_action = QtGui.QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)
        self.exit_action = exit_action

        load_action = QtGui.QAction('&Load', self)
        load_action.setShortcut('Ctrl+O')
        load_action.setStatusTip('Load data')
        load_action.triggered.connect(self.load_data)
        self.load_action = load_action

        about_action = QtGui.QAction('&About', self)
        about_action.setStatusTip('About application')
        about_action.triggered.connect(self.about)
        self.about_action = about_action

    def init_menus(self):
        self.init_actions()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(self.exit_action)
        file_menu.addAction(self.load_action)
        # file_menu.addAction(self.about_action)

    def init_toolbar(self):
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit_action)
        self.toolbar.addAction(self.load_action)
        self.toolbar.addAction(self.about_action)


    def load_data(self):
        raise NotImplementedError

    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b> About this program </b> v %s
               <p>Copyright  2015 Yaroslav Nayden.
               All rights reserved in accordance with
               GPL v2 or later - NO WARRANTIES!
               <p>This application can be used for
               displaying OS and platform details.
               <p>Python %s -  PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))

    def init_tabs(self):
        self.tabs = QtGui.QTabWidget()
        self.tabs.addTab(Table(), self.tr('Data'))
        self.tabs.addTab(Plot(), self.tr('Plot'))



class Table(QtGui.QWidget):
    ''' table tab-widget for main app
    '''
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)

        cols = 3
        rows = 12
        table = QtGui.QTableWidget(rows, cols, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(table)

        self.setLayout(layout)


class Plot(QtGui.QWidget):
    ''' widget for plot
    '''

    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)
        layout = QtGui.QVBoxLayout()

        text = QtGui.QLabel('not implemented yet')

        layout.addWidget(text)

        self.setLayout(layout)
