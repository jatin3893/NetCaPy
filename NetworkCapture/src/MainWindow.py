from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow, QAction
from Others.CaptureFrame import CaptureFrame
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SLOT

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.initUi()

        self.AnalysisList = ["PacketCount"]
        self.FiltersList = ["BPF"]

        self.LoadInput()
        self.LoadAnalysis()
        self.LoadFilters()

        self.show()

    def initUi(self):
        self.Ui = loadUi('ui/MainWindow.ui', self)

        self.Ui.toolbarFilter.addStretch();

        captureFrame = CaptureFrame()
        self.Ui.tabWidget.addTab(captureFrame, "Main Page")

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

    def LoadHelpMenu(self):
        print "Load Help Menu"

    #
    # Could lead to run time errors. Use try/catch to detect import errors
    def AddFilter(self, filter):
        filterUi = filter + "_ui"
        path = "src.Filter." + filterUi
        mod = __import__(path, fromlist=[filterUi])
        filterClass = getattr(mod, filterUi)
        object = filterClass(self.Ui.menuFilter)
        self.Ui.toolbarFilter.insertWidget(self.Ui.toolbarFilter.count() - 1, object.frame)
        self.Ui.menuFilter.addAction(object.action)

    # 
    # Could lead to run time errors. Use try/catch to detect import errors
    def AddAnalysis(self, analysis):
        analysis = analysis + "_ui"
        path = "src.Analysis." + analysis
        mod = __import__(path, fromlist=[analysis])
        AnalysisClass = getattr(mod, analysis)
        object = AnalysisClass()

    # This can be used to load a Filter at RunTime
    def AddCustomFilter(self, customFilter):
        self.FiltersList.append(customFilter)
        self.AddFilter(customFilter)