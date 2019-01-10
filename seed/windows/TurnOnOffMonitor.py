
'''
https://stackoverflow.com/questions/713498/turn-on-off-monitor
    turn on screen monitor
        user32.dll.SendMessage(-1,0x0112,0xF170,-1)
    turn off screen monitor
        user32.dll.SendMessage(-1,0x0112,0xF170,2)

win32api.SendMessage
    prototype(("SendMessage", windll.user32), ??paramflags??)

int WM_SYSCOMMAND = 0x0112;
int SC_MONITORPOWER = 0xF170;
SendMessage hWnd, WM_SYSCOMMAND, SC_MONITORPOWER, param

'''

__all__ = '''
    TurnOnOffMonitor
    turn_monitor_off_by
    '''.split()


import win32api # SendMessage Sleep
import win32con # WM_SYSCOMMAND SC_MONITORPOWER
win32api.SendMessage
win32api.Sleep


class TurnOnOffMonitor:
    ON = -1
    OFF = 2
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    assert WM_SYSCOMMAND == win32con.WM_SYSCOMMAND
    assert SC_MONITORPOWER == win32con.SC_MONITORPOWER

    @classmethod
    def turn_monitor_off_or_on(cls, on:bool):
        param = cls.ON if on else cls.OFF
        hWnd = -1
        win32api.SendMessage(hWnd, cls.WM_SYSCOMMAND, cls.SC_MONITORPOWER, param)
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


def _show_win32con():
    for name in dir(win32con):
        value = getattr(win32con, name)
        print(f'{name} = {value!r}')
def _show_win32con__to_find_ON_OFF(_2_pred, *, value_pred=None):
    values_to_find = (TurnOnOffMonitor.ON, TurnOnOffMonitor.OFF)
    for name in dir(win32con):
        value = getattr(win32con, name)
        if (type(value) is int and
            (value in values_to_find)
                if value_pred is None
                else value_pred(value)
            ):
            if _2_pred(name=name, value=value):
                print(f'{name} = {value!r}')

if __name__ == "__main__":
    # _show_win32con()
    # _show_win32con__to_find_ON_OFF(pred)

    pred = None
    value_pred = None
    if 0:
        pred = (lambda *, name, value:
            'ON' in name or 'OFF' in name)
    elif 0:
        pred = (lambda *, name, value:
                ('ON' in name and value == ON)
                or ('OFF' in name and value == OFF)
                )
    elif 1:
        pred = (lambda *, name, value:
            'MON' in name # MONITOR POWER
            )
        value_pred = lambda value: True
        '''
        MONITOR_DEFAULTTONEAREST = 2
        MONITOR_DEFAULTTONULL = 0
        MONITOR_DEFAULTTOPRIMARY = 1
        '''

    if pred is not None:
        _show_win32con__to_find_ON_OFF(pred, value_pred=value_pred)


