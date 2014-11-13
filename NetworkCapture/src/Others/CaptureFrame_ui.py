from PyQt4.QtGui import QFrame
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot
from src.Input.LiveCapture_ui import LiveCapture_ui
from src.Input.ReadFromFile_ui import ReadFromFile_ui
import webbrowser;

#################################################################
class CaptureFrame_ui(QFrame):
    def __init__(self, liveCapture = None, readFromFile = None, parent = None):
        super(CaptureFrame_ui, self).__init__(parent)
        self.parent = parent
        self.Ui = loadUi('ui/Others/CaptureFrame.ui', self)

        self.Ui.buttonInterfaceList.clicked.connect(self.buttonInterfaceListClicked)
        self.Ui.buttonStartCapture.clicked.connect(liveCapture.triggerStart)
        self.Ui.buttonFileOpen.clicked.connect(readFromFile.triggerOpen)
        self.Ui.buttonSampleFiles.clicked.connect(self.buttonSampleFilesClicked)
        self.Ui.buttonProjectPage.clicked.connect(self.buttonProjectPageClicked)
        self.Ui.buttonHowTo.clicked.connect(self.buttonHowToClicked)

        parent.AddTab(self, "Main Page")

    @pyqtSlot()
    def buttonInterfaceListClicked(self):
        print "Interfaces list"
        
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