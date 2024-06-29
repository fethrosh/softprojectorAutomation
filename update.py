#imports
from pyautogui import locateCenterOnScreen as l, click as c, hotkey as h, typewrite as t,keyDown, keyUp
from keyboard import write
from time import sleep
from datetime import datetime as dt, timedelta as td
import sqlite3

RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
RE = "\u001b[0m"

annImg = 'announcement_img.jpg'
edit = 'edit_ann.jpg'
home = 'home_position.jpg'
save = 'save_changes.jpg'
Announce1 = 'Announce1.jpg'
announce2 = 'Announce2.jpg'

'''
def date_update_sun():
    h('f8')
    sleep(.1)
    c(l(annImg,confidence=.8))
    sleep(1)
    c(l(edit,confidence=.9))
    sleep(2)
    c(l(Announce1,confidence=.9))
    h('home', 'pageup')
    keyDown('shift')
    c(l(announce2,confidence=.9))
    h('up','up')
    h('left')
    keyUp('shift')
    h('backspace')
    write("Announce 1\nВоскресное служение!\nSunday service!\n"
      +numbers(7)+" 12:00pm - 2:00pm\n\n"+
      "Вечернее Воскресное служение\nEvening Sunday Service\n"
      +numbers(0)+" 6:00pm - 8:00pm\n\n"+
      "Вторник - Спевка и Молитва!\nTuesday - Choir and Prayer!\n"
      +numbers(2)+" 7:00pm - 9:00pm\n\n"+
      "Пятница - Молитвенное служение/Детская Библейская школа\nFriday - Prayer service/Kids Bible school!\n"
      +numbers(5)+" 7:00pm - 9:00pm\n\nAnnounce ")
    c(l(save, confidence=.7))
    h("f6")

def date_update_fri():
    h('f8')
    c(l(annImg,confidence=.8))
    c(l(edit,confidence=.8))
    sleep(.5)
    c(l(home,confidence=.8))
    h('home', 'pageup')
    keyDown('shift')
    for i in range(18):
        h('down')
    h('left')
    keyUp('shift')
    h('backspace')
    write("Announce 1\nВоскресное служение!\nSunday service!\n"
      +numbers(2)+" 12:00pm - 2:00pm\n\n"+
      "Вечернее Воскресное служение\nEvening Sunday Service\n"
      +numbers(2)+" 6:00pm - 8:00pm\n\n"+
      "Вторник - Спевка и Молитва!\nTuesday - Choir and Prayer!\n"
      +numbers(4)+" 7:00pm - 9:00pm\n\n"+
      "Пятница - Молитвенное служение/Детская Библейская школа\nFriday - Prayer service/Kids Bible school!\n"
      +numbers(7)+" 7:00pm - 9:00pm\n")
    c(l(save, confidence=.7))
    h("f6")
'''

def numbers(delta):
    if (delta == 0):
        return dt.now().strftime("%m/%d/%y")
    timed = td(days=delta)
    now = dt.now()
    future = now+timed
    return future.strftime("%m/%d/%y")

def update():
    conn = sqlite3.connect("C:/Users/grace/SoftProjector/spData.sqlite")
    cu = conn.cursor()
    file = open("date.txt",'r')
    line = file.readline()
    file.close()
    SQLString = """UPDATE Announcements SET text=? WHERE id=7;"""
    if (dt.today().weekday()==6):
        #date_update_sun()
        print(YELLOW+"Starting Sunday Update"+RE)
        SunM = numbers(7)
        SunE = numbers(0)
        Tues = numbers(2)
        Fri = numbers(5)
        UpdateString = f"""Announce 1
Воскресное служение!
Sunday service!
{SunM} 12:00pm - 2:00pm

Вечернее Воскресное служение
Evening Sunday Service
{SunE} 6:00pm - 8:00pm
      
Вторник - Спевка и Молитва!
Tuesday - Choir and Prayer!
{Tues} 7:00pm - 9:00pm
      
Пятница - Молитвенное служение/Детская Библейская школа
Friday - Prayer service/Kids Bible school!
{Fri} 7:00pm - 9:00pm
        
Announce 2
Церковь Благодать Спасения
(Grace of Salvation Church)

05-19-2024
Сбор
$100.00"""
    elif (dt.today().weekday()==4):
        #date_update_fri()
        print(YELLOW+"Starting Friday update"+RE)
        SunM = numbers(2)
        SunE = numbers(2)
        Tues = numbers(4)
        Fri = numbers(7)
        UpdateString = f"""Announce 1
Воскресное служение!
Sunday service!
{SunM} 12:00pm - 2:00pm

Вечернее Воскресное служение
Evening Sunday Service
{SunE} 6:00pm - 8:00pm
      
Вторник - Спевка и Молитва!
Tuesday - Choir and Prayer!
{Tues} 7:00pm - 9:00pm
      
Пятница - Молитвенное служение/Детская Библейская школа
Friday - Prayer service/Kids Bible school!
{Fri} 7:00pm - 9:00pm
        
Announce 2
Церковь Благодать Спасения
(Grace of Salvation Church)

05-19-2024
Сбор
$0.00"""
    file = open("date.txt",'w')
    x = dt.today().strftime("%m/%d/%y")
    file.write(x)
    file.close()
    if(line!=dt.today().strftime("%m/%d/%y")):
        try:
            cu.execute(SQLString,(UpdateString,))
            print(GREEN+"Update of Announcement successful"+RE)
            conn.commit()
        except Exception as e:
            print(RED+"Unable to update the database\n\n"+RE)
            traceback.print_exec()
    else:
        print(GREEN+"Update already completed. Skipping"+RE)
    conn.close()

if __name__=="__main__":
    update()
