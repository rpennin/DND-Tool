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
        self.populateNpcSpellTable()
        self.populateLibraryTable()
    
    def populateLibraryTable(self):
        librarySpellList = select_all_library_spells()
        self.spellLibraryTableWidget.setRowCount(0)
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
        self.npcSpellTableWidget.setRowCount(0)
        self.npcSpellTableWidget.setColumnHidden(0, False)
        for spell in spellList:
            numRows = self.npcSpellTableWidget.rowCount()
            self.npcSpellTableWidget.insertRow(numRows)
            self.npcSpellTableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(spell[0])))
            self.npcSpellTableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(spell[1].name)))
        self.npcSpellTableWidget.setColumnHidden(0, True)

    def addSpell(self):
        if self.currentLibraryKey:
            insert_npc_spell((self.currentLibraryKey, self.parent().currentPk))
            self.populateNpcSpellTable()

    def removeSpell(self):
        if self.currentNpcSpellKey:
            delete_npc_spell(self.currentNpcSpellKey)
            self.populateNpcSpellTable()

    def updateLibraryChoice(self, row, column):
        self.spellLibraryTableWidget.setColumnHidden(0, False)
        item = self.spellLibraryTableWidget.item(row, 0)
        self.currentLibraryKey = item.text()
        self.spellLibraryTableWidget.setColumnHidden(0, True)
        

    def updateNpcSpellChoice(self, row, column):
        self.npcSpellTableWidget.setColumnHidden(0, False)
        item = self.npcSpellTableWidget.item(row, 0)
        self.currentNpcSpellKey = item.text()
        self.npcSpellTableWidget.setColumnHidden(0, True)