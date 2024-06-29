"""import tkinter as tk
import os

window = tk.Tk()

def printer():
    print("hello world")

def printer2():
    print("second module printed")

button=tk.Button(window,text="test",command=printer)
button2=tk.Button(window,text="test 2",command=printer2,width=10)
button.pack()
button2.pack()
"""

 
"""import os, random as r

photos_dir="C:\\Users\\grace\\Pictures\\Saved Pictures"
photos=os.listdir(photos_dir)

photo = r.randint(0,len(photos)-1)

print(photos[photo])

os.startfile(os.path.join(photos_dir,photos[photo]))"""

file1 = open("database.txt", 'r')
file2 = open("backup.txt", 'w')

lines = file1.readlines()

for i in range(len(lines)):
    file2.write(lines[i])
file1.close()
file2.close()
