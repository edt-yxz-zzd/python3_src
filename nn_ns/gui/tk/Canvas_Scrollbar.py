import tkinter as tk
'''
m = tk.messagebox.Message()
m.show()'''

'''
print(tk.messagebox.showinfo('title', 'info'))
print(tk.simpledialog.askstring('title', 'input'))'''

gif = r'E:/multimedia/picture/funny/NO_PLEASE.gif'
jpg = r'E:/multimedia/picture/funny/ugly_girl.jpg'


root = tk.Tk()
pic = tk.PhotoImage(file=gif)
'''
b = tk.Label(master=root, image=pic)
b.pack()'''

from PIL import Image, ImageTk
image = Image.open(jpg)
pic = ImageTk.PhotoImage(image)

'''
scrollbar = tk.Scrollbar(root)
scrollbar.pack( side = tk.RIGHT, fill=tk.Y )
#'''


'''
ls = tk.Listbox(root, yscrollcommand = scrollbar.set)
b = tk.Button(master=ls, image=pic)
b.pack()
b2 = tk.Button(master=ls, image=pic).pack()

ls.insert(tk.END, b, b2)
ls.pack( side = tk.LEFT, fill = tk.BOTH)

#'''

#'''
cv = tk.Canvas(root,bg = 'white', width=pic.width(), height=500,
               scrollregion=(0, 0, pic.width(), 2*pic.height()))
cv.pack(side = tk.LEFT, fill = tk.BOTH)

scrollY = tk.Scrollbar(root, orient=tk.VERTICAL, command=cv.yview)
scrollY.pack(side = tk.RIGHT, fill=tk.Y)
cv['yscrollcommand'] = scrollY.set

cv.create_image((0,0), image = pic, anchor = 'nw')
cv.create_image((0,pic.height()), image = pic, anchor = 'nw')
#'''

'''
canv = tk.Canvas(root, width=600, height=400,
        scrollregion=(0, 0, 1200, 800))
canv.grid(row=0, column=0)

scrollY = tk.Scrollbar(root, orient=tk.VERTICAL,
    command=canv.yview)
scrollY.grid(row=0, column=1, sticky=tk.N+tk.S)

scrollX = tk.Scrollbar(root, orient=tk.HORIZONTAL,
    command=canv.xview)
scrollX.grid(row=1, column=0, sticky=tk.E+tk.W)

canv['xscrollcommand'] = scrollX.set
canv['yscrollcommand'] = scrollY.set
canv.create_image((0,0), image = pic, anchor = 'nw')
'''

#del pic
root.mainloop()
'''
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.m = tk.messagebox(self)
        print(self.m.config())
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

#'''



