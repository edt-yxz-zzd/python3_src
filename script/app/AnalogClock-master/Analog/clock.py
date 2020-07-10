#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#  S.S.B
#  surajsinghbisht054@gmail.com
#  bitforestinfo.blogspot.com
#

# Create Simple Analog Clock App Using Python
# http://www.bitforestinfo.com/2017/01/how-to-create-analog-clock-using-python.html


# Import Module
try:
    import Tkinter
except:
    import tkinter as Tkinter
try:
    xrange = range
except:pass


import math # Required For Coordinates Calculation
import time # Required For Time Handling
#
#
# class
class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x=150 # Center Point x
        self.y=150 # Center Point
        self.length=50 # Stick Length
        self.creating_all_function_trigger()

    # Creating Trigger For Other Functions
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background_()
        self.creating_sticks()
        return

    # Creating Background
    def creating_background_(self):
        self.image=Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(150,150, image=self.image)
        return

    # creating Canvas
    def create_canvas_for_shapes(self):
        self.canvas=Tkinter.Canvas(self, bg='skyblue')
        self.canvas.pack(expand='yes',fill='both')
        return

    # Creating Moving Sticks
    def creating_sticks(self):
        self.sticks=[]
        for i in xrange(3):
            store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2)
            self.sticks.append(store)
        return

    # Function Need Regular Update
    def update_class(self):
        now=time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime( "%I", t ))*5
        now=(hour,now.tm_min,now.tm_sec)
        # Changing Stick Coordinates
        for n,i in enumerate(now):
            x,y=self.canvas.coords(self.sticks[n])[0:2]
            cr=[x,y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
        return

# Main Function Trigger
if __name__ == '__main__':
    root=main()

    # Creating Main Loop
    while True:
        root.update()
        root.update_idletasks()
        root.update_class()


