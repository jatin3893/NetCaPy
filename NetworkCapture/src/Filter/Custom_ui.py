from Filter_ui import Filter_ui, FilterAction, FilterFrame
from Custom import Custom
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi

#################################################################
class Custom_ui(Filter_ui):
    def __init__(self, parent = None):
        Filter_ui.__init__(self)
        self.parent = parent
        self.frame = CustomFrame()
        self.action = CustomAction(self, parent)

        toolbarFilter = self.parent.GetToolBar("Filter")
        if toolbarFilter != None:
            toolbarFilter.insertWidget(toolbarFilter.count() - 1, self.frame)

        menuFilter = self.parent.GetMenu("Filter")
        if menuFilter != None:
            menuFilter.addAction(self.action)

    def OnTrigger(self):
        print "Custom Ui Trigger"

#################################################################
class CustomFrame(FilterFrame):
    def __init__(self, parent = None):
        FilterFrame.__init__(self, parent)
        self.Ui = loadUi('ui/Filter/Custom_ui.ui', self)
        self.Ui.buttonCustom.clicked.connect(self.buttonCustomClicked)
    
    @pyqtSlot()
    def buttonCustomClicked(self):
        print "Custom Button Clicked"

#################################################################
class CustomAction(FilterAction):
    def __init__(self, filterUi, parent = None):
        FilterAction.__init__(self, filterUi, parent)
        self.setText("Custom")
