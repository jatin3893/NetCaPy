#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ReadFromFile_test                                                     #
# Description:                                                                  #
# Test file for testing the ReadFromFile Module                                 #
#                                                                               #
#################################################################################

from PyQt4.uic import loadUi
from PyQt4.QtGui import QMainWindow, QAction, qApp
from Others.CaptureFrame_ui import CaptureFrame_ui
from Input.LiveCapture_ui import LiveCapture_ui
from Output.PacketData_ui import PacketData_ui
from Input.ReadFromFile_ui import ReadFromFile_ui
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SLOT
import os

'''
Description:

'''
class MainWindow(QMainWindow):

    '''
    Description:

    '''
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.Ui = loadUi(os.path.dirname(os.path.realpath(__file__)) + '/MainWindow.ui', self)
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

    '''
    Description:

    '''
    def AddTab(self, frame, name):
        index = self.Ui.tabWidget.addTab(frame, name)
        self.Ui.tabWidget.setCurrentIndex(index)
        return index

    '''
    Description:

    '''
    def GetCurrentTab(self):
        return self.Ui.tabWidget.currentWidget()

    '''
    Description:

    '''
    def GetMenu(self, index):
        return self.menuDictionary[index]

    '''
    Description:

    '''
    def GetToolBar(self, index):
        return self.toolbarDictionary[index]

    '''
    Description:

    '''
    def LoadAnalysis(self):
        for analysis in self.AnalysisList:
            self.AddAnalysis(analysis)

    '''
    Description:

    '''
    def LoadFilters(self):
        for filter in self.FiltersList:
            self.AddFilter(filter)

    '''
    Description:

    '''
    def LoadHelpMenu(self):
        print "Load Help Menu"

 
    '''
    Description:

    '''
    def AddFilter(self, filter):
        # Could lead to run time errors. Use try/catch to detect import errors
        filterUi = filter + "_ui"
        path = "src.Filter." + filterUi
        mod = __import__(path, fromlist=[filterUi])
        filterUiClass = getattr(mod, filterUi)
        object = filterUiClass(self)

    '''
    Description:

    '''
    def AddAnalysis(self, analysis):
        # Could lead to run time errors. Use try/catch to detect import errors
        analysisUi = analysis + "_ui"
        path = "src.Analysis." + analysisUi
        mod = __import__(path, fromlist=[analysisUi])
        AnalysisUiClass = getattr(mod, analysisUi)
        object = AnalysisUiClass(self)

    '''
    Description:

    '''
    def AddCustomFilter(self, customFilter):
        # This can be used to load a Filter at RunTime
        self.FiltersList.append(customFilter)
        self.AddFilter(customFilter)