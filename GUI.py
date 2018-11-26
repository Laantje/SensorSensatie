from tkinter import *
import sys
from velden import *
from database import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import test_support

from matplotlib import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    test_support.init(root, top)
    top.add_table(top.TFrame4)
    top.add_table(top.TFrame7)
    top.add_table(top.TFrame10)
    top.add_table(top.TFrame13)
    top.add_table(top.TFrame16)
    root.mainloop()



w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    test_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1357x844+281+69")
        top.title("Centrale")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var1.set(0)
        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.0, rely=0.0, relheight=0.053, relwidth=0.991)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(width=1325)

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.0, rely=0.222, height=24, width=86)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font9)
        self.TLabel1.configure(relief='flat')
        self.TLabel1.configure(text='''Handmatig:''')

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton1.place(relx=0.059, rely=0.222, relwidth=0.031
                , relheight=0.0, height=26)
        self.TRadiobutton1.configure(text='''Uit''', variable=self.var1, value=0, command= self.handmatigUit)

        self.TRadiobutton2 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton2.place(relx=0.097, rely=0.222, relwidth=0.036
                , relheight=0.0, height=26)
        self.TRadiobutton2.configure(text='''Aan''', variable=self.var1, value=1, command= self.handmatigAan)

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.149, rely=0.222, height=24, width=107)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font9)
        self.TLabel2.configure(relief='flat')
        self.TLabel2.configure(text='''Alle schermen:''')

        self.TRadiobutton3 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton3.place(relx=0.223, rely=0.222, relwidth=0.06
                , relheight=0.0, height=26)
        self.TRadiobutton3.configure(takefocus="")
        self.TRadiobutton3.configure(text='''Oprollen''', variable=self.var2, value=0)

        self.TRadiobutton4 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton4.place(relx=0.283, rely=0.222, relwidth=0.059
                , relheight=0.0, height=26)
        self.TRadiobutton4.configure(takefocus="")
        self.TRadiobutton4.configure(text='''Uitrollen''', variable=self.var2, value=1)

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.394, rely=0.222, height=24, width=116)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief='flat')
        self.TLabel3.configure(text='''Op- of uitgerold:''')

        self.Label4 = tk.Label(self.TFrame1)
        self.Label4.place(relx=0.476, rely=0.222, height=26, width=17)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''1:''')

        self.Label5 = tk.Label(self.TFrame1)
        self.Label5.place(relx=0.58, rely=0.222, height=26, width=17)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''2:''')

        self.Label6 = tk.Label(self.TFrame1)
        self.Label6.place(relx=0.684, rely=0.222, height=26, width=17)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''3:''')

        self.Label7 = tk.Label(self.TFrame1)
        self.Label7.place(relx=0.788, rely=0.222, height=26, width=17)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''4:''')

        self.Label8 = tk.Label(self.TFrame1)
        self.Label8.place(relx=0.892, rely=0.222, height=26, width=14)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''5:''')

        self.TProgressbar1 = ttk.Progressbar(self.TFrame1)
        self.TProgressbar1.place(relx=0.491, rely=0.222, relwidth=0.074
                                 , relheight=0.0, height=22)

        self.TProgressbar2 = ttk.Progressbar(self.TFrame1)
        self.TProgressbar2.place(relx=0.595, rely=0.222, relwidth=0.074
                , relheight=0.0, height=22)

        self.TProgressbar3 = ttk.Progressbar(self.TFrame1)
        self.TProgressbar3.place(relx=0.699, rely=0.222, relwidth=0.074
                , relheight=0.0, height=22)

        self.TProgressbar4 = ttk.Progressbar(self.TFrame1)
        self.TProgressbar4.place(relx=0.803, rely=0.222, relwidth=0.074
                , relheight=0.0, height=22)

        self.TProgressbar5 = ttk.Progressbar(self.TFrame1)
        self.TProgressbar5.place(relx=0.907, rely=0.222, relwidth=0.074
                , relheight=0.0, height=22)

        self.TFrame2 = ttk.Frame(top) # eerste blok
        self.TFrame2.place(relx=0.0, rely=0.047, relheight=0.19, relwidth=0.991)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(width=1325)

        self.TFrame3 = ttk.Frame(self.TFrame2)
        self.TFrame3.place(relx=0.004, rely=0.031, relheight=0.906
                , relwidth=0.227)
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(width=305)

        self.TFrame4 = ttk.Frame(self.TFrame2)
        self.TFrame4.place(relx=0.242, rely=0.031, relheight=0.906
                , relwidth=0.16)
        self.TFrame4.configure(relief='groove')
        self.TFrame4.configure(borderwidth="2")
        self.TFrame4.configure(relief='groove')
        self.TFrame4.configure(width=215)

        self.TLabel9 = ttk.Label(self.TFrame2)
        self.TLabel9.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font=font9)
        self.TLabel9.configure(relief='flat')
        self.TLabel9.configure(text='''Diagrammen''')

        self.TButton1 = ttk.Button(self.TFrame2)
        self.TButton1.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Lijndiagram''')

        self.TButton2 = ttk.Button(self.TFrame2)
        self.TButton2.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Staafdiagram''')
        self.TButton2.configure(command=lambda: self.add_bar(self.TFrame3))

        self.TLabel10 = ttk.Label(self.TFrame2)
        self.TLabel10.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font9)
        self.TLabel10.configure(relief='flat')
        self.TLabel10.configure(text='''Maximale rolstand''')

        self.TLabel11 = ttk.Label(self.TFrame2)
        self.TLabel11.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font="TkDefaultFont")
        self.TLabel11.configure(relief='flat')
        self.TLabel11.configure(wraplength="0")
        self.TLabel11.configure(takefocus="0")
        self.TLabel11.configure(text='''Oprollen:''')
        self.TLabel11.configure(width=0)

        self.TLabel12 = ttk.Label(self.TFrame2)
        self.TLabel12.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief='flat')
        self.TLabel12.configure(wraplength="0")
        self.TLabel12.configure(takefocus="0")
        self.TLabel12.configure(text='''%''')
        self.TLabel12.configure(width=0)

        self.TLabel13 = ttk.Label(self.TFrame2)
        self.TLabel13.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel13.configure(background="#d9d9d9")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font="TkDefaultFont")
        self.TLabel13.configure(relief='flat')
        self.TLabel13.configure(wraplength="0")
        self.TLabel13.configure(takefocus="0")
        self.TLabel13.configure(text='''Uitrollen:''')
        self.TLabel13.configure(width=0)

        self.TLabel14 = ttk.Label(self.TFrame2)
        self.TLabel14.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font="TkDefaultFont")
        self.TLabel14.configure(relief='flat')
        self.TLabel14.configure(wraplength="0")
        self.TLabel14.configure(takefocus="0")
        self.TLabel14.configure(text='''%''')
        self.TLabel14.configure(width=0)

        self.Scale1 = tk.Scale(self.TFrame2)
        self.Scale1.place(relx=0.584, rely=0.17, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale1.configure(activebackground="#ececec")
        self.Scale1.configure(background="#d9d9d9")
        self.Scale1.configure(font="TkTextFont")
        self.Scale1.configure(foreground="#000000")
        self.Scale1.configure(highlightbackground="#d9d9d9")
        self.Scale1.configure(highlightcolor="black")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="#d9d9d9")

        self.Scale2 = tk.Scale(self.TFrame2)
        self.Scale2.place(relx=0.584, rely=0.40, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale2.configure(activebackground="#ececec")
        self.Scale2.configure(background="#d9d9d9")
        self.Scale2.configure(font="TkTextFont")
        self.Scale2.configure(foreground="#000000")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="black")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(troughcolor="#d9d9d9")

        self.TButton3 = ttk.Button(self.TFrame2)
        self.TButton3.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Submit''')

        self.TLabel15 = ttk.Label(self.TFrame2)
        self.TLabel15.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel15.configure(background="#d9d9d9")
        self.TLabel15.configure(foreground="#000000")
        self.TLabel15.configure(font=font9)
        self.TLabel15.configure(relief='flat')
        self.TLabel15.configure(text='''Waarde op/uitrollen''')

        self.Entry1 = tk.Entry(self.TFrame2)
        self.Entry1.place(relx=0.73, rely=0.38,height=24, relwidth=0.04)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.TButton4 = ttk.Button(self.TFrame2)
        self.TButton4.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Submit''')

        self.TLabel16 = ttk.Label(self.TFrame2)
        self.TLabel16.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel16.configure(background="#d9d9d9")
        self.TLabel16.configure(foreground="#000000")
        self.TLabel16.configure(font=font9)
        self.TLabel16.configure(relief='flat')
        self.TLabel16.configure(text='''Handmatig''')

        self.var3 = StringVar()

        self.TRadiobutton5 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton5.place(relx=0.848, rely=0.26, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton5.configure(text='''Oprollen''', variable=self.var3, value=0)

        self.TRadiobutton6 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton6.place(relx=0.848, rely=0.5, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton6.configure(text='''Uitrollen''', variable=self.var3, value=1)

        self.TButton5 = ttk.Button(self.TFrame2)
        self.TButton5.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''X''')

        self.TButton6 = ttk.Button(self.TFrame2)
        self.TButton6.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''V''')

        self.TFrame5 = ttk.Frame(top) # begin 2e blok
        self.TFrame5.place(relx=0.0, rely=0.231, relheight=0.19, relwidth=0.991)
        self.TFrame5.configure(relief='groove')
        self.TFrame5.configure(borderwidth="2")
        self.TFrame5.configure(relief='groove')
        self.TFrame5.configure(width=1325)

        self.TFrame6 = ttk.Frame(self.TFrame5)
        self.TFrame6.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame6.configure(relief='groove')
        self.TFrame6.configure(borderwidth="2")
        self.TFrame6.configure(relief='groove')
        self.TFrame6.configure(width=305)

        self.TFrame7 = ttk.Frame(self.TFrame5)
        self.TFrame7.place(relx=0.242, rely=0.031, relheight=0.906
                            , relwidth=0.16)
        self.TFrame7.configure(relief='groove')
        self.TFrame7.configure(borderwidth="2")
        self.TFrame7.configure(relief='groove')
        self.TFrame7.configure(width=215)

        self.TLabel17 = ttk.Label(self.TFrame5)
        self.TLabel17.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel17.configure(background="#d9d9d9")
        self.TLabel17.configure(foreground="#000000")
        self.TLabel17.configure(font=font9)
        self.TLabel17.configure(relief='flat')
        self.TLabel17.configure(text='''Diagrammen''')

        self.TButton7 = ttk.Button(self.TFrame5)
        self.TButton7.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(text='''Lijndiagram''')


        self.TButton8 = ttk.Button(self.TFrame5)
        self.TButton8.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(text='''Staafdiagram''')
        self.TButton8.configure(command=lambda: self.add_bar(self.TFrame6))

        self.TLabel18 = ttk.Label(self.TFrame5)
        self.TLabel18.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel18.configure(background="#d9d9d9")
        self.TLabel18.configure(foreground="#000000")
        self.TLabel18.configure(font=font9)
        self.TLabel18.configure(relief='flat')
        self.TLabel18.configure(text='''Maximale rolstand''')

        self.TLabel19 = ttk.Label(self.TFrame5)
        self.TLabel19.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel19.configure(background="#d9d9d9")
        self.TLabel19.configure(foreground="#000000")
        self.TLabel19.configure(font="TkDefaultFont")
        self.TLabel19.configure(relief='flat')
        self.TLabel19.configure(wraplength="0")
        self.TLabel19.configure(takefocus="0")
        self.TLabel19.configure(text='''Oprollen:''')
        self.TLabel19.configure(width=0)

        self.TLabel20 = ttk.Label(self.TFrame5)
        self.TLabel20.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel20.configure(background="#d9d9d9")
        self.TLabel20.configure(foreground="#000000")
        self.TLabel20.configure(font="TkDefaultFont")
        self.TLabel20.configure(relief='flat')
        self.TLabel20.configure(wraplength="0")
        self.TLabel20.configure(takefocus="0")
        self.TLabel20.configure(text='''%''')
        self.TLabel20.configure(width=0)

        self.TLabel21 = ttk.Label(self.TFrame5)
        self.TLabel21.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel21.configure(background="#d9d9d9")
        self.TLabel21.configure(foreground="#000000")
        self.TLabel21.configure(font="TkDefaultFont")
        self.TLabel21.configure(relief='flat')
        self.TLabel21.configure(wraplength="0")
        self.TLabel21.configure(takefocus="0")
        self.TLabel21.configure(text='''Uitrollen:''')
        self.TLabel21.configure(width=0)

        self.TLabel22 = ttk.Label(self.TFrame5)
        self.TLabel22.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel22.configure(background="#d9d9d9")
        self.TLabel22.configure(foreground="#000000")
        self.TLabel22.configure(font="TkDefaultFont")
        self.TLabel22.configure(relief='flat')
        self.TLabel22.configure(wraplength="0")
        self.TLabel22.configure(takefocus="0")
        self.TLabel22.configure(text='''%''')
        self.TLabel22.configure(width=0)

        self.Scale3 = tk.Scale(self.TFrame5)
        self.Scale3.place(relx=0.584, rely=0.17, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale3.configure(activebackground="#ececec")
        self.Scale3.configure(background="#d9d9d9")
        self.Scale3.configure(font="TkTextFont")
        self.Scale3.configure(foreground="#000000")
        self.Scale3.configure(highlightbackground="#d9d9d9")
        self.Scale3.configure(highlightcolor="black")
        self.Scale3.configure(orient="horizontal")
        self.Scale3.configure(troughcolor="#d9d9d9")

        self.Scale4 = tk.Scale(self.TFrame5)
        self.Scale4.place(relx=0.584, rely=0.40, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale4.configure(activebackground="#ececec")
        self.Scale4.configure(background="#d9d9d9")
        self.Scale4.configure(font="TkTextFont")
        self.Scale4.configure(foreground="#000000")
        self.Scale4.configure(highlightbackground="#d9d9d9")
        self.Scale4.configure(highlightcolor="black")
        self.Scale4.configure(orient="horizontal")
        self.Scale4.configure(troughcolor="#d9d9d9")

        self.TButton9 = ttk.Button(self.TFrame5)
        self.TButton9.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton9.configure(takefocus="")
        self.TButton9.configure(text='''Submit''')

        self.TLabel23 = ttk.Label(self.TFrame5)
        self.TLabel23.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel23.configure(background="#d9d9d9")
        self.TLabel23.configure(foreground="#000000")
        self.TLabel23.configure(font=font9)
        self.TLabel23.configure(relief='flat')
        self.TLabel23.configure(text='''Waarde op/uitrollen''')

        self.Entry2 = tk.Entry(self.TFrame5)
        self.Entry2.place(relx=0.73, rely=0.38, height=24, relwidth=0.04)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.TButton10 = ttk.Button(self.TFrame5)
        self.TButton10.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton10.configure(takefocus="")
        self.TButton10.configure(text='''Submit''')

        self.TLabel24 = ttk.Label(self.TFrame5)
        self.TLabel24.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel24.configure(background="#d9d9d9")
        self.TLabel24.configure(foreground="#000000")
        self.TLabel24.configure(font=font9)
        self.TLabel24.configure(relief='flat')
        self.TLabel24.configure(text='''Handmatig''')

        self.var4 = StringVar()

        self.TRadiobutton7 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton7.place(relx=0.848, rely=0.26, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton7.configure(text='''Oprollen''', variable=self.var4, value=0)

        self.TRadiobutton8 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton8.place(relx=0.848, rely=0.5, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton8.configure(text='''Uitrollen''', variable=self.var4, value=1)

        self.TButton11 = ttk.Button(self.TFrame5)
        self.TButton11.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton11.configure(takefocus="")
        self.TButton11.configure(text='''X''')

        self.TButton12 = ttk.Button(self.TFrame5)
        self.TButton12.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton12.configure(takefocus="")
        self.TButton12.configure(text='''V''')

        self.TFrame8 = ttk.Frame(top)
        self.TFrame8.place(relx=0.0, rely=0.782, relheight=0.19, relwidth=0.991)
        self.TFrame8.configure(relief='groove')
        self.TFrame8.configure(borderwidth="2")
        self.TFrame8.configure(relief='groove')
        self.TFrame8.configure(width=1325)

        self.TFrame9 = ttk.Frame(self.TFrame8)
        self.TFrame9.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame9.configure(relief='groove')
        self.TFrame9.configure(borderwidth="2")
        self.TFrame9.configure(relief='groove')
        self.TFrame9.configure(width=305)

        self.TFrame10 = ttk.Frame(self.TFrame8)
        self.TFrame10.place(relx=0.242, rely=0.031, relheight=0.906
                            , relwidth=0.16)
        self.TFrame10.configure(relief='groove')
        self.TFrame10.configure(borderwidth="2")
        self.TFrame10.configure(relief='groove')
        self.TFrame10.configure(width=215)

        self.TLabel25 = ttk.Label(self.TFrame8)
        self.TLabel25.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel25.configure(background="#d9d9d9")
        self.TLabel25.configure(foreground="#000000")
        self.TLabel25.configure(font=font9)
        self.TLabel25.configure(relief='flat')
        self.TLabel25.configure(text='''Diagrammen''')


        self.TButton13 = ttk.Button(self.TFrame8)
        self.TButton13.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton13.configure(takefocus="")
        self.TButton13.configure(text='''Lijndiagram''')

        self.TButton14 = ttk.Button(self.TFrame8)
        self.TButton14.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton14.configure(takefocus="")
        self.TButton14.configure(text='''Staafdiagram''')
        self.TButton14.configure(command=lambda: self.add_bar(self.TFrame9))

        self.TLabel26 = ttk.Label(self.TFrame8)
        self.TLabel26.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel26.configure(background="#d9d9d9")
        self.TLabel26.configure(foreground="#000000")
        self.TLabel26.configure(font=font9)
        self.TLabel26.configure(relief='flat')
        self.TLabel26.configure(text='''Maximale rolstand''')

        self.TLabel27 = ttk.Label(self.TFrame8)
        self.TLabel27.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel27.configure(background="#d9d9d9")
        self.TLabel27.configure(foreground="#000000")
        self.TLabel27.configure(font="TkDefaultFont")
        self.TLabel27.configure(relief='flat')
        self.TLabel27.configure(wraplength="0")
        self.TLabel27.configure(takefocus="0")
        self.TLabel27.configure(text='''Oprollen:''')
        self.TLabel27.configure(width=0)

        self.TLabel28 = ttk.Label(self.TFrame8)
        self.TLabel28.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel28.configure(background="#d9d9d9")
        self.TLabel28.configure(foreground="#000000")
        self.TLabel28.configure(font="TkDefaultFont")
        self.TLabel28.configure(relief='flat')
        self.TLabel28.configure(wraplength="0")
        self.TLabel28.configure(takefocus="0")
        self.TLabel28.configure(text='''%''')
        self.TLabel28.configure(width=0)

        self.TLabel29 = ttk.Label(self.TFrame8)
        self.TLabel29.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel29.configure(background="#d9d9d9")
        self.TLabel29.configure(foreground="#000000")
        self.TLabel29.configure(font="TkDefaultFont")
        self.TLabel29.configure(relief='flat')
        self.TLabel29.configure(wraplength="0")
        self.TLabel29.configure(takefocus="0")
        self.TLabel29.configure(text='''Uitrollen:''')
        self.TLabel29.configure(width=0)

        self.TLabel30 = ttk.Label(self.TFrame8)
        self.TLabel30.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel30.configure(background="#d9d9d9")
        self.TLabel30.configure(foreground="#000000")
        self.TLabel30.configure(font="TkDefaultFont")
        self.TLabel30.configure(relief='flat')
        self.TLabel30.configure(wraplength="0")
        self.TLabel30.configure(takefocus="0")
        self.TLabel30.configure(text='''%''')
        self.TLabel30.configure(width=0)

        self.Scale5 = tk.Scale(self.TFrame8)
        self.Scale5.place(relx=0.584, rely=0.17, relwidth=0.074, relheight=0.0
                           , height=47, bordermode='ignore')
        self.Scale5.configure(activebackground="#ececec")
        self.Scale5.configure(background="#d9d9d9")
        self.Scale5.configure(font="TkTextFont")
        self.Scale5.configure(foreground="#000000")
        self.Scale5.configure(highlightbackground="#d9d9d9")
        self.Scale5.configure(highlightcolor="black")
        self.Scale5.configure(orient="horizontal")
        self.Scale5.configure(troughcolor="#d9d9d9")

        self.Scale5 = tk.Scale(self.TFrame8)
        self.Scale5.place(relx=0.584, rely=0.40, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale5.configure(activebackground="#ececec")
        self.Scale5.configure(background="#d9d9d9")
        self.Scale5.configure(font="TkTextFont")
        self.Scale5.configure(foreground="#000000")
        self.Scale5.configure(highlightbackground="#d9d9d9")
        self.Scale5.configure(highlightcolor="black")
        self.Scale5.configure(orient="horizontal")
        self.Scale5.configure(troughcolor="#d9d9d9")

        self.TButton15 = ttk.Button(self.TFrame8)
        self.TButton15.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton15.configure(takefocus="")
        self.TButton15.configure(text='''Submit''')

        self.TLabel31 = ttk.Label(self.TFrame8)
        self.TLabel31.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel31.configure(background="#d9d9d9")
        self.TLabel31.configure(foreground="#000000")
        self.TLabel31.configure(font=font9)
        self.TLabel31.configure(relief='flat')
        self.TLabel31.configure(text='''Waarde op/uitrollen''')

        self.Entry3 = tk.Entry(self.TFrame8)
        self.Entry3.place(relx=0.73, rely=0.38, height=24, relwidth=0.04)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.TButton16 = ttk.Button(self.TFrame8)
        self.TButton16.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton16.configure(takefocus="")
        self.TButton16.configure(text='''Submit''')

        self.TLabel32 = ttk.Label(self.TFrame8)
        self.TLabel32.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel32.configure(background="#d9d9d9")
        self.TLabel32.configure(foreground="#000000")
        self.TLabel32.configure(font=font9)
        self.TLabel32.configure(relief='flat')
        self.TLabel32.configure(text='''Handmatig''')

        self.var5 = StringVar()

        self.TRadiobutton9 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton9.place(relx=0.848, rely=0.26, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton9.configure(text='''Oprollen''', variable=self.var5, value=0)

        self.TRadiobutton10 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton10.place(relx=0.848, rely=0.5, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton10.configure(text='''Uitrollen''', variable=self.var5, value=1)

        self.TButton17 = ttk.Button(self.TFrame8)
        self.TButton17.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton17.configure(takefocus="")
        self.TButton17.configure(text='''X''')

        self.TButton18 = ttk.Button(self.TFrame8)
        self.TButton18.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton18.configure(takefocus="")
        self.TButton18.configure(text='''V''')

        self.TFrame11 = ttk.Frame(top)
        self.TFrame11.place(relx=0.0, rely=0.598, relheight=0.19, relwidth=0.991)
        self.TFrame11.configure(relief='groove')
        self.TFrame11.configure(borderwidth="2")
        self.TFrame11.configure(relief='groove')
        self.TFrame11.configure(width=1325)

        self.TFrame12 = ttk.Frame(self.TFrame11)
        self.TFrame12.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame12.configure(relief='groove')
        self.TFrame12.configure(borderwidth="2")
        self.TFrame12.configure(relief='groove')
        self.TFrame12.configure(width=305)

        self.TFrame13 = ttk.Frame(self.TFrame11)
        self.TFrame13.place(relx=0.242, rely=0.031, relheight=0.906
                            , relwidth=0.16)
        self.TFrame13.configure(relief='groove')
        self.TFrame13.configure(borderwidth="2")
        self.TFrame13.configure(relief='groove')
        self.TFrame13.configure(width=215)

        self.TLabel33 = ttk.Label(self.TFrame11)
        self.TLabel33.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel33.configure(background="#d9d9d9")
        self.TLabel33.configure(foreground="#000000")
        self.TLabel33.configure(font=font9)
        self.TLabel33.configure(relief='flat')
        self.TLabel33.configure(text='''Diagrammen''')

        self.TButton19 = ttk.Button(self.TFrame11)
        self.TButton19.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton19.configure(takefocus="")
        self.TButton19.configure(text='''Lijndiagram''')

        self.TButton20 = ttk.Button(self.TFrame11)
        self.TButton20.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton20.configure(takefocus="")
        self.TButton20.configure(text='''Staafdiagram''')
        self.TButton20.configure(command=lambda: self.add_bar(self.TFrame12))

        self.TLabel34 = ttk.Label(self.TFrame11)
        self.TLabel34.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel34.configure(background="#d9d9d9")
        self.TLabel34.configure(foreground="#000000")
        self.TLabel34.configure(font=font9)
        self.TLabel34.configure(relief='flat')
        self.TLabel34.configure(text='''Maximale rolstand''')

        self.TLabel35 = ttk.Label(self.TFrame11)
        self.TLabel35.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel35.configure(background="#d9d9d9")
        self.TLabel35.configure(foreground="#000000")
        self.TLabel35.configure(font="TkDefaultFont")
        self.TLabel35.configure(relief='flat')
        self.TLabel35.configure(wraplength="0")
        self.TLabel35.configure(takefocus="0")
        self.TLabel35.configure(text='''Oprollen:''')
        self.TLabel35.configure(width=0)

        self.TLabel36 = ttk.Label(self.TFrame11)
        self.TLabel36.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel36.configure(background="#d9d9d9")
        self.TLabel36.configure(foreground="#000000")
        self.TLabel36.configure(font="TkDefaultFont")
        self.TLabel36.configure(relief='flat')
        self.TLabel36.configure(wraplength="0")
        self.TLabel36.configure(takefocus="0")
        self.TLabel36.configure(text='''%''')
        self.TLabel36.configure(width=0)

        self.TLabel37 = ttk.Label(self.TFrame11)
        self.TLabel37.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel37.configure(background="#d9d9d9")
        self.TLabel37.configure(foreground="#000000")
        self.TLabel37.configure(font="TkDefaultFont")
        self.TLabel37.configure(relief='flat')
        self.TLabel37.configure(wraplength="0")
        self.TLabel37.configure(takefocus="0")
        self.TLabel37.configure(text='''Uitrollen:''')
        self.TLabel37.configure(width=0)

        self.TLabel38 = ttk.Label(self.TFrame11)
        self.TLabel38.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel38.configure(background="#d9d9d9")
        self.TLabel38.configure(foreground="#000000")
        self.TLabel38.configure(font="TkDefaultFont")
        self.TLabel38.configure(relief='flat')
        self.TLabel38.configure(wraplength="0")
        self.TLabel38.configure(takefocus="0")
        self.TLabel38.configure(text='''%''')
        self.TLabel38.configure(width=0)

        self.Scale6 = tk.Scale(self.TFrame11)
        self.Scale6.place(relx=0.584, rely=0.17, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale6.configure(activebackground="#ececec")
        self.Scale6.configure(background="#d9d9d9")
        self.Scale6.configure(font="TkTextFont")
        self.Scale6.configure(foreground="#000000")
        self.Scale6.configure(highlightbackground="#d9d9d9")
        self.Scale6.configure(highlightcolor="black")
        self.Scale6.configure(orient="horizontal")
        self.Scale6.configure(troughcolor="#d9d9d9")

        self.Scale7 = tk.Scale(self.TFrame11)
        self.Scale7.place(relx=0.584, rely=0.40, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale7.configure(activebackground="#ececec")
        self.Scale7.configure(background="#d9d9d9")
        self.Scale7.configure(font="TkTextFont")
        self.Scale7.configure(foreground="#000000")
        self.Scale7.configure(highlightbackground="#d9d9d9")
        self.Scale7.configure(highlightcolor="black")
        self.Scale7.configure(orient="horizontal")
        self.Scale7.configure(troughcolor="#d9d9d9")

        self.TButton21 = ttk.Button(self.TFrame11)
        self.TButton21.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton21.configure(takefocus="")
        self.TButton21.configure(text='''Submit''')

        self.TLabel39 = ttk.Label(self.TFrame11)
        self.TLabel39.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel39.configure(background="#d9d9d9")
        self.TLabel39.configure(foreground="#000000")
        self.TLabel39.configure(font=font9)
        self.TLabel39.configure(relief='flat')
        self.TLabel39.configure(text='''Waarde op/uitrollen''')

        self.Entry4 = tk.Entry(self.TFrame11)
        self.Entry4.place(relx=0.73, rely=0.38, height=24, relwidth=0.04)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.TButton22 = ttk.Button(self.TFrame11)
        self.TButton22.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton22.configure(takefocus="")
        self.TButton22.configure(text='''Submit''')

        self.TLabel40 = ttk.Label(self.TFrame11)
        self.TLabel40.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel40.configure(background="#d9d9d9")
        self.TLabel40.configure(foreground="#000000")
        self.TLabel40.configure(font=font9)
        self.TLabel40.configure(relief='flat')
        self.TLabel40.configure(text='''Handmatig''')

        self.var6 = StringVar()

        self.TRadiobutton11 = ttk.Radiobutton(self.TFrame11)
        self.TRadiobutton11.place(relx=0.848, rely=0.26, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton11.configure(text='''Oprollen''', variable=self.var6, value=0)

        self.TRadiobutton12 = ttk.Radiobutton(self.TFrame11)
        self.TRadiobutton12.place(relx=0.848, rely=0.5, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton12.configure(text='''Uitrollen''', variable=self.var6, value=1)

        self.TButton23 = ttk.Button(self.TFrame11)
        self.TButton23.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton23.configure(takefocus="")
        self.TButton23.configure(text='''X''')

        self.TButton24 = ttk.Button(self.TFrame11)
        self.TButton24.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton24.configure(takefocus="")
        self.TButton24.configure(text='''V''')

        self.TFrame14 = ttk.Frame(top)
        self.TFrame14.place(relx=0.0, rely=0.415, relheight=0.19, relwidth=0.991)
        self.TFrame14.configure(relief='groove')
        self.TFrame14.configure(borderwidth="2")
        self.TFrame14.configure(relief='groove')
        self.TFrame14.configure(width=1325)

        self.TFrame15 = ttk.Frame(self.TFrame14)
        self.TFrame15.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame15.configure(relief='groove')
        self.TFrame15.configure(borderwidth="2")
        self.TFrame15.configure(relief='groove')
        self.TFrame15.configure(width=305)

        self.TFrame16 = ttk.Frame(self.TFrame14)
        self.TFrame16.place(relx=0.242, rely=0.031, relheight=0.906
                               , relwidth=0.16)
        self.TFrame16.configure(relief='groove')
        self.TFrame16.configure(borderwidth="2")
        self.TFrame16.configure(relief='groove')
        self.TFrame16.configure(width=215)

        self.TLabel41 = ttk.Label(self.TFrame14)
        self.TLabel41.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel41.configure(background="#d9d9d9")
        self.TLabel41.configure(foreground="#000000")
        self.TLabel41.configure(font=font9)
        self.TLabel41.configure(relief='flat')
        self.TLabel41.configure(text='''Diagrammen''')

        self.TButton25 = ttk.Button(self.TFrame14)
        self.TButton25.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton25.configure(takefocus="")
        self.TButton25.configure(text='''Lijndiagram''')

        self.TButton26 = ttk.Button(self.TFrame14)
        self.TButton26.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton26.configure(takefocus="")
        self.TButton26.configure(text='''Staafdiagram''')
        self.TButton26.configure(command=lambda: self.add_bar(self.TFrame15))

        self.TLabel42 = ttk.Label(self.TFrame14)
        self.TLabel42.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel42.configure(background="#d9d9d9")
        self.TLabel42.configure(foreground="#000000")
        self.TLabel42.configure(font=font9)
        self.TLabel42.configure(relief='flat')
        self.TLabel42.configure(text='''Maximale rolstand''')

        self.TLabel43 = ttk.Label(self.TFrame14)
        self.TLabel43.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel43.configure(background="#d9d9d9")
        self.TLabel43.configure(foreground="#000000")
        self.TLabel43.configure(font="TkDefaultFont")
        self.TLabel43.configure(relief='flat')
        self.TLabel43.configure(wraplength="0")
        self.TLabel43.configure(takefocus="0")
        self.TLabel43.configure(text='''Oprollen:''')
        self.TLabel43.configure(width=0)

        self.TLabel44 = ttk.Label(self.TFrame14)
        self.TLabel44.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel44.configure(background="#d9d9d9")
        self.TLabel44.configure(foreground="#000000")
        self.TLabel44.configure(font="TkDefaultFont")
        self.TLabel44.configure(relief='flat')
        self.TLabel44.configure(wraplength="0")
        self.TLabel44.configure(takefocus="0")
        self.TLabel44.configure(text='''%''')
        self.TLabel44.configure(width=0)

        self.TLabel45 = ttk.Label(self.TFrame14)
        self.TLabel45.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel45.configure(background="#d9d9d9")
        self.TLabel45.configure(foreground="#000000")
        self.TLabel45.configure(font="TkDefaultFont")
        self.TLabel45.configure(relief='flat')
        self.TLabel45.configure(wraplength="0")
        self.TLabel45.configure(takefocus="0")
        self.TLabel45.configure(text='''Uitrollen:''')
        self.TLabel45.configure(width=0)

        self.TLabel46 = ttk.Label(self.TFrame14)
        self.TLabel46.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel46.configure(background="#d9d9d9")
        self.TLabel46.configure(foreground="#000000")
        self.TLabel46.configure(font="TkDefaultFont")
        self.TLabel46.configure(relief='flat')
        self.TLabel46.configure(wraplength="0")
        self.TLabel46.configure(takefocus="0")
        self.TLabel46.configure(text='''%''')
        self.TLabel46.configure(width=0)

        self.Scale8 = tk.Scale(self.TFrame14)
        self.Scale8.place(relx=0.584, rely=0.17, relwidth=0.074, relheight=0.0
                           , height=47, bordermode='ignore')
        self.Scale8.configure(activebackground="#ececec")
        self.Scale8.configure(background="#d9d9d9")
        self.Scale8.configure(font="TkTextFont")
        self.Scale8.configure(foreground="#000000")
        self.Scale8.configure(highlightbackground="#d9d9d9")
        self.Scale8.configure(highlightcolor="black")
        self.Scale8.configure(orient="horizontal")
        self.Scale8.configure(troughcolor="#d9d9d9")

        self.Scale9 = tk.Scale(self.TFrame14)
        self.Scale9.place(relx=0.584, rely=0.40, relwidth=0.074, relheight=0.0
                          , height=47, bordermode='ignore')
        self.Scale9.configure(activebackground="#ececec")
        self.Scale9.configure(background="#d9d9d9")
        self.Scale9.configure(font="TkTextFont")
        self.Scale9.configure(foreground="#000000")
        self.Scale9.configure(highlightbackground="#d9d9d9")
        self.Scale9.configure(highlightcolor="black")
        self.Scale9.configure(orient="horizontal")
        self.Scale9.configure(troughcolor="#d9d9d9")

        self.TButton27 = ttk.Button(self.TFrame14)
        self.TButton27.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton27.configure(takefocus="")
        self.TButton27.configure(text='''Submit''')

        self.TLabel47 = ttk.Label(self.TFrame14)
        self.TLabel47.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel47.configure(background="#d9d9d9")
        self.TLabel47.configure(foreground="#000000")
        self.TLabel47.configure(font=font9)
        self.TLabel47.configure(relief='flat')
        self.TLabel47.configure(text='''Waarde op/uitrollen''')

        self.Entry5 = tk.Entry(self.TFrame14)
        self.Entry5.place(relx=0.73, rely=0.38, height=24, relwidth=0.04)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.TButton28 = ttk.Button(self.TFrame14)
        self.TButton28.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton28.configure(takefocus="")
        self.TButton28.configure(text='''Submit''')

        self.TLabel48 = ttk.Label(self.TFrame14)
        self.TLabel48.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel48.configure(background="#d9d9d9")
        self.TLabel48.configure(foreground="#000000")
        self.TLabel48.configure(font=font9)
        self.TLabel48.configure(relief='flat')
        self.TLabel48.configure(text='''Handmatig''')

        self.var7 = StringVar()

        self.TRadiobutton13 = ttk.Radiobutton(self.TFrame14)
        self.TRadiobutton13.place(relx=0.848, rely=0.26, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton13.configure(text='''Oprollen''', variable=self.var7, value=0)

        self.TRadiobutton14 = ttk.Radiobutton(self.TFrame14)
        self.TRadiobutton14.place(relx=0.848, rely=0.5, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton14.configure(text='''Uitrollen''', variable=self.var7, value=1)

        self.TButton29 = ttk.Button(self.TFrame14)
        self.TButton29.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton29.configure(takefocus="")
        self.TButton29.configure(text='''X''')

        self.TButton30 = ttk.Button(self.TFrame14)
        self.TButton30.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton30.configure(takefocus="")
        self.TButton30.configure(text='''V''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


    def handmatigUit(self):
        self.TRadiobutton3.config(state='disable')
        self.TRadiobutton4.config(state='disable')
        self.TRadiobutton5.config(state='disable')
        self.TRadiobutton6.config(state='disable')
        self.TRadiobutton7.config(state='disable')
        self.TRadiobutton8.config(state='disable')
        self.TRadiobutton9.config(state='disable')
        self.TRadiobutton10.config(state='disable')
        self.TRadiobutton11.config(state='disable')
        self.TRadiobutton12.config(state='disable')
        self.TRadiobutton13.config(state='disable')
        self.TRadiobutton14.config(state='disable')
        self.Entry1.config(state='normal')
        self.Entry2.config(state='normal')
        self.Entry3.config(state='normal')
        self.Entry4.config(state='normal')
        self.Entry5.config(state='normal')
        self.TButton4.config(state='normal')
        self.TButton10.config(state='normal')
        self.TButton16.config(state='normal')
        self.TButton22.config(state='normal')
        self.TButton28.config(state='normal')

    def handmatigAan(self):
        self.TRadiobutton3.config(state='normal')
        self.TRadiobutton4.config(state='normal')
        self.TRadiobutton5.config(state='normal')
        self.TRadiobutton6.config(state='normal')
        self.TRadiobutton7.config(state='normal')
        self.TRadiobutton8.config(state='normal')
        self.TRadiobutton9.config(state='normal')
        self.TRadiobutton10.config(state='normal')
        self.TRadiobutton11.config(state='normal')
        self.TRadiobutton12.config(state='normal')
        self.TRadiobutton13.config(state='normal')
        self.TRadiobutton14.config(state='normal')
        self.Entry1.config(state='disable')
        self.Entry2.config(state='disable')
        self.Entry3.config(state='disable')
        self.Entry4.config(state='disable')
        self.Entry5.config(state='disable')
        self.TButton4.config(state='disable')
        self.TButton10.config(state='disable')
        self.TButton16.config(state='disable')
        self.TButton22.config(state='disable')
        self.TButton28.config(state='disable')

    def add_bar(self,frame):
        self.frame = frame
        x=lijngrafiek(self.frame)
        x.build()
    def add_table(self,frames):
        self.frames = frames
        y= tabel(self.frames)
        y.build()

    

if __name__ == '__main__':
    vp_start_gui()


