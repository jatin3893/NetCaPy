#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: BPF                                                                   #
# Description:                                                                  #
# Module for applying BPF filter on list of packets                             #
#                                                                               #
#################################################################################

from Filter import Filter
from scapy.all import *
import os
import subprocess

'''
Description:
Applying Berkeley Packet Filter filter on list of packets
'''
class BPF(Filter):
    '''
    Description:

    '''
    def __init__(self):
        Filter.__init__(self)
        self.filterExpression = ''
        self.filteredPacketList = []
        self.originalPacketList = []

    '''
    Description:

    '''
    def setFilterExpression(self, filterExpression):
        self.filterExpression = filterExpression

    '''
    Description:

    '''
    def getFilterExpression(self):
        return self.filterExpression

    '''
    Description:

    '''
    def setOriginalPacketList(self, packetList):
        self.originalPacketList = packetList

    '''
    Description:

    '''
    def getFilteredPacketList(self):
        return self.filteredPacketList

    '''
    Description:
    Dump list into a pcap file, apply BPF using tcpdump and read the output pcap file into a list
    '''
    def filterPacketList(self):
        wrpcap("temp.pcap", self.originalPacketList)
        subprocess.call(['tcpdump', '-r', 'temp.pcap', self.filterExpression, '-w', 'temp2.pcap'])
        self.filteredPacketList = rdpcap('temp2.pcap')
        os.remove('temp.pcap')
        os.remove('temp2.pcap')



