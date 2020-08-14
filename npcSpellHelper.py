from dbUtil import *
from PyQt5 import QtCore, QtGui, QtWidgets
from npcSpell import Ui_npcSpell

class NpcSpell(QtWidgets.QDialog, Ui_npcSpell):
    def __init__(self, *args, obj=None, **kwargs):
        super(NpcSpell, self).__init__(*args, **kwargs)
        self.setupUi(self)