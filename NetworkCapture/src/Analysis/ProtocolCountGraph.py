from Analysis import Analysis
import matplotlib.pyplot as plt
from scapy.all import *

class ProtocolCountGraph(Analysis):
	def __init__(self):
		Analysis.__init__(self)
		self.packetList = []

	def setPacketList(self, packetList):
		self.packetList = packetList

	def plotGraph(self):
		protocol_count = {"TCP":0, "UDP":0, "ARP":0, "Others":0}

		for packet in self.packetList:
			if TCP in packet:
				protocol_count["TCP"] += 1
			elif UDP in packet:
				protocol_count["UDP"] += 1
			elif ARP in packet:
				protocol_count["ARP"] += 1
			else:
				protocol_count["Others"] += 1

		plt.bar(range(len(protocol_count)), protocol_count.values(), align='center')
		plt.xticks(range(len(protocol_count)), protocol_count.keys())
		plt.xlabel('Protocol')
		plt.ylabel('Count')
		plt.title('Protocol Count Graph')
		plt.show()
