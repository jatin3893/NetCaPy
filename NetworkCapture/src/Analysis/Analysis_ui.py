#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: Analysis_ui                                                           #
# Description:                                                                  #
# Top level module for implementation of features related                       #
# to Analysis of packets                                                        #
#################################################################################

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QAction
from abc import abstractmethod

'''
Description:
Top level class for Analysis based operations
'''
class Analysis_ui(QObject):
    def __init__(self, parent = None):
        super(Analysis_ui, self).__init__(parent)

'''
Description:

'''
class AnalysisAction(QAction):
    def __init__(self, analysisUi, parent = None):
        super(AnalysisAction, self).__init__(parent)
        self.analysisUi = analysisUi
        self.triggered.connect(self.OnTrigger)

    '''
    Description:

    '''
    @abstractmethod
    def OnTrigger(self):
        self.analysisUi.OnTrigger()
