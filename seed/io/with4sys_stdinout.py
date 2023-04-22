#__all__:goto
r'''[[[
e ../../python3_src/seed/io/with4sys_stdinout.py


seed.io.with4sys_stdinout
py -m nn_ns.app.debug_cmd   seed.io.with4sys_stdinout -x
py -m nn_ns.app.doctest_cmd seed.io.with4sys_stdinout:__doc__ -v
py -m nn_ns.app.doctest_cmd seed.io.with4sys_stdinout!
py_adhoc_call   seed.io.with4sys_stdinout   @f


>>> from seed.io.with4sys_stdinout import with_as_tmp_stdxxx_, with_as_tmp_stdin, with_as_tmp_stdout, with_as_tmp_stderr
>>> import sys
>>> from sys import stdin, stdout, stderr

>>> with with_as_tmp_stdin('aaa') as ifile:
...     ifile.read()
...     stdin is not sys.stdin is ifile
'aaa'
True
>>> stdout is sys.stdout is not ifile
True
>>> with with_as_tmp_stdout('bbb') as ofile:
...     ofile.seek(3)
...     ofile.write('xxx')
...     ofile.getvalue()
...     stdout is not sys.stdout is ofile
>>> stdout is sys.stdout is not ofile
True
>>> print(ofile.getvalue())
bbb3
xxx3
'bbb3\nxxx3\n'
True
<BLANKLINE>
>>> with with_as_tmp_stderr('ccc') as ofile:
...     ofile.seek(3)
...     ofile.write('yyy')
...     ofile.getvalue()
...     stderr is not sys.stderr is ofile
3
3
'cccyyy'
True
>>> stderr is sys.stderr is not ofile
True


#]]]'''
__all__ = r'''
with_as_tmp_stdxxx_
    with_as_tmp_stdin
    with_as_tmp_stdout
    with_as_tmp_stderr
'''.split()#'''
__all__

from seed.helper.with4cleanup import no_cleanup, with4cleanup_, with4cleanup__on_err_, with4cleanup__on_no_err, with4cleanup__on_exit, with4cleanup__never
import sys
from io import StringIO

def _prepare(nm, xfile, /):
    if type(xfile) is str:
        s = xfile
        xfile = StringIO(s)
    stdnm = 'std'+nm
    stdxxx = getattr(sys, stdnm)
    setattr(sys, stdnm, xfile)
    internal_state = nm, stdxxx
    external_obj = xfile
    return (internal_state, external_obj)
def _cleanup(internal_state, external_obj, /):
    nm, stdxxx = internal_state
    xfile = external_obj
    stdnm = 'std'+nm
    _xfile = getattr(sys, stdnm)
    setattr(sys, stdnm, stdxxx)
    if not xfile is _xfile: raise Exception(f'sys.{stdnm} was changed')
        #check _xfile is xfile?

def with_as_tmp_stdxxx_(nm, xfile, /):
    'tmp replace sys.std{nm} #donot close xfile'
    if not nm in 'in out err':raise TypeError(nm)
    return with4cleanup__on_exit(_cleanup, 2, _prepare, nm, xfile)

def with_as_tmp_stdin(ifile, /):
    'tmp replace sys.stdin #donot close ifile'
    return with_as_tmp_stdxxx_('in', ifile)
def with_as_tmp_stdout(ofile, /):
    'tmp replace sys.stdout #donot close ofile'
    return with_as_tmp_stdxxx_('out', ofile)
def with_as_tmp_stderr(ofile, /):
    'tmp replace sys.stderr #donot close ofile'
    return with_as_tmp_stdxxx_('err', ofile)



__all__


from seed.io.with4sys_stdinout import with_as_tmp_stdxxx_, with_as_tmp_stdin, with_as_tmp_stdout, with_as_tmp_stderr
from seed.io.with4sys_stdinout import *
