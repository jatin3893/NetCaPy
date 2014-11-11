from PyQt4.QtCore import QObject
from PyQt4.QtGui import QAction
from abc import abstractmethod

#################################################################
class Analysis_ui(QObject):
    def __init__(self, parent = None):
        super(Analysis_ui, self).__init__(parent)
    
    @abstractmethod
    def OnTrigger(self):
        pass
#################################################################
class AnalysisAction(QAction):
    def __init__(self, analysisUi, parent = None):
        super(AnalysisAction, self).__init__(parent)
        self.analysisUi = analysisUi
        self.triggered.connect(self.OnTrigger)

    @abstractmethod
    def OnTrigger(self):
        self.analysisUi.OnTrigger()
