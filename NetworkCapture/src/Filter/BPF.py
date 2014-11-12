from Filter import Filter
from scapy.all import *
import os
#################################################################
class BPF(Filter):
    def __init__(self):
        Filter.__init__(self)
        self.filterExpression = ''
        self.filteredPacketList = []
        self.originalPacketList = []

    def setFilterExpression(self, filterExpression):
    	self.filterExpression = filterExpression

    def getFilterExpression(self):
    	return self.filterExpression

    def setOriginalPacketList(self, packetList):
    	self.originalPacketList = packetList

    def getFilteredPacketList(self):
    	return self.filteredPacketList

    def filterPacketList(self):
    	wrpcap("temp.pcap", self.originalPacketList)
    	self.filteredPacketList = sniff(offline="temp.pcap", filter=self.filterExpression)
    	os.remove("temp.pcap")



