
#Tkinter Digital Clock
#https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python
#This short Python code gets the local time from the PC as a formatted string using time.strftime('%H:%M:%S'). The time string is displayed in a label using a larger font. A recursive function checks the time five times per second, and updates the time string, if it has changed. Five times per second may sound like overkill, but keeps the display from acting spasmodic.
#######################################################



if True:
    # use Tkinter to show a digital clock
    # tested with Python24    vegaseat    10sep2006
    try:
        from Tkinter import *
    except:
        from tkinter import *
    import time
    from datetime import datetime

    root = Tk()
    time1 = ''
    clock = Label(root, font=('times', 200, 'bold'), bg='green')
    clock.pack(fill=BOTH, expand=1)
    def tick():
        global time1
        # get the current local time from the PC
        #time2 = time.strftime('%H:%M:%S')
        time2 = datetime.now().strftime('%Y-%m-%d\n%w  %H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)
    tick()
    root.mainloop(  )


