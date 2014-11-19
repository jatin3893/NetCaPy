#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: LiveCapture                                                           #
# Description:                                                                  #
# This module controls the packet capturing thread from the                     #
# selected interface                                                            #
#                                                                               #
#################################################################################

from LiveCaptureThread import LiveCaptureThread
import os, sys

'''
Description:

'''
class LiveCapture:
    def __init__(self):
        self.packetBuffer = []
        self.packetList = []
        self.liveCaptureThread = LiveCaptureThread(self)
        self.interface = 'eth0'

    def getPacketList(self):
        return self.packetList

    '''
    Description:
    Dequeue a packet from the non empty buffer of captured packets
    '''
    def getPacket(self):
        if not self.packetBuffer:
            return None
        else:
            return self.packetBuffer.pop(0)

    '''
    Description:
    Check if user has appropriate privilege levels to live LiveCapture
    If yes, then start capturing in a separate thread
    '''
    def startLiveCapture(self):
        # geteuid() Might have portability issues
        if os.geteuid() != 0:
            print >> sys.stderr, "Failed to initialise the Application. You need root permissions to do this.!"
            return -1
        self.liveCaptureThread.start()

    '''
    Description:
    Notify the capturing thread to stop capturing
    '''
    def stopLiveCapture(self):
        self.liveCaptureThread.flag = True

    '''
    Description:
    Get/Set the name of the interface for Capturing
    '''
    def getInterface(self):
        return self.interface
    def setInterface(self, interface):
        self.interface = interface
