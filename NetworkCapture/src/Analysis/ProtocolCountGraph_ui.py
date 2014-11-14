from Analysis_ui import Analysis_ui, AnalysisAction
from ProtocolCountGraph import ProtocolCountGraph
from src.Output.PacketData_ui import PacketData_ui
from PyQt4.QtGui import QIcon, QPixmap, QToolButton
from PyQt4.QtCore import QSize

#################################################################
class ProtocolCountGraph_ui(Analysis_ui):
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

    def OnTrigger(self):
        widget = self.parent.GetCurrentTab()
        if widget != None and isinstance(widget, PacketData_ui):
            obj = ProtocolCountGraph()
            obj.setPacketList(widget.packetList)
            obj.plotGraph()

class ProtocolCountGraphAction(AnalysisAction):
    def __init__(self, analysisUi, parent = None):
        AnalysisAction.__init__(self, analysisUi, parent)
        self.setText("Protocol Count Graph")