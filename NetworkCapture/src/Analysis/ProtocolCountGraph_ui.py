#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ProtocolCountGraph_ui                                                 #
# Description:                                                                  #
# PyQt wrapper on ProtocolCountGraph for displaying Widgets in the GUI          #
#                                                                               #
#################################################################################

from Analysis_ui import Analysis_ui, AnalysisAction
from ProtocolCountGraph import ProtocolCountGraph
from src.Output.PacketData_ui import PacketData_ui
from PyQt4.QtGui import QIcon, QPixmap, QToolButton
from PyQt4.QtCore import QSize

'''
Description:
PyQt GUI over the ProtocolCountGraph module
'''
class ProtocolCountGraph_ui(Analysis_ui):
    '''
    Description:
    Initialize the Men bar with actions and tool bar with tool buttons
    '''
    def __init__(self, parent = None):
        Analysis_ui.__init__(self)
        self.parent = parent
        self.action = ProtocolCountGraphAction(self, parent)
        
        menuAnalysis = self.parent.GetMenu("Analysis")
        if menuAnalysis != None:
            menuAnalysis.addAction(self.action)

        toolBarAnalysis = self.parent.GetToolBar("Analysis")
        if toolBarAnalysis != None:
            pcgPixmap = QPixmap("icons/barGraph.png")
            pcgIcon = QIcon(pcgPixmap)
            self.pcgButton = QToolButton(self.parent)
            self.pcgButton.setIcon(pcgIcon)
            self.pcgButton.setIconSize(QSize(32, 32))
            self.pcgButton.clicked.connect(self.OnTrigger)
            toolBarAnalysis.addWidget(self.pcgButton)

    '''
    Description:
    Set the packet list to be analysed and plot the graph
    '''
    def OnTrigger(self):
        widget = self.parent.GetCurrentTab()
        if widget != None and isinstance(widget, PacketData_ui):
            obj = ProtocolCountGraph()
            obj.setPacketList(widget.packetList)
            obj.plotGraph()

'''
Description:

'''
class ProtocolCountGraphAction(AnalysisAction):
    def __init__(self, analysisUi, parent = None):
        AnalysisAction.__init__(self, analysisUi, parent)
        self.setText("Protocol Count Graph")