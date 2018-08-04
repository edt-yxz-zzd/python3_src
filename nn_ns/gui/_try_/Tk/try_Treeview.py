
from tkinter import *
from tkinter.ttk import *

T = Treeview



class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        sbar = SBar(self, command=show)
        print(sbar.configure())
        sbar.pack(side='right', expand=3)
        t = self.t = T(self, yscrollcommand=sbar)
        i1 = t.insert('', 'end')
        t.pack(side="top")
        assert t.exists(i1)
        print(t.item(i1))
        {'text': '', 'values': '', 'tags': '', 'open': 0, 'image': ''}
        t.item(i1, text='text i1', tags='tags i1',
               image='timg')

        t.insert('', 'end', image='timg', text = 'xxxxx i2')
        t.insert('', 'end', tags='tags i3', text = 'xxxxx i3')

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
img_name = r'E:\multimedia\picture\beauty\small\7\005.gif'
img = PhotoImage('timg', file=img_name)
def show(*args, **kwargs):
    print(*args, **kwargs)
class SBar(Scrollbar):
    def set(*args, **kwargs):
        print(*args, **kwargs)

app = Application(master=root)
app.mainloop()



