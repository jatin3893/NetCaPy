#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: PacketSizeGraph                                                       #
# Description:                                                                  #
# Use matplotlib to display a graphy of Packet vs Packet Size                   #
#                                                                               #
#################################################################################

from Analysis import Analysis
import matplotlib.pyplot as plt

'''
Description:
Generate Packet vs Packet Size graph
'''
class PacketSizeGraph(Analysis):
    def __init__(self):
        Analysis.__init__(self)
        self.packetList = []

    '''
    Description:
    Set packet list to be analysed for drawing the graph
    '''
    def setPacketList(self, packetList):
        self.packetList = packetList

    '''
    Description:
    Use matplotlib to do the corresponding Analysis
    '''
    def plotGraph(self):
        countList = []
        sizeList = []
        count = 0

        for packet in self.packetList:
            countList.append(count)
            count = count + 1
            sizeList.append(len(packet))
        
        plt.plot(countList, sizeList, 'ro')
        plt.xlabel('Packet Number')
        plt.ylabel('Packet Size (bytes)')
        plt.title('Packet Size Graph')
        plt.show()
