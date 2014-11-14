from Analysis_ui import Analysis_ui, AnalysisAction
from PacketSizeGraph import PacketSizeGraph
from src.Output.PacketData_ui import PacketData_ui
from PyQt4.QtGui import QIcon, QPixmap, QToolButton
from PyQt4.QtCore import QSize

#################################################################
class PacketSizeGraph_ui(Analysis_ui):
    def __init__(self, parent = None):
        Analysis_ui.__init__(self)
        self.parent = parent
        self.action = PacketSizeGraphAction(self, parent)
        
        menuAnalysis = self.parent.GetMenu("Analysis")
        if menuAnalysis != None:
        	menuAnalysis.addAction(self.action)

        toolBarAnalysis = self.parent.GetToolBar("Analysis")
        if toolBarAnalysis != None:
            pSizePixmap = QPixmap("icons/pointChart.png")
            pSizeIcon = QIcon(pSizePixmap)
            self.pSizeButton = QToolButton(self.parent)
            self.pSizeButton.setIcon(pSizeIcon)
            self.pSizeButton.setIconSize(QSize(32, 32))
            self.pSizeButton.clicked.connect(self.OnTrigger)
            toolBarAnalysis.addWidget(self.pSizeButton)

    def OnTrigger(self):
        widget = self.parent.GetCurrentTab()
        if widget != None and isinstance(widget, PacketData_ui):
            obj = PacketSizeGraph()
            obj.setPacketList(widget.packetList)
            obj.plotGraph()

class PacketSizeGraphAction(AnalysisAction):
    def __init__(self, analysisUi, parent = None):
        AnalysisAction.__init__(self, analysisUi, parent)
        self.setText("Packet Size Graph")