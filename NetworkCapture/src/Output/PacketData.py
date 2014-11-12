from scapy.all import *

class PacketData:
    def __init__(self, packet):
        self.packet = packet
        self.srcIp = "-"
        self.dstIp = "-"

        if IP in packet:
            self.srcIp = packet[IP].src
            self.dstIp = packet[IP].dst
        
        if ARP in packet:
            pass
