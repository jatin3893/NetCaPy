#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: BPF_test                                                              #
# Description:                                                                  #
# Test file for testing BPF Modules                                             #
#                                                                               #
#################################################################################

from unittest import TestCase, main
from BPF import BPF
from scapy.all import *

'''
Description:
Testing BPF Module
'''
class BPFTest(TestCase):
    '''
    Test:

    '''
    def test_EmptyFilter(self):
        x = BPF()
        x.setFilterExpression('')

        packet1 = IP(dst="10.4.12.91")/ICMP()/"HelloWorld"
        packet2 = IP(dst="10.4.12.91")/TCP(dport=23)
        packets = [packet1, packet2, packet1, packet2, packet1, packet2, packet1, packet2, packet1, packet2]

        x.setOriginalPacketList(packets)
        x.filterPacketList()
        y = x.getFilteredPacketList()

        for (packetA, packetB) in zip(packets, y):
            self.assertEqual(hexdump(packetA), hexdump(packetB) )

    '''
    Test:

    '''
    def test_DestExprFilter(self):
        x = BPF()
        packet3 = IP(dst="10.4.12.91")/TCP(dport=23)/"HelloWorld"
        packet4 = IP(dst="10.4.12.92")/TCP(dport=23)/"HelloWorld"
        packets2 = [packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4]

        x.setOriginalPacketList(packets2)
        x.setFilterExpression('dst host "10.4.12.91"')
        y = x.getFilteredPacketList()

        for  packetB in zip (y):
            self.assertEqual(hexdump(packet3), hexdump(packetB) )   

    '''
    Test:

    '''
    def test_PortExprFilter(self):
        x = BPF()
        packet3 = IP(dst="10.4.12.91")/TCP(dport=23)/"HelloWorld"
        packet4 = IP(dst="10.4.12.91")/TCP(dport=24)/"HelloWorld"
        packets2 = [packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4]

        x.setOriginalPacketList(packets2)
        x.setFilterExpression('dst port 23')
        y = x.getFilteredPacketList()

        for  packetB in zip (y):
            self.assertEqual(hexdump(packet3), hexdump(packetB) )   

    '''
    Test:

    '''
    def test_ComboExprFilter(self):
        x = BPF()
    

        packet3 = IP(dst="10.4.12.91")/TCP(dport=23)/"HelloWorld"
        packet4 = IP(dst="10.4.12.92")/TCP(dport=24)/"HelloWorld"
        packets2 = [packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4]

        x.setOriginalPacketList(packets2)
        x.setFilterExpression('dst port 23 and dst host "10.4.12.92"')
        y = x.getFilteredPacketList()

        self.assertEqual(y,[])

    '''
    Test:

    '''
    def test_ProtoExprFilter(self):
        x = BPF()
        packet3 = IP(dst="10.4.12.91")/TCP(dport=23)/"HelloWorld"
        packet4 = IP(dst="10.4.12.91")/ICMP()/"HelloWorld"
        packets2 = [packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4, packet3, packet4]

        x.setOriginalPacketList(packets2)
        x.setFilterExpression('proto ICMP')
        y = x.getFilteredPacketList()

        for  packetB in zip (y):
            self.assertEqual(hexdump(packet4), hexdump(packetB) )

if __name__ == '__main__':
    main()

