

'''
usage:
    maybe_output_fname = args.output_fname
    lazy_fout = lambda:open(maybe_output_fname, 'x', ...)

    with with_if(maybe_output_fname is not None
            , lazy_fout, lambda:sys.stdout) as fout:
        fout.write(...)

'''

__all__ = '''
    with_if
    '''.split()

import contextlib
@contextlib.contextmanager
def with_if(__to_with, __fobj, fdefault=None):
    '''if __to_with, then (with __fobj():) else use fdefault() and not with.
'''
    if __to_with:
        with __fobj() as obj:
            yield obj
    else:
        if fdefault is None:
            fdefault = __fobj
        yield fdefault()
    return
with_if.__doc__ += __doc__


def _t():
    enter = exit = False
    def reset():
        nonlocal enter, exit
        enter = exit = False
    @contextlib.contextmanager
    def try_():
        nonlocal enter, exit
        enter = True
        yield
        exit = True

    reset()
    assert not enter
    assert not exit
    with try_():
        assert enter
        assert not exit
    assert enter
    assert exit



    reset()
    assert not enter
    assert not exit
    with with_if(True, try_):
        assert enter
        assert not exit
    assert enter
    assert exit


    reset()
    assert not enter
    assert not exit
    with with_if(False, try_):
        assert not enter
        assert not exit
    assert not enter
    assert not exit

if __name__ == '__main__':
    _t()
    help(with_if)

del _t
del contextlib

