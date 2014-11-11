from scapy.all import *

class ReadFromFile:
	def __init__(filename):
		self.filename = filename

	def readPackets():
		return rdpcap(self.filename)