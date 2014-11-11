from LiveCaptureThread import LiveCaptureThread

class LiveCapture:
	def __init__(self):
		self.packetBuffer = []
		self.packetList = []
		self.liveCaptureThread = LiveCaptureThread(self)

	def getPacketList(self):
		return self.packetList

	def getPacket(self):
		if not self.packetBuffer:
			return None
		else:
			return self.packetBuffer.pop(0)

	def startLiveCapture(self):
		self.liveCaptureThread.start()

	def stopLiveCapturing(self):
		self.liveCaptureThread.flag = True;