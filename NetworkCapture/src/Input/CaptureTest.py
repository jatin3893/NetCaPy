from unittest import TestCase, main

import LiveCapture, LiveCaptureThread

class TestCapture(TestCase):
	def test_StopCapture(self):
		capture = LiveCapture()
		capture.startLiveCapture()
		
		packet1 = IP(dst="10.4.12.91")/ICMP()/"HelloWorld"
		packet2 = IP(dst="10.1.99.2")/TCP(dport=23)
		packets = [packet1, packet2]
		for packet in packets
			send(packet)
		
		capture.stopLiveCapture()
		assertEquals(packets, capture.packetList)
		
		self.assertRaises(Exception, send, packet1)
if __name__ == '__main__':
	main()