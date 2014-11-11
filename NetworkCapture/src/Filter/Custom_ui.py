from Filter_ui import Filter_ui, FilterAction, FilterFrame
from Custom import Custom
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi

#################################################################
class Custom_ui(Filter_ui):
    def __init__(self, parentMenu = None):
        Filter_ui.__init__(self)
        self.frame = CustomFrame()
        self.action = CustomAction(parentMenu)

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
    def __init__(self, parent = None):
        FilterAction.__init__(self, parent)
        self.setText("Custom")
        self.triggered.connect(self.OnTrigger)

    @pyqtSlot()
    def OnTrigger(self):
        print "Custom Action Triggered"