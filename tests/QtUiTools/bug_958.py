import unittest
from PySide2 import QtWidgets, QtUiTools
from helper import adjust_filename
from helper import TimedQApplication

class Gui_Qt(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Gui_Qt, self).__init__(parent)

        lLoader = QtUiTools.QUiLoader()

        # this used to cause a segfault because the old inject code used to destroy the parent layout
        self._cw = lLoader.load(adjust_filename('bug_958.ui', __file__),  self)

        self.setCentralWidget(self._cw)

class BugTest(TimedQApplication):
    def testCase(self):
        lMain = Gui_Qt()
        lMain.show()
        self.app.exec_()

if __name__ == "__main__":
    unittest.main()
