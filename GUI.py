from tkinter import *
import sys

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
        self.TLabel1.configure(text='''Alle schermen:''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.075, rely=0.222, height=24, width=107)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font=font9)
        self.TLabel2.configure(relief='flat')
        self.TLabel2.configure(text='''Handmatig:''')

        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton1.place(relx=0.13, rely=0.222, relwidth=0.031
                , relheight=0.0, height=26)
        self.TRadiobutton1.configure(text='''Uit''', variable=self.var1, value=0, command=self.AlleHandmatigUit)

        self.TRadiobutton2 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton2.place(relx=0.160, rely=0.222, relwidth=0.036
                , relheight=0.0, height=26)
        self.TRadiobutton2.configure(text='''Aan''', variable=self.var1, value=1, command=self.AlleHandmatigAan)

        self.TLabel3 = ttk.Label(self.TFrame1)
        self.TLabel3.place(relx=0.2, rely=0.222, height=24, width=107)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font=font9)
        self.TLabel3.configure(relief='flat')
        self.TLabel3.configure(text='''Op/uitrollen:''')

        self.TRadiobutton3 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton3.place(relx=0.263, rely=0.222, relwidth=0.06
                , relheight=0.0, height=26)
        self.TRadiobutton3.configure(takefocus="")
        self.TRadiobutton3.configure(text='''Oprollen''', variable=self.var2, value=0, state='disable')

        self.TRadiobutton4 = ttk.Radiobutton(self.TFrame1)
        self.TRadiobutton4.place(relx=0.323, rely=0.222, relwidth=0.059
                , relheight=0.0, height=26)
        self.TRadiobutton4.configure(takefocus="")
        self.TRadiobutton4.configure(text='''Uitrollen''', variable=self.var2, value=1, state='disable')

        self.TLabel4 = ttk.Label(self.TFrame1)
        self.TLabel4.place(relx=0.394, rely=0.222, height=24, width=116)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief='flat')
        self.TLabel4.configure(text='''Op- of uitgerold:''')

        self.Label5 = tk.Label(self.TFrame1)
        self.Label5.place(relx=0.476, rely=0.222, height=26, width=17)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''1:''')

        self.Label6 = tk.Label(self.TFrame1)
        self.Label6.place(relx=0.58, rely=0.222, height=26, width=17)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''2:''')

        self.Label7 = tk.Label(self.TFrame1)
        self.Label7.place(relx=0.684, rely=0.222, height=26, width=17)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''3:''')

        self.Label8 = tk.Label(self.TFrame1)
        self.Label8.place(relx=0.788, rely=0.222, height=26, width=17)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''4:''')

        self.Label9 = tk.Label(self.TFrame1)
        self.Label9.place(relx=0.892, rely=0.222, height=26, width=14)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''5:''')

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

        self.TFrame2 = ttk.Frame(top)
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

        self.TLabel10 = ttk.Label(self.TFrame2)
        self.TLabel10.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font=font9)
        self.TLabel10.configure(relief='flat')
        self.TLabel10.configure(text='''Diagrammen''')

        self.TButton1 = ttk.Button(self.TFrame2)
        self.TButton1.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Lijndiagram''')

        self.TButton2 = ttk.Button(self.TFrame2)
        self.TButton2.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Staafdiagram''')

        self.TLabel11 = ttk.Label(self.TFrame2)
        self.TLabel11.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font=font9)
        self.TLabel11.configure(relief='flat')
        self.TLabel11.configure(text='''Maximale rolstand''')

        self.TLabel12 = ttk.Label(self.TFrame2)
        self.TLabel12.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief='flat')
        self.TLabel12.configure(wraplength="0")
        self.TLabel12.configure(takefocus="0")
        self.TLabel12.configure(text='''Oprollen:''')
        self.TLabel12.configure(width=0)

        self.TLabel13 = ttk.Label(self.TFrame2)
        self.TLabel13.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel13.configure(background="#d9d9d9")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font="TkDefaultFont")
        self.TLabel13.configure(relief='flat')
        self.TLabel13.configure(wraplength="0")
        self.TLabel13.configure(takefocus="0")
        self.TLabel13.configure(text='''%''')
        self.TLabel13.configure(width=0)

        self.TLabel14 = ttk.Label(self.TFrame2)
        self.TLabel14.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font="TkDefaultFont")
        self.TLabel14.configure(relief='flat')
        self.TLabel14.configure(wraplength="0")
        self.TLabel14.configure(takefocus="0")
        self.TLabel14.configure(text='''Uitrollen:''')
        self.TLabel14.configure(width=0)

        self.TLabel15 = ttk.Label(self.TFrame2)
        self.TLabel15.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel15.configure(background="#d9d9d9")
        self.TLabel15.configure(foreground="#000000")
        self.TLabel15.configure(font="TkDefaultFont")
        self.TLabel15.configure(relief='flat')
        self.TLabel15.configure(wraplength="0")
        self.TLabel15.configure(takefocus="0")
        self.TLabel15.configure(text='''%''')
        self.TLabel15.configure(width=0)

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

        self.TLabel16 = ttk.Label(self.TFrame2)
        self.TLabel16.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel16.configure(background="#d9d9d9")
        self.TLabel16.configure(foreground="#000000")
        self.TLabel16.configure(font=font9)
        self.TLabel16.configure(relief='flat')
        self.TLabel16.configure(text='''Waarde op/uitrollen''')

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

        self.TLabel17 = ttk.Label(self.TFrame2)
        self.TLabel17.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel17.configure(background="#d9d9d9")
        self.TLabel17.configure(foreground="#000000")
        self.TLabel17.configure(font=font9)
        self.TLabel17.configure(relief='flat')
        self.TLabel17.configure(text='''Handmatig''')

        self.var3 = StringVar()
        self.var3.set(0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton5 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton5.place(relx=0.86, rely=0.2, relwidth=0.031
                                 , relheight=0.0, height=26)
        self.TRadiobutton5.configure(text='''Uit''', variable=self.var3, value=0, command=self.S1HandmatigUit)

        self.TRadiobutton6 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton6.place(relx=0.86, rely=0.35, relwidth=0.036
                                 , relheight=0.0, height=26)
        self.TRadiobutton6.configure(text='''Aan''', variable=self.var3, value=1, command=self.S1HandmatigAan)

        self.TLabel18 = ttk.Label(self.TFrame2)
        self.TLabel18.place(relx=0.848, rely=0.5, height=24, width=107)
        self.TLabel18.configure(background="#d9d9d9")
        self.TLabel18.configure(foreground="#000000")
        self.TLabel18.configure(font=font9)
        self.TLabel18.configure(relief='flat')
        self.TLabel18.configure(text='''Op/uitrollen:''')

        self.var4 = StringVar()

        self.TRadiobutton7 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton7.place(relx=0.848, rely=0.65, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton7.configure(text='''Oprollen''', variable=self.var4, value=0, state='disable')

        self.TRadiobutton8 = ttk.Radiobutton(self.TFrame2)
        self.TRadiobutton8.place(relx=0.848, rely=0.8, relwidth=0.06
                                   , relheight=0.0, height=26)
        self.TRadiobutton8.configure(text='''Uitrollen''', variable=self.var4, value=1, state='disable')

        self.TButton5 = ttk.Button(self.TFrame2)
        self.TButton5.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''X''')

        self.TButton6 = ttk.Button(self.TFrame2)
        self.TButton6.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''V''')

        self.TFrame5 = ttk.Frame(top)
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

        self.TLabel19 = ttk.Label(self.TFrame5)
        self.TLabel19.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel19.configure(background="#d9d9d9")
        self.TLabel19.configure(foreground="#000000")
        self.TLabel19.configure(font=font9)
        self.TLabel19.configure(relief='flat')
        self.TLabel19.configure(text='''Diagrammen''')

        self.TButton7 = ttk.Button(self.TFrame5)
        self.TButton7.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(text='''Lijndiagram''')

        self.TButton8 = ttk.Button(self.TFrame5)
        self.TButton8.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(text='''Staafdiagram''')

        self.TLabel20 = ttk.Label(self.TFrame5)
        self.TLabel20.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel20.configure(background="#d9d9d9")
        self.TLabel20.configure(foreground="#000000")
        self.TLabel20.configure(font=font9)
        self.TLabel20.configure(relief='flat')
        self.TLabel20.configure(text='''Maximale rolstand''')

        self.TLabel21 = ttk.Label(self.TFrame5)
        self.TLabel21.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel21.configure(background="#d9d9d9")
        self.TLabel21.configure(foreground="#000000")
        self.TLabel21.configure(font="TkDefaultFont")
        self.TLabel21.configure(relief='flat')
        self.TLabel21.configure(wraplength="0")
        self.TLabel21.configure(takefocus="0")
        self.TLabel21.configure(text='''Oprollen:''')
        self.TLabel21.configure(width=0)

        self.TLabel22 = ttk.Label(self.TFrame5)
        self.TLabel22.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel22.configure(background="#d9d9d9")
        self.TLabel22.configure(foreground="#000000")
        self.TLabel22.configure(font="TkDefaultFont")
        self.TLabel22.configure(relief='flat')
        self.TLabel22.configure(wraplength="0")
        self.TLabel22.configure(takefocus="0")
        self.TLabel22.configure(text='''%''')
        self.TLabel22.configure(width=0)

        self.TLabel23 = ttk.Label(self.TFrame5)
        self.TLabel23.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel23.configure(background="#d9d9d9")
        self.TLabel23.configure(foreground="#000000")
        self.TLabel23.configure(font="TkDefaultFont")
        self.TLabel23.configure(relief='flat')
        self.TLabel23.configure(wraplength="0")
        self.TLabel23.configure(takefocus="0")
        self.TLabel23.configure(text='''Uitrollen:''')
        self.TLabel23.configure(width=0)

        self.TLabel24 = ttk.Label(self.TFrame5)
        self.TLabel24.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel24.configure(background="#d9d9d9")
        self.TLabel24.configure(foreground="#000000")
        self.TLabel24.configure(font="TkDefaultFont")
        self.TLabel24.configure(relief='flat')
        self.TLabel24.configure(wraplength="0")
        self.TLabel24.configure(takefocus="0")
        self.TLabel24.configure(text='''%''')
        self.TLabel24.configure(width=0)

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

        self.TLabel25 = ttk.Label(self.TFrame5)
        self.TLabel25.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel25.configure(background="#d9d9d9")
        self.TLabel25.configure(foreground="#000000")
        self.TLabel25.configure(font=font9)
        self.TLabel25.configure(relief='flat')
        self.TLabel25.configure(text='''Waarde op/uitrollen''')

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

        self.TLabel26 = ttk.Label(self.TFrame5)
        self.TLabel26.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel26.configure(background="#d9d9d9")
        self.TLabel26.configure(foreground="#000000")
        self.TLabel26.configure(font=font9)
        self.TLabel26.configure(relief='flat')
        self.TLabel26.configure(text='''Handmatig''')

        self.var5 = StringVar()
        self.var5.set(0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton9 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton9.place(relx=0.86, rely=0.2, relwidth=0.031
                                 , relheight=0.0, height=26)
        self.TRadiobutton9.configure(text='''Uit''', variable=self.var5, value=0, command=self.S2HandmatigUit)

        self.TRadiobutton10 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton10.place(relx=0.86, rely=0.35, relwidth=0.036
                                 , relheight=0.0, height=26)
        self.TRadiobutton10.configure(text='''Aan''', variable=self.var5, value=1, command=self.S2HandmatigAan)

        self.TLabel27 = ttk.Label(self.TFrame5)
        self.TLabel27.place(relx=0.848, rely=0.5, height=24, width=107)
        self.TLabel27.configure(background="#d9d9d9")
        self.TLabel27.configure(foreground="#000000")
        self.TLabel27.configure(font=font9)
        self.TLabel27.configure(relief='flat')
        self.TLabel27.configure(text='''Op/uitrollen:''')

        self.var6 = StringVar()

        self.TRadiobutton11 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton11.place(relx=0.848, rely=0.65, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton11.configure(text='''Oprollen''', variable=self.var6, value=0, state='disable')

        self.TRadiobutton12 = ttk.Radiobutton(self.TFrame5)
        self.TRadiobutton12.place(relx=0.848, rely=0.8, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton12.configure(text='''Uitrollen''', variable=self.var6, value=1, state='disable')

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

        self.TLabel28 = ttk.Label(self.TFrame8)
        self.TLabel28.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel28.configure(background="#d9d9d9")
        self.TLabel28.configure(foreground="#000000")
        self.TLabel28.configure(font=font9)
        self.TLabel28.configure(relief='flat')
        self.TLabel28.configure(text='''Diagrammen''')

        self.TButton13 = ttk.Button(self.TFrame8)
        self.TButton13.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton13.configure(takefocus="")
        self.TButton13.configure(text='''Lijndiagram''')

        self.TButton14 = ttk.Button(self.TFrame8)
        self.TButton14.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton14.configure(takefocus="")
        self.TButton14.configure(text='''Staafdiagram''')

        self.TLabel29 = ttk.Label(self.TFrame8)
        self.TLabel29.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel29.configure(background="#d9d9d9")
        self.TLabel29.configure(foreground="#000000")
        self.TLabel29.configure(font=font9)
        self.TLabel29.configure(relief='flat')
        self.TLabel29.configure(text='''Maximale rolstand''')

        self.TLabel30 = ttk.Label(self.TFrame8)
        self.TLabel30.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel30.configure(background="#d9d9d9")
        self.TLabel30.configure(foreground="#000000")
        self.TLabel30.configure(font="TkDefaultFont")
        self.TLabel30.configure(relief='flat')
        self.TLabel30.configure(wraplength="0")
        self.TLabel30.configure(takefocus="0")
        self.TLabel30.configure(text='''Oprollen:''')
        self.TLabel30.configure(width=0)

        self.TLabel31 = ttk.Label(self.TFrame8)
        self.TLabel31.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel31.configure(background="#d9d9d9")
        self.TLabel31.configure(foreground="#000000")
        self.TLabel31.configure(font="TkDefaultFont")
        self.TLabel31.configure(relief='flat')
        self.TLabel31.configure(wraplength="0")
        self.TLabel31.configure(takefocus="0")
        self.TLabel31.configure(text='''%''')
        self.TLabel31.configure(width=0)

        self.TLabel32 = ttk.Label(self.TFrame8)
        self.TLabel32.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel32.configure(background="#d9d9d9")
        self.TLabel32.configure(foreground="#000000")
        self.TLabel32.configure(font="TkDefaultFont")
        self.TLabel32.configure(relief='flat')
        self.TLabel32.configure(wraplength="0")
        self.TLabel32.configure(takefocus="0")
        self.TLabel32.configure(text='''Uitrollen:''')
        self.TLabel32.configure(width=0)

        self.TLabel33 = ttk.Label(self.TFrame8)
        self.TLabel33.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel33.configure(background="#d9d9d9")
        self.TLabel33.configure(foreground="#000000")
        self.TLabel33.configure(font="TkDefaultFont")
        self.TLabel33.configure(relief='flat')
        self.TLabel33.configure(wraplength="0")
        self.TLabel33.configure(takefocus="0")
        self.TLabel33.configure(text='''%''')
        self.TLabel33.configure(width=0)

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

        self.TLabel34 = ttk.Label(self.TFrame8)
        self.TLabel34.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel34.configure(background="#d9d9d9")
        self.TLabel34.configure(foreground="#000000")
        self.TLabel34.configure(font=font9)
        self.TLabel34.configure(relief='flat')
        self.TLabel34.configure(text='''Waarde op/uitrollen''')

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

        self.TLabel35 = ttk.Label(self.TFrame8)
        self.TLabel35.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel35.configure(background="#d9d9d9")
        self.TLabel35.configure(foreground="#000000")
        self.TLabel35.configure(font=font9)
        self.TLabel35.configure(relief='flat')
        self.TLabel35.configure(text='''Handmatig''')

        self.var7 = StringVar()
        self.var7.set(0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton13 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton13.place(relx=0.86, rely=0.2, relwidth=0.031
                                 , relheight=0.0, height=26)
        self.TRadiobutton13.configure(text='''Uit''', variable=self.var7, value=0, command=self.S3HandmatigUit)

        self.TRadiobutton14 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton14.place(relx=0.86, rely=0.35, relwidth=0.036
                                 , relheight=0.0, height=26)
        self.TRadiobutton14.configure(text='''Aan''', variable=self.var7, value=1, command=self.S3HandmatigAan)

        self.TLabel36 = ttk.Label(self.TFrame8)
        self.TLabel36.place(relx=0.848, rely=0.5, height=24, width=107)
        self.TLabel36.configure(background="#d9d9d9")
        self.TLabel36.configure(foreground="#000000")
        self.TLabel36.configure(font=font9)
        self.TLabel36.configure(relief='flat')
        self.TLabel36.configure(text='''Op/uitrollen:''')

        self.var8 = StringVar()

        self.TRadiobutton15 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton15.place(relx=0.848, rely=0.65, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton15.configure(text='''Oprollen''', variable=self.var8, value=0, state='disable')

        self.TRadiobutton16 = ttk.Radiobutton(self.TFrame8)
        self.TRadiobutton16.place(relx=0.848, rely=0.8, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton16.configure(text='''Uitrollen''', variable=self.var8, value=1, state='disable')

        self.TButton17 = ttk.Button(self.TFrame8)
        self.TButton17.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton17.configure(takefocus="")
        self.TButton17.configure(text='''X''')

        self.TButton18 = ttk.Button(self.TFrame8)
        self.TButton18.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton18.configure(takefocus="")
        self.TButton18.configure(text='''V''')

        self.TFrame12 = ttk.Frame(top)
        self.TFrame12.place(relx=0.0, rely=0.598, relheight=0.19, relwidth=0.991)
        self.TFrame12.configure(relief='groove')
        self.TFrame12.configure(borderwidth="2")
        self.TFrame12.configure(relief='groove')
        self.TFrame12.configure(width=1325)

        self.TFrame13 = ttk.Frame(self.TFrame12)
        self.TFrame13.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame13.configure(relief='groove')
        self.TFrame13.configure(borderwidth="2")
        self.TFrame13.configure(relief='groove')
        self.TFrame13.configure(width=305)

        self.TFrame14 = ttk.Frame(self.TFrame12)
        self.TFrame14.place(relx=0.242, rely=0.031, relheight=0.906
                            , relwidth=0.16)
        self.TFrame14.configure(relief='groove')
        self.TFrame14.configure(borderwidth="2")
        self.TFrame14.configure(relief='groove')
        self.TFrame14.configure(width=215)

        self.TLabel37 = ttk.Label(self.TFrame12)
        self.TLabel37.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel37.configure(background="#d9d9d9")
        self.TLabel37.configure(foreground="#000000")
        self.TLabel37.configure(font=font9)
        self.TLabel37.configure(relief='flat')
        self.TLabel37.configure(text='''Diagrammen''')

        self.TButton19 = ttk.Button(self.TFrame12)
        self.TButton19.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton19.configure(takefocus="")
        self.TButton19.configure(text='''Lijndiagram''')

        self.TButton20 = ttk.Button(self.TFrame12)
        self.TButton20.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton20.configure(takefocus="")
        self.TButton20.configure(text='''Staafdiagram''')

        self.TLabel38 = ttk.Label(self.TFrame12)
        self.TLabel38.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel38.configure(background="#d9d9d9")
        self.TLabel38.configure(foreground="#000000")
        self.TLabel38.configure(font=font9)
        self.TLabel38.configure(relief='flat')
        self.TLabel38.configure(text='''Maximale rolstand''')

        self.TLabel39 = ttk.Label(self.TFrame12)
        self.TLabel39.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel39.configure(background="#d9d9d9")
        self.TLabel39.configure(foreground="#000000")
        self.TLabel39.configure(font="TkDefaultFont")
        self.TLabel39.configure(relief='flat')
        self.TLabel39.configure(wraplength="0")
        self.TLabel39.configure(takefocus="0")
        self.TLabel39.configure(text='''Oprollen:''')
        self.TLabel39.configure(width=0)

        self.TLabel40 = ttk.Label(self.TFrame12)
        self.TLabel40.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel40.configure(background="#d9d9d9")
        self.TLabel40.configure(foreground="#000000")
        self.TLabel40.configure(font="TkDefaultFont")
        self.TLabel40.configure(relief='flat')
        self.TLabel40.configure(wraplength="0")
        self.TLabel40.configure(takefocus="0")
        self.TLabel40.configure(text='''%''')
        self.TLabel40.configure(width=0)

        self.TLabel41 = ttk.Label(self.TFrame12)
        self.TLabel41.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel41.configure(background="#d9d9d9")
        self.TLabel41.configure(foreground="#000000")
        self.TLabel41.configure(font="TkDefaultFont")
        self.TLabel41.configure(relief='flat')
        self.TLabel41.configure(wraplength="0")
        self.TLabel41.configure(takefocus="0")
        self.TLabel41.configure(text='''Uitrollen:''')
        self.TLabel41.configure(width=0)

        self.TLabel42 = ttk.Label(self.TFrame12)
        self.TLabel42.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel42.configure(background="#d9d9d9")
        self.TLabel42.configure(foreground="#000000")
        self.TLabel42.configure(font="TkDefaultFont")
        self.TLabel42.configure(relief='flat')
        self.TLabel42.configure(wraplength="0")
        self.TLabel42.configure(takefocus="0")
        self.TLabel42.configure(text='''%''')
        self.TLabel42.configure(width=0)

        self.Scale6 = tk.Scale(self.TFrame12)
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

        self.Scale7 = tk.Scale(self.TFrame12)
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

        self.TButton21 = ttk.Button(self.TFrame12)
        self.TButton21.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton21.configure(takefocus="")
        self.TButton21.configure(text='''Submit''')

        self.TLabel43 = ttk.Label(self.TFrame12)
        self.TLabel43.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel43.configure(background="#d9d9d9")
        self.TLabel43.configure(foreground="#000000")
        self.TLabel43.configure(font=font9)
        self.TLabel43.configure(relief='flat')
        self.TLabel43.configure(text='''Waarde op/uitrollen''')

        self.Entry4 = tk.Entry(self.TFrame12)
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

        self.TButton22 = ttk.Button(self.TFrame12)
        self.TButton22.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton22.configure(takefocus="")
        self.TButton22.configure(text='''Submit''')

        self.TLabel44 = ttk.Label(self.TFrame12)
        self.TLabel44.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel44.configure(background="#d9d9d9")
        self.TLabel44.configure(foreground="#000000")
        self.TLabel44.configure(font=font9)
        self.TLabel44.configure(relief='flat')
        self.TLabel44.configure(text='''Handmatig''')

        self.var9 = StringVar()
        self.var9.set(0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton17 = ttk.Radiobutton(self.TFrame12)
        self.TRadiobutton17.place(relx=0.86, rely=0.2, relwidth=0.031
                                 , relheight=0.0, height=26)
        self.TRadiobutton17.configure(text='''Uit''', variable=self.var9, value=0, command=self.S4HandmatigUit)

        self.TRadiobutton18 = ttk.Radiobutton(self.TFrame12)
        self.TRadiobutton18.place(relx=0.86, rely=0.35, relwidth=0.036
                                 , relheight=0.0, height=26)
        self.TRadiobutton18.configure(text='''Aan''', variable=self.var9, value=1, command=self.S4HandmatigAan)

        self.TLabel45 = ttk.Label(self.TFrame12)
        self.TLabel45.place(relx=0.848, rely=0.5, height=24, width=107)
        self.TLabel45.configure(background="#d9d9d9")
        self.TLabel45.configure(foreground="#000000")
        self.TLabel45.configure(font=font9)
        self.TLabel45.configure(relief='flat')
        self.TLabel45.configure(text='''Op/uitrollen:''')

        self.var10 = StringVar()

        self.TRadiobutton19 = ttk.Radiobutton(self.TFrame12)
        self.TRadiobutton19.place(relx=0.848, rely=0.65, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton19.configure(text='''Oprollen''', variable=self.var10, value=0, state='disable')

        self.TRadiobutton20 = ttk.Radiobutton(self.TFrame12)
        self.TRadiobutton20.place(relx=0.848, rely=0.8, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton20.configure(text='''Uitrollen''', variable=self.var10, value=1, state='disable')

        self.TButton23 = ttk.Button(self.TFrame12)
        self.TButton23.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton23.configure(takefocus="")
        self.TButton23.configure(text='''X''')

        self.TButton24 = ttk.Button(self.TFrame12)
        self.TButton24.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton24.configure(takefocus="")
        self.TButton24.configure(text='''V''')

        self.TFrame15 = ttk.Frame(top)
        self.TFrame15.place(relx=0.0, rely=0.415, relheight=0.19, relwidth=0.991)
        self.TFrame15.configure(relief='groove')
        self.TFrame15.configure(borderwidth="2")
        self.TFrame15.configure(relief='groove')
        self.TFrame15.configure(width=1325)

        self.TFrame16 = ttk.Frame(self.TFrame15)
        self.TFrame16.place(relx=0.004, rely=0.031, relheight=0.906
                           , relwidth=0.227)
        self.TFrame16.configure(relief='groove')
        self.TFrame16.configure(borderwidth="2")
        self.TFrame16.configure(relief='groove')
        self.TFrame16.configure(width=305)

        self.TFrame17 = ttk.Frame(self.TFrame15)
        self.TFrame17.place(relx=0.242, rely=0.031, relheight=0.906
                            , relwidth=0.16)
        self.TFrame17.configure(relief='groove')
        self.TFrame17.configure(borderwidth="2")
        self.TFrame17.configure(relief='groove')
        self.TFrame17.configure(width=215)

        self.TLabel46 = ttk.Label(self.TFrame15)
        self.TLabel46.place(relx=0.431, rely=0.05, height=24, width=95)
        self.TLabel46.configure(background="#d9d9d9")
        self.TLabel46.configure(foreground="#000000")
        self.TLabel46.configure(font=font9)
        self.TLabel46.configure(relief='flat')
        self.TLabel46.configure(text='''Diagrammen''')

        self.TButton25 = ttk.Button(self.TFrame15)
        self.TButton25.place(relx=0.424, rely=0.3, height=30, width=98)
        self.TButton25.configure(takefocus="")
        self.TButton25.configure(text='''Lijndiagram''')

        self.TButton26 = ttk.Button(self.TFrame15)
        self.TButton26.place(relx=0.424, rely=0.6, height=30, width=100)
        self.TButton26.configure(takefocus="")
        self.TButton26.configure(text='''Staafdiagram''')

        self.TLabel47 = ttk.Label(self.TFrame15)
        self.TLabel47.place(relx=0.569, rely=0.05, height=24, width=114)
        self.TLabel47.configure(background="#d9d9d9")
        self.TLabel47.configure(foreground="#000000")
        self.TLabel47.configure(font=font9)
        self.TLabel47.configure(relief='flat')
        self.TLabel47.configure(text='''Maximale rolstand''')

        self.TLabel48 = ttk.Label(self.TFrame15)
        self.TLabel48.place(relx=0.539, rely=0.26, height=24, width=60)
        self.TLabel48.configure(background="#d9d9d9")
        self.TLabel48.configure(foreground="#000000")
        self.TLabel48.configure(font="TkDefaultFont")
        self.TLabel48.configure(relief='flat')
        self.TLabel48.configure(wraplength="0")
        self.TLabel48.configure(takefocus="0")
        self.TLabel48.configure(text='''Oprollen:''')
        self.TLabel48.configure(width=0)

        self.TLabel49 = ttk.Label(self.TFrame15)
        self.TLabel49.place(relx=0.659, rely=0.26, height=24, width=60)
        self.TLabel49.configure(background="#d9d9d9")
        self.TLabel49.configure(foreground="#000000")
        self.TLabel49.configure(font="TkDefaultFont")
        self.TLabel49.configure(relief='flat')
        self.TLabel49.configure(wraplength="0")
        self.TLabel49.configure(takefocus="0")
        self.TLabel49.configure(text='''%''')
        self.TLabel49.configure(width=0)

        self.TLabel50 = ttk.Label(self.TFrame15)
        self.TLabel50.place(relx=0.539, rely=0.50, height=24, width=60)
        self.TLabel50.configure(background="#d9d9d9")
        self.TLabel50.configure(foreground="#000000")
        self.TLabel50.configure(font="TkDefaultFont")
        self.TLabel50.configure(relief='flat')
        self.TLabel50.configure(wraplength="0")
        self.TLabel50.configure(takefocus="0")
        self.TLabel50.configure(text='''Uitrollen:''')
        self.TLabel50.configure(width=0)

        self.TLabel51 = ttk.Label(self.TFrame15)
        self.TLabel51.place(relx=0.659, rely=0.50, height=24, width=60)
        self.TLabel51.configure(background="#d9d9d9")
        self.TLabel51.configure(foreground="#000000")
        self.TLabel51.configure(font="TkDefaultFont")
        self.TLabel51.configure(relief='flat')
        self.TLabel51.configure(wraplength="0")
        self.TLabel51.configure(takefocus="0")
        self.TLabel51.configure(text='''%''')
        self.TLabel51.configure(width=0)

        self.Scale8 = tk.Scale(self.TFrame15)
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

        self.Scale9 = tk.Scale(self.TFrame15)
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

        self.TButton27 = ttk.Button(self.TFrame15)
        self.TButton27.place(relx=0.569, rely=0.7, height=30, width=98)
        self.TButton27.configure(takefocus="")
        self.TButton27.configure(text='''Submit''')

        self.TLabel52 = ttk.Label(self.TFrame15)
        self.TLabel52.place(relx=0.71, rely=0.05, height=24, width=120)
        self.TLabel52.configure(background="#d9d9d9")
        self.TLabel52.configure(foreground="#000000")
        self.TLabel52.configure(font=font9)
        self.TLabel52.configure(relief='flat')
        self.TLabel52.configure(text='''Waarde op/uitrollen''')

        self.Entry5 = tk.Entry(self.TFrame15)
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

        self.TButton28 = ttk.Button(self.TFrame15)
        self.TButton28.place(relx=0.715, rely=0.7, height=30, width=98)
        self.TButton28.configure(takefocus="")
        self.TButton28.configure(text='''Submit''')

        self.TLabel53 = ttk.Label(self.TFrame15)
        self.TLabel53.place(relx=0.85, rely=0.05, height=24, width=94)
        self.TLabel53.configure(background="#d9d9d9")
        self.TLabel53.configure(foreground="#000000")
        self.TLabel53.configure(font=font9)
        self.TLabel53.configure(relief='flat')
        self.TLabel53.configure(text='''Handmatig''')

        self.var11 = StringVar()
        self.var11.set(0)

        self.style.map('TRadiobutton', background=
        [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton21 = ttk.Radiobutton(self.TFrame15)
        self.TRadiobutton21.place(relx=0.86, rely=0.2, relwidth=0.031
                                 , relheight=0.0, height=26)
        self.TRadiobutton21.configure(text='''Uit''', variable=self.var11, value=0, command=self.S5HandmatigUit)

        self.TRadiobutton22 = ttk.Radiobutton(self.TFrame15)
        self.TRadiobutton22.place(relx=0.86, rely=0.35, relwidth=0.036
                                 , relheight=0.0, height=26)
        self.TRadiobutton22.configure(text='''Aan''', variable=self.var11, value=1, command=self.S5HandmatigAan)

        self.TLabel54 = ttk.Label(self.TFrame15)
        self.TLabel54.place(relx=0.848, rely=0.5, height=24, width=107)
        self.TLabel54.configure(background="#d9d9d9")
        self.TLabel54.configure(foreground="#000000")
        self.TLabel54.configure(font=font9)
        self.TLabel54.configure(relief='flat')
        self.TLabel54.configure(text='''Op/uitrollen:''')

        self.var12 = StringVar()

        self.TRadiobutton23 = ttk.Radiobutton(self.TFrame15)
        self.TRadiobutton23.place(relx=0.848, rely=0.65, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton23.configure(text='''Oprollen''', variable=self.var12, value=0, state='disable')

        self.TRadiobutton24 = ttk.Radiobutton(self.TFrame15)
        self.TRadiobutton24.place(relx=0.848, rely=0.8, relwidth=0.06
                                 , relheight=0.0, height=26)
        self.TRadiobutton24.configure(text='''Uitrollen''', variable=self.var12, value=1, state='disable')

        self.TButton29 = ttk.Button(self.TFrame15)
        self.TButton29.place(relx=0.974, rely=0.0, height=30, width=38)
        self.TButton29.configure(takefocus="")
        self.TButton29.configure(text='''X''')

        self.TButton30 = ttk.Button(self.TFrame15)
        self.TButton30.place(relx=0.948, rely=0.0, height=30, width=38)
        self.TButton30.configure(takefocus="")
        self.TButton30.configure(text='''V''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    def AlleHandmatigUit(self):
        self.TRadiobutton3.config(state='disable')
        self.TRadiobutton4.config(state='disable')
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
        self.TRadiobutton7.config(state='disable')
        self.TRadiobutton8.config(state='disable')
        self.TRadiobutton11.config(state='disable')
        self.TRadiobutton12.config(state='disable')
        self.TRadiobutton15.config(state='disable')
        self.TRadiobutton16.config(state='disable')
        self.TRadiobutton19.config(state='disable')
        self.TRadiobutton20.config(state='disable')
        self.TRadiobutton23.config(state='disable')
        self.TRadiobutton24.config(state='disable')
        self.TRadiobutton5.config(state='normal')
        self.TRadiobutton6.config(state='normal')
        self.TRadiobutton9.config(state='normal')
        self.TRadiobutton10.config(state='normal')
        self.TRadiobutton13.config(state='normal')
        self.TRadiobutton14.config(state='normal')
        self.TRadiobutton17.config(state='normal')
        self.TRadiobutton18.config(state='normal')
        self.TRadiobutton21.config(state='normal')
        self.TRadiobutton22.config(state='normal')

    def AlleHandmatigAan(self):
        self.TRadiobutton3.config(state='normal')
        self.TRadiobutton4.config(state='normal')
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
        self.TRadiobutton15.config(state='disable')
        self.TRadiobutton16.config(state='disable')
        self.TRadiobutton17.config(state='disable')
        self.TRadiobutton18.config(state='disable')
        self.TRadiobutton19.config(state='disable')
        self.TRadiobutton20.config(state='disable')
        self.TRadiobutton21.config(state='disable')
        self.TRadiobutton22.config(state='disable')
        self.TRadiobutton23.config(state='disable')
        self.TRadiobutton24.config(state='disable')

    def S1HandmatigUit(self):
        self.TRadiobutton7.config(state='disable')
        self.TRadiobutton8.config(state='disable')
        self.Entry1.config(state='normal')
        self.TButton4.config(state='normal')

    def S1HandmatigAan(self):
        self.TRadiobutton7.config(state='normal')
        self.TRadiobutton8.config(state='normal')
        self.Entry1.config(state='disable')
        self.TButton4.config(state='disable')

    def S2HandmatigUit(self):
        self.TRadiobutton11.config(state='disable')
        self.TRadiobutton12.config(state='disable')
        self.Entry2.config(state='normal')
        self.TButton10.config(state='normal')

    def S2HandmatigAan(self):
        self.TRadiobutton11.config(state='normal')
        self.TRadiobutton12.config(state='normal')
        self.Entry3.config(state='disable')
        self.TButton10.config(state='disable')

    def S3HandmatigUit(self):
        self.TRadiobutton15.config(state='disable')
        self.TRadiobutton16.config(state='disable')
        self.Entry3.config(state='normal')
        self.TButton16.config(state='normal')

    def S3HandmatigAan(self):
        self.TRadiobutton15.config(state='normal')
        self.TRadiobutton16.config(state='normal')
        self.Entry3.config(state='disable')
        self.TButton16.config(state='disable')

    def S4HandmatigUit(self):
        self.TRadiobutton19.config(state='disable')
        self.TRadiobutton20.config(state='disable')
        self.Entry4.config(state='normal')
        self.TButton22.config(state='normal')

    def S4HandmatigAan(self):
        self.TRadiobutton19.config(state='normal')
        self.TRadiobutton20.config(state='normal')
        self.Entry4.config(state='disable')
        self.TButton22.config(state='disable')

    def S5HandmatigUit(self):
        self.TRadiobutton23.config(state='disable')
        self.TRadiobutton24.config(state='disable')
        self.Entry5.config(state='normal')
        self.TButton28.config(state='normal')

    def S5HandmatigAan(self):
        self.TRadiobutton23.config(state='normal')
        self.TRadiobutton24.config(state='normal')
        self.Entry5.config(state='disable')
        self.TButton28.config(state='disable')

if __name__ == '__main__':
    vp_start_gui()


