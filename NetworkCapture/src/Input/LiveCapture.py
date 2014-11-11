from LiveCaptureThread import LiveCaptureThread

class LiveCapture:
	def __init__(self):
		self.packetBuffer = []
		self.packetList = []

	def getPacketList(self):
		return self.packetList

	def getPacketBuffer(self):
		return self.packetBuffer

	def startLiveCapture(self):
		self.liveCaptureThread = LiveCaptureThread(self)
		self.liveCaptureThread.start()