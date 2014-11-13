from PyQt4.QtGui import QFrame, QTableWidgetItem, QLabel
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot
from PacketData import PacketData
import time
import sys
import StringIO

#################################################################
class PacketData_ui(QFrame):
    def __init__(self, parent = None):
        super(PacketData_ui, self).__init__(parent)

        self.TIME = 0
        self.SOURCE = 1
        self.DESTINATION = 2
        self.PROTOCOL = 3
        self.LENGTH = 4
        self.INFO = 5

        self.Ui = loadUi('ui/Output/PacketData.ui', self)
        self.originalList = []
        self.packetList = []
        self.Ui.tableWidgetPacketData.itemSelectionChanged.connect(self.itemSelectionChangedCallback)
        parent.AddTab(self, "Packet Info")

    def ClearPacketList(self):
        self.packetList = []

    def AddPacket(self, packet):
        self.originalList.append(packet)
        self.AddPacketData(packet)

    def AddPacketData(self, packet):
        packetData = PacketData(packet)
        self.packetList.append(packet)

        row = self.Ui.tableWidgetPacketData.rowCount()
        self.Ui.tableWidgetPacketData.insertRow(row)
        
        pktTime = time.strftime('%I:%M:%S %p', time.localtime(packetData.packetTime))
        # Setting data in the cells. Data to be obtained fom packetData
        self.Ui.tableWidgetPacketData.setItem(row, self.TIME, QTableWidgetItem(pktTime))
        self.Ui.tableWidgetPacketData.setItem(row, self.SOURCE, QTableWidgetItem(packetData.srcIp))
        self.Ui.tableWidgetPacketData.setItem(row, self.DESTINATION, QTableWidgetItem(packetData.dstIp))
        self.Ui.tableWidgetPacketData.setItem(row, self.PROTOCOL, QTableWidgetItem(packetData.layers[-2]))
        self.Ui.tableWidgetPacketData.setItem(row, self.LENGTH, QTableWidgetItem(str(packetData.length)))
        self.Ui.tableWidgetPacketData.setItem(row, self.INFO, QTableWidgetItem(packet.summary()))

    def ClearAll(self):
        self.Ui.tableWidgetPacketData.clear()
        self.Ui.tableWidgetPacketData.setRowCount(0)

    def SetPacketList(self, packetLists):
        self.ClearAll()
        self.packetList = []
        for packet in packetLists:
            self.AddPacketData(packet)

    def itemSelectionChangedCallback(self):
        x = self.Ui.tableWidgetPacketData.currentRow()

        stdout = sys.stdout  #keep a handle on the real standard output
        sys.stdout = mystdout = StringIO.StringIO() #Choose a file-like object to write to
        self.packetList[x].show()
        sys.stdout = stdout
        # self.Ui.textBrowserPacketInfo.setText(mystdout.getvalue())
        self.Ui.textBrowserPacketInfo.setText(self.packetList[x].summary())


