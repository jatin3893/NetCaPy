#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: Filter_ui                                                             #
# Description:                                                                  #
#                                                                               #
#################################################################################

from abc import abstractmethod
from PyQt4.QtGui import QFrame, QAction
from PyQt4.QtCore import pyqtSlot, QObject

'''
Description:

'''
class Filter_ui(QObject):
    def __init__(self, parent = None):
        super(Filter_ui, self).__init__(parent)

    @abstractmethod
    def OnTrigger(self):
        pass
        
'''
Description:

'''
class FilterFrame(QFrame):
    def __init__(self, parent = None):
        super(FilterFrame, self).__init__(parent)

'''
Description:

'''
class FilterAction(QAction):
    def __init__(self, filterUi, parent = None):
        super(FilterAction, self).__init__(parent)
        self.triggered.connect(self.OnTrigger)
        self.filterUi = filterUi

    @pyqtSlot()
    def OnTrigger(self):
        self.filterUi.OnTrigger()