
r'''
e ../../python3_src/seed/sys/timeout/timeout_via_signal_alarm.py
view ../lots/NOTE/Python/howto/set-timeout-to-kill-thread-or-subprocess.txt

from seed.sys.timeout.timeout_via_signal_alarm import timeout_via_signal_alarm

#'''


__all__ = '''
    timeout_via_signal_alarm

    '''.split()

#import sys
#import random
#import time
import signal
#help(signal.signal)
#help(signal.alarm)



#class _TimeoutError(TimeoutError):pass
class _TimeoutError(BaseException):pass
def handle_timeout(sig, frame):
    raise _TimeoutError


def timeout_via_signal_alarm(seconds, f, /):
    if not seconds > 0: raise ValueError
    if not callable(f): raise TypeError
    prev_handler = signal.signal(signal.SIGALRM, handle_timeout)

    prev_remain_seconds = signal.alarm(seconds)

    try:
        result = f()
    except _TimeoutError as exc:
        tmay_result = ()
    else:
        tmay_result = (result,)
    finally:
        signal.signal(signal.SIGALRM, prev_handler)
        if prev_remain_seconds > 0:
            prev_remain_seconds -= seconds
        if prev_remain_seconds > 0:
            signal.alarm(prev_remain_seconds)
        else:
            signal.alarm(0)
    return tmay_result





