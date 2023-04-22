#__all__:goto
r'''[[[
e ../../python3_src/seed/io/iter_line_contents__ver2.py


seed.io.iter_line_contents__ver2
py -m nn_ns.app.debug_cmd   seed.io.iter_line_contents__ver2 -x
py -m nn_ns.app.doctest_cmd seed.io.iter_line_contents__ver2:__doc__ -ff -v


>>> from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path__human, iter_line_contents__path
>>> from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__file__human, iter_line_contents__file
>>> from seed.io.iter_line_contents__ver2 import check_newlines, split_out_newline_, default_newlines, default_may_newlines
>>> from seed.io.iter_line_contents__ver2 import default_may_smay_newline
>>> from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path_, iter_line_contents_ex__file_


TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
>>> from io import BytesIO, TextIOWrapper

>>> bs = b''
>>> ibfile = BytesIO(bs)
>>> ifile = TextIOWrapper(ibfile, newline=None)
>>> ifile.reconfigure(newline=None)
>>> ifile.reconfigure(newline='')
>>> ifile.reconfigure(newline='\r')
>>> ifile.reconfigure(newline='\n')
>>> ifile.reconfigure(newline='\r\n')
>>> ifile.reconfigure(newline='+')
Traceback (most recent call last):
    ...
ValueError: illegal newline value: +


>>> bs = b'\n\r\r\n'
>>> ibfile = BytesIO(bs)
>>> ifile = TextIOWrapper(ibfile, newline=default_may_smay_newline, encoding='u8')
>>> [*iter_line_contents_ex__file__human(ifile)]
[('', '\n'), ('', '\r'), ('', '\r\n'), ('', '')]
>>> __ = ifile.seek(0)
>>> [*iter_line_contents_ex__file__human(ifile, without_last_line_if_empty=True)]
[('', '\n'), ('', '\r'), ('', '\r\n')]
>>> __ = ifile.seek(0)
>>> [*iter_line_contents__file(ifile, without_last_line_if_empty=True)]
['', '', '']
>>> __ = ifile.seek(0)
>>> [*iter_line_contents__file(ifile)]
['', '', '', '']


>>> bs = b'\n\r\r\n777'
>>> ibfile = BytesIO(bs)
>>> ifile = TextIOWrapper(ibfile, newline=default_may_smay_newline, encoding='u8')
>>> [*iter_line_contents_ex__file__human(ifile)]
[('', '\n'), ('', '\r'), ('', '\r\n'), ('777', '')]
>>> __ = ifile.seek(0)
>>> [*iter_line_contents_ex__file__human(ifile, without_last_line_if_empty=True)]
[('', '\n'), ('', '\r'), ('', '\r\n'), ('777', '')]
>>> __ = ifile.seek(0)
>>> [*iter_line_contents__file(ifile, without_last_line_if_empty=True)]
['', '', '', '777']
>>> __ = ifile.seek(0)
>>> [*iter_line_contents__file(ifile)]
['', '', '', '777']


>>> def f(may_smay_newline, /):
...     ifile.reconfigure(newline=may_smay_newline)
...     __ = ifile.seek(0)
...     return [*iter_line_contents_ex__file__human(ifile, newlines__or__may_smay_newline=may_smay_newline)]


>>> f(None)
[('', '\n'), ('', '\n'), ('', '\n'), ('777', '')]

>>> f('')
[('', '\n'), ('', '\r'), ('', '\r\n'), ('777', '')]

>>> f('\r')
[('\n', '\r'), ('', '\r'), ('\n777', '')]

>>> f('\n')
[('', '\n'), ('\r\r', '\n'), ('777', '')]

>>> f('\r\n')
[('\n\r', '\r\n'), ('777', '')]



#]]]'''
__all__ = r'''
check_newlines
    split_out_newline_
    default_newlines
    default_may_newlines

default_may_smay_newline
newlines5may_smay_newline_
    may_smay_newline2newlines
    check_may_smay_newline

iter_line_contents_ex__path_
    iter_line_contents_ex__path__human
    iter_line_contents__path

iter_line_contents_ex__file_
    iter_line_contents_ex__file__human
    iter_line_contents__file



'''.split()#'''
__all__

