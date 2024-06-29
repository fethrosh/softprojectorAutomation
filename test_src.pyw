#imports
import pyautogui as p
from time import sleep
import database as db
import update as up
import os
import pygetwindow as gw

#loading images
img1 = 'softproj.jpg'
img2 = 'taskbar.png'
img3 = 'softproj_focus.jpg'
img4 = 'contains.jpg'
img5 = 'match.jpg'
img6 = 'filter.jpg'
img7 = 'filter_selected'
img8 = 'announcement_img.jpg'

#making sure sofproject is the tab in focus
def focus_win ():
    try:
        focus = gw.getWindowsWithTitle('SoftProjector 2.1')[0]
        focus.activate()
        focus.maximize()
    except:
        print("Program not found. Attempting launch")
        import subprocess
        subprocess.Popen('C:\\Users\\grace\\SoftProjector\\SoftProjector.exe')
        sleep(5)
        focus_win()

#song display code
def song(chorus, number, verses, delay_verse, delay_chorus, delay_end):
    #switches to song tab
    p.hotkey('f7')
    #switches the filter type to "exact match"
    try:
        p.moveTo(p.locateCenterOnScreen(img4,confidence = .9))
        p.click()
        sleep(.5)
        p.moveTo(p.locateCenterOnScreen(img5,confidence = .9))
        p.click()
    except:
        sleep(.5)
    #selects the filter and types the song number
    p.moveTo(p.locateCenterOnScreen(img6,confidence = .9))
    p.move(30,0)
    p.click()
    sleep(.5)
    number=number.replace('e','')
    number=number.replace('r','')
    p.typewrite(number)
    p.alert(text='Press Ok when ready to start timers')
    
    p.hotkey('f5')
    for i in range (1,int(verses)-1):
        print("Displaying verse "+str(i))
        sleep(int(delay_verse))
        p.hotkey('right')
        if (int(delay_chorus)==0):
            sleep(0)
        else:
            print('displaying chorus')
            sleep(int(delay_chorus))
            p.hotkey('right')
    if (not chorus):
        sleep(int(delay_end))
    else:
        sleep(int(delay_verse))
        p.hotkey('right')
        sleep(int(delay_chorus))
    print('escaping')
    p.hotkey('escape')
    p.moveTo(p.locateCenterOnScreen(img6,confidence = .9))
    p.move(35,0)
    p.doubleClick()
    p.hotkey('backspace')
    p.hotkey('f6')

#locates announcemnt and sends it to the display
def announcement1():
    focus_win()
    rerun=True
    #focus on announcment tab
    p.hotkey('f8')
    #locate and click on the announcement
    p.moveTo(p.locateCenterOnScreen(img8,confidence=.8))
    p.click()
    #display selection
    p.hotkey('f5')
    #switcher between the two slides
    while (rerun):
        for i in range (3):
            sleep(30)
            p.hotkey('right')
            sleep(30)
            p.hotkey('left')
        p.hotkey('escape')
        rerun = confirm()

#same as announcement1(), but keeps itself up for 40 sec
def announcement2():
    focus_win()
    rerun=True
    p.hotkey('f8')
    sleep(.5)
    p.moveTo(p.locateCenterOnScreen(img8, confidence=.8))
    p.click()
    p.hotkey('f5')
    while(rerun):
        sleep(40)
        p.hotkey('escape')
        rerun = confirm()

def confirm():
    d = p.confirm(text="Do you want to rerun, shutdown, or exit?",
                      title="Decision",buttons=("Rerun","Shutdown","Exit"))
    if (d=="Rerun"):
        return True
    elif (d=="Shutdown"):
        p.hotkey('escape')
        sleep(5)
        d = p.confirm(text="Confirm shutdown?",buttons=("Confirm","Cancel"))
        if (d=="Confirm"):
            os.system("shutdown /s /t 1")
            exit()
    else:
        p.hotkey('escape')
        return False

#takes input from the user
def input():
    return p.prompt(text = 'What is the song number you need?\n\nann: Announcement with zbor\n'+
                            'ann2: Announcement only\nadd: Add to discography\nexit:'+
                             ' Exit program',title = 'songs',default = 'eg. r735, e13')
num =""
try:
    x,y=p.locateCenterOnScreen(img3)
except:
    focus_win()
sleep(10)
up.update()
num = input()
#loops until told to exit
while(num!='exit'):
        #makes sure the Softprojector software is on top
    try:
         x,y=p.locateCenterOnScreen(img3, confidence=.9)
         print("program focused, skipping")
    except:
         focus_win()
    #main code
    #decision tree for what the user wants to do
    if(num=='ann'or num=='фтт'):
        announcement1()
        num = 'exit'
    elif(num=='ann2'or num=='фтт2'):
        announcement2()
        num='exit'
    #runs the database discography adder
    elif(num=='add'or num=='фвв'):
        db.add_to_discography()
        num = input()
    elif(num=='timer'or num=='ешьук'):
        db.timer()
        num = input()
    elif(num=='exit' or num=='учше'):
        continue
    elif (num=='shutdown'):
        os.system("shutdown /s /t 1")
        exit()
    else:
        songObject=db.read_library(int(num))
        #error checking
        if (songObject==-1):
            p.alert(text='Unknown input. Try again',title='ERROR')
            num=input()
        #starts the projecting of the song input
        else:
            values=str(songObject).split()
            song(values[0],values[1],values[2],values[3],values[4],values[5])
            num=input()
    
