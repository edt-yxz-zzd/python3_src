


r"""
>>> f = lambda fin: fin.read()
>>> g = None

>>> with_text_input_file__text("1753", f, g, yield_from=False)
'1753'

>>> with_text_input_file__bytes(b"1753", f, g, encoding='utf8', yield_from=False)
'1753'

>>> this = with_text_input_file__path(__file__, f, g, encoding='utf8', yield_from=False)
>>> all(nm in this for nm in __all__)
True

>>> with io.FileIO(__file__) as rawfile:
...     this_r = with_text_input_file__binary(rawfile, f, g, encoding='utf8', yield_from=False)
>>> this == this_r
True

>>> with open(__file__, 'rb') as bbfile:
...     this_b = with_text_input_file__binary(bbfile, f, g, encoding='utf8', yield_from=False)
>>> this == this_b
True

>>> with open(__file__, 'rt', encoding='utf8') as tfile:
...     this_t = with_text_input_file(tfile, f, g, yield_from=False)
>>> this == this_t
True




#with_text_input_file_

>>> with_text_input_file_("1753", f, g, encoding='', case='data', yield_from=False)
'1753'
>>> with_text_input_file_(b"1753", f, g, encoding='utf8', case='data', yield_from=False)
'1753'
>>> this == with_text_input_file_(__file__, f, g, encoding='utf8', case='path', yield_from=False)
True

>>> with io.FileIO(__file__) as rawfile:
...     this_r = with_text_input_file_(rawfile, f, g, encoding='utf8', case='stream', yield_from=False)
>>> this == this_r
True

>>> with open(__file__, 'rb') as bbfile:
...     this_b = with_text_input_file_(bbfile, f, g, encoding='utf8', case='stream', yield_from=False)
>>> this == this_b
True

>>> with open(__file__, 'rt', encoding='utf8') as tfile:
...     this_t = with_text_input_file_(tfile, f, g, encoding='', case='stream', yield_from=False)
>>> this == this_t
True






# yield_from

>>> with_text_input_file__text("1753", f, g, yield_from=True) #doctest: +ELLIPSIS
<generator object yield_from4with_text_input_file at ...>

>>> [*_]
['1', '7', '5', '3']

#"""

__all__ = '''
    is_RawIO
    is_BufferedIO
    is_TextIO
    binary_input_file2text_input_file

    with_text_input_file
    with_text_input_file_
        with_text_input_file__text
        with_text_input_file__path
        with_text_input_file__bytes
        with_text_input_file__binary

        kwargs2tuple4with_text_input_file
        open_ex4with_text_input_file
        return4with_text_input_file
        yield_from4with_text_input_file
    '''.split()

import io
from pathlib import PurePath
from seed.tiny import ifNone, echo
#from seed.tiny import print_err


def is_RawIO(stream):
    return hasattr(stream, 'readall')
def is_BufferedIO(stream):
    return hasattr(stream, 'readinto1')
def is_TextIO(stream):
    return hasattr(stream, 'encoding') and hasattr(stream, 'newlines')

def binary_input_file2text_input_file(binary_input_file, encoding):
    bfile = binary_input_file
    if is_RawIO(bfile):
        bfile = io.BufferedReader(bfile)
    assert is_BufferedIO(bfile)
    tfile = io.TextIOWrapper(bfile, encoding=encoding)
    text_input_file = tfile
    return text_input_file

def with_text_input_file_(input, on_file, may_post_file, *, yield_from:bool, encoding, case:'stream|path|data'):
    _input = kwargs2tuple4with_text_input_file(input, encoding=encoding, case=case)
    return with_text_input_file(_input, on_file, may_post_file, yield_from=yield_from)

def _yield_Nothing_then_echo(x):
    return x; yield
def with_text_input_file(input, on_file, may_post_file, *, yield_from:bool):
    yield_from = bool(yield_from)
    on_file = ifNone(on_file, echo) #maybe closed fin
    may_post_file = ifNone(may_post_file, (echo if not yield_from else _yield_Nothing_then_echo))

    did_open, tfile = open_ex4with_text_input_file(input)
    if yield_from:
        f = yield_from4with_text_input_file
    else:
        f = return4with_text_input_file
    return f(did_open, tfile, on_file, may_post_file)

