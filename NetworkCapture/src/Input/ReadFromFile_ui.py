#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: ReadFromFile_ui                                                       #
# Description:                                                                  #
# PyQt based GUI wrapper on top of the ReadFromFile Module to implement the     #
# Open/Save pcap file actions                                                   #
#                                                                               #
#################################################################################

from PyQt4.QtGui import QIcon, QPixmap, QToolButton, QPushButton, QAction, QFileDialog
from PyQt4.QtCore import pyqtSlot, QObject, QSize
from ReadFromFile import ReadFromFile
from src.Output.PacketData_ui import PacketData_ui
import os

'''
'''
class ReadFromFile_ui(QObject):
    def __init__(self, parent = None):
        super(ReadFromFile_ui, self).__init__(parent)
        self.parent = parent
        self.initUi()
        self.packetDataUi = None

    '''
    Description:
    Initialise the Icons and Menu Items to add to the Interface
    '''
    def initUi(self):
        openPixmap = QPixmap(os.path.dirname(os.path.realpath(__file__)) + '/Open.png')
        savePixmap = QPixmap(os.path.dirname(os.path.realpath(__file__)) + '/Save.png')

        openIcon = QIcon(openPixmap)
        saveIcon = QIcon(savePixmap)

        self.openToolButton = QToolButton(self.parent)
        self.saveToolButton = QToolButton(self.parent)

        self.openToolButton.setIcon(openIcon)
        self.saveToolButton.setIcon(saveIcon)

        self.openToolButton.setIconSize(QSize(32, 32))
        self.saveToolButton.setIconSize(QSize(32, 32))

        self.openToolButton.clicked.connect(self.openToolButtonClicked)
        self.saveToolButton.clicked.connect(self.saveToolButtonClicked)

        self.openAction = QAction("Open", self.parent)
        self.openAction.triggered.connect(self.openToolButtonClicked)

        self.saveAction = QAction("Save", self.parent)
        self.saveAction.triggered.connect(self.saveToolButtonClicked)

        menuCapture = self.parent.GetMenu("File")
        if menuCapture != None:
            menuCapture.addAction(self.openAction)
            menuCapture.addAction(self.saveAction)
        menuCapture.addSeparator()

        toolBarCapture = self.parent.GetToolBar("File")
        if toolBarCapture != None:
            toolBarCapture.addWidget(self.openToolButton)
            toolBarCapture.addWidget(self.saveToolButton)

    '''
    Description:
    On clicking Open Button/Action:
    Obtain file path and read the pcap file into a list
    Send the packets read by the reader to be displayed using PacketData_Ui
    '''
    @pyqtSlot()
    def openToolButtonClicked(self):
        filename = QFileDialog.getOpenFileName(self.parent, "Load Pcap File", "/home/", "*.pcap")
        if str(filename) != "":
            readFromFile = ReadFromFile()
            readFromFile.setFilename(str(filename))
            packets = readFromFile.readPackets()
            self.packetDataUi = PacketData_ui(self.parent)
            for packet in packets:
                self.packetDataUi.AddPacket(packet)


    '''
    Description:
    On clicking Save Button/Action:
    Check if current tab is a PacketDataUi. If yes, then get path of the destination file and
    dump the list in pcap format at the specified destination
    '''
    @pyqtSlot()
    def saveToolButtonClicked(self):            
        widget = self.parent.GetCurrentTab()
        if widget != None and isinstance(widget, PacketData_ui):
            filename = QFileDialog.getSaveFileName(self.parent, "Save Pcap File", "/home/", "*.pcap")
            strFilename = str(filename)
            if not strFilename.endswith(".pcap"):
                strFilename = strFilename + ".pcap"
            ReadFromFile().saveFile(strFilename, widget.packetList)

    '''
    Description:
    Wrapper to trigger the Open File action
    '''
    @pyqtSlot()
    def triggerOpen(self):
        self.openAction.trigger()

    '''
    Description:
    Wrapper to trigger the Save file action
    '''
    @pyqtSlot()
    def triggerSave(self):
        self.saveAction.trigger()