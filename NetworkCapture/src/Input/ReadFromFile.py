from scapy.all import *

class ReadFromFile:
	def __init__():
		self.filename = ''

	def readPackets(self):
		return rdpcap(self.filename)

	def getFilename(self):
		return self.filename

	def setFilename(self, filename):
		self.filename = filename