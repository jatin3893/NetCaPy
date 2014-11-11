from PyQt4.QtGui import QFrame, QAction
from PyQt4.QtCore import pyqtSlot

#################################################################
class Filter_ui():
    def __init__(self):
        print "Filter Ui"

#################################################################
class FilterFrame(QFrame):
    def __init__(self, parent = None):
        super(FilterFrame, self).__init__(parent)

#################################################################
class FilterAction(QAction):
    def __init__(self, parent = None):
        super(FilterAction, self).__init__(parent)

    @pyqtSlot()
    def OnTrigger(self):
        print "Custom Action Triggered"