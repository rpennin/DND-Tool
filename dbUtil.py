import sqlite3
from sqlite3 import Error
from npc import Npc
from spell import Spell
import os.path

#creates the database connection
def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('./database.db')
        # print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

#returns a list of Npc objects from the database
def select_all_npcs():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc")
    query_result = cur.fetchall()
    conn.close()
    npcList = []
    for row in query_result:
        npc = Npc(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45])
        npcList.append(npc)
    return npcList

#returns an Npc based on the primary key
def select_npc_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc WHERE id=?", (pk,))
    row = cur.fetchall()[0]
    conn.close()
    npc = Npc(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45])
    return npc

def delete_npc_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM npc WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def insert_npc(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO npc(name,description,size,type,alignment,ac,ac_desc,hp,hp_calc,speed,str,str_sav,dex,dex_sav,con,con_sav,int,int_sav,wis,wis_sav,cha,cha_sav,damage_resistance,acrobatics,animal_handling,arcana,athletics,deception,history,insight,intimidation,investigation,medicine,nature,perception,performance,persuasion,religion,sleight_of_hand,stealth,survival,senses,languages,cr,xp)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def update_npc_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE npc
    SET name = ? ,
        description = ? ,
        size = ? ,
        type = ? ,
        alignment = ? ,
        ac = ? ,
        ac_desc = ? ,
        hp = ? ,
        hp_calc = ? ,
        speed = ? ,
        str = ? ,
        str_sav = ? ,
        dex = ? ,
        dex_sav = ? ,
        con = ? ,
        con_sav = ? ,
        int = ? ,
        int_sav = ? ,
        wis = ? ,
        wis_sav = ? ,
        cha = ? ,
        cha_sav = ? ,
        damage_resistance = ? ,
        acrobatics = ? ,
        animal_handling = ? ,
        arcana = ? ,
        athletics = ? ,
        deception = ? ,
        history = ? ,
        insight = ? ,
        intimidation = ? ,
        investigation = ? ,
        medicine = ? ,
        nature = ? ,
        perception = ? ,
        performance = ? ,
        persuasion = ? ,
        religion = ? ,
        sleight_of_hand = ? ,
        stealth = ? ,
        survival = ? ,
        senses = ? ,
        languages = ? ,
        cr = ? ,
        xp = ?
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def select_all_abilities_by_npc(npc_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc_ability WHERE npc_id=?", [npc_id])
    query_result = cur.fetchall()
    conn.close()
    abilitiesList = []
    for row in query_result:
        ability = [row[0], row[1], row[2]]
        abilitiesList.append(ability)
    return abilitiesList

def select_all_actions_by_npc(npc_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc_action WHERE npc_id=?", [npc_id])
    query_result = cur.fetchall()
    conn.close()
    actionsList = []
    for row in query_result:
        action = [row[0], row[1], row[2]]
        actionsList.append(action)
    return actionsList

def select_all_reactions_by_npc(npc_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc_reaction WHERE npc_id=?", [npc_id])
    query_result = cur.fetchall()
    conn.close()
    reactionsList = []
    for row in query_result:
        reaction = [row[0], row[1], row[2]]
        reactionsList.append(reaction)
    return reactionsList

def select_all_legendary_actions_by_npc(npc_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM npc_legendary_action WHERE npc_id=?", [npc_id])
    query_result = cur.fetchall()
    conn.close()
    legendaryActionsList = []
    for row in query_result:
        action = [row[0], row[1], row[2]]
        legendaryActionsList.append(action)
    return legendaryActionsList

def insert_npc_ability(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO npc_ability(ability_name, ability_description, npc_id)
    VALUES(?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def insert_npc_action(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO npc_action(action_name, action_description, npc_id)
    VALUES(?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def insert_npc_legendary_action(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO npc_legendary_action(legendary_action_name, legendary_action_description, npc_id)
    VALUES(?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def insert_npc_reaction(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO npc_reaction(npc_reaction_name, npc_reaction_description, npc_id)
    VALUES(?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def update_npc_ability_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE npc_ability
    SET ability_name = ? ,
        ability_description = ? ,
        npc_id = ?
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def update_npc_action_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE npc_action
    SET action_name = ? ,
        action_description = ? ,
        npc_id = ?
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def update_npc_reaction_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE npc_reaction
    SET npc_reaction_name = ? ,
        npc_reaction_description = ? ,
        npc_id = ?
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def update_npc_legendary_action_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE npc_legendary_action
    SET legendary_action_name = ? ,
        legendary_action_description = ? ,
        npc_id = ?
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def delete_npc_legendary_action_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM npc_legendary_action WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def delete_npc_action_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM npc_action WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def delete_npc_ability_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM npc_ability WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def delete_npc_reaction_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM npc_reaction WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def select_all_library_spells():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM spell_library")
    query_result = cur.fetchall()
    conn.close()
    spellList = []
    for row in query_result:
        spell = Spell(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
        spellList.append(spell)
        # print(row)
    return spellList

def select_spell_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM spell_library WHERE id=?", (pk,))
    row = cur.fetchall()[0]
    conn.close()
    spell = Spell(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
    return spell

def delete_spell_by_pk(pk):
    pk = str(pk)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM spell_library WHERE id=?", (pk,))
    conn.commit()
    conn.close()

def update_spell_by_pk(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''UPDATE spell_library
    SET name = ? ,
        level = ? ,
        casting_time = ? ,
        range = ? ,
        components = ? ,
        duration = ? ,
        description = ? ,
        higher_level = ? ,
        ritual = ? ,
        concentration = ? ,
        school = ? ,
        material = ? ,
        class = ? 
    WHERE id=?'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def insert_spell(values):
    conn = create_connection()
    cur = conn.cursor()
    sql = '''INSERT INTO spell_library(name, level, casting_time, range, components, duration, description, higher_level, ritual, concentration, school, material, class)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cur.execute(sql, values)
    conn.commit()
    conn.close()