from Filter_ui import Filter_ui, FilterAction, FilterFrame
from BPF import BPF
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi
from src.Output.PacketData_ui import PacketData_ui

#################################################################
class BPF_ui(Filter_ui):
    def __init__(self, parent = None):
        Filter_ui.__init__(self)
        self.parent = parent

        self.frame = BPFFrame(parent)
        self.action = BPFAction(self, parent)

        toolBarFilter = self.parent.GetToolBar("Filter")
        if toolBarFilter != None:
            toolBarFilter.addWidget(self.frame)
            toolBarFilter.addSeparator()

        menuFilter = self.parent.GetMenu("Filter")
        if menuFilter != None:
            menuFilter.addAction(self.action)
    
    @pyqtSlot()
    def OnTrigger(self):
        print "BPF Action Triggered"

#################################################################
class BPFFrame(FilterFrame):
    def __init__(self, parent = None):
        FilterFrame.__init__(self, parent)
        self.parent = parent
        self.Ui = loadUi('ui/Filter/BPF_ui.ui', self)

        self.Ui.buttonClear.clicked.connect(self.buttonClearClicked)
        self.Ui.buttonApply.clicked.connect(self.buttonApplyClicked)

    @pyqtSlot()
    def buttonClearClicked(self):
        self.Ui.lineEditExpression.clear()
        self.buttonApplyClicked()

    @pyqtSlot()
    def buttonApplyClicked(self):
        widget = self.parent.GetCurrentTab()
        if widget != None and isinstance(widget, PacketData_ui):
            bpf = BPF()
            bpf.setFilterExpression(self.Ui.lineEditExpression.text())
            bpf.setOriginalPacketList(widget.originalList)
            bpf.filterPacketList()
            newList = bpf.getFilteredPacketList()
            widget.SetPacketList(newList)
        
#################################################################
class BPFAction(FilterAction):
    def __init__(self, filterUi, parent = None):
        FilterAction.__init__(self, filterUi, parent)
        self.setText("BPF")
