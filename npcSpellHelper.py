from dbUtil import *
from PyQt5 import QtCore, QtGui, QtWidgets
from npcSpell import Ui_npcSpell

class NpcSpell(QtWidgets.QDialog, Ui_npcSpell):
    def __init__(self, *args, obj=None, **kwargs):
        super(NpcSpell, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.currentLibraryKey = None
        self.currentNpcSpellKey = None
        self.spellLibraryTableWidget.setColumnHidden(0, True)
        self.npcSpellTableWidget.setColumnHidden(0, True)
        self.populateLibraryTable()
        self.populateNpcSpellTable()
    
    def populateLibraryTable(self):
        librarySpellList = select_all_library_spells()
        self.spellLibraryTableWidget.setRowCount = 0
        self.spellLibraryTableWidget.setColumnHidden(0, False)
        for spell in librarySpellList:
            numRows = self.spellLibraryTableWidget.rowCount()
            self.spellLibraryTableWidget.insertRow(numRows)
            self.spellLibraryTableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(spell.pk)))
            self.spellLibraryTableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(spell.name)))
            self.spellLibraryTableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(spell.school)))
            self.spellLibraryTableWidget.setItem(numRows, 3, QtWidgets.QTableWidgetItem(str(spell.level)))
        self.spellLibraryTableWidget.setColumnHidden(0, True)

    def populateNpcSpellTable(self):
        spellList = get_spells_by_npc(self.parent().currentPk)
        self.npcSpellTableWidget.setRowCount = 0
        self.npcSpellTableWidget.setColumnHidden(0, False)
        for spell in spellList:
            print(spell.pk)
            print(spell.name)
            numRows = self.npcSpellTableWidget.rowCount()
            self.npcSpellTableWidget.insertRow(numRows)
            self.npcSpellTableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(spell.pk)))
            self.npcSpellTableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(spell.name)))
        self.npcSpellTableWidget.setColumnHidden(0, True)

    def addSpell(self):
        pass

    def removeSpell(self):
        pass

    def updateLibraryChoice(self, row, column):
        pass
        # self.libraryTableWidget.setColumnHidden(0, False)
        # item = self.libraryTableWidget.item(row, 0)
        # self.currentPk = item.text()
        # self.libraryTableWidget.setColumnHidden(0, True)
        # self.populateFields(select_npc_by_pk(self.currentPk))

    def updateNpcSpellChoice(self, row, column):
        pass
            # self.libraryTableWidget.setColumnHidden(0, False)
            # item = self.libraryTableWidget.item(row, 0)
            # self.currentPk = item.text()
            # self.libraryTableWidget.setColumnHidden(0, True)
            # self.populateFields(select_npc_by_pk(self.currentPk))