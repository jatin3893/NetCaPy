from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow
from Others.CaptureFrame import CaptureFrame

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.Ui = loadUi('ui/MainWindow.ui', self)

        self.FeaturesList = []
        self.FiltersList = []

        self.LoadInput()
        self.LoadAnalysis()
        self.LoadFilters()

        captureFrame = CaptureFrame()
        self.Ui.tabWidget.addTab(captureFrame, "Main Page")

        self.show()

    def LoadInput(self):
        print "Load Input"

    def LoadAnalysis(self):
        print "Load Analysis"

    def LoadFilters(self):
        print "Load Filters"