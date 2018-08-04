import os, sys

import tkinter as tk

from PIL import Image, ImageTk

def get_root_dir():
    return r'E:/download/comic'



def list_subdirs_pics(path):pass

def sort_dirs(dirs):pass
def sort_pics(pics):pass
    

pic_dir = r'E:/download/comic/鬼王/0000_1'
pic_dir = r'E:/download/comic/那年那兔那些事儿[有妖气]/2012112500_狗大户鹰酱买灰姬'
def get_pics(path):
    ls = []
    for file in os.listdir(path):
        fn = os.path.join(path, file)
        if (not os.path.isfile(fn)) or os.path.islink(fn):
            continue

        if os.path.splitext(file)[1].lower() not in {'.jpg', '.jpeg', '.gif', '.png'}:
            continue
        
        ls.append(file)
    
    return ls 




def pics2imgs(path, pics, resize_img):
    return list(ImageTk.PhotoImage(resize_img(Image.open(os.path.join(path, pic)))) for pic in pics)

def resize_image(img, width):
    img_width, img_height = img.size
    if img_width >= width:
        return img

    height = img_height * width // img_width
    return img.resize((width, height))


def resize_imgs(imgs, width):
    return list(resize_image(img, width) for img in imgs)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
#screen_width, screen_height = 1000, 500
pic_width = screen_width-100
def get_imgs(path):
    return pics2imgs(path, get_pics(path), lambda x:resize_image(x, pic_width))




class ImageList(tk.Frame):
    def __init__(self, master=None, imgs=[]):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)

        self.imgs = imgs # hold it!!!
        self.createWidgets(imgs)

    def createWidgets(self, imgs):
        total_height = sum(img.height() for img in imgs)
        max_width = 0 if not imgs else max(img.width() for img in imgs)


        # resizable
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # scroll canvas at both x,y axis
        cv = tk.Canvas(self, scrollregion=(0, 0, max_width, total_height),
                       bg = 'white')
        cv.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
     
        scrollY = tk.Scrollbar(self, orient=tk.VERTICAL, command=cv.yview)
        scrollY.grid(row=0, column=1, sticky=tk.N+tk.S)
        cv['yscrollcommand'] = scrollY.set
        
        scrollX = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=cv.xview)
        scrollX.grid(row=1, column=0, sticky=tk.E+tk.W)
        cv['xscrollcommand'] = scrollX.set


        # save
        self.cv = cv
        self.scrollY = scrollY
        self.scrollX = scrollX

        # draw images
        dy = 0
        for img in imgs:
            cv.create_image((0,dy), image = img, anchor = 'nw')
            dy += img.height()


dirname = 'd:/新建文件夹'
dirname = pic_dir

#help(tk.Tk.wm_state)
help(tk.Tk)
quit_flag = False
def new_quit():
    #print('quit')
    global quit_flag
    quit_flag = True
    t.destroy()

while True:
    quit_flag = False
    t = tk.Tk()
    #t.withdraw()
    #t.wm_state('zoomed')
    #t.protocol("WM_DELETE_WINDOW", new_quit)
    w,h = s = t.maxsize()
    print(s)
    t.geometry('{}x{}+{}+{}'.format(w, h, 0, 0))
    t.bind("<Destroy>", new_quit)


    dirname = os.path.abspath(os.path.realpath(dirname))
    #print(dirname)
    b_dirname = dirname.encode(sys.getfilesystemencoding())
    dirname = tk.filedialog.askdirectory(initialdir=b_dirname, mustexist=True, parent=t)


    if quit_flag:break
    if not dirname:
        new_quit()
        break

    
    #top = tk.Toplevel()
    t.destroy()
    app = ImageList(t, get_imgs(dirname))
    app.master.title('ImageList')
    #t.wm_state('zoomed')
    app.mainloop()
    print('yugiui')
    t.destroy()


if not quit_flag:
    t.destroy()

assert quit_flag

'''
cv = tk.Canvas(root, scrollregion=(0, 0, max_width, total_height))
cv.pack(side = tk.LEFT, fill = tk.BOTH)

scrollY = tk.Scrollbar(root, orient=tk.VERTICAL, command=cv.yview)
scrollY.pack(side = tk.RIGHT, fill=tk.Y)
cv['yscrollcommand'] = scrollY.set


scrollX = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=cv.xview)
scrollX.pack(side = tk.BOTTOM, fill=tk.X)
cv['xscrollcommand'] = scrollX.set



top=root.winfo_toplevel()
#raise
assert top is root
top.rowconfigure(0, weight=1)
top.columnconfigure(0, weight=1)
root.grid(sticky=tk.N+tk.S+tk.E+tk.W)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

cv.rowconfigure(0, weight=1)
cv.columnconfigure(0, weight=1)
cv.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

dy = 0
for img in imgs:
    cv.create_image((0,dy), image = img, anchor = 'nw')
    dy += img.height()

root.mainloop()
        
'''
