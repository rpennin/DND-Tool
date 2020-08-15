from dbUtil import *
from PyQt5 import QtCore, QtGui, QtWidgets
from npcSpell import Ui_npcSpell

class NpcSpell(QtWidgets.QDialog, Ui_npcSpell):
    def __init__(self, *args, obj=None, **kwargs):
        super(NpcSpell, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.currentLibraryKey = None
        self.currentNpcSpellKey = None
        self.populateLibraryTable()
    
    def populateLibraryTable(self):
        librarySpellList = select_all_library_spells()
        self.spellLibraryTableWidget.setRowCount = 0
        for spell in librarySpellList:
            numRows = self.spellLibraryTableWidget.rowCount()
            self.spellLibraryTableWidget.insertRow(numRows)
            self.spellLibraryTableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(spell.name)))
            self.spellLibraryTableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(spell.school)))
            self.spellLibraryTableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(spell.level)))
            

    def addSpell(self):
        pass

    def removeSpell(self):
        pass