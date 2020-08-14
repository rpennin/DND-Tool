from actionsAbilitiesReactions import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from dbUtil import *

class ActionsAbilitiesReactions(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ActionsAbilitiesReactions, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.aarLabel.setText(self.parent().aar)
        self.setWindowTitle(self.parent().aar + ' Setup')
        self.tableWidget.setColumnHidden(0, True)
        if (self.parent().aar == 'Actions'):
            self.itemsList = select_all_actions_by_npc(self.parent().currentPk)
            self.populateTable()
        elif (self.parent().aar == 'Reactions'):
            self.itemsList = select_all_reactions_by_npc(self.parent().currentPk)
            self.populateTable()
        elif (self.parent().aar == 'Abilities'):
            self.itemsList = select_all_abilities_by_npc(self.parent().currentPk)
            self.populateTable()
        elif (self.parent().aar == 'Legendary Actions'):
            self.itemsList = select_all_legendary_actions_by_npc(self.parent().currentPk)
            self.populateTable()
        self.accepted.connect(self.saveItems)
        self.currentPk = None

    def populateTable(self):
        self.tableWidget.setRowCount(0)
        for item in self.itemsList:
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(item[1])))
            self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(item[2])))
    
    def insertRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        
    def deleteRows(self):
        self.tableWidget.setColumnHidden(0, False)
        rows = sorted(set(index.row() for index in self.tableWidget.selectedIndexes()))
        for row in reversed(rows):
            if (self.tableWidget.item(row, 0) == None):
                self.tableWidget.removeRow(row)
            else:
                pk = self.tableWidget.item(row, 0).text()
                if (self.parent().aar == 'Actions'):
                    delete_npc_action_by_pk(pk)
                elif (self.parent().aar == 'Reactions'):
                    delete_npc_reaction_by_pk(pk)
                elif (self.parent().aar == 'Abilities'):
                    delete_npc_ability_by_pk(pk)
                elif (self.parent().aar == 'Legendary Actions'):
                    delete_npc_legendary_action_by_pk(pk)
                self.tableWidget.removeRow(row)
        self.tableWidget.setColumnHidden(0, True)

    def saveItems(self):
        updateEntryList = []
        newEntryList = []
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.setColumnHidden(0,False)
        for row in range(rowCount):
            item = self.tableWidget.item(row, 0)
            if (item == None):
                if (self.tableWidget.item(row, 1) == None):
                    name = ""
                else:
                    name = self.tableWidget.item(row, 1).text()
                if (self.tableWidget.item(row, 2) == None):
                    description = ""
                else:
                    description = self.tableWidget.item(row, 2).text()
                entry = (name, description, self.parent().currentPk)
                newEntryList.append(entry)
            else:
                if (self.tableWidget.item(row, 1) == None):
                    name = ""
                else:
                    name = self.tableWidget.item(row, 1).text()
                if (self.tableWidget.item(row, 2) == None):
                    description = ""
                else:
                    description = self.tableWidget.item(row, 2).text()
                entry = (name, description, self.parent().currentPk, self.tableWidget.item(row, 0).text())
                updateEntryList.append(entry)

        for entry in updateEntryList:
            if (self.parent().aar == 'Actions'):
                update_npc_action_by_pk(entry)
            elif (self.parent().aar == 'Reactions'):
                update_npc_reaction_by_pk(entry)
            elif (self.parent().aar == 'Abilities'):
                update_npc_ability_by_pk(entry)
            elif (self.parent().aar == 'Legendary Actions'):
                update_npc_legendary_action_by_pk(entry)
            
        for entry in newEntryList:
            if (self.parent().aar == 'Actions'):
                insert_npc_action(entry)
            elif (self.parent().aar == 'Reactions'):
                insert_npc_reaction(entry)
            elif (self.parent().aar == 'Abilities'):
                insert_npc_ability(entry)
            elif (self.parent().aar == 'Legendary Actions'):
                insert_npc_legendary_action(entry)