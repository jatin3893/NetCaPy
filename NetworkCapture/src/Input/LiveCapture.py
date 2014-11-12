from LiveCaptureThread import LiveCaptureThread
import os, sys

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
        # geteuid() Might have portability issues
        if os.geteuid() != 0:
            print >> sys.stderr, "Failed to initialise the Application. You need root permissions to do this.!"
            return -1
        self.liveCaptureThread.start()

    def stopLiveCapture(self):
        self.liveCaptureThread.flag = True;
