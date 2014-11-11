from Filter_ui import Filter_ui, FilterAction, FilterFrame
from BPF import BPF
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi

#################################################################
class BPF_ui(Filter_ui):
    def __init__(self, parentMenu = None):
        Filter_ui.__init__(self)
        self.frame = BPFFrame()
        self.action = BPFAction(self, parentMenu)
    
    @pyqtSlot()
    def OnTrigger(self):
        print "BPF Action Triggered"

#################################################################
class BPFFrame(FilterFrame):
    def __init__(self, parent = None):
        FilterFrame.__init__(self, parent)
        self.Ui = loadUi('ui/Filter/BPF_ui.ui', self)

        self.Ui.buttonClear.clicked.connect(self.buttonClearClicked)
        self.Ui.buttonApply.clicked.connect(self.buttonApplyClicked)

    @pyqtSlot()
    def buttonClearClicked(self):
        self.Ui.lineEditExpression.clear()

    @pyqtSlot()
    def buttonApplyClicked(self):
        print "Apply Button on BPF Filter Clicked"
		applyFilter(self.Ui.lineEditExpression.text, PcapFile)
		
#################################################################
class BPFAction(FilterAction):
    def __init__(self, filterUi, parent = None):
        FilterAction.__init__(self, filterUi, parent)
        self.setText("BPF")