from itertools import pairwise
from seed.tiny import check_type_is
from seed.tiny import ifNonef, fst, MapView

def check_newlines(newlines, /):
    check_type_is(tuple, newlines)
    assert newlines
    assert all(type(x) is str for x in newlines)
    assert all(newlines)
    assert all(m <= n for m,n in pairwise(map(len, newlines)))
    assert newlines == tuple(sorted(newlines, key=len))

def split_out_newline_(newlines, line, /):
    r'''-> (line_content, smay_newline)

    precondition:
        [check_newlines(newlines)]
            [len(newlines) > 0]
            [all(newlines)]
            [newlines == tuple(sorted(newlines, key=len))]

    postcondition:
        [line == line_content++smay_newline]

    '''#'''
    #check_newlines(newlines)

    for newline in reversed(newlines):
        #assert newlines == tuple(sorted(newlines, key=len))
        #   <<== [check_newlines(newlines)]
        if line.endswith(newline):
            smay_newline = newline
            break
    else:
        smay_newline = ''
    smay_newline
    L = len(line)-len(smay_newline)
    line_content = line[:L]
    assert smay_newline == line[L:]
    return (line_content, smay_newline)






#_newlines = ('\r\n', '\r', '\n')
_newlines = ('\r', '\n', '\r\n')
check_newlines(_newlines)
default_newlines = _newlines
default_may_newlines = None


_newline = ''
default_may_smay_newline = _newline
assert not _newline in _newlines
assert not _newline is None

may_smay_newline2newlines = MapView(
{None: ('\n',)
    #[read] -> [universal_newline][all translate into "\n"]
,'': _newlines
    #[read/write] -> [universal_newline][no translation takes place]
,'\r':('\r',)
    #[read] -> [no translation takes place]
,'\n':('\n',)
    #[read] -> [no translation takes place]
,'\r\n':('\r\n',)
    #[read] -> [no translation takes place]
})

def check_may_smay_newline(may_smay_newline, /):
    if not may_smay_newline is None:
        smay_newline = may_smay_newline
        check_type_is(str, smay_newline)

def newlines5may_smay_newline_(may_smay_newline, /):
    check_may_smay_newline(may_smay_newline)
    return ifNonef(may_smay_newline2newlines.get(may_smay_newline), lambda:(may_smay_newline,))
    return may_smay_newline2newlines[may_smay_newline]
assert default_newlines is newlines5may_smay_newline_(default_may_smay_newline)



def iter_line_contents_ex__path_(ipath, /, *, encoding, newline, kwargs4open, may_newlines, without_last_line_if_empty):
    r'''-> Iter (line_content, smay_newline)

    [[newline := ""] -> [universal_newline][no translation takes place]]
    input:
        encoding :: may str

        newline :: may str
            newline <- [None, '', '\r', '\n', '\r\n']

        kwargs4open :: kwargs of py.open() except `encoding`,`newline`

        may_newlines :: may tuple<str>
        without_last_line_if_empty :: bool

    precondition:
        [check_newlines(newlines)]
            [len(newlines) > 0]
            [all(newlines)]
            [newlines == tuple(sorted(newlines, key=len))]

    postcondition:
        [line == line_content++smay_newline]
        [[len(smay_newline) == 0] -> [last_line]]

        * [without_last_line_if_empty==True]:
            [[len(smay_newline) == 0] -> [[last_line][len(line_content) > 0]]]
        * [without_last_line_if_empty==False]:
            [[len(smay_newline) == 0] <-> [last_line]]


    '''#'''
    check_type_is(bool, without_last_line_if_empty)

    newlines = ifNonef(may_newlines, lambda:newlines5may_smay_newline_(newline))
    check_type_is(tuple, newlines)

    kwargs4open = ifNonef(kwargs4open, dict)


    with open(ipath, 'rt', encoding=encoding, newline=newline, **kwargs4open) as ifile:
        yield from iter_line_contents_ex__file_(ifile, newlines__or__may_smay_newline=newlines, without_last_line_if_empty=without_last_line_if_empty)

