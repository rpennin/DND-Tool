from mainWindow import Ui_MainWindow
from npcListHelper import NpcList
from spellLibraryHelper import SpellLibrary
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def openEncounter(self):
        pass

    def openPartyManager(self):
        pass
    
    def openPCList(self):
        pass
    
    def openNPCList(self):
        self.npcList = NpcList()
        self.npcList.show()

    def openSpellLibrary(self):
        self.spellLibrary = SpellLibrary()
        self.spellLibrary.show()