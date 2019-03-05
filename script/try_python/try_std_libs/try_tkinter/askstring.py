
if 0:
    from tkinter.simpledialog  import askstring
    from tkinter import Tk
    top = Tk()
    r = askstring("title", ">>>", show=True, parent=top)
    print(repr(r))
    top.destroy()


from tkinter import Tk, Label, Entry, Button
import tkinter
import tkinter.messagebox

top = Tk()

#https://www.tutorialspoint.com/python/python_gui_programming.htm
#https://www.tutorialspoint.com/python/tk_entry.htm
L1 = Label(top, text="User Name")
L1.pack()
E1 = Entry(top, bd =5)
E1.pack()
E1.focus_set()

#https://www.tutorialspoint.com/python/tk_button.htm
def helloCallBack():
    tkinter.messagebox.showinfo("Hello", repr(E1.get()), master=top)
    return True # useless

B = Button(top, text ="Hello", command = helloCallBack)
B.pack()

image_path = r'E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\app\Django\favicon.ico'
#photo = tkinter.PhotoImage(file=image_path)
import PIL.Image, PIL.ImageTk
img = PIL.Image.open(image_path)
#img = PIL.ImageTk.open(image_path)

#https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/
canvas = tkinter.Canvas(top, width = img.width, height = img.height)
canvas.pack()
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
photo = PIL.ImageTk.PhotoImage(image = img)

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

print(type(photo).mro())
top.mainloop()

