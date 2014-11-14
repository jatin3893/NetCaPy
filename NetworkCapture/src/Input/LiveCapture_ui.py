from LiveCapture import LiveCapture
from src.Output.PacketData_ui import PacketData_ui
from PyQt4.QtGui import QIcon, QPixmap, QToolButton, QAction, QDialog, QTableWidgetItem
from PyQt4.QtCore import QSize, QObject
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi
import threading
import netifaces

class LiveCapture_ui(QObject):
    def __init__(self, parent = None):
        super(LiveCapture_ui, self).__init__(parent)
        self.parent = parent
        self.initUi()

        self.liveCapture = None
        self.packetDataUi = None

    def initUi(self):
        startPixmap = QPixmap("icons/Start.png")
        stopPixmap = QPixmap("icons/Stop.png")

        startIcon = QIcon(startPixmap)
        stopIcon = QIcon(stopPixmap)

        self.startToolButton = QToolButton(self.parent)
        self.stopToolButton = QToolButton(self.parent)

        self.startToolButton.setIcon(startIcon)
        self.stopToolButton.setIcon(stopIcon)

        self.startToolButton.setIconSize(QSize(32, 32))
        self.stopToolButton.setIconSize(QSize(32, 32))

        self.startToolButton.clicked.connect(self.startToolButtonClicked)
        self.stopToolButton.clicked.connect(self.stopToolButtonClicked)

        self.startAction = QAction("Start Live Capturing", self.parent)
        self.startAction.triggered.connect(self.startToolButtonClicked)

        self.stopAction = QAction("Stop Live Capture", self.parent)
        self.stopAction.triggered.connect(self.stopToolButtonClicked)

        self.startToolButton.setEnabled(True)
        self.stopToolButton.setDisabled(True)
        self.startAction.setEnabled(True)
        self.stopAction.setDisabled(True)

        menuCapture = self.parent.GetMenu("Capture")
        if menuCapture != None:
            menuCapture.addAction(self.startAction)
            menuCapture.addAction(self.stopAction)
        menuCapture.addSeparator()

        toolBarCapture = self.parent.GetToolBar("Capture")
        if toolBarCapture != None:
            toolBarCapture.addWidget(self.startToolButton)
            toolBarCapture.addWidget(self.stopToolButton)

    @pyqtSlot()
    def startToolButtonClicked(self):
        self.liveCapture = LiveCapture()
        iface = InterfaceSelection(self.parent)
        ifaceName = iface.GetInterface()
        if ifaceName == None:
            return
        self.liveCapture.setInterface(ifaceName)

        retVal = self.liveCapture.startLiveCapture()
        if retVal != -1:
            self.startToolButton.setDisabled(True)
            self.stopToolButton.setEnabled(True)
            self.startAction.setDisabled(True)
            self.stopAction.setEnabled(True)
            self.packetDataUi = PacketData_ui(self.parent)
            getPacketThread = GetPacketThread(self.liveCapture, self.packetDataUi)


    @pyqtSlot()
    def stopToolButtonClicked(self):
        self.startToolButton.setEnabled(True)
        self.stopToolButton.setDisabled(True)
        self.startAction.setEnabled(True)
        self.stopAction.setDisabled(True)
        self.liveCapture.stopLiveCapture()

    def triggerStart(self):
        self.startAction.trigger()

    def triggerStop(self):
        self.stopAction.trigger()
        
class GetPacketThread(threading.Thread):
    def __init__(self, liveCaptureObj, packetDataUiObj):
        threading.Thread.__init__(self)
        self.stop = threading.Event()
        self.liveCaptureObj = liveCaptureObj
        self.packetDataUiObj = packetDataUiObj
        self.start()

    def run(self):
        while True:
            if self.liveCaptureObj.liveCaptureThread.flag == True and not self.liveCaptureObj.packetBuffer:
                break
            else:
                packet = self.liveCaptureObj.getPacket()
                if packet != None:
                    self.packetDataUiObj.AddPacket(packet)
        

class InterfaceSelection(QDialog):
    def __init__(self, parent = None):
        super(InterfaceSelection, self).__init__(parent)
        self.Ui = loadUi('ui/Input/InterfaceSelectionDialog.ui', self)
        self.loadInterfaces()

    def loadInterfaces(self):
        count = 0
        for i in netifaces.interfaces():
            self.Ui.tableWidgetInterface.insertRow(count)
            self.Ui.tableWidgetInterface.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1

    def GetInterface(self):
        retVal = self.exec_()
        if retVal == QDialog.Rejected:
                return None
        x = self.Ui.tableWidgetInterface.currentRow()
        return str(self.Ui.tableWidgetInterface.item(x, 0).text())