from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow
from Others.CaptureFrame import CaptureFrame
from PyQt4.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.Ui = loadUi('ui/MainWindow.ui', self)

        self.AnalysisList = ["PacketCount"]
        self.FiltersList = ["BPF", "Custom"]

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
        for analysis in self.AnalysisList:
            self.AddAnalysis(analysis)

    def LoadFilters(self):
        print "Load Filters"
        for filter in self.FiltersList:
            self.AddFilter(filter)
        self.Ui.toolbarFilter.addStretch()

    def AddFilter(self, filter):
        filter = filter + "_ui"
        path = "src.Filter." + filter
        mod = __import__(path, fromlist=[filter])
        filterClass = getattr(mod, filter)
        object = filterClass()
        self.Ui.toolbarFilter.addWidget(object.frame)

    def AddAnalysis(self, analysis):
        analysis = analysis + "_ui"
        path = "src.Analysis." + analysis
        mod = __import__(path, fromlist=[analysis])
        AnalysisClass = getattr(mod, analysis)
        object = AnalysisClass()