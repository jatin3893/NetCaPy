from Custom import Custom
from PyQt4.QtGui import QFrame
from PyQt4.uic import loadUi

class Custom_ui():
    def __init__(self):
        print "Custom Filter Base Class"
        self.frame = CustomFrame()

class CustomFrame(QFrame):
    def __init__(self, parent = None):
        super(CustomFrame, self).__init__(parent)
        self.Ui = loadUi('ui/Filter/Custom_ui.ui', self)