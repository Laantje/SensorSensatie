from GUI import *
from database import *
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import *
from tkinter.ttk import *

class lijngrafiek(Toplevel1):
    def __init__(self,frame):
        #super().__init__()
        #self.com = com
        #self.data =
        self.frame=frame
    def build(self):
        #self.root = Frame(self.frame)
        f = Figure(figsize=(1, 1), dpi=100)
        ax = f.add_subplot(111)
        data =[22,21,23,24,25,35,22,23,24]
        n = len(data)
        ind = numpy.arange(n)  # the x locations for the groups
        width = .35

        rects1 = ax.bar(ind, data, width, label='temperatuur')

        ax.set_ylabel('temperatuur')

        # ax.set_xticklabels(('leeg veld','maandag','dinsdag','woensdag','Donderdag','Vrijdag','zaterdag','Zondag'))
        ax.set_xticks(ind)
        ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'))
        canvas = FigureCanvasTkAgg(f, master=self.frame)

        canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)


class tabel(Toplevel1):
    def __init__(self,frame):
        self.frame = frame
    def build(self):
        table = Treeview(self.frame, columns=("uur", "value"), show='headings')
        table.column("uur", width=100)
        table.column("value", width=100)
        table.heading("uur", text="uur")
        table.heading("value", text="Waarde")
        table.grid(column=1, row=0, sticky=NSEW)
