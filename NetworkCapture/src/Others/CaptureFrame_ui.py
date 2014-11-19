#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: CaptureFrame_ui                                                        #
# Description:                                                                  #
#                                                                               #
#################################################################################

from PyQt4.QtGui import QFrame, QDialog, QTableWidgetItem
from PyQt4.uic import loadUi
from PyQt4.QtCore import pyqtSlot
from src.Input.LiveCapture_ui import LiveCapture_ui
from src.Input.ReadFromFile_ui import ReadFromFile_ui
import webbrowser
import netifaces
import os

'''
Description:

'''
class CaptureFrame_ui(QFrame):
    '''
    Description:

    '''
    def __init__(self, liveCapture = None, readFromFile = None, parent = None):
        super(CaptureFrame_ui, self).__init__(parent)
        self.parent = parent
        self.Ui = loadUi(os.path.dirname(os.path.realpath(__file__)) + '/CaptureFrame.ui', self)

        self.Ui.buttonInterfaceList.clicked.connect(self.buttonInterfaceListClicked)
        self.Ui.buttonStartCapture.clicked.connect(liveCapture.triggerStart)
        self.Ui.buttonFileOpen.clicked.connect(readFromFile.triggerOpen)
        self.Ui.buttonSampleFiles.clicked.connect(self.buttonSampleFilesClicked)
        self.Ui.buttonProjectPage.clicked.connect(self.buttonProjectPageClicked)
        self.Ui.buttonHowTo.clicked.connect(self.buttonHowToClicked)

        parent.AddTab(self, "Main Page")

    '''
    Description:

    '''
    @pyqtSlot()
    def buttonInterfaceListClicked(self):
        obj = QDialog()
        objUi = loadUi(os.path.dirname(os.path.realpath(__file__)) + '/InterfaceSelectionDialog.ui', obj)
        count = 0
        for i in netifaces.interfaces():
            objUi.tableWidgetInterface.insertRow(count)
            objUi.tableWidgetInterface.setItem(count, 0, QTableWidgetItem(i))
            count = count + 1
        obj.exec_()

    '''
    Description:

    '''
    @pyqtSlot()
    def buttonSampleFilesClicked(self):
        print "Sample Files"

    '''
    Description:

    '''
    @pyqtSlot()
    def buttonProjectPageClicked(self):
        url = "https://github.com/jatin3893/ScaPyQtNetworkCapture"
        webbrowser.open(url)

    '''
    Description:

    '''
    @pyqtSlot()
    def buttonHowToClicked(self):
        print "How To"