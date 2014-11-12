from PyQt4.QtGui import QFrame, QTableWidgetItem
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot
from PacketData import PacketData

#################################################################
class PacketData_ui(QFrame):
    def __init__(self, parent = None):

        self.SOURCE = 1
        self.DESTINATION = 2
        self.INFO = 5

        super(PacketData_ui, self).__init__(parent)
        self.Ui = loadUi('ui/Output/PacketData.ui', self)
        self.Ui.packetList = []
        self.Ui.tableWidgetPacketData.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        parent.AddTab(self, "Packet Info")

    def AddPacketData(self, packet):
        self.packetList.append(packet)
        packetData = PacketData(packet)
        
        row = self.Ui.tableWidgetPacketData.rowCount()
        self.Ui.tableWidgetPacketData.insertRow(row)
        
        # Setting data in the cells. Data to be obtained fom packetData
        self.Ui.tableWidgetPacketData.setItem(row, self.SOURCE, QTableWidgetItem(packetData.srcIp))
        self.Ui.tableWidgetPacketData.setItem(row, self.DESTINATION, QTableWidgetItem(packetData.dstIp))
        self.Ui.tableWidgetPacketData.setItem(row, self.INFO, QTableWidgetItem(packet.summary()))

    def itemSelectionChangedCallback(self):
        x = self.Ui.tableWidgetPacketData.currentRow()
        self.Ui.textBrowserPacketInfo.setText(self.packetList[x].summary())

