from tkinter import *
from random import randint

from functools import partial

import time

class Raam:
    def __init__(self, name):
        self.name = name
        self.mode = True
        self.rolluikPercentage = 0

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def getName(self):
        return self.name

    def getMode(self):
        return self.mode

    def getRolluik(self):
        return self.rolluikPercentage

    def setName(self, name):
        self.name = name

    def setRolluik(self, perc):
        self.rolluikPercentage = perc

def value_to_y(val):
    return 550-5*val

# init global vars grgnengorn
s = 1
x2 = 50
y2 = value_to_y(randint(0,100))
bool1 = True
max = 100
min = 0




def step():
    if bool1 == True:
        global s, x2, y2
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            canvas.delete('temp') # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s*50
        temp = randint(min,max)
        y2 = value_to_y(temp)
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s+1

        for raam in ramen:
            if raam.getMode() == True:
                raam.setRolluik(temp)

        updateMainScreen()
        canvas.after(500, step)

def pause():
    global bool1
    if bool1 == True:
        bool1 = False;
    else:
        bool1 = True;
        canvas.after(300, step)

def settingsWindow(i):
    popup = Tk()
    popup.title("Settings " + str(ramen[i].getName()))
    popup.geometry('350x200')

    Label(popup, text="Window Name").grid(row=0, sticky=W)
    Label(popup, text="Rolluik percentage").grid(row=1, sticky=W)

    e1 = Entry(popup)
    e2 = Entry(popup)
    e1.insert(10,str(ramen[i].getName()))
    e2.insert(10,str(ramen[i].getRolluik()))

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    def update():
        ramen[i].setName(e1.get())
        ramen[i].setRolluik(e2.get())
        updateMainScreen()

    Button(popup, text='Update', command=update).grid(row=3, column=0, sticky=W, pady=4)
    Button(popup, text='Quit', command=popup.quit).grid(row=3, column=1, sticky=W, pady=4)

    popup.mainloop()



# Ramen maken:
ramen = []
raam1 = Raam("raam1")
raam2 = Raam("raam2")
raam3 = Raam("raam3")
raam4 = Raam("raam4")
ramen.append(raam1)
ramen.append(raam2)
ramen.append(raam3)
ramen.append(raam4)

# Main Window code:
mainScreen = Tk()
mainScreen.title("Admin Panel")
#mainScreen.geometry('350x200')
mainWindow = Frame(mainScreen)
viewSelect = Frame(mainScreen)

labels = []

def printMainScreen():
    i = 0
    for raam in ramen:
        # Print naam raam:
        lbl = Label(mainWindow, text=raam.getName())

        # Print status raam:
        if raam.getMode() == True:
            lbl2 = Label(mainWindow, text="Automatisch")

        else:
            lbl2 = Label(mainWindow, text="Handmatig")

        # Print rolluikPercentage:
        lbl3 = Label(mainWindow, text=str(raam.getRolluik()) + "%")

        # Print Modeknop:
        def veranderMode(i):
            ramen[i].changeMode()
            updateMainScreen()

        veranderModeI = partial(veranderMode, i)

        btn = Button(mainWindow, text="Verander mode", command=veranderModeI)

        settingsI = partial(settingsWindow, i)

        btn2 = Button(mainWindow, text="Settings", command=settingsI)

        # Alle collumnen in grid zetten:
        lbl.grid(column=0, row=i)
        lbl2.grid(column=1, row=i)
        lbl3.grid(column=2, row=i)
        btn.grid(column=3, row=i)
        btn2.grid(column=4, row=i)

        labels.append(lbl)
        labels.append(lbl2)
        labels.append(lbl3)

        i = i+1

    btn = Button(viewSelect, text="Temperatuur Lijn view")
    btn2 = Button(viewSelect, text="Temperatuur Staaf view")
    btn3 = Button(viewSelect, text="Licht lijn view")
    btn4 = Button(viewSelect, text="Licht staaf view")

    btn.grid(column=0, row=(i))
    btn2.grid(column=1, row=(i))
    btn3.grid(column=2, row=(i))
    btn4.grid(column=3, row=(i))

def updateMainScreen():
    i = 0
    # Delete labels:
    for label in labels:
        label.destroy()

    for raam in ramen:

        # Print naam raam:
        lbl = Label(mainWindow, text=raam.getName())

        # Print status raam:
        if raam.getMode() == True:
            lbl2 = Label(mainWindow, text="Automatisch")

        else:
            lbl2 = Label(mainWindow, text="Handmatig")

        # Print rolluikPercentage:
        lbl3 = Label(mainWindow, text=str(raam.getRolluik()) + "%")

        # Alle collumnen in grid zetten:
        lbl.grid(column=0, row=i)
        lbl2.grid(column=1, row=i)
        lbl3.grid(column=2, row=i)

        i = i+1

        labels.append(lbl)
        labels.append(lbl2)
        labels.append(lbl3)

root = Frame(mainScreen)
#root.title('simple plot')

canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)

Button(root, text='Pause', command=pause).pack()
Button(root, text='Quit', command=root.quit).pack()

canvas.create_line(50,550,1150,550, width=2) # x-axis
canvas.create_line(50,550,50,50, width=2)    # y-axis

# x-axis
for i in range(23):
    x = 50 + (i * 50)
    canvas.create_line(x,550,x,50, width=1, dash=(2,5))
    canvas.create_text(x,550, text='%d'% (10*i), anchor=N)

# y-axis
for i in range(11):
    y = 550 - (i * 50)
    canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
    canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

canvas.after(300, step)

root.grid(column=0, row=0)
mainWindow.grid(column=0, row=1, sticky=W)
viewSelect.grid(column=0, row=2, sticky=W)

printMainScreen()
mainWindow.mainloop()





