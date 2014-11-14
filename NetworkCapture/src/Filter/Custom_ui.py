#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: Custom_ui                                                             #
# Description:                                                                  #
#                                                                               #
#################################################################################

from Filter_ui import Filter_ui, FilterAction, FilterFrame
from Custom import Custom
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi

'''
Description:

'''
class Custom_ui(Filter_ui):
    '''
    Description:

    '''
    def __init__(self, parent = None):
        Filter_ui.__init__(self)
        self.parent = parent
        self.frame = CustomFrame()
        self.action = CustomAction(self, parent)

        toolBarFilter = self.parent.GetToolBar("Filter")
        if toolBarFilter != None:
            toolBarFilter.addWidget(self.frame)
            toolBarFilter.addSeparator()

        menuFilter = self.parent.GetMenu("Filter")
        if menuFilter != None:
            menuFilter.addAction(self.action)

    def OnTrigger(self):
        print "Custom Ui Trigger"

'''
Description:

'''
class CustomFrame(FilterFrame):
    def __init__(self, parent = None):
        FilterFrame.__init__(self, parent)
        self.Ui = loadUi('ui/Filter/Custom_ui.ui', self)
        self.Ui.buttonCustom.clicked.connect(self.buttonCustomClicked)
    
    @pyqtSlot()
    def buttonCustomClicked(self):
        print "Custom Button Clicked"

'''
Description:

'''
class CustomAction(FilterAction):
    def __init__(self, filterUi, parent = None):
        FilterAction.__init__(self, filterUi, parent)
        self.setText("Custom")
