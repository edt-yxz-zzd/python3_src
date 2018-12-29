
'''
https://stackoverflow.com/questions/713498/turn-on-off-monitor
    turn on screen monitor
        user32.dll.SendMessage(-1,0x0112,0xF170,-1)
    turn off screen monitor
        user32.dll.SendMessage(-1,0x0112,0xF170,2)

int WM_SYSCOMMAND = 0x0112;
int SC_MONITORPOWER = 0xF170;
SendMessage hWnd, WM_SYSCOMMAND, SC_MONITORPOWER, param

'''


from ctypes import windll
windll.user32

import win32api
SendMessage = win32api.SendMessage

class TurnOnOffMonitor:
    ON = -1
    OFF = 2
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    def turn_monitor_off_or_on(cls, on:bool):
        param = cls.ON if on else cls.OFF
        hWnd = -1
        SendMessage(hWnd, cls.WM_SYSCOMMAND, cls.SC_MONITORPOWER, param)
    def turn_on(cls):
        cls.turn_monitor_on_or_off(True)
    def turn_off(cls):
        cls.turn_monitor_on_or_off(False)

if False:
    win32api.Sleep(3000)
else:
    TurnOnOffMonitor.turn_off()
    win32api.Sleep(3000)
    TurnOnOffMonitor.turn_on()


