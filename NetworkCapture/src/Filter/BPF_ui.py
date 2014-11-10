from BPF import BPF
from PyQt4.QtGui import QFrame
from PyQt4.uic import loadUi

class BPF_ui():
    def __init__(self):
        print "BPF Filter Base Class"
        self.frame = BPFFrame()

class BPFFrame(QFrame):
    def __init__(self, parent = None):
        super(BPFFrame, self).__init__(parent)
        self.Ui = loadUi('ui/Filter/BPF_ui.ui', self)