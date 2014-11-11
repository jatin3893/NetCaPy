from BPF import BPF
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QFrame, QAction
from PyQt4.uic import loadUi

class BPF_ui():
    def __init__(self, parentMenu = None):
        print "BPF Filter Base Class"
        self.frame = BPFFrame()
        self.action = BPFAction(parentMenu)

# For adding shortcut in the toolbar
# To be made optional
class BPFFrame(QFrame):
    def __init__(self, parent = None):
        super(BPFFrame, self).__init__()
        self.Ui = loadUi('ui/Filter/BPF_ui.ui', self)

        self.Ui.buttonClear.clicked.connect(self.buttonClearClicked)
        self.Ui.buttonApply.clicked.connect(self.buttonApplyClicked)

    @pyqtSlot()
    def buttonClearClicked(self):
        self.Ui.lineEditExpression.clear()

    @pyqtSlot()
    def buttonApplyClicked(self):
        print "Apply Button on BPF Filter Clicked"

# For adding QAction in the Menu Bar
class BPFAction(QAction):
    def __init__(self, parent = None):
        super(BPFAction, self).__init__(parent)
        self.setText("BPF")
        self.triggered.connect(self.OnTrigger)

    @pyqtSlot()
    def OnTrigger(self):
        print "BPF Action Triggered"