from scapy.all import *

class ReadFromFile:
	def __init__(self):
		self.filename = ''

	def readPackets(self):
		return rdpcap(self.filename)

	def getFilename(self):
		return self.filename

	def setFilename(self, filename):
		self.filename = filename

	def saveFile(self, filename, packetList):
		wrpcap(filename, packetList)