def iter_line_contents_ex__path__human(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
    return iter_line_contents_ex__path_(ipath, encoding=encoding, newline=newline, kwargs4open=kwargs4open, may_newlines=may_newlines, without_last_line_if_empty=without_last_line_if_empty)
iter_line_contents_ex__path__human.__doc__ = iter_line_contents_ex__path_.__doc__

def iter_line_contents__path(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
    r'-> Iter line_content # without newline'
    return map(fst, iter_line_contents_ex__path_(ipath, encoding=encoding, newline=newline, kwargs4open=kwargs4open, may_newlines=may_newlines, without_last_line_if_empty=without_last_line_if_empty))








def iter_line_contents_ex__file_(ifile, /, *, newlines__or__may_smay_newline, without_last_line_if_empty):
    r'''-> Iter (line_content, smay_newline)

    input:
        newlines__or__may_smay_newline :: newlines/tuple<str> | may_smay_newline/(may str)
        without_last_line_if_empty :: bool

    precondition:
        [check_newlines(newlines)]
            [len(newlines) > 0]
            [all(newlines)]
            [newlines == tuple(sorted(newlines, key=len))]

    postcondition:
        [line == line_content++smay_newline]
        [[len(smay_newline) == 0] -> [last_line]]

        * [without_last_line_if_empty==True]:
            [[len(smay_newline) == 0] -> [[last_line][len(line_content) > 0]]]
        * [without_last_line_if_empty==False]:
            [[len(smay_newline) == 0] <-> [last_line]]


    '''#'''
    check_type_is(bool, without_last_line_if_empty)

    if not type(newlines__or__may_smay_newline) is tuple:
        may_smay_newline = newlines__or__may_smay_newline
        newlines = newlines5may_smay_newline_(may_smay_newline)
    else:
        newlines = newlines__or__may_smay_newline

    check_newlines(newlines)

    smay_newline = 999
    for line in ifile:
        if not smay_newline: raise ValueError(newlines, smay_newline, line) #expect eof
            # <<== [[len(smay_newline) == 0] -> [last_line]]

        (line_content, smay_newline) = split_out_newline_(newlines, line)
        yield (line_content, smay_newline)
    if smay_newline and not without_last_line_if_empty:
        yield ('', '')

def iter_line_contents_ex__file__human(ifile, /, *, newlines__or__may_smay_newline=default_newlines, without_last_line_if_empty=False):
    return iter_line_contents_ex__file_(ifile, newlines__or__may_smay_newline=newlines__or__may_smay_newline, without_last_line_if_empty=without_last_line_if_empty)
iter_line_contents_ex__file__human.__doc__ = iter_line_contents_ex__file_.__doc__

def iter_line_contents__file(ifile, /, *, newlines__or__may_smay_newline=default_newlines, without_last_line_if_empty=False):
    r'-> Iter line_content # without newline'
    return map(fst, iter_line_contents_ex__file_(ifile, newlines__or__may_smay_newline=newlines__or__may_smay_newline, without_last_line_if_empty=without_last_line_if_empty))


r'''
iter_line_contents_ex__file_
    iter_line_contents_ex__file__human
    iter_line_contents__file

iter_line_contents_ex__lines_
    iter_line_contents_ex__lines__human
    iter_line_contents__lines
'''#'''


from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path__human, iter_line_contents__path
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__file__human, iter_line_contents__file
from seed.io.iter_line_contents__ver2 import check_newlines, split_out_newline_, default_newlines, default_may_newlines
from seed.io.iter_line_contents__ver2 import default_may_smay_newline
from seed.io.iter_line_contents__ver2 import newlines5may_smay_newline_, may_smay_newline2newlines, check_may_smay_newline
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path_, iter_line_contents_ex__file_
from seed.io.iter_line_contents__ver2 import *
