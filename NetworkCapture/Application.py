from PyQt4.QtGui import QApplication
from src.MainWindow import MainWindow
import sys

App = QApplication(sys.argv)
window = MainWindow()
window.AddCustomFilter("Custom")
App.exec_() 