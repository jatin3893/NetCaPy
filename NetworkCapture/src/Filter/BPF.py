from Filter import Filter
from scapy.all import *
import os
import subprocess
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
    	subprocess.call(['tcpdump', '-r', 'temp.pcap', self.filterExpression, '-w', 'temp2.pcap'])
        self.filteredPacketList = rdpcap('temp2.pcap')
        os.remove('temp.pcap')
        os.remove('temp2.pcap')



