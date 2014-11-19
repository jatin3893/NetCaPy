#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: BPF_ui                                                                #
# Description:                                                                  #
# PyQt wrapper on BPF module for applying BPF on list of packets                #
#                                                                               #
#################################################################################

from Filter_ui import Filter_ui, FilterAction, FilterFrame
from BPF import BPF
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog
from PyQt4.uic import loadUi
from NetCaPy.Output.PacketData_ui import PacketData_ui
import os

'''
Description:
PyQt wrapper on BPF Module to apply BPF on list of packets
'''
class BPF_ui(Filter_ui):
    '''
    Description:
    Initialise menu bar and toolbar actions for applying BPF
    '''
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
    
    '''
    Description:
    Display BPF Dialog and apply filter accordingly
    '''
    @pyqtSlot()
    def OnTrigger(self):
        obj = QDialog()
        objUi = loadUi(os.path.dirname(os.path.realpath(__file__)) + '/BPFDialog_ui.ui', obj)
        if obj.exec_() == QDialog.Accepted:
            self.frame.Ui.lineEditExpression.setText(objUi.lineEditExpression.text())
            self.frame.buttonApplyClicked()

'''
Description:
Initialise frame to be added in tool bar for applying BPF Filter
'''
class BPFFrame(FilterFrame):
    '''
    Description:

    '''
    def __init__(self, parent = None):
        FilterFrame.__init__(self, parent)
        self.parent = parent
        self.Ui = loadUi(os.path.dirname(os.path.realpath(__file__)) + '/BPFToolbar_ui.ui', self)

        self.Ui.buttonClear.clicked.connect(self.buttonClearClicked)
        self.Ui.buttonApply.clicked.connect(self.buttonApplyClicked)

    '''
    Description:

    '''
    @pyqtSlot()
    def buttonClearClicked(self):
        self.Ui.lineEditExpression.clear()
        self.buttonApplyClicked()

    '''
    Description:
    Obtain packet list from current tab and apply BPF filter as specified
    '''
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
        
'''
Description:

'''
class BPFAction(FilterAction):
    def __init__(self, filterUi, parent = None):
        FilterAction.__init__(self, filterUi, parent)
        self.setText("BPF")

'''
Description:

'''
class BPFDialog(QDialog):
    def __init__(self, parent = None):
        super(InterfaceSelection, self).__init__(parent)
        self.Ui = loadUi('ui/Filter/BPFDialog_ui.ui', self)