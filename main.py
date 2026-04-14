from initiative_app import *
from tkinter import *
from tkinter.ttk import *
initiv_list = {}
def initiaative_or_monster():
    def throw():
        global initiv_list
        beast = beast.get()
        sign = sign.get()
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
        advantage = advantage.get()
        initiv_list = enemy.throw(initiative,advantage,beast,sign)
        lbl.configure(root,text = dict(sorted(initiv_list.items(), key=lambda item: item[1])))
    tk = Tk()
    tk.title('Колесо инициативы для NPC')
    tk.geometry('400x100')
    lbl_inc = Label(tk,text='Монстр')
    lbl_inc.grid(column=0,row = 0)
    lbl_adv = Label(tk,text='Преймущество')
    lbl_adv.grid(column=1,row=0)
    beast = Entry(tk,width=20)
    beast.grid(column=1,row = 1)
    advantage = Entry(tk,width=10)
    advantage.grid(row=1, column= 0)
    lbl_sign = Label(tk, text= 'Отличительная черта')
    lbl_sign.grid(column=2,row=0)
    txt = Entry(tk,width=10)
    txt.grid(column = 2, row = 1)
    btn = Button(tk,text='Ввести',command=enemy.throw())
    btn.grid(column=1,row = 2)
    tk.mainloop()
def initiative_for_player():
    def dice_throw():
        global initiv_list
        name = name.get()
        initiative = int(initiative.get()
        initiv_list = player.throw(initiative,name)
    pl = Tk()
    pl.title('Колесо инициативы для игроков')
    pl.geometry('400x100')
    lbl_iniz = Label(pl, text = 'Введите инициативу с бонусами')
    lbl_iniz.grid(column=1, row = 0)
    initiative = Entry(pl)
    initiative.grid(column=1,row = 1)
    name = Entry(pl)
    name.grid(column=0, row=1)
    lbl_name = Label(pl,text = 'Имя')
    lbl_name.grid(column=0,row=0)
    btn = Button(pl,text='Ввести',command=dice_throw)
    btn.grid(column=0,row=2)
    lbl.configure(root,text = dict(sorted(initiv_list.items(), key=lambda item: item[1])))
    pl.mainloop()
root = Tk()
root.geometry('200x100')
root.title('Колесо инициативы')    
lbl = Label()
players = Button(root,text='_________Для игроков_________',command=initiative_for_player)
players.grid(column=0,row=0)
dms = Button(root,text='_________Для ДМа_________',command=initiaative_or_monster)
dms.grid(column=0,row=1)
root.mainloop()
