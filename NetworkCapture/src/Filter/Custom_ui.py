from Custom import Custom
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QFrame, QAction
from PyQt4.uic import loadUi

class Custom_ui():
    def __init__(self, parentMenu = None):
        print "Custom Filter Base Class"
        self.frame = CustomFrame()
        self.action = CustomAction(parentMenu)

class CustomFrame(QFrame):
    def __init__(self, parent = None):
        super(CustomFrame, self).__init__(parent)
        self.Ui = loadUi('ui/Filter/Custom_ui.ui', self)
        self.Ui.buttonCustom.clicked.connect(self.buttonCustomClicked)
    
    @pyqtSlot()
    def buttonCustomClicked(self):
        print "Custom Button Clicked"

# For adding QAction in the Menu Bar
# To be made Optional
class CustomAction(QAction):
    def __init__(self, parent = None):
        super(CustomAction, self).__init__(parent)
        self.setText("Custom")
        self.triggered.connect(self.OnTrigger)

    @pyqtSlot()
    def OnTrigger(self):
        print "Custom Action Triggered"