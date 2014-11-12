from unittest import TestCase, main
from ReadFromFile import ReadFromFile
from scapy.all import *

class ReadFromFileTest(TestCase):
	
	def test_EmptyFile(self):
		x = ReadFromFile()
		x.setFilename('sample.pcap')
		
		y = rdpcap('sample.pcap')
		x1 = x.readPackets()

		for i in range (0 , y.__len__() - 1) :
			self.assertEqual(x1[i], y[i])

if __name__ == '__main__':
	main()