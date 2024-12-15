#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_signal.py

seed.for_libs.for_signal
py -m nn_ns.app.debug_cmd   seed.for_libs.for_signal -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_signal:__doc__ -ht # -ff -df

[[
源起:
view ../../python3_src/seed/io/continue_io__folder.py
view script/搜索冫某进制表达数乊多种进制解读皆为素数.py
    py_adhoc_call   script.搜索冫某进 制表达数乊多种进制解读皆为素数   @_八位十六进制数囗后 续五种素进制解读皆为素数囗断点重启冫拆分成两百五十六个串行子任务
++kw:to_postpone_KeyboardInterrupt_until_subtask_switchover
(Ctrl+C)KeyboardInterrupt 延迟触发直到子任务切换
]]

[[[
KeyboardInterrupt
httpd -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html
    http://127.0.0.1:3124/library/signal.html#handlers-and-exceptions
        Note on Signal Handlers and Exceptions
signal.SIGINT
long-running calculation implemented purely in C

signal.getsignal(signalnum)
signal.strsignal(signalnum)
signal.raise_signal(signum)
signal.signal(signalnum, handler)


[signal.getsignal :: (signalnum) -> may_xhandler]
[signal.strsignal :: (signalnum) -> may description<xhandler>/str]
[signal.signal :: (signalnum, xhandler) -> prev may_xhandler]
[may_xhandler == (xhandler|None)]
[xhandler == (handler|SIG_DFL/default|SIG_IGN/ignore)]
[handler :: (signum, frame) -> None|^BaseException]
    handler只被主线程所部署
    handler只被主线程所调用
    若handler抛出异常，则任何地方都可能抛出异常，python没有任何机制保证状态健全(__enter__执行(或半执行)而__exit__不执行)，所以最好退出程序
===

signal.getsignal(signalnum)
Return the current signal handler for the signal signalnum. The returned value may be a callable Python object, or one of the special values signal.SIG_IGN, signal.SIG_DFL or None. Here, signal.SIG_IGN means that the signal was previously ignored, signal.SIG_DFL means that the default way of handling the signal was previously in use, and None means that the previous signal handler was not installed from Python.

signal.strsignal(signalnum)
Returns the description of signal signalnum, such as “Interrupt” for SIGINT. Returns None if signalnum has no description. Raises ValueError if signalnum is invalid.

Added in version 3.8.


signal.raise_signal(signum)¶
Sends a signal to the calling process. Returns nothing.

Added in version 3.8.



signal.signal(signalnum, handler)
Set the handler for signal signalnum to the function handler. handler can be a callable Python object taking two arguments (see below), or one of the special values signal.SIG_IGN or signal.SIG_DFL. The previous signal handler will be returned (see the description of getsignal() above). (See the Unix man page signal(2) for further information.)

When threads are enabled, this function can only be called from the main thread of the main interpreter; attempting to call it from other threads will cause a ValueError exception to be raised.

The handler is called with two arguments: the signal number and the current stack frame (None or a frame object; for a description of frame objects, see the description in the type hierarchy or see the attribute descriptions in the inspect module).

On Windows, signal() can only be called with SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, SIGTERM, or SIGBREAK. A ValueError will be raised in any other case. Note that not all systems define the same set of signal names; an AttributeError will be raised if a signal name is not defined as SIG* module level constant.


===
example:

import signal, os

def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm
Note on SIGPIPE

===
===
===
===
]]]

