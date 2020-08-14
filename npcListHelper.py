from dbUtil import *
from PyQt5 import QtCore, QtGui, QtWidgets
from npcList import Ui_npcList
from actionsAbilitiesReactionsHelper import ActionsAbilitiesReactions
from npcSpellHelper import NpcSpell
from npc import *
from fractions import Fraction

class NpcList(QtWidgets.QWidget, Ui_npcList):
    def __init__(self, *args, obj=None, **kwargs):
        super(NpcList, self).__init__(*args, **kwargs)
        self.setupUi(self)
        sizes = ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']
        types = ['Aberration', 'Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Fiend', 'Giant', 'Humanoid', 'Monstrosity', 'Ooze', 'Plant', 'Undead']
        alignments = ['Unaligned', 'Lawful good', 'Neutral good', 'Chaotic good', 'Lawful neutral', 'Neutral', 'Chaotic neutral', 'Lawful evil', 'Neutral evil', 'Chaotic evil']
        self.npcSizeComboBox.addItems(sizes)
        self.npcTypeComboBox.addItems(types)
        self.npcAlignmentComboBox.addItems(alignments)
        self.libraryTableWidget.setColumnHidden(0, True)
        self.libraryTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.populateLibraryTable()
        self.libraryTableWidget.show()
        self.currentPk = None

    def populateLibraryTable(self):
        npcList = select_all_npcs()
        self.libraryTableWidget.setRowCount(0)
        for npc in npcList:
            numRows = self.libraryTableWidget.rowCount()
            self.libraryTableWidget.insertRow(numRows)
            self.libraryTableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(npc.pk)))
            self.libraryTableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(npc.name)))

    def createNewNpc(self):
        self.nameLineEdit.setText("")
        self.npcSizeComboBox.setCurrentIndex(0)
        self.npcTypeComboBox.setCurrentIndex(0)
        self.npcAlignmentComboBox.setCurrentIndex(0)
        self.armorClassLineEdit.setText("")
        self.armorClassDescLineEdit.setText("")
        self.hPLineEdit.setText("")
        self.hPCalcLineEdit.setText("")
        self.speedLineEdit.setText("")
        self.challengeLineEdit.setText("")
        self.xPLineEdit.setText("")
        self.languagesLineEdit.setText("")
        self.sensesLineEdit.setText("")
        self.descriptionTextEdit.setText("")
        self.damageResistanceTextEdit.setText("")
        self.acrobaticsLineEdit.setText("0")
        self.animalHandlingLineEdit.setText("0")
        self.arcanaLineEdit.setText("0")
        self.athleticsLineEdit.setText("0")
        self.deceptionLineEdit.setText("0")
        self.historyLineEdit.setText("0")
        self.insightLineEdit.setText("0")
        self.intimidationLineEdit.setText("0")
        self.investigationLineEdit.setText("0")
        self.medicineLineEdit.setText("0")
        self.natureLineEdit.setText("0")
        self.perceptionLineEdit.setText("0")
        self.performanceLineEdit.setText("0")
        self.persuasionLineEdit.setText("0")
        self.religionLineEdit.setText("0")
        self.sleightOfHandLineEdit.setText("0")
        self.stealthLineEdit.setText("0")
        self.survivalLineEdit.setText("0")
        self.npcStrLineEdit.setText("10")
        self.strSavingThrowLineEdit.setText("0")
        self.npcDexLineEdit.setText("10")
        self.dexSavingThrowLineEdit.setText("0")
        self.npcConLineEdit.setText("10")
        self.conSavingThrowLineEdit.setText("0")
        self.npcIntLineEdit.setText("10")
        self.intSavingThrowLineEdit.setText("0")
        self.npcWisLineEdit.setText("10")
        self.wisSavingThrowLineEdit.setText("0")
        self.npcChaLineEdit.setText("10")
        self.chaSavingThrowLineEdit.setText("0")
        self.npcStrLabel.setText("(+0)")
        self.npcIntLabel.setText("(+0)")
        self.npcDexLabel.setText("(+0)")
        self.npcWisLabel.setText("(+0)")
        self.npcConLabel.setText("(+0)")
        self.npcChaLabel.setText("(+0)")
        self.currentPk = None
    
    def saveNpc(self):
        if self.currentPk:
            name = self.nameLineEdit.text()
            size = self.npcSizeComboBox.currentText()
            npc_type = self.npcTypeComboBox.currentText()
            alignment = self.npcAlignmentComboBox.currentText()
            ac = self.armorClassLineEdit.text()
            ac_desc = self.armorClassDescLineEdit.text()
            hp = self.hPLineEdit.text()
            hp_calc = self.hPCalcLineEdit.text()
            speed = self.speedLineEdit.text()
            cr = self.challengeLineEdit.text()
            cr = float(sum(Fraction(s) for s in str(cr).split()))
            xp = self.xPLineEdit.text()
            languages = self.languagesLineEdit.text()
            senses = self.sensesLineEdit.text()
            description = self.descriptionTextEdit.toPlainText()
            damage_resistance = self.damageResistanceTextEdit.toPlainText()
            acrobatics = self.acrobaticsLineEdit.text()
            animal_handling = self.animalHandlingLineEdit.text()
            arcana = self.arcanaLineEdit.text()
            athletics = self.athleticsLineEdit.text()
            deception = self.deceptionLineEdit.text()
            history = self.historyLineEdit.text()
            insight = self.insightLineEdit.text()
            intimidation = self.intimidationLineEdit.text()
            investigation = self.investigationLineEdit.text()
            medicine = self.medicineLineEdit.text()
            nature = self.natureLineEdit.text()
            perception = self.perceptionLineEdit.text()
            performance = self.performanceLineEdit.text()
            persuasion = self.persuasionLineEdit.text()
            religion = self.religionLineEdit.text()
            sleight_of_hand = self.sleightOfHandLineEdit.text()
            stealth = self.stealthLineEdit.text()
            survival = self.survivalLineEdit.text()
            str_stat = self.npcStrLineEdit.text()
            str_sav = self.strSavingThrowLineEdit.text()
            dex_stat = self.npcDexLineEdit.text()
            dex_sav = self.dexSavingThrowLineEdit.text()
            con_stat = self.npcConLineEdit.text()
            con_sav = self.conSavingThrowLineEdit.text()
            int_stat = self.npcIntLineEdit.text()
            int_sav = self.intSavingThrowLineEdit.text()
            wis_stat = self.npcWisLineEdit.text()
            wis_sav = self.wisSavingThrowLineEdit.text()
            cha_stat = self.npcChaLineEdit.text()
            cha_sav = self.chaSavingThrowLineEdit.text()
            try:
                test = float(self.npcStrLineEdit.text())
                if(self.npcStrLineEdit.text() == "-"):
                    str_stat = "0"
            except:
                str_stat = "0"
            try:
                test = float(self.npcDexLineEdit.text())
                if(self.npcDexLineEdit.text() == "-"):
                    dex_stat = "0"
            except:
                int_stat = "0"
            try:
                test = float(self.npcIntLineEdit.text())
                if(self.npcIntLineEdit.text() == "-"):
                    int_stat = "0"
            except:
                dex_stat = "0"
            try:
                test = float(self.npcWisLineEdit.text())
                if(self.npcWisLineEdit.text() == "-"):
                    wis_stat = "0"
            except:
                wis_stat = "0"
            try:
                test = float(self.npcConLineEdit.text())
                if(self.npcConLineEdit.text() == "-"):
                    con_stat = "0"
            except:
                con_stat = "0"
            try:
                test = float(self.npcChaLineEdit.text())
                if(self.npcChaLineEdit.text() == "-"):
                    cha_stat = "0"
            except:
                cha_stat = "0"
            
            update_npc_by_pk((name,description,size,npc_type,alignment,ac,ac_desc,hp,hp_calc,speed,str_stat,str_sav,dex_stat,dex_sav,con_stat,con_sav,int_stat,int_sav,wis_stat,wis_sav,cha_stat,cha_sav,damage_resistance,acrobatics,animal_handling,arcana,athletics,deception,history,insight,intimidation,investigation,medicine,nature,perception,performance,persuasion,religion,sleight_of_hand,stealth,survival,senses,languages,cr,xp,self.currentPk))
            self.populateLibraryTable()
        else:
            self.saveAsNewNpc()
    
    def saveAsNewNpc(self):
        name = self.nameLineEdit.text()
        size = self.npcSizeComboBox.currentText()
        npc_type = self.npcTypeComboBox.currentText()
        alignment = self.npcAlignmentComboBox.currentText()
        ac = self.armorClassLineEdit.text()
        ac_desc = self.armorClassDescLineEdit.text()
        hp = self.hPLineEdit.text()
        hp_calc = self.hPCalcLineEdit.text()
        speed = self.speedLineEdit.text()
        cr = self.challengeLineEdit.text()
        cr = float(sum(Fraction(s) for s in str(cr).split()))
        xp = self.xPLineEdit.text()
        languages = self.languagesLineEdit.text()
        senses = self.sensesLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()
        damage_resistance = self.damageResistanceTextEdit.toPlainText()
        acrobatics = self.acrobaticsLineEdit.text()
        animal_handling = self.animalHandlingLineEdit.text()
        arcana = self.arcanaLineEdit.text()
        athletics = self.athleticsLineEdit.text()
        deception = self.deceptionLineEdit.text()
        history = self.historyLineEdit.text()
        insight = self.insightLineEdit.text()
        intimidation = self.intimidationLineEdit.text()
        investigation = self.investigationLineEdit.text()
        medicine = self.medicineLineEdit.text()
        nature = self.natureLineEdit.text()
        perception = self.perceptionLineEdit.text()
        performance = self.performanceLineEdit.text()
        persuasion = self.persuasionLineEdit.text()
        religion = self.religionLineEdit.text()
        sleight_of_hand = self.sleightOfHandLineEdit.text()
        stealth = self.stealthLineEdit.text()
        survival = self.survivalLineEdit.text()
        str_stat = self.npcStrLineEdit.text()
        str_sav = self.strSavingThrowLineEdit.text()
        dex_stat = self.npcDexLineEdit.text()
        dex_sav = self.dexSavingThrowLineEdit.text()
        con_stat = self.npcConLineEdit.text()
        con_sav = self.conSavingThrowLineEdit.text()
        int_stat = self.npcIntLineEdit.text()
        int_sav = self.intSavingThrowLineEdit.text()
        wis_stat = self.npcWisLineEdit.text()
        wis_sav = self.wisSavingThrowLineEdit.text()
        cha_stat = self.npcChaLineEdit.text()
        cha_sav = self.chaSavingThrowLineEdit.text()
        try:
            test = float(self.npcStrLineEdit.text())
            if(self.npcStrLineEdit.text() == "-"):
                str_stat = "0"
        except:
            str_stat = "0"
        try:
            test = float(self.npcDexLineEdit.text())
            if(self.npcDexLineEdit.text() == "-"):
                dex_stat = "0"
        except:
            int_stat = "0"
        try:
            test = float(self.npcIntLineEdit.text())
            if(self.npcIntLineEdit.text() == "-"):
                int_stat = "0"
        except:
            dex_stat = "0"
        try:
            test = float(self.npcWisLineEdit.text())
            if(self.npcWisLineEdit.text() == "-"):
                wis_stat = "0"
        except:
            wis_stat = "0"
        try:
            test = float(self.npcConLineEdit.text())
            if(self.npcConLineEdit.text() == "-"):
                con_stat = "0"
        except:
            con_stat = "0"
        try:
            test = float(self.npcChaLineEdit.text())
            if(self.npcChaLineEdit.text() == "-"):
                cha_stat = "0"
        except:
            cha_stat = "0"
        insert_npc((name,description,size,npc_type,alignment,ac,ac_desc,hp,hp_calc,speed,str_stat,str_sav,dex_stat,dex_sav,con_stat,con_sav,int_stat,int_sav,wis_stat,wis_sav,cha_stat,cha_sav,damage_resistance,acrobatics,animal_handling,arcana,athletics,deception,history,insight,intimidation,investigation,medicine,nature,perception,performance,persuasion,religion,sleight_of_hand,stealth,survival,senses,languages,cr,xp))
        self.populateLibraryTable()

    def deleteNpc(self):
        if self.currentPk:
            delete_npc_by_pk(self.currentPk)
            self.populateLibraryTable()
            self.createNewNpc()
        else:
            self.createNewNpc()

    def openNpcActionsList(self):
        if (self.currentPk == None):
            QtWidgets.QMessageBox.about(self, 'Error','Please select an NPC')
        else:
            self.aar = 'Actions'
            self.actionsAbilitiesReactions = ActionsAbilitiesReactions(self)
            self.actionsAbilitiesReactions.show()

    def openNpcLegendaryActionsList(self):
        if (self.currentPk == None):
            QtWidgets.QMessageBox.about(self, 'Error','Please select an NPC')
        else:
            self.aar = 'Legendary Actions'
            self.actionsAbilitiesReactions = ActionsAbilitiesReactions(self)
            self.actionsAbilitiesReactions.show()

    def openNpcReactionsList(self):
        if (self.currentPk == None):
            QtWidgets.QMessageBox.about(self, 'Error','Please select an NPC')
        else:
            self.aar = 'Reactions'
            self.actionsAbilitiesReactions = ActionsAbilitiesReactions(self)
            self.actionsAbilitiesReactions.show()

    def openNpcAbilitiesList(self):
        if (self.currentPk == None):
            QtWidgets.QMessageBox.about(self, 'Error','Please select an NPC')
        else:
            self.aar = 'Abilities'
            self.actionsAbilitiesReactions = ActionsAbilitiesReactions(self)
            self.actionsAbilitiesReactions.show()

    def openNpcSpellsList(self):
        if (self.currentPk == None):
            QtWidgets.QMessageBox.about(self, 'Error','Please select an NPC')
        else:
            self.npcSpell = NpcSpell(self)
            self.npcSpell.show()

    def updateNpcStr(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcStrLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcStrLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcStrLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcStrLineEdit.setText("0")
                    self.npcStrLabel.setText("(+0)")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateNpcWis(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcWisLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcWisLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcWisLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcWisLabel.setText("(+0)")
                    self.npcWisLineEdit.setText("0")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateNpcCha(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcChaLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcChaLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcChaLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcChaLineEdit.setText("0")
                    self.npcChaLabel.setText("(+0)")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateNpcInt(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcIntLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcIntLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcIntLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcIntLineEdit.setText("0")
                    self.npcIntLabel.setText("(+0)")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateNpcDex(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcDexLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcDexLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcDexLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcDexLineEdit.setText("0")
                    self.npcDexLabel.setText("(+0)")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateNpcCon(self, stat):
        if(stat == "." or stat == "-" or stat == "-." or stat == "" or stat == " "):
            self.npcConLabel.setText("(+0)")
        else:
            try:
                bonus = int((float(stat) - 10)/2)
                if ((bonus % 2) != 0) & (bonus < 0):
                    bonus = int(bonus - 0.5)
                if (bonus >= 0):
                    self.npcConLabel.setText("(+" + str(bonus) + ")")
                else:
                    self.npcConLabel.setText("(" + str(bonus) + ")")
            except:
                    self.npcConLineEdit.setText("0")
                    self.npcConLabel.setText("(+0)")
                    QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')

    def updateFromClick(self, row, column):
        self.libraryTableWidget.setColumnHidden(0, False)
        item = self.libraryTableWidget.item(row, 0)
        self.currentPk = item.text()
        self.libraryTableWidget.setColumnHidden(0, True)
        self.populateFields(select_npc_by_pk(self.currentPk))

    def populateFields(self, selectedNpc):
        self.nameLineEdit.setText(str(selectedNpc.name))
        comboIndex = self.npcSizeComboBox.findText(str(selectedNpc.size).capitalize())
        self.npcSizeComboBox.setCurrentIndex(comboIndex)
        comboIndex = self.npcTypeComboBox.findText(str(selectedNpc.npc_type).capitalize())
        self.npcTypeComboBox.setCurrentIndex(comboIndex)
        comboIndex = self.npcAlignmentComboBox.findText(str(selectedNpc.alignment).capitalize())
        self.npcAlignmentComboBox.setCurrentIndex(comboIndex)
        self.armorClassLineEdit.setText(str(selectedNpc.ac))
        self.armorClassDescLineEdit.setText(str(selectedNpc.ac_desc))
        self.hPLineEdit.setText(str(selectedNpc.hp))
        self.hPCalcLineEdit.setText(str(selectedNpc.hp_calc))
        self.speedLineEdit.setText(str(selectedNpc.speed))
        self.challengeLineEdit.setText(str(Fraction(selectedNpc.cr)))
        self.xPLineEdit.setText(str(selectedNpc.xp))
        self.languagesLineEdit.setText(str(selectedNpc.languages))
        self.sensesLineEdit.setText(str(selectedNpc.senses))
        self.descriptionTextEdit.setText(str(selectedNpc.description))
        self.damageResistanceTextEdit.setText(str(selectedNpc.damage_resistance))
        self.acrobaticsLineEdit.setText(str(selectedNpc.acrobatics))
        self.animalHandlingLineEdit.setText(str(selectedNpc.animal_handling))
        self.arcanaLineEdit.setText(str(selectedNpc.arcana))
        self.athleticsLineEdit.setText(str(selectedNpc.athletics))
        self.deceptionLineEdit.setText(str(selectedNpc.deception))
        self.historyLineEdit.setText(str(selectedNpc.history))
        self.insightLineEdit.setText(str(selectedNpc.insight))
        self.intimidationLineEdit.setText(str(selectedNpc.intimidation))
        self.investigationLineEdit.setText(str(selectedNpc.investigation))
        self.medicineLineEdit.setText(str(selectedNpc.medicine))
        self.natureLineEdit.setText(str(selectedNpc.nature))
        self.perceptionLineEdit.setText(str(selectedNpc.perception))
        self.performanceLineEdit.setText(str(selectedNpc.performance))
        self.persuasionLineEdit.setText(str(selectedNpc.persuasion))
        self.religionLineEdit.setText(str(selectedNpc.religion))
        self.sleightOfHandLineEdit.setText(str(selectedNpc.sleight_of_hand))
        self.stealthLineEdit.setText(str(selectedNpc.stealth))
        self.survivalLineEdit.setText(str(selectedNpc.survival))
        self.npcStrLineEdit.setText(str(selectedNpc.str_stat))
        self.strSavingThrowLineEdit.setText(str(selectedNpc.str_sav))
        self.npcDexLineEdit.setText(str(selectedNpc.dex_stat))
        self.dexSavingThrowLineEdit.setText(str(selectedNpc.dex_sav))
        self.npcConLineEdit.setText(str(selectedNpc.con_stat))
        self.conSavingThrowLineEdit.setText(str(selectedNpc.con_sav))
        self.npcIntLineEdit.setText(str(selectedNpc.int_stat))
        self.intSavingThrowLineEdit.setText(str(selectedNpc.int_sav))
        self.npcWisLineEdit.setText(str(selectedNpc.wis_stat))
        self.wisSavingThrowLineEdit.setText(str(selectedNpc.wis_sav))
        self.npcChaLineEdit.setText(str(selectedNpc.cha_stat))
        self.chaSavingThrowLineEdit.setText(str(selectedNpc.cha_sav))
        str_bonus = selectedNpc.calculate_bonus(int(selectedNpc.str_stat))
        int_bonus = selectedNpc.calculate_bonus(int(selectedNpc.int_stat))
        dex_bonus = selectedNpc.calculate_bonus(int(selectedNpc.dex_stat))
        wis_bonus = selectedNpc.calculate_bonus(int(selectedNpc.wis_stat))
        con_bonus = selectedNpc.calculate_bonus(int(selectedNpc.con_stat))
        cha_bonus = selectedNpc.calculate_bonus(int(selectedNpc.cha_stat))
        if (str_bonus >= 0):
            self.npcStrLabel.setText("(+" + str(str_bonus) + ")")
        else:
            self.npcStrLabel.setText("(" + str(str_bonus) + ")")
        if (int_bonus >= 0):
            self.npcIntLabel.setText("(+" + str(int_bonus) + ")")
        else:
            self.npcIntLabel.setText("(" + str(int_bonus) + ")")
        if (dex_bonus >= 0):
            self.npcDexLabel.setText("(+" + str(dex_bonus) + ")")
        else:
            self.npcDexLabel.setText("(" + str(dex_bonus) + ")")
        if (wis_bonus >= 0):
            self.npcWisLabel.setText("(+" + str(wis_bonus) + ")")
        else:
            self.npcWisLabel.setText("(" + str(wis_bonus) + ")")
        if (con_bonus >= 0):
            self.npcConLabel.setText("(+" + str(con_bonus) + ")")
        else:
            self.npcConLabel.setText("(" + str(con_bonus) + ")")
        if (cha_bonus >= 0):
            self.npcChaLabel.setText("(+" + str(cha_bonus) + ")")
        else:
            self.npcChaLabel.setText("(" + str(cha_bonus) + ")")