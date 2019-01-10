
from seed.windows.TurnOnOffMonitor import (
    TurnOnOffMonitor, turn_monitor_off_by
    )
import win32api # Sleep

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


