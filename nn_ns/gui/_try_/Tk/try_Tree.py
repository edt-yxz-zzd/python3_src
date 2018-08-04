from tkinter import tix
from tkinter.constants import *
import tkinter as tk

# destroy option_get pack_forget quit

def f():
    print('callback')
    print(b.configure())
    b.destroy()
    
root = tk.Tk()
b = tk.Button(text='button', command=f)
b.pack(anchor='nw', side='left', expand=0, fill = 'x')
b.mainloop()


if 0:
    root = tix.Tk()

    Tree = tix.Tree



    L = tix.Label(root)
    L.pack(anchor='nw', side='left', expand=0, fill = 'x')
    L["text"] = 'Label'
    L['command'] = f
    L.mainloop()
##
##
##B = tix.ButtonBox(root)
##B.pack()
##B["text"] = 'ButtonBox'
##
##t = Tree(root)
##t.pack()
##t.mainloop()

