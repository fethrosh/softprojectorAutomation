import pyautogui as p
import keyboard as k
from time import sleep, time
from threading import Thread
from datetime import datetime as dt
from song import song as s
import sqlite3

conn = sqlite3.connect("songs.db")
cursor = conn.cursor()

RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
RE = "\u001b[0m"

#readies the necessary databases
lines = []
song_db = []

#loads the database file 
def read_database():
    line_num = len(open("database.txt","r").readlines())
    file = open("database.txt","r")
    for i in range(line_num):
        line = file.readline().split()
        try:
            song_db.append(s(int(line[1]),int(line[0]),int(line[2]),
                             int(line[3]),int(line[4]),int(line[5])))
        except:
            print(RED+"Unsuccessful in adding song "+line[0]+RE)
    file.close()
    print(GREEN+"Database loaded successfully"+RE)

def reread(array={}):
    temp = [len(array),0]
    line_num = len(open("database.txt","r").readlines())
    file = open("database.txt","r")
    for i in range(line_num):
        line = file.readline().split()
        try:
            temp.append(s(int(line[1]),int(line[0]),int(line[2]),
                             int(line[3]),int(line[4]),int(line[5])))
        except:
            print(RED+"Unsuccessful in adding song "+line[1]+RE)
    song_db = temp
    print(GREEN+"Database reread successfully"+RE)

#finds the spot where the relevent data is located
def read_library(number):
    for i in range(len(song_db)):
        if (song_db[i].getNumber() == number):
            print("found")
            database_number = song_db[i]
            print(str(database_number))
            return database_number
    print("unable to find")
    return -1

#adds to the databases and the save file
def add_to_discography():
    songbook = p.prompt(text='What songbook do you want to add to?\n(e) - English\n(r) - Russian')    
    if (songbook == "r"):
        file = open("database.txt",'a')
    else:
        file = open("englishDB.txt",'a')
    number = p.prompt(text = 'What song do you want to add?',title = 'songs to add')
    verses = p.prompt(text = 'How many verses?',title = 'Verses')
    delay_verse = p.prompt(text = 'Delay for verse?',title = 'Delay')
    delay_chorus = p.prompt(text = 'Delay for chorus?',title = 'Delay')
    delay_end = p.prompt(text = 'Delay for the end?',title = 'Delay')
    save_string= str(number)+"\t"+str(verses)+"\t"+str(delay_verse)+"\t"+str(delay_chorus)+"\t"+str(delay_end)+"\n"
    song = s(int(number),int(verses),int(delay_verse),int(delay_chorus),
                     int(delay_end))
    song_db.append(song)
    print("adding to database with line "+save_string)
    reorderDB()
    file.write(str(song))
    file.close()

def reorderDB():
    temp = []
    mini = song_db[0].getNumber()
    loc = 0
    while (len(song_db)!=0):
        for i in range(len(song_db)):
            if (int(song_db[i].getNumber())<=int(mini)):
                loc = i
                mini = song_db[i].getNumber()
        temp.append(song_db.pop(loc))
        if(len(song_db) != 0):
            mini = song_db[0].getNumber()
    for i in range(len(temp)):
        song_db.append(temp[i])
    print(GREEN+"Database successfully reordered"+RE)

#gets the amount of time that it takes to sing a song and saves it (hopefully...)
def timer():
    chorus=0
    x=True
    counter =0
    verse_count = 0
    verse_time =[]
    chorus_time = []
    time=0
    song = p.prompt(text="What song do you want to time?")
    input=p.prompt(text='Does the song have a chorus or refrain?\n\ny/n',
             title='chorus')
    if(input=='yes' or input=='y'):
        chorus=1
    sleep(1)
    while x:
        pressed = k.read_key(suppress=True)
        if(pressed=='s' or pressed=='ы'):
            print("starting timer")
            timer_start = dt.now()
            song_start=timer_start
            start_time=timer_start.strftime("%H:%M:%S")
            print("start time = "+start_time)
            sleep(1)
        elif (pressed == 'd' or pressed == 'в'):
            print("displaying song")
            k.press('f5')
        elif (pressed=='e' or pressed=='у'):
            print("stopping timer")
            timer_end = dt.now()
            end_time=timer_end.strftime("%H:%M:%S")
            print(end_time)
            k.press('esc')
            sleep(1)
            length = timer_end-timer_start
            songLength= timer_end-song_start
            print(songLength)
            x=False
        elif (pressed=='right' or pressed=='down'):
            p.press('right')
            if(counter%2==1 and chorus==True):
                chorus_time.append(dt.now()-timer_start)
                print("adding chorus")
                timer_start = dt.now()
                counter+=1
            else:
                verse_time.append(dt.now()-timer_start)
                print("adding verse")
                timer_start = dt.now()
                counter+=1
                verse_count+=1
            sleep(.5)
        else:
            p.press(pressed)
    verseAverage = calcAverage(verse_time)
    chorusAverage = calcAverage(chorus_time)
    line = "\n"+str(song)+"\t"+str(verse_count+1)+"\t"+str(verseAverage)+"\t"+str(chorusAverage)+"\t"+str(length.seconds)
    temp = s(int(song),chorus,int(verse_count+1),int(verseAverage),int(chorusAverage),
             int(length.seconds))
    try:
        print(YELLOW+"Adding song "+str(song)+" to database with line "+line+RE)
        song_db.append(temp)
        reorderDB()
        backup("database.txt","backup.txt")
        reset = open("database.txt",'w')
        reset.write("")
        reset.close()
        file = open("database.txt",'a')
        for i in song_db:
            file.write(str(i)+"\n")
        file.close()
        print(GREEN+"Successfully wrote song "+song+" to database"+RE)
    except:
        print(RED+"Error in writing "+line+RE)
    try:
        reread()
    except:
        print(RED+"Error in rereading database"+RE)

def backup(OriginalFile, BackupFile):
    file1 = open(OriginalFile, 'r')
    file2 = open(BackupFile, 'w')

    lines = file1.readlines()
    try:
        for i in range(len(lines)):
            file2.write(lines[i])
        print(GREEN+"Successfully backed up"+RE)
    except:
        print(RED+"Error in writing to backup. Pease manually copy the data"+RE)
    file1.close()
    file2.close()
    
def calcAverage(array={}):
    average=0
    if (len(array)==0):
        return 0
    for i in range(len(array)):
        average=average+array[i].seconds
    return round(average/len(array))

read_database()