def kwargs2tuple4with_text_input_file(input, *, encoding, case:'stream|path|data'):
    r"""
    stream+encoding ==>> text_input_file
    stream+'' ==>> binary_input_file
    data+encoding ==>> text
    data+'' ==>> bytes
    path+encoding ==>> path
    path+'' ==>> err

    #"""
    if case not in ('stream', 'path', 'data'): raise ValueError

    if case == 'path':
        path = input
        if not encoding: raise ValueError("should not omit encoding")
        _input = 'path', path, encoding
    else:
        is_text = not encoding
        if case == 'data':
            _case = 'text' if is_text else 'bytes'
        elif case == 'stream':
            _case = 'text_input_file' if is_text else 'binary_input_file'
        else:
            raise logic-error
        if is_text:
            _input = _case, input
        else:
            _input = _case, input, encoding
    return _input

def return4with_text_input_file(did_open, tfile, on_file, may_post_file):
    if did_open:
        with tfile:
            mid = on_file(tfile)
    else:
        mid = on_file(tfile)
    return may_post_file(mid)
def yield_from4with_text_input_file(did_open, tfile, on_file, may_post_file):
    if did_open:
        with tfile:
            mid = yield from on_file(tfile)
    else:
        mid = yield from on_file(tfile)
    r = yield from may_post_file(mid)
    return r


def open_ex4with_text_input_file(input):
    r"""
    #input = fin | txt | (path, encoding) | (bytes, encoding)
    input
        = text_input_file
        | ('text_input_file', text_input_file)
        | ('text', txt)
        | ('path', path_or_fd, encoding)
        | ('bytes', bytes, encoding)
        | ('binary_input_file', binary_input_file, encoding)
    #"""

    if type(input) is not tuple:
        if isinstance(input, (int, str, bytes, bytearray, memoryview, PurePath)):
            raise TypeError
        ####
        if not hasattr(input, 'readline'):
            raise TypeError
        text_input_file = input
        input = ('text_input_file', text_input_file)
    ####
    assert type(input) is tuple
    if not input:
        raise TypeError

    ####
    case2len = dict(
            text_input_file=2
            ,text=2
            ,path=3
            ,bytes=3
            ,binary_input_file=3
            )
    case = input[0]
    if case2len.get(case, -1) != len(input):
        raise TypeError(f"case={case!r}; len={len(input)}")



    if case == 'path':
        _, path_or_fd, encoding = input
        tfile = open(path_or_fd, "rt", encoding=encoding)
        #with open(path_or_fd, "rt", encoding=encoding) as tfile:
            #mid = on_file(tfile)
        did_open = True
    else:
        if case == 'text_input_file':
            _, tfile = input
        elif case == 'text':
            _, txt = input
            tfile = io.StringIO(txt)
        elif case == 'binary_input_file':
            _, bfile, encoding = input
            tfile = binary_input_file2text_input_file(bfile, encoding)
        elif case == 'bytes':
            _, bs, encoding = input
            bfile = io.BytesIO(memoryview(bs))
            tfile = binary_input_file2text_input_file(bfile, encoding)
        else:
            raise logic-error
        assert is_TextIO(tfile)
        #if __debug__: print_err(tfile.encoding)
        #mid = on_file(tfile)
        did_open = False
    #return may_post_file(mid)
    return did_open, tfile



def with_text_input_file__text(txt, on_file, may_post_file, *, yield_from):
    input = ('text', txt)
    return with_text_input_file(input, on_file, may_post_file, yield_from=yield_from)

def with_text_input_file__path(path, on_file, may_post_file, *, encoding, yield_from):
    input = ('path', path, encoding)
    return with_text_input_file(input, on_file, may_post_file, yield_from=yield_from)

def with_text_input_file__bytes(bs, on_file, may_post_file, *, encoding, yield_from):
    input = ('bytes', bs, encoding)
    return with_text_input_file(input, on_file, may_post_file, yield_from=yield_from)

def with_text_input_file__binary(bfile, on_file, may_post_file, *, encoding, yield_from):
    input = ('binary_input_file', bfile, encoding)
    return with_text_input_file(input, on_file, may_post_file, yield_from=yield_from)





if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