py_adhoc_call   seed.for_libs.for_signal   @f
]]]'''#'''
__all__ = r'''
PostponeKeyboardInterrupt

check_xhandler_or_whether_turnoff
check_xhandler
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.debug.print_err import print_err
from contextlib import AbstractContextManager
import signal
___end_mark_of_excluded_global_names__0___ = ...

def check_xhandler(xhandler, /):
    if not (callable(xhandler) or xhandler is signal.SIG_IGN or xhandler is signal.SIG_DFL): raise TypeError
def check_xhandler_or_whether_turnoff(xhandler_or_whether_turnoff, /):
    if not type(xhandler_or_whether_turnoff) is bool:
        xhandler = xhandler_or_whether_turnoff
        check_xhandler(xhandler)
class PostponeKeyboardInterrupt(AbstractContextManager):
    'see: kw:to_postpone_KeyboardInterrupt_until_subtask_switchover'
    __slots__ = ()
    def __init__(sf, xhandler_or_whether_turnoff=False, /, may_prompt_string=None):
        if not (may_prompt_string is None or type(may_prompt_string) is str):raise TypeError(type(may_prompt_string))
        check_xhandler_or_whether_turnoff(xhandler_or_whether_turnoff)
        if xhandler_or_whether_turnoff is False:
            # [xhandler==SIG_IGN] <==> whether_turnoff==False]
            xhandler_or_whether_turnoff = signal.SIG_IGN
        sf._off_or_xhdlr = xhandler_or_whether_turnoff
        sf._tmay_prev = ()
        sf._b_interrupt = False
        sf._m_prompt = may_prompt_string
    def handler(sf, signum, frame, /):
        assert signum == signal.SIGINT
        #signame = signal.Signals(signum).name
        off_or_xhdlr = sf._off_or_xhdlr
        if off_or_xhdlr is True: raise 000
        assert not off_or_xhdlr is False
        xhandler = off_or_xhdlr

        sf._b_interrupt = True
        if callable(xhandler):
            handler = xhandler
            handler(signum, frame)
        elif xhandler is signal.SIG_IGN:
            # [xhandler==SIG_IGN] <==> whether_turnoff==False]
            may_prompt_string = sf._m_prompt
            if not may_prompt_string is None:
                prompt_string = may_prompt_string
                print_err(prompt_string, end='')
            pass#SIG_IGN
        elif xhandler is signal.SIG_DFL:
            assert signum == signal.SIGINT
            raise KeyboardInterrupt
        else:
            raise Exception('unknown case', xhandler)

    #@override
    def __enter__(sf, /):
        '-> (prev_may_xhandler if not turnoff else False)'
        off_or_xhdlr = sf._off_or_xhdlr
        if off_or_xhdlr is True:
            # turnoff PostponeKeyboardInterrupt
            return False
        #xhandler = off_or_xhdlr

        if sf._tmay_prev:raise Exception('re-enter')
        if sf._b_interrupt:raise Exception('re-enter')
        prev_may_xhandler = signal.signal(signal.SIGINT, sf.handler)
        sf._tmay_prev = (prev_may_xhandler,)
        return prev_may_xhandler

    #@override
    def __exit__(sf, exc_type, exc_value, traceback, /):
        r'''
        Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.

        If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.

        Note that __exit__() methods should not reraise the passed-in exception; this is the caller’s responsibility.
        #'''
        off_or_xhdlr = sf._off_or_xhdlr
        if off_or_xhdlr is True:
            # turnoff PostponeKeyboardInterrupt
            return None#reraise
            return False
        #xhandler = off_or_xhdlr

        [prev_may_xhandler] = sf._tmay_prev
        whether_interrupt = sf._b_interrupt
        sf._tmay_prev = ()
        sf._b_interrupt = False

        #if not sf.handler == signal.signal(signal.SIGINT, prev_may_xhandler): raise 000
        _handler = signal.signal(signal.SIGINT, prev_may_xhandler)
        if not sf.handler == _handler: raise 000

        if not exc_type is None:
            return None#reraise
        if whether_interrupt:
            signal.raise_signal(signal.SIGINT)

PostponeKeyboardInterrupt()
PostponeKeyboardInterrupt(False)
PostponeKeyboardInterrupt(True)

__all__
from seed.for_libs.for_signal import PostponeKeyboardInterrupt
from seed.for_libs.for_signal import *
