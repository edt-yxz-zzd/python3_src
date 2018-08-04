##25.1.6.5. The Window Manager In Tk, there is a utility command, wm,
##for interacting with the window manager. Options to the wm command
##allow you to control things like titles, placement, icon bitmaps, and
##the like. In tkinter, these commands have been implemented as methods
##on the Wm class. Toplevel widgets are subclassed from the Wm class,
##and so can call the Wm methods directly.
##
##To get at the toplevel window that contains a given widget, you can
##often just refer to the widget’s master. Of course if the widget has
##been packed inside of a frame, the master won’t represent a toplevel
##window. To get at the toplevel window that contains an arbitrary
##widget, you can call the _root() method. This method begins with an
##underscore to denote the fact that this function is part of the
##implementation, and not an interface to Tk functionality.
##
##Here are some examples of typical usage:

from tkinter import *
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()
