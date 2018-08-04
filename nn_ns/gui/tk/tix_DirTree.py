from tkinter import tix


root = tix.Tk()
#root.tk.eval('package require Tix')


#help(tix.DirTree)
#help(tix.ScrolledHList)
#help(tix.ScrolledWidget)

def c(p):print('command ', p)
def b(p):print('browsecmd ', p)
def d(p):print('dircmd ', p)


def fdsd():
    dsd = tix.DirSelectDialog(master=None, command=c)
    db = dsd.dirbox
    '''
    print(type(dsd.dirbox))
    print(db.keys())
    print(dir(db))
    print(help(db.set_silent))
    print(help(db.setvar))'''
    db.set_silent('d:/')
    #print(dsd.keys())
    dsd.popup()

def fdt():
    dt = tix.DirTree(root, command=c, browsecmd=b, directory='c:/')
    dt.chdir('d:')
    dt.pack()
    #print(dt.keys())
    dt.mainloop()

    
fdsd()
