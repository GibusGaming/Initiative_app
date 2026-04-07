from tkinter import *
from random import randint
import sqlite3
initiv_list = {}
class unit():
    def __init__(self,initiative,advantage,):
        self.initiative = initiative
        self.adv = advantage

class enemy(unit):
    def __init__(self, initiative):
        super().__init__(initiative)

    def for_dm():
        def throw(self,initiative,advantage,beast,sign):
            beast = name.get()
            sign = txt.get()
            cons = sqlite3.connect('monsters.db')
            cur = cons.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS monsters (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    initiva = INTEGER
                )
            """)

            cons.commit()

            cur.execute("SELECT initiva FROM monsters WHERE name = {beast}")
            initiative = cur.fetchone()
            advantage = ent.get()
            if advantage == 1:
                initiative = max([randint(1,21)+initiative,randint(1,20)+initiative])
            elif advantage == -1:
                initiative = min([randint(1,21)+initiative,randint(1,21)+initiative])
            initiv_list[beast+sign] = initiative
            
        tk = Tk()
        tk.title('Колесо инициативы')
        lbl_inc = Label(tk,text='Монстр')
        lbl_inc.grid(column=0,row = 0)
        lbl_adv = Label(tk,text='Преймущество')
        lbl_adv.grid(column=1,row=0)
        name = Entry()
        name.grid(column=1,row = 1)
        ent = Entry()
        ent.grid(row=1, column= 0)
        lbl_sign = Label(tk, text= 'Отличительная черта')
        lbl_sign.grid(column=2,row=0)
        txt = Entry()
        txt.grid(column = 2, row = 1)
        tk.mainloop()

    class player(unit):
        def __init__(self, initiative, advantage,name):
            super().__init__(initiative, advantage,name)
    def for_tk():
            def throw(self,initiative,name):
                name = name.get()
                initiative = int(init.get())
                initiv_list[name] = initiative
            tk = Tk()
            lbl_iniz = Label(tk, text = 'Введите инициативу с бонусами')
            lbl_iniz.grid(column=1, row = 0)
            init = Entry()
            init.grid(column=1,row = 1)
            name = Entry()
            name.grid(column=0, row=1)
            lbl_name = Label(tk, text = 'Имя')
            lbl_name.grid(column=0,row=1)
            tk.mainloop()
