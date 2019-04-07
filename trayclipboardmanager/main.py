#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from core import TrayClipboardManager


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = QtGui.QIcon(os.path.join(os.path.dirname(__file__), "icon.png"))
    tray_app = TrayClipboardManager(icon)
    app.clipboard().dataChanged.connect(tray_app.data_changed)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
