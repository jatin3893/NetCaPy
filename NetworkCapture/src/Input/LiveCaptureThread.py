#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: LiveCaptureThread                                                     #
# Description:                                                                  #
# Python threading module based Thread to capture packets from the              #
# specified interface and store it in appropriate locations                     #
#                                                                               #
#################################################################################

import threading
from scapy.all import *

'''
Description:

'''
class LiveCaptureThread(threading.Thread):
    def __init__(self, liveCaptureObj):
        threading.Thread.__init__(self)
        self.liveCaptureObj = liveCaptureObj
        self.flag = False

    '''
    Description:
    Start sniffing and wait until it is stopped by an appropriate exception
    '''
    def run(self):
        try:
            sniff(prn=self.recv, iface=self.liveCaptureObj.interface)
        except Exception:
            pass

    '''
    Description:
    Store the captured packet in appropriate buffers
    Stop capturing if appropriate flag is set and raise an exception 
    to end thread execution
    '''
    def recv(self, packet):
        if self.flag:
            raise Exception('Stop Packet Capturing')
        self.liveCaptureObj.packetList.append(packet)
        self.liveCaptureObj.packetBuffer.append(packet)
