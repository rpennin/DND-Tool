class Npc():
    def __init__(self,pk,name,description,size,npc_type,alignment,ac,ac_desc,hp,hp_calc,speed,str_stat,str_sav,dex_stat,dex_sav,con_stat,con_sav,int_stat,int_sav,wis_stat,wis_sav,cha_stat,cha_sav,damage_resistance,acrobatics,animal_handling,arcana,athletics,deception,history,insight,intimidation,investigation,medicine,nature,perception,performance,persuasion,religion,sleight_of_hand,stealth,survival,senses,languages,cr,xp):
        self.pk = pk
        self.name = name
        self.description = description
        self.size = size
        self.npc_type = npc_type
        self.alignment = alignment
        self.ac = ac
        self.ac_desc = ac_desc
        self.hp = hp
        self.hp_calc = hp_calc
        self.speed = speed
        self.str_stat = str_stat
        self.str_sav = str_sav
        self.dex_stat = dex_stat
        self.dex_sav = dex_sav
        self.con_stat = con_stat
        self.con_sav = con_sav
        self.int_stat = int_stat
        self.int_sav = int_sav
        self.wis_stat = wis_stat
        self.wis_sav = wis_sav
        self.cha_stat = cha_stat
        self.cha_sav = cha_sav
        self.damage_resistance = damage_resistance
        self.acrobatics = acrobatics
        self.animal_handling = animal_handling
        self.arcana = arcana
        self.athletics = athletics
        self.deception = deception
        self.history = history
        self.insight = insight
        self.intimidation = intimidation
        self.investigation = investigation
        self.medicine = medicine
        self.nature = nature
        self.perception = perception
        self.performance = performance
        self.persuasion = persuasion
        self.religion = religion
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth
        self.survival = survival
        self.senses = senses
        self.languages = languages
        self.cr = cr
        self.xp = xp

    def calculate_bonus(self, attribute_level):
        bonus = (attribute_level - 10)/2
        if ((bonus % 2) != 0) & (bonus < 0):
            bonus = int(bonus - 0.5)
        return int(bonus)