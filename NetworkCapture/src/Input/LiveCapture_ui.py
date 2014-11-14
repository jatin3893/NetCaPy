#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: LiveCapture_ui                                                        #
# Description:                                                                  #
# PyQt based GUI wrapper on top of the LiveCapture Module to implement the      #
# Start/Stop live capture of packets                                            #
#                                                                               #
#################################################################################

from LiveCapture import LiveCapture
from src.Output.PacketData_ui import PacketData_ui
from PyQt4.QtGui import QIcon, QPixmap, QToolButton, QAction, QDialog, QTableWidgetItem
from PyQt4.QtCore import QSize, QObject
from PyQt4.QtCore import pyqtSlot
from PyQt4.uic import loadUi
import threading
import netifaces

'''
Description:
The main wrapper over the LiveCapture module to initialise the GUI objects
and the threads for capturing data
'''
class LiveCapture_ui(QObject):
    def __init__(self, parent = None):
        super(LiveCapture_ui, self).__init__(parent)
        self.parent = parent
        self.initUi()

        self.liveCapture = None
        self.packetDataUi = None

    '''
    Description:
    Initialise the buttons and actions to control the live captring of data
    graphically.
    Add corresponding actions/tool buttons to toolbars/menubars of the mainWindow
    '''
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

        # Setup initial values for the buttons/actions
        self.startToolButton.setEnabled(True)
        self.stopToolButton.setDisabled(True)
        self.startAction.setEnabled(True)
        self.stopAction.setDisabled(True)

        # Add Actions to the Menu bar
        menuCapture = self.parent.GetMenu("Capture")
        if menuCapture != None:
            menuCapture.addAction(self.startAction)
            menuCapture.addAction(self.stopAction)
        menuCapture.addSeparator()

        # Add tool buttons to the appropriate tool bar
        toolBarCapture = self.parent.GetToolBar("Capture")
        if toolBarCapture != None:
            toolBarCapture.addWidget(self.startToolButton)
            toolBarCapture.addWidget(self.stopToolButton)

    '''
    Description:
    Obtain the interface to capture the data from.
    Check if user has appropriate privilege levels to start capturing data.
    Toggle tools in the GUI and initialise the packet capturing/display 
    process in separate threads.
    '''
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

    '''
    Description:
    Notify the capturing thread to stop and toggle the buttons in the GUI
    '''
    @pyqtSlot()
    def stopToolButtonClicked(self):
        self.startToolButton.setEnabled(True)
        self.stopToolButton.setDisabled(True)
        self.startAction.setEnabled(True)
        self.stopAction.setDisabled(True)
        self.liveCapture.stopLiveCapture()
    
    '''
    Description:
    Description:
    Wrapper to trigger the Start capturing
    '''
    def triggerStart(self):
        self.startAction.trigger()
    
    '''
    Description:
    Description:
    Wrapper to trigger the Stop capturing
    '''
    def triggerStop(self):
        self.stopAction.trigger()
    
'''
Description:
Python threading module based thread to obtain packets from the underlying 
Packet Capturing thread and display it in the GUI
'''    
class GetPacketThread(threading.Thread):
    def __init__(self, liveCaptureObj, packetDataUiObj):
        threading.Thread.__init__(self)
        self.stop = threading.Event()
        self.liveCaptureObj = liveCaptureObj
        self.packetDataUiObj = packetDataUiObj
        self.start()

    '''
    Description:
    If packet buffer is empty and flag set by Stop Action then kill thread
    Else get new packet and display it
    '''
    def run(self):
        while True:

            if self.liveCaptureObj.liveCaptureThread.flag == True and not self.liveCaptureObj.packetBuffer:
                break
            else:
                packet = self.liveCaptureObj.getPacket()
                if packet != None:
                    self.packetDataUiObj.AddPacket(packet)   

'''
Description:
A PyQt Dialog box for selection of the Network Interfaces for capturing
the packet
'''
class InterfaceSelection(QDialog):
    def __init__(self, parent = None):
        super(InterfaceSelection, self).__init__(parent)
        self.Ui = loadUi('ui/Others/InterfaceSelectionDialog.ui', self)
        self.loadInterfaces()

    '''
    Description:
    Find list of currently active interfaces on the system and add
    them to the display widget
    '''
    def loadInterfaces(self):
        count = 0
        for i in netifaces.interfaces():
            self.Ui.tableWidgetInterface.insertRow(count)
            self.Ui.tableWidgetInterface.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1

    '''
    Description:
    Get name of the currently selected interface from the dialog box
    '''
    def GetInterface(self):
        retVal = self.exec_()
        if retVal == QDialog.Rejected:
                return None
        x = self.Ui.tableWidgetInterface.currentRow()
        return str(self.Ui.tableWidgetInterface.item(x, 0).text())