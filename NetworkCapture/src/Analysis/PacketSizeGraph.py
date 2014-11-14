from Analysis import Analysis
import matplotlib.pyplot as plt

class PacketSizeGraph(Analysis):
	def __init__(self):
		Analysis.__init__(self)
		self.packetList = []

	def setPacketList(self, packetList):
		self.packetList = packetList

	def plotGraph(self):
		countList = []
		sizeList = []
		count = 0

		for packet in self.packetList:
			countList.append(count)
			count = count + 1
			sizeList.append(len(packet))
		
		plt.plot(countList, sizeList, 'ro')
		plt.xlabel('Packet Number')
		plt.ylabel('Packet Size (bytes)')
		plt.title('Packet Size Graph')
		plt.show()
