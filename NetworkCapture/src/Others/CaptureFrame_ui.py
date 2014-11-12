from PyQt4.QtGui import QFrame
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot

import webbrowser;

#################################################################
class CaptureFrame_ui(QFrame):
    def __init__(self, parent = None):
        super(CaptureFrame_ui, self).__init__(parent)
        self.Ui = loadUi('ui/Others/CaptureFrame.ui', self)

        self.Ui.buttonInterfaceList.clicked.connect(self.buttonInterfaceListClicked)
        self.Ui.buttonStartCapture.clicked.connect(self.buttonStartCaptureClicked)

        self.Ui.buttonFileOpen.clicked.connect(self.buttonFileOpenClicked)
        self.Ui.buttonSampleFiles.clicked.connect(self.buttonSampleFilesClicked)

        self.Ui.buttonProjectPage.clicked.connect(self.buttonProjectPageClicked)
        self.Ui.buttonHowTo.clicked.connect(self.buttonHowToClicked)

        parent.AddTab(self, "Main Page")

    @pyqtSlot()
    def buttonInterfaceListClicked(self):
        print "Interfaces list"

    @pyqtSlot()
    def buttonStartCaptureClicked(self):
        print "Start Capture"

    @pyqtSlot()
    def buttonFileOpenClicked(self):
        print "File Open"

    @pyqtSlot()
    def buttonSampleFilesClicked(self):
        print "Sample Files"

    @pyqtSlot()
    def buttonProjectPageClicked(self):
        url = "https://github.com/jatin3893/ScaPyQtNetworkCapture"
        webbrowser.open(url)

    @pyqtSlot()
    def buttonHowToClicked(self):
        print "How To"