import threading
from scapy.all import *

class LiveCaptureThread(threading.Thread):
	def __init__(self, liveCaptureObj):
		threading.Thread.__init__(self)
		self.liveCaptureObj = liveCaptureObj
	
	def run(self):
		sniff(prn=self.recv)

	def recv(self, packet):
			self.liveCaptureObj.packetList.append(packet)
			self.liveCaptureObj.packetBuffer.append(packet)
			print packet.summary()