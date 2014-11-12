from scapy.all import *

class PacketData:
    def __init__(self, packet):
        self.packet = packet
        #self.packetInfo = [0, packet[IP].src, packet[IP].dst, "", 0, ""]
