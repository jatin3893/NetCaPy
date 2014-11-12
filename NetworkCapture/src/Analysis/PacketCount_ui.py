from Analysis_ui import Analysis_ui, AnalysisAction
from PacketCount import PacketCount

#################################################################
class PacketCount_ui(Analysis_ui):
    def __init__(self, parent = None):
        Analysis_ui.__init__(self)
        self.parent = parent
        self.action = PacketCountAction(self, parent)
        
        menuAnalysis = self.parent.GetMenu("Analysis")
        if menuAnalysis != None:
        	menuAnalysis.addAction(self.action)

    def OnTrigger(self):
        print "Packet Count Triggered"

class PacketCountAction(AnalysisAction):
    def __init__(self, analysisUi, parent = None):
        AnalysisAction.__init__(self, analysisUi, parent)
        self.setText("Packet Count")