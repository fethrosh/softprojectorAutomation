import sqlite3

conn = sqlite3.connect("songs.db")

cursor = conn.cursor()

def creator():
    try:
        cursor.execute("""SELECT * FROM songs;""")
    except:
        cursor.execute("""CREATE TABLE songs (number INTEGER PRIMARY KEY,
                            verses INTEGER, chorus BOOLEAN, verseTime INTEGER,
                            chorusTime INTEGER, endTime INTEGER);""")
        creator()

def addSongs():
    RED = "\u001b[31m"
    RE = "\u001b[0m"
    line_num = len(open("database.txt","r").readlines())
    file = open("database.txt","r")
    for i in range(line_num):
        line = file.readline().split()
        try:
            cursor.execute("""INSERT INTO songs VALUES (?,?,?,?,?,?)""",
                           (int(line[1]),int(line[0]),int(line[2]),
                             int(line[3]),int(line[4]),int(line[5])));
        except:
            print(RED+"Unsuccessful in adding song "+line[1]+RE)

    conn.commit()
    conn.close()

            
creator()
addSongs()

