#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/input7timeout.py

seed.lang.input7timeout
py -m nn_ns.app.debug_cmd   seed.lang.input7timeout -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.lang.input7timeout:__doc__ -ht # -ff -df
#######

[[
]]
[[
===
py.input() has no timeout:
===
e ../../python3_src/seed/for_libs/for_time.py
from seed.for_libs.for_time import sleep9KeyboardInterrupt_
===
e ../../python3_src/seed/for_libs/for_time.py
===
grep -F timeout -r /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/  -l
view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/curses.txt
view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/selectors.txt
view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/subprocess.txt

===
摘要如下:
===
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)
help read
  read -n 1
    <==> getch
  read -n 1 -t timeout -p prompt
  read -n 1 -t 3.0 -p '>>:' && printf %s  "$REPLY"
os.system(r'read -n 1 -t 3.0 -p ">>:" && printf %s  "$REPLY"')
  =>:sh: read: -p: no coprocess
  =>:512

===
class selectors.BaseSelector
   abstractmethod select(timeout=None)
   abstractmethod register(fileobj, events, data=None)
   abstractmethod unregister(fileobj)
   close()
class selectors.DefaultSelector

   The default selector class, using the most efficient implementation
   available on the current platform. This should be the default
   choice for most users.


class selectors.BaseSelector
   A "BaseSelector" is used to wait for I/O event readiness on
   multiple file objects. It supports file stream registration,
   unregistration, and a method to wait for I/O events on those
   streams, with an optional timeout. It's an abstract base class, so
   cannot be instantiated. Use "DefaultSelector" instead, or one of
   "SelectSelector", "KqueueSelector" etc. if you want to specifically
   use an implementation, and your platform supports it.
   "BaseSelector" and its concrete implementations support the
   *context manager* protocol.

   abstractmethod register(fileobj, events, data=None)

      Register a file object for selection, monitoring it for I/O
      events.

      *fileobj* is the file object to monitor.  It may either be an
      integer file descriptor or an object with a "fileno()" method.
      *events* is a bitwise mask of events to monitor. *data* is an
      opaque object.

      This returns a new "SelectorKey" instance, or raises a
      "ValueError" in case of invalid event mask or file descriptor,
      or "KeyError" if the file object is already registered.

   abstractmethod unregister(fileobj)

      Unregister a file object from selection, removing it from
      monitoring. A file object shall be unregistered prior to being
      closed.

      *fileobj* must be a file object previously registered.

      This returns the associated "SelectorKey" instance, or raises a
      "KeyError" if *fileobj* is not registered.  It will raise
      "ValueError" if *fileobj* is invalid (e.g. it has no "fileno()"
      method or its "fileno()" method has an invalid return value).


   abstractmethod select(timeout=None)

      Wait until some registered file objects become ready, or the
      timeout expires.

      If "timeout > 0", this specifies the maximum wait time, in
      seconds. If "timeout <= 0", the call won't block, and will
      report the currently ready file objects. If *timeout* is "None",
      the call will block until a monitored file object becomes ready.

      This returns a list of "(key, events)" tuples, one for each
      ready file object.

      *key* is the "SelectorKey" instance corresponding to a ready
      file object. *events* is a bitmask of events ready on this file
      object.

      Note:

        This method can return before any file object becomes ready or
        the timeout has elapsed if the current process receives a
        signal: in this case, an empty list will be returned.

      Changed in version 3.5: The selector is now retried with a
      recomputed timeout when interrupted by a signal if the signal
      handler did not raise an exception (see **PEP 475** for the
      rationale), instead of returning an empty list of events before
      the timeout.

   close()

      Close the selector.

      This must be called to make sure that any underlying resource is
      freed. The selector shall not be used once it has been closed.

def read_(fd, mask):
    print((fd, mask), (0, selectors.EVENT_READ))
    print(input('xxx:'))

def f():
    import selectors
    sel = selectors.DefaultSelector()
    key0 = sel.register(0, selectors.EVENT_READ, read_)
    assert read_ is key0.data
    assert 0 == key0.fileobj
    for _ in range(3):
        events = sel.select(timeout=3.0)
        for key, mask in events:
            assert key is key0
            callback = key.data
            callback(key.fileobj, mask)
    sel.close()

f() #可行！


===
使用curses容易造成界面混乱:
===
curses.initscr()

   Initialize the library. Return a window object which represents the
   whole screen.

   Note:

     If there is an error opening the terminal, the underlying curses
     library may cause the interpreter to exit.


curses.newwin(nlines, ncols)
curses.newwin(nlines, ncols, begin_y, begin_x)

   Return a new window, whose left-upper corner is at  "(begin_y,
   begin_x)", and whose height/width is  *nlines*/*ncols*.

   By default, the window will extend from the  specified position to
   the lower right corner of the screen.



Window objects, as returned by "initscr()" and "newwin()" above, have the following methods and attributes:

window.timeout(delay)

   Set blocking or non-blocking read behavior for the window.  If
   *delay* is negative, blocking read is used (which will wait
   indefinitely for input).  If *delay* is zero, then non-blocking
   read is used, and "getch()" will return "-1" if no input is
   waiting.  If *delay* is positive, then "getch()" will block for
   *delay* milliseconds, and return "-1" if there is still no input at
   the end of that time.



window.getch([y, x])

   Get a character. Note that the integer returned does *not* have to
   be in ASCII range: function keys, keypad keys and so on are
   represented by numbers higher than 255.  In no-delay mode, return
   "-1" if there is no input, otherwise wait until a key is pressed.

window.get_wch([y, x])

   Get a wide character. Return a character for most keys, or an
   integer for function keys, keypad keys, and other special keys. In
   no-delay mode, raise an exception if there is no input.

   Added in version 3.3.

window.getkey([y, x])

   Get a character, returning a string instead of an integer, as
   "getch()" does. Function keys, keypad keys and other special keys
   return a multibyte string containing the key name.  In no-delay
   mode, raise an exception if there is no input.
===
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.lang.input7timeout   @input7timeout_  :input:  =3.0 =False =666
py_adhoc_call   seed.lang.input7timeout   @input7timeout_  :input:  =3.0 =True =666

]]]'''#'''
__all__ = r'''
input7timeout_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


def input7timeout_(prompt, timeout, raise_if_timeout, default=None):
    'prompt/str -> timeout/float{unit:second} -> raise_if_timeout/bool -> str if not timeout else (default if not raise_if_timeout else ^TimeoutError)'
    from seed.tiny_.check import check_type_is
    check_type_is(str, prompt)
    check_type_is(float, timeout)
    check_type_is(bool, raise_if_timeout)

    import selectors
    with selectors.DefaultSelector() as sel:
        key0 = sel.register(0, selectors.EVENT_READ, '999')
        assert 0 == key0.fileobj
        assert '999' == key0.data
        print(prompt, end='', flush=True)
        events = sel.select(timeout=timeout)
        for key, mask in events:
            assert key is key0
            #bug:return input(prompt)
            return input()
        else:
            if raise_if_timeout:
                raise TimeoutError((prompt, timeout, default))
            return default





__all__
from seed.lang.input7timeout import input7timeout_
from seed.lang.input7timeout import *
