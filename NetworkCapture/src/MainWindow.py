from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow, QAction, qApp
from Others.CaptureFrame_ui import CaptureFrame_ui
from Input.LiveCapture_ui import LiveCapture_ui
from Output.PacketData_ui import PacketData_ui
from Input.ReadFromFile_ui import ReadFromFile_ui
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SLOT

#################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.Ui = loadUi('ui/MainWindow.ui', self)
        self.showMaximized()

        self.AnalysisList = ["PacketSizeGraph", "ProtocolCountGraph"]
        self.FiltersList = ["BPF"]

        self.menuDictionary = { "File" : self.Ui.menuFile,
                                "Capture" : self.Ui.menuCapture,
                                "Filter" : self.Ui.menuFilter,
                                "Analysis" : self.Ui.menuAnalysis,
                                "Help" : self.Ui.menuHelp}

        self.toolbarDictionary = {  "Capture" : self.Ui.toolBarLiveCapture,
                                    "Filter" : self.Ui.toolBarFilter,
                                    "File" : self.Ui.toolBarFile,
                                    "Analysis" : self.Ui.toolBarAnalysis}

        self.liveCapture_ui = LiveCapture_ui(self)
        self.readFromFile_ui = ReadFromFile_ui(self)
        self.captureFrame_ui = CaptureFrame_ui(self.liveCapture_ui, self.readFromFile_ui, self)

        self.LoadAnalysis()
        self.LoadFilters()

        exit = QAction("Exit", self)
        exit.triggered.connect(qApp.closeAllWindows)
        self.Ui.menuFile.addAction(exit)
        
        self.show()

    def AddTab(self, frame, name):
        index = self.Ui.tabWidget.addTab(frame, name)
        self.Ui.tabWidget.setCurrentIndex(index)
        return index

    def GetCurrentTab(self):
        return self.Ui.tabWidget.currentWidget()

    def GetMenu(self, index):
        return self.menuDictionary[index]

    def GetToolBar(self, index):
        return self.toolbarDictionary[index]

    def LoadAnalysis(self):
        for analysis in self.AnalysisList:
            self.AddAnalysis(analysis)

    def LoadFilters(self):
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

    # This can be used to load a Filter at RunTime
    def AddCustomFilter(self, customFilter):
        self.FiltersList.append(customFilter)
        self.AddFilter(customFilter)