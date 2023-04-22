#__all__:goto
r'''[[[
e ../../python3_src/seed/io/with4seekback.py
see:
    seed.helper.with4cleanup
    seed.io.with4seekback

restore file/stream position finally or on error




seed.io.with4seekback
py -m nn_ns.app.debug_cmd   seed.io.with4seekback
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.io.with4seekback   @f
py -m nn_ns.app.doctest_cmd seed.io.with4seekback:__doc__ -v




from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err

from seed.io.with4seekback import with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_





>>> from seed.io.with4seekback import with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_

>>> from io import BytesIO
>>> ibfile = BytesIO(b'abc123')
>>> ibfile.read(2)
b'ab'
>>> ibfile.tell()
2
>>> with with4seekback__on_err(ibfile) as saved_position:
...     saved_position
...     ibfile.read(2)
2
b'c1'
>>> ibfile.tell()
4
>>> with with4seekback__on_err(ibfile) as saved_position:
...     assert saved_position == 4
...     assert ibfile.read(2) == b'23'
...     assert ibfile.tell() == 6
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ibfile.tell()
4



>>> ibfile.seek(2)
2
>>> ibfile.tell()
2
>>> with with4seekback__on_no_err(ibfile) as saved_position:
...     saved_position
...     assert ibfile.tell() == saved_position == 2
...     ibfile.read(2)
...     assert ibfile.tell() == 4
2
b'c1'
>>> ibfile.tell()
2
>>> with with4seekback__on_no_err(ibfile) as saved_position:
...     assert saved_position == 2
...     assert ibfile.read(2) == b'c1'
...     assert ibfile.tell() == 4
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ibfile.tell()
4


>>> ibfile.seek(2)
2
>>> ibfile.tell()
2
>>> with with4seekback__on_exit(ibfile) as saved_position:
...     saved_position
...     assert ibfile.tell() == saved_position == 2
...     ibfile.read(2)
...     assert ibfile.tell() == 4
2
b'c1'
>>> ibfile.tell()
2
>>> with with4seekback__on_exit(ibfile) as saved_position:
...     assert saved_position == 2
...     assert ibfile.read(2) == b'c1'
...     assert ibfile.tell() == 4
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ibfile.tell()
2



>>> ibfile.seek(2)
2
>>> ibfile.tell()
2
>>> with with4seekback__never(ibfile) as saved_position:
...     saved_position
...     assert ibfile.tell() == saved_position == 2
...     ibfile.read(2)
...     assert ibfile.tell() == 4
2
b'c1'
>>> ibfile.tell()
4
>>> with with4seekback__never(ibfile) as saved_position:
...     assert saved_position == 4
...     assert ibfile.read(2) == b'23'
...     assert ibfile.tell() == 6
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ibfile.tell()
6





#]]]'''
__all__ = r'''
with4seekback_
    with4seekback__on_err
    with4seekback__on_no_err
    with4seekback__on_exit
    with4seekback__never
'''.split()#'''
__all__


def _mk__with4seekbackX(with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, /):
    def with4seekback_(stream, /, *, on_err:bool, on_no_err:bool):
        if on_err:
            if on_no_err:
                f = with4seekback__on_exit
            else:
                f = with4seekback__on_err
        else:
            if on_no_err:
                f = with4seekback__on_no_err
            else:
                f = with4seekback__never
        return f(stream)
    return with4seekback_

def _via__contextlib():
    import contextlib
    m = len(locals())

    @contextlib.contextmanager
    def with4seekback__on_err(stream, /):
        saved_position = stream.tell()
        try:
            yield saved_position
        except:
            stream.seek(saved_position)
            raise
    @contextlib.contextmanager
    def with4seekback__on_no_err(stream, /):
        saved_position = stream.tell()
        yield saved_position
        stream.seek(saved_position)
    @contextlib.contextmanager
    def with4seekback__on_exit(stream, /):
        saved_position = stream.tell()
        try:
            yield saved_position
        finally:
            stream.seek(saved_position)
    @contextlib.contextmanager
    def with4seekback__never(stream, /):
        saved_position = stream.tell()
        yield saved_position
    with4seekback_ = _mk__with4seekbackX(with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never)

    n = len(locals())
    n -= m+1
    result = (with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_)
    assert n == len(result)
    return result
#end-def _via__contextlib():

def _via__with4cleanup():
    from seed.helper.with4cleanup import no_cleanup, with4cleanup_, with4cleanup__on_err_, with4cleanup__on_no_err, with4cleanup__on_exit, with4cleanup__never

    def _prepare4seekback(stream, /):
        saved_position = stream.tell()
        internal_state = stream
        external_obj = saved_position
        return (internal_state, external_obj)
    def _seek8cleanup(stream8internal_state, saved_position8external_obj, /):
        #internal_state = stream
        #external_obj = saved_position
        stream8internal_state.seek(saved_position8external_obj)


    m = len(locals())

    def with4seekback__on_err(stream, /):
        return with4cleanup__on_err_(True, _seek8cleanup, 1, _prepare4seekback, stream)
    def with4seekback__on_no_err(stream, /):
        return with4cleanup__on_no_err(_seek8cleanup, 1, _prepare4seekback, stream)
    def with4seekback__on_exit(stream, /):
        return with4cleanup__on_exit(_seek8cleanup, 1, _prepare4seekback, stream)
    def with4seekback__never(stream, /):
        return with4cleanup__never(1, _prepare4seekback, stream)
    with4seekback_ = _mk__with4seekbackX(with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never)

    n = len(locals())
    n -= m+1
    result = (with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_)
    assert n == len(result)
    return result
#end-def _via__with4cleanup():
class _with4seekback_API__via__contextlib:
    (with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_) = _via__contextlib()
    #print(' '.join(locals()))
class _with4seekback_API__via__with4cleanup:
    (with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_) = _via__with4cleanup()


__ = _with4seekback_API__via__with4cleanup if 1 else _with4seekback_API__via__contextlib
#
# .,.+4s/.*/\0 = __.\0/g
with4seekback__on_err = __.with4seekback__on_err
with4seekback__on_no_err = __.with4seekback__on_no_err
with4seekback__on_exit = __.with4seekback__on_exit
with4seekback__never = __.with4seekback__never
with4seekback_ = __.with4seekback_





from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err

from seed.io.with4seekback import with4seekback__on_err, with4seekback__on_no_err, with4seekback__on_exit, with4seekback__never, with4seekback_

from seed.io.with4seekback import *
