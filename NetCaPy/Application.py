from PyQt4.QtGui import QApplication
from MainWindow import MainWindow
import sys

def main():  
    App = QApplication(sys.argv)
    window = MainWindow()
    window.AddCustomFilter("Custom")
    App.exec_()

if __name__ == "__main__":
    main()