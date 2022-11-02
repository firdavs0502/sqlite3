import sqlite3 as sql

boglanish = sql.connect("programmerstlar.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Sutident(
    situdent TEXT,
    bekorchilar TEXT,
    programmerstlar TEXT
    kursi INTEGER  
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Bekorchilar(
   ism TEXT
   familiya TEXT
   yosh INTEGE
   qanchadan beri TEXT
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Programmerstlar(
   ism TEXT
   familiya TEXT
   yosh INTEGER 
   staji INTEGER
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Yomon(
   ism TEXT
   familiya TEXT
   yosh INTEGER 
   nimaga TEXT
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Yaxshi(
   ism TEXT
   familiya TEXT
   yosh INTEGER 
   ha TEXT
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS O'rtacha(
   ism TEXT
   familiya TEXT
   yosh INTEGER 
   hm TEXT
)

''')