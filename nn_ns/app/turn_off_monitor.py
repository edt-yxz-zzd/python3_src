
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
    @classmethod
    def turn_monitor_off_or_on(cls, on:bool):
        param = cls.ON if on else cls.OFF
        hWnd = -1
        SendMessage(hWnd, cls.WM_SYSCOMMAND, cls.SC_MONITORPOWER, param)
    @classmethod
    def turn_on(cls):
        cls.turn_monitor_off_or_on(True)
    @classmethod
    def turn_off(cls):
        cls.turn_monitor_off_or_on(False)

def turn_monitor_off_by(ms):
    TurnOnOffMonitor.turn_off()
    win32api.Sleep(ms)
    TurnOnOffMonitor.turn_on()


def string2maybe_uint(s):
    try:
        u = int(s)
    except Exception:
        return None
    if u < 0:
        print('uint should not < 0')
        return None
    return u
def string2uint(s):
    u = string2maybe_uint(s)
    if u is None: raise ValueError
    return u
def string2uints(s):
    return list(map(string2uint, s.split()))
while True:
    s = input('input (mseconds[, times]) (enter "quit" to exit):')
    if s == 'quit': break

    try:
        us = string2uints(s)
    except Exception:
        continue
    L = len(us)
    if L == 1:
        [ms], times = us, 1
    elif L == 2:
        ms, times = us
    else:
        print(f'bad: {us}')
        continue

    ms += 10
    #times += 1

    for _ in range(times):
        TurnOnOffMonitor.turn_off()
        win32api.Sleep(ms)
        TurnOnOffMonitor.turn_on()
        win32api.Sleep(ms)


