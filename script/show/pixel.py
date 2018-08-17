'''
https://stackoverflow.com/questions/12284311/python-tkinter-how-to-work-with-pixels
https://stackoverflow.com/questions/15269682/python-tkinter-canvas-fail-to-bind-keyboard

'''

def f1():
    from tkinter import Tk, Canvas, PhotoImage, mainloop
    from math import sin

    WIDTH, HEIGHT = 640, 480

    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canvas.image = img
        # Don't forget to save a reference after canvas.create_image. In some cases, especially when working with the PIL module, python will garbage-collect the image, even though it is being displayed!

    for x in range(4 * WIDTH):
        y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
        img.put("#ffffff", (x//4,y))

    mainloop()


def f2():
    from tkinter import Tk, Canvas, PhotoImage, mainloop
    from math import sin

    WIDTH, HEIGHT = 640, 480

    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    canvas.image = img
        # Don't forget to save a reference after canvas.create_image. In some cases, especially when working with the PIL module, python will garbage-collect the image, even though it is being displayed!

    for x in range(4 * WIDTH):
        y = int(HEIGHT/2 + HEIGHT/4 * sin(x/80.0))
        img.put("#ffffff", (x//4,y))


    def callback(event):
        print('callback with', event)
    canvas.focus_set()
    canvas.bind('<KeyPress>', callback)
    canvas.bind('<KeyRelease>', callback)
    canvas.bind('<Enter>', callback)
    canvas.bind('<Motion>', callback)
    canvas.bind('<Leave>', callback)
    canvas.bind('<ButtonPress>', callback)
    canvas.bind('<ButtonRelease>', callback)
    mainloop()


f2()

