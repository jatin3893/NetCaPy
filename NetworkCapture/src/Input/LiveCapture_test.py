from unittest import TestCase, main
from scapy.all import *
from LiveCapture import LiveCapture
from LiveCaptureThread import LiveCaptureThread

class TestCapture(TestCase):
    def test_StopCapture(self):
        capture = LiveCapture()
        capture.startLiveCapture()
        
        packet1 = IP(dst="10.4.12.91")/ICMP()/"HelloWorld"
        packet2 = IP(dst="10.4.12.91")/TCP(dport=23)

        packets = [packet1, packet2, packet1, packet2, packet1, packet2, packet1, packet2, packet1, packet2]
        for packet in packets:
            send(packet, iface='lo')
        
        capture.stopLiveCapture()
            
        for (packetA, packetB) in zip(capture.packetList, packets):
            self.assertEqual(hexdump(packetA[IP]), hexdump(packetB[IP]) )
        
if __name__ == '__main__':
    main()