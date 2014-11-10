from PyQt4.QtGui import QFrame
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot

import webbrowser;

class CaptureFrame(QFrame):
    def __init__(self, parent = None):
        super(CaptureFrame, self).__init__(parent)
        self.Ui = loadUi('ui/Others/CaptureFrame.ui', self)

        self.Ui.buttonProjectPage.clicked.connect(self.buttonProjectPageClicked)

        print "Output Base Class"

    @pyqtSlot()
    def buttonProjectPageClicked(self):
        url = "https://github.com/jatin3893/ScaPyQtNetworkCapture"
        webbrowser.open(url)