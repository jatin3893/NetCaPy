from PyQt4.QtGui import QIcon, QPixmap, QToolButton, QPushButton, QAction, QFileDialog
from PyQt4.QtCore import pyqtSlot, QObject, QSize
from ReadFromFile import ReadFromFile
from src.Output.PacketData_ui import PacketData_ui

class ReadFromFile_ui(QObject):
    def __init__(self, parent = None):
        super(ReadFromFile_ui, self).__init__(parent)
        self.parent = parent
        self.initUi()

        self.packetDataUi = None

    def initUi(self):
        openPixmap = QPixmap("icons/Open.png")
        savePixmap = QPixmap("icons/Save.png")

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

    @pyqtSlot()
    def openToolButtonClicked(self):
        filename = QFileDialog.getOpenFileName(self.parent, "Load Pcap File", "/home/", "*.pcap")
        readFromFile = ReadFromFile()
        readFromFile.setFilename(str(filename))
        print filename
        packets = readFromFile.readPackets()
        self.packetDataUi = PacketData_ui(self.parent)
        for packet in packets:
            self.packetDataUi.AddPacket(packet)


    @pyqtSlot()
    def saveToolButtonClicked(self):
        print QFileDialog.getSaveFileName(self.parent, "Save Pcap File", "/home/", "*.pcap")