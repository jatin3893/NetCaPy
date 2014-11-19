#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ReadFromFile_test                                                     #
# Description:                                                                  #
# Test file for testing the ReadFromFile Module                                 #
#                                                                               #
#################################################################################

from unittest import TestCase, main
from ReadFromFile import ReadFromFile
from scapy.all import *

'''
Description:

'''
class ReadFromFileTest(TestCase):
    
    '''
    Test 1:
    Read using the ReadFromFile module and then using the Scapy Read module.
    Compare the obtained result to verify
    '''
    def test_EmptyFile(self):
        x = ReadFromFile()
        x.setFilename('sample.pcap')
        
        y = rdpcap('sample.pcap')
        x1 = x.readPackets()

        for i in range (0 , y.__len__() - 1) :
            self.assertEqual(x1[i], y[i])

if __name__ == '__main__':
    main()