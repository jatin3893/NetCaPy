#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ReadFromFile_ui                                                       #
# Description:                                                                  #
# Obtain specific fields from packet as required for display                    #
#                                                                               #
#################################################################################

from scapy.all import *

'''
'''
class PacketData:

    '''
    Obtatin Time, Src, Dst, Protocol, length and Summary of the packet 
    '''
    def __init__(self, packet):
        self.packet = packet

        self.layers = []
        counter = 0
        while True:
            layer = self.packet.getlayer(counter)
            if (layer != None):
                self.layers.append(layer.name)
            else:
                break
            counter += 1
            
        self.srcIp = "-"
        self.dstIp = "-"
        if IP in packet:
            self.srcIp = packet[IP].src
            self.dstIp = packet[IP].dst
        elif IPv6 in packet:
            self.srcIp = packet[IPv6].src
            self.dstIp = packet[IPv6].dst
        elif ARP in packet:
            self.srcIp = packet[ARP].hwsrc
            self.dstIp = packet[ARP].hwdst

        self.packetTime = packet.time
        self.length = len(self.packet)
