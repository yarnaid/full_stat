__author__ = 'yarnaid'

import wx
from gui.app import FullStatFrame

TITLE = 'Full Stat'


def run_gui():
    app = wx.App()
    frame = FullStatFrame(None, title=TITLE)
    app.MainLoop()


def main():
    run_gui()

if __name__ == '__main__':
    main()