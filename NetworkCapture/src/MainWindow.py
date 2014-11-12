from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow, QAction
from Others.CaptureFrame_ui import CaptureFrame_ui
from Input.LiveCapture_ui import LiveCapture_ui
from Output.PacketData_ui import PacketData_ui
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SLOT

#################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.Ui = loadUi('ui/MainWindow.ui', self)

        self.AnalysisList = ["PacketCount"]
        self.FiltersList = ["BPF"]

        self.menuDictionary = { "File" : self.Ui.menuFile,
                                "Capture" : self.Ui.menuCapture,
                                "Filter" : self.Ui.menuFilter,
                                "Analysis" : self.Ui.menuAnalysis,
                                "Help" : self.Ui.menuHelp}

        self.toolbarDictionary = {  "Capture" : self.Ui.toolBarCapture,
                                    "Filter" : self.Ui.toolbarFilter,
                                    "Analysis" : self.Ui.toolBarAnalysis}

        self.initUi()
        self.liveCapture_ui = None
        self.captureFrame_ui = None

        self.LoadAnalysis()
        self.LoadFilters()

        self.show()

    def initUi(self):
        self.Ui.toolbarFilter.addStretch();
        self.liveCapture_ui = LiveCapture_ui(self)
        self.captureFrame_ui = CaptureFrame_ui(self)

    def AddTab(self, frame, name):
        index = self.Ui.tabWidget.addTab(frame, name)
        self.Ui.tabWidget.setCurrentIndex(index)
        return index

    def GetMenu(self, index):
        return self.menuDictionary[index]

    def GetToolBar(self, index):
        return self.toolbarDictionary[index]

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
        filterUiClass = getattr(mod, filterUi)
        object = filterUiClass(self)

    # 
    # Could lead to run time errors. Use try/catch to detect import errors
    def AddAnalysis(self, analysis):
        analysisUi = analysis + "_ui"
        path = "src.Analysis." + analysisUi
        mod = __import__(path, fromlist=[analysisUi])
        AnalysisUiClass = getattr(mod, analysisUi)
        object = AnalysisUiClass(self)
        self.Ui.menuAnalysis.addAction(object.action)

    # This can be used to load a Filter at RunTime
    def AddCustomFilter(self, customFilter):
        self.FiltersList.append(customFilter)
        self.AddFilter(customFilter)