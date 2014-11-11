from abc import abstractmethod
from PyQt4.QtGui import QFrame, QAction
from PyQt4.QtCore import pyqtSlot, QObject

#################################################################
class Filter_ui(QObject):
    def __init__(self, parent = None):
        super(Filter_ui, self).__init__(parent)

    @abstractmethod
    def OnTrigger(self):
    	pass
    	
#################################################################
class FilterFrame(QFrame):
    def __init__(self, parent = None):
        super(FilterFrame, self).__init__(parent)

#################################################################
class FilterAction(QAction):
    def __init__(self, filterUi, parent = None):
        super(FilterAction, self).__init__(parent)
        self.triggered.connect(self.OnTrigger)
        self.filterUi = filterUi

    @pyqtSlot()
    def OnTrigger(self):
        self.filterUi.OnTrigger()