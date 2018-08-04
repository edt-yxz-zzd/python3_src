import tkinter as tk
from tkinter import tix
tk = tix

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        # resizable
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=9)
        self.columnconfigure(0, weight=9)
        self.columnconfigure(1, weight=1)


        self.s = tk.StringVar()
        self.s.set('c:/')
        self.t = tk.Entry(self, textvariable=self.s)
        self.t.grid(row=0, column=0, sticky=tk.E+tk.W)


        self.b = tk.Button(self, text='browse', command=self.browse)
        self.b.grid(row=0, column=1, sticky=tk.E+tk.W)

        self.d = tix.DirTree(self, browsecmd=self.browsecmd, directory='c:/')
        self.d.grid(row=1, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.d.chdir('c:/')

        #print(self.t.keys())

    def browse(self):
        path = self.s.get()
        self.d.chdir(path)
        print('browse ', path)

    def browsecmd(self, path):
        self.s.set(path)
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
