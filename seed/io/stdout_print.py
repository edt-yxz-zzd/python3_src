

__all__ = ['stdout_print']

#from sys import stdout
import sys
from io import StringIO
def stdout_print(*args, encoding='utf8', **kwargs):
    sout = StringIO()
    print(*args, **kwargs, file=sout)
    string = sout.getvalue()

    b_stdout = sys.stdout.buffer
    bs = string.encode(encoding=encoding)
    b_stdout.write(bs)


