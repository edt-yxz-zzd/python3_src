
# 25.1.6.4. Coupling Widget Variables
# 25.1.6.7. Bindings and Events


r'''

    KeyPress, KeyRelease - for keyboard events
    ButtonPress, ButtonRelease, Motion, Enter, Leave, MouseWheel - for mouse events
    Visibility, Unmap, Map, Expose, FocusIn, FocusOut, Circulate,
    Colormap, Gravity, Reparent, Property, Destroy, Activate,
    Deactivate - for window events.


    "win32" {
	event add <<Cut>> <Control-Key-x> <Shift-Key-Delete> \
	    <Control-Lock-Key-X>
	event add <<Copy>> <Control-Key-c> <Control-Key-Insert> \
	    <Control-Lock-Key-C>
	event add <<Paste>> <Control-Key-v> <Shift-Key-Insert> \
	    <Control-Lock-Key-V>
	event add <<PasteSelection>> <ButtonRelease-2>
  	event add <<Undo>> <Control-Key-z> <Control-Lock-Key-Z>
	event add <<Redo>> <Control-Key-y> <Control-Lock-Key-Y>
	}


bind TMenubutton <Enter>	{ %W instate !disabled {%W state active } }
bind TMenubutton <Leave>	{ %W state !active }
bind TMenubutton <Key-space> 	{ ttk::menubutton::Popdown %W }
bind TMenubutton <<Invoke>> 	{ ttk::menubutton::Popdown %W }

if {[tk windowingsystem] eq "x11"} {
    bind TMenubutton <ButtonPress-1>  	{ ttk::menubutton::Pulldown %W }
    bind TMenubutton <ButtonRelease-1>	{ ttk::menubutton::TransferGrab %W }
    bind TMenubutton <B1-Leave> 	{ ttk::menubutton::TransferGrab %W }
} else {
    bind TMenubutton <ButtonPress-1>  \
	{ %W state pressed ; ttk::menubutton::Popdown %W }
    bind TMenubutton <ButtonRelease-1>  \
	{ %W state !pressed }
}

./tix8.4.3/demos/widget:    bind .s <MouseWheel> {
./tix8.4.3/demos/widget:    bind .s <Up> {
./tix8.4.3/demos/widget:    bind .s <Down> {
./tix8.4.3/demos/widget:    bind .s <Prior> {
./tix8.4.3/demos/widget:    bind .s <Next> {
./tix8.4.3/demos/widget:    bind .s <Home> {
./tix8.4.3/demos/widget:    bind .s <End> {
./tix8.4.3/Grid.tcl:    tixBind TixGrid <Return> {
./tix8.4.3/Grid.tcl:    tixBind TixGrid <space> {
./tix8.4.3/Grid.tcl:    bind TixGrid <MouseWheel> {
./tix8.4.3/Grid.tcl:    tixGrid:IndicatorCmd $w <Arm> $ent
./tix8.4.3/Grid.tcl:	tixGrid:IndicatorCmd $w <Activate> $tkPriv(tix,indicator)
./tix8.4.3/Grid.tcl:	tixGrid:IndicatorCmd $w <Disarm>   $tkPriv(tix,indicator)
./tix8.4.3/Grid.tcl:	tixGrid:IndicatorCmd $w <Arm> $tkPriv(tix,indicator)
./tix8.4.3/Grid.tcl:	tixGrid:IndicatorCmd $w <Disarm> $t
<Double-ButtonPress-1>
'''



from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
        self.entrythingy.bind("<Enter>", self.turnRed, '+')
        self.entrythingy.bind("<Leave>", self.turnGreen, '+')



        self.bind('<KeyPress>', self.show_event, '+')
        self.event_add('<<or-event>>', '<question>', '<slash>')
        self.bind('<<or-event>>', self.or_event, '+')
        self.entrythingy.event_add('<<or-event>>', '<space>')
        self.focus_set()

    def or_event(self, event):
        print('or event')
        print(event.__dict__)
        
    def show_event(self, event):
        print('keysym', repr(event.keysym))
        print('x, y = ', event.x, event.y)
        print('type', event.type)
        print(event.__dict__)
        
    def turnGreen(self, event):
        print('<Leave>')
        event.widget["fg"] = "green"
        self.show_event(event)
    def turnRed(self, event):
        print('<Enter>')
        event.widget["fg"] = "red"
        self.show_event(event)



    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())




root = Tk()
app = App(master=root)
app.mainloop()


