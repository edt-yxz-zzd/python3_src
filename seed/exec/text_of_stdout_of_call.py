r'''
example:
    >>> text_of_stdout_of_call('py -c print(1)'.split())
    '1\n'
    >>> text_of_stdout_of_call('py -c print(1 1)'.split(), stderr=DEVNULL) #doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    subprocess.CalledProcessError:...

import subprocess
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)¶
from seed.exec.text_of_stdout_of_call import text_of_stdout_of_call
def text_of_stdout_of_call(args, **kwargs):

#'''

__all__ = '''
    text_of_stdout_of_call
    '''.split()

from subprocess import Popen, PIPE, DEVNULL
import subprocess
import locale

def text_of_stdout_of_call(args, **kwargs):
    r = subprocess.run(args
            , stdout=PIPE, universal_newlines=True, check=True, **kwargs)
    stdout = r.stdout
    #encoding = locale.getpreferredencoding(False)
    #bug: return stdout.decode(encoding)
    assert type(stdout) is str # since universal_newlines=True??
    txt = stdout
    return txt

    #https://stackoverflow.com/questions/33435110/subprocess-popen-stdout
    #bufsize=1?
    with Popen(args, stdout=PIPE, universal_newlines=True, check=True, **kwargs) as process:
        bs = b''.join(process.stdout)
        return bs.decode(encoding)
        if 0:
            for line in io.TextIOWrapper(process.stdout, encoding=encoding):
                print(line, end='')
        else:
            for line in process.stdout: # b'\n', b'\r\n', b'\r' are recognized as newline
                print(line, end='')


from seed.exec.text_of_stdout_of_call import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

from seed.exec.text_of_stdout_of_call import text_of_stdout_of_call
from seed.exec.text_of_stdout_of_call import *
