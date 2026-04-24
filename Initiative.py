from tkinter import *
from random import randint
import sqlite3
class unit():
    def __init__(self,initiative,advantage,):
        self.initiative = initiative
        self.adv = advantage

class enemy(unit):
    def __init__(self, initiative):
        super().__init__(initiative)

    def throw(self,initiative,advantage,beast,sign):
        if advantage == 1:
            initiative = max([randint(1,21)+initiative,randint(1,20)+initiative])
        elif advantage == -1:
            initiative = min([randint(1,21)+initiative,randint(1,21)+initiative])
        initiv_list[beast+','+sign] = initiative
        return initiv_list
        

class player(unit):
    def __init__(self, initiative,name):
        super().__init__(initiative,name)
    def throw(self,initiative,name):
        global initiv_list
        initiv_list[name] = initiative
