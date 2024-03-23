# This Python file uses the following encoding: utf-8

import sys

from PySide6 import QtWidgets
from caixaMultibanco import CaixaMultibanco

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = CaixaMultibanco()
    window.show()

    app.exec()

