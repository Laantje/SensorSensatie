from tkinter import *
from tkinter.ttk import *
from random import randint
from functools import partial
import matplotlib, numpy
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import time

class Raam:
    def __init__(self, name, port):
        self.name = name
        self.port = port
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
global p
p = 0

def step():
    if bool1 == True:
        global s, x2, y2
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            canvas.delete('temp') # only delete items tagged as temp
            table.delete()
            treevieuw()

        x1 = x2
        y1 = y2
        x2 = 50 + s*50
        temp = randint(min,max)
        y2 = value_to_y(temp)
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        table.insert('', 'end', value=['lalal', y2])

        #print(s, x1, y1, x2, y2)
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

def nieuwRaamWindow():
    popup = Tk()
    popup.title("Raam toevoegen")
    popup.geometry('350x200')

    Label(popup, text="Raam naam").grid(row=0, sticky=W)
    Label(popup, text="Poort").grid(row=1, sticky=W)

    e1 = Entry(popup)
    e2 = Entry(popup)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    def raamToevoegen():
        raam = Raam(str(e1.get()), str(e2.get()))
        ramen.append(raam)
        printMainWindow()

    Button(popup, text='Update', command=raamToevoegen).grid(row=3, column=0, sticky=W, pady=4)
    Button(popup, text='Quit', command=popup.quit).grid(row=3, column=1, sticky=W, pady=4)

    popup.mainloop()

# Ramen maken:
ramen = []
"""raam1 = Raam("raam1")
raam2 = Raam("raam2")
raam3 = Raam("raam3")
raam4 = Raam("raam4")
ramen.append(raam1)
ramen.append(raam2)
ramen.append(raam3)
ramen.append(raam4)"""

# Main Window code:
mainScreen = Tk()
mainScreen.title("Admin Panel")
#mainScreen.geometry('350x200')
mainWindow = Frame(mainScreen)
viewSelect = Frame(mainScreen)
adminPanel = Frame(mainScreen)

labels = []
buttons = []

def printMainWindow():
    # Delete labels:
    for label in labels:
        label.destroy()

    for button in buttons:
        button.destroy()

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

        def verwijderWindow(i):
            ramen.remove(ramen[i])
            printMainWindow()

        veranderModeI = partial(veranderMode, i)

        btn = Button(mainWindow, text="Verander mode", command=veranderModeI)

        settingsI = partial(settingsWindow, i)

        btn2 = Button(mainWindow, text="Settings", command=settingsI)

        verwijderI = partial(verwijderWindow, i)

        btn3 = Button(mainWindow, text="Verwijder", command=verwijderI)



        # Alle collumnen in grid zetten:
        lbl.grid(column=0, row=i, padx=(1, 0), pady=1)
        lbl2.grid(column=1, row=i, padx=(1, 0), pady=1)
        lbl3.grid(column=2, row=i, padx=(1, 0), pady=1)
        btn.grid(column=3, row=i, padx=(1, 0), pady=1)
        btn2.grid(column=4, row=i, padx=(1, 0), pady=1)
        btn3.grid(column=5, row=i, padx=(1, 0), pady=1)

        labels.append(lbl)
        labels.append(lbl2)
        labels.append(lbl3)

        buttons.append(btn)
        buttons.append(btn2)
        buttons.append(btn3)

        i = i+1

def printViewWindow():
    btn = Button(viewSelect, text="Temperatuur Lijn view", command = lijngrafiek)
    btn2 = Button(viewSelect, text="Temperatuur Staaf view", command= staafdiagram )
    btn3 = Button(viewSelect, text="Licht lijn view")
    btn4 = Button(viewSelect, text="Licht staaf view")

    btn.grid(column=0, row=(0))
    btn2.grid(column=1, row=(0))
    btn3.grid(column=2, row=(0))
    btn4.grid(column=3, row=(0))

def printAdminPanel():
    btn = Button(adminPanel, text="Nieuw Raam", command=nieuwRaamWindow)
    btn.grid(column=0, row=(0))

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

def lijngrafiek():
    global p, root, canvas
    if (p>=1):
        root.destroy()

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

    root.grid(column=0, row=0)
    treevieuw()
    canvas.after(300, step)
    p=+1

def staafdiagram():
    global p, root
    if (p>=1):
        root.destroy()
    root = Frame(mainScreen)
    f = Figure(figsize=(12, 5), dpi=100)
    ax = f.add_subplot(111)
    data = (20, 35, 30, 35, 27, 55, 66, 23, 44, 60, 6, 2, 5)
    n = len(data)
    ind = numpy.arange(n)  # the x locations for the groups
    width = .35

    rects1 = ax.bar(ind, data, width, label='temperatuur')

    ax.set_ylabel('temperatuur')

    # ax.set_xticklabels(('leeg veld','maandag','dinsdag','woensdag','Donderdag','Vrijdag','zaterdag','Zondag'))
    ax.set_xticks(ind)
    ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'))
    ax.legend()
    canvas = FigureCanvasTkAgg(f, master=root)
    # canvas.show()
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)
    root.grid(column=0,row=0)
    treevieuw()
    p=+1


def treevieuw():

    global table
    table = Treeview(mainScreen, columns=("uur", "value"), show='headings')
    table.column("uur", width=100)
    table.column("value", width=100)
    table.heading("uur", text="uur")
    table.heading("value", text="Waarde")
    table.grid(column=1, row=0, sticky=NSEW)


mainWindow.grid(column=0, row=1, sticky=W)
viewSelect.grid(column=0, row=2, sticky=W)
adminPanel.grid(column=0, row=3, sticky=W)


printMainWindow()
printViewWindow()
printAdminPanel()
mainScreen.mainloop()





