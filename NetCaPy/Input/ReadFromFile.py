#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ReadFromFile                                                          #
# Description:                                                                  #
# This module reads/writes pcap files from/to a list of packets                 #
#                                                                               #
#################################################################################

from scapy.all import *

'''
Description:

'''
class ReadFromFile:
    def __init__(self):
        self.filename = ''

    '''
    Description:
    Use scapy's api to get list of packets from a pcap file
    '''
    def readPackets(self):
        return rdpcap(self.filename)

    '''
    Description:
    Simple Get to obtain the source/destination file path
    '''
    def getFilename(self):
        return self.filename

    '''
    Description:
    Simple Set to specify the source/destination file path
    '''
    def setFilename(self, filename):
        self.filename = filename


    '''
    Description:
    Wrapper to Scapy's function to write a list of packets into a pcap file
    as specified in the filename as destination
    '''
    def saveFile(self, filename, packetList):
        wrpcap(filename, packetList)