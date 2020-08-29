from dbUtil import *
from PyQt5 import QtCore, QtGui, QtWidgets
from spellLibrary import Ui_spellLibrary
from npc import *
from fractions import Fraction

class SpellLibrary(QtWidgets.QWidget, Ui_spellLibrary):
    def __init__(self, *args, obj=None, **kwargs):
        super(SpellLibrary, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.tableWidget.hideColumn(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.populateTable()
        self.currentPk = None

    def populateTable(self):
        spellList = select_all_library_spells()
        self.tableWidget.setRowCount(0)
        for spell in spellList:
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(spell.pk)))
            self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(spell.name)))

    def newSpell(self):
        self.nameLineEdit.setText("")
        self.descriptionTextEdit.setText("")
        self.higherLevelTextEdit.setText("")
        self.levelComboBox.setCurrentIndex(0)
        self.schoolComboBox.setCurrentIndex(0)
        self.castingTimeLineEdit.setText("")
        self.rangeLineEdit.setText("")
        self.vCheckBox.setChecked(False)
        self.sCheckBox.setChecked(False)
        self.mCheckBox.setChecked(False)
        self.materialTextEdit.setText("")
        self.ritualCheckBox.setChecked(False)
        self.concentrationCheckBox.setChecked(False)
        self.durationLineEdit.setText("")
        self.bardCheckBox.setChecked(False)
        self.clericCheckBox.setChecked(False)
        self.druidCheckBox.setChecked(False)
        self.paladinCheckBox.setChecked(False)
        self.rangerCheckBox.setChecked(False)
        self.sorcererCheckBox.setChecked(False)
        self.warlockCheckBox.setChecked(False)
        self.wizardCheckBox.setChecked(False)
        self.currentPk = None

    def saveSpell(self):
        if self.currentPk:
            name = self.nameLineEdit.text()
            level = self.levelComboBox.currentText()
            casting_time = self.castingTimeLineEdit.text()
            spell_range = self.rangeLineEdit.text()
            duration = self.durationLineEdit.text()
            description = self.descriptionTextEdit.toPlainText()
            higher_level = self.higherLevelTextEdit.toPlainText()
            if self.ritualCheckBox.isChecked():
                ritual = 'yes'
            else:
                ritual = 'no'
            if self.concentrationCheckBox.isChecked():
                concentration = 'yes'
            else:
                concentration = 'no'
            material = self.materialTextEdit.toPlainText()
            school = self.schoolComboBox.currentText()
            component_string = ""
            if self.vCheckBox.isChecked():
                component_string += "V,"
            if self.sCheckBox.isChecked():
                component_string += "S,"
            if self.mCheckBox.isChecked():
                component_string += "M"
            class_string = ""
            if self.bardCheckBox.isChecked():
                class_string += "bard,"
            if self.clericCheckBox.isChecked():
                class_string += "cleric,"
            if self.druidCheckBox.isChecked():
                class_string += "druid,"
            if self.paladinCheckBox.isChecked():
                class_string += "paladin,"
            if self.rangerCheckBox.isChecked():
                class_string += "ranger,"
            if self.sorcererCheckBox.isChecked():
                class_string += "sorcerer,"
            if self.warlockCheckBox.isChecked():
                class_string += "warlock,"
            if self.wizardCheckBox.isChecked():
                class_string += "wizard"
            
            update_spell_by_pk((name, level, casting_time, spell_range, component_string, duration, description, higher_level, ritual, concentration, school, material, class_string, self.currentPk))
            self.populateTable()
        else:
            self.saveAsNewSpell()

    def saveAsNewSpell(self):
        name = self.nameLineEdit.text()
        level = self.levelComboBox.currentText()
        casting_time = self.castingTimeLineEdit.text()
        spell_range = self.rangeLineEdit.text()
        duration = self.durationLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()
        higher_level = self.higherLevelTextEdit.toPlainText()
        if self.ritualCheckBox.isChecked():
            ritual = 'yes'
        else:
            ritual = 'no'
        if self.concentrationCheckBox.isChecked():
            concentration = 'yes'
        else:
            concentration = 'no'
        material = self.materialTextEdit.toPlainText()
        school = self.schoolComboBox.currentText()
        component_string = ""
        if self.vCheckBox.isChecked():
            component_string += "V,"
        if self.sCheckBox.isChecked():
            component_string += "S,"
        if self.mCheckBox.isChecked():
            component_string += "M"
        class_string = ""
        if self.bardCheckBox.isChecked():
            class_string += "bard,"
        if self.clericCheckBox.isChecked():
            class_string += "cleric,"
        if self.druidCheckBox.isChecked():
            class_string += "druid,"
        if self.paladinCheckBox.isChecked():
            class_string += "paladin,"
        if self.rangerCheckBox.isChecked():
            class_string += "ranger,"
        if self.sorcererCheckBox.isChecked():
            class_string += "sorcerer,"
        if self.warlockCheckBox.isChecked():
            class_string += "warlock,"
        if self.wizardCheckBox.isChecked():
            class_string += "wizard"
        insert_spell((name, level, casting_time, spell_range, component_string, duration, description, higher_level, ritual, concentration, school, material, class_string))
        self.populateTable()

    def deleteSpell(self):
        if self.currentPk:
            delete_spell_by_pk(self.currentPk)
            self.populateTable()
            self.newSpell()
        else:
            self.newSpell()

    def updateFromClick(self, row, column):
        self.tableWidget.setColumnHidden(0, False)
        item = self.tableWidget.item(row, 0)
        self.currentPk = item.text()
        self.tableWidget.setColumnHidden(0, True)
        self.populateFields(select_spell_by_pk(self.currentPk))

    def populateFields(self, selectedSpell):
        self.nameLineEdit.setText(str(selectedSpell.name))
        self.descriptionTextEdit.setText(str(selectedSpell.description))
        self.higherLevelTextEdit.setText(str(selectedSpell.higherLevel))
        comboIndex = self.levelComboBox.findText(str(selectedSpell.level).capitalize())
        self.levelComboBox.setCurrentIndex(comboIndex)
        comboIndex = self.schoolComboBox.findText(str(selectedSpell.school).capitalize())
        self.schoolComboBox.setCurrentIndex(comboIndex)
        self.castingTimeLineEdit.setText(str(selectedSpell.castingTime))
        self.rangeLineEdit.setText(str(selectedSpell.range))
        selectedSpell.components = selectedSpell.components.replace(" ", "").upper().split(',')
        if 'V' in selectedSpell.components:
            self.vCheckBox.setChecked(True)
        else:
            self.vCheckBox.setChecked(False)
        if 'S' in selectedSpell.components:
            self.sCheckBox.setChecked(True)
        else:
            self.sCheckBox.setChecked(False)
        if 'M' in selectedSpell.components:
            self.mCheckBox.setChecked(True)
        else:
            self.mCheckBox.setChecked(False)
        self.materialTextEdit.setText(str(selectedSpell.material))
        if (selectedSpell.ritual.upper() == 'YES'):
            self.ritualCheckBox.setChecked(True)
        else:
            self.ritualCheckBox.setChecked(False)
        if (selectedSpell.concentration.upper() == 'YES'):
            self.concentrationCheckBox.setChecked(True)
        else:
            self.concentrationCheckBox.setChecked(False)
        self.durationLineEdit.setText(str(selectedSpell.duration))
        selectedSpell.spellClass = selectedSpell.spellClass.replace(" ", "").lower().split(',')
        if 'bard' in selectedSpell.spellClass:
            self.bardCheckBox.setChecked(True)
        else:
            self.bardCheckBox.setChecked(False)
        if 'cleric' in selectedSpell.spellClass:
            self.clericCheckBox.setChecked(True)
        else:
            self.clericCheckBox.setChecked(False)
        if 'paladin' in selectedSpell.spellClass:
            self.paladinCheckBox.setChecked(True)
        else:
            self.paladinCheckBox.setChecked(False)
        if 'ranger' in selectedSpell.spellClass:
            self.rangerCheckBox.setChecked(True)
        else:
            self.rangerCheckBox.setChecked(False)
        if 'sorcerer' in selectedSpell.spellClass:
            self.sorcererCheckBox.setChecked(True)
        else:
            self.sorcererCheckBox.setChecked(False)
        if 'warlock' in selectedSpell.spellClass:
            self.warlockCheckBox.setChecked(True)
        else:
            self.warlockCheckBox.setChecked(False)
        if 'druid' in selectedSpell.spellClass:
            self.druidCheckBox.setChecked(True)
        else:
            self.druidCheckBox.setChecked(False)
        if 'wizard' in selectedSpell.spellClass:
            self.wizardCheckBox.setChecked(True)
        else:
            self.wizardCheckBox.setChecked(False)