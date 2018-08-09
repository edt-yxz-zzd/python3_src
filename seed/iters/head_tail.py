
'''
fdefault :: () -> object

'''

__all__ = '''
    unlist_fdefault
    head_tail_fdefault
    forward1_fdefault
    head_tail
    forward1_fdefault

    with_fdefault
    mk_fdefault
    with_default

    fdefault__null_iter_raise
    '''.split()

from .null_iter import null_iter
from .put import put

# helper
def fdefault__null_iter_raise():
    head, *tail = null_iter
    raise logic-error
def get_args(*args):
    return args




# main func

def unlist_fdefault(iterable, fdefault, f1, *args):
    it = iter(iterable)
    for head in it:
        return f1(*args, head, it)
    return fdefault()

def head_tail_fdefault(iterable, fdefault):
    # no raise
    return unlist_fdefault(iterable, lambda: (fdefault(), null_iter), get_args)


def with_fdefault(iterable, fdefault):
    # the result iterable will be nonempty
    head, it = head_tail_fdefault(iterable, fdefault)
    return put(head, it)
def mk_fdefault(default):
    return lambda: default
def with_default(iterable, default):
    # the result iterable will be nonempty
    return with_fdefault(iterable, mk_fdefault(default))


def forward1_fdefault(f1, iterable, fdefault):
    # no raise
    # forward1_fdefault != unlist_fdefault
    # forward1_fdefault f1 (h:ts) fd == unlist_fdefault (h:ts) fd f1
    # forward1_fdefault f1 [] fd == f1 fd() [] != fd() == unlist_fdefault [] fd f1
    head, tail = head_tail_fdefault(iterable, fdefault)
    return f1(head, tail)




def head_tail(iterable):
    # raise when null iterable
    return unlist_fdefault(iterable, fdefault__null_iter_raise, get_args)

def forward1(f1, iterable):
    # raise when null iterable
    # forward1(f1, with_default(iterable, default))
    # forward1(f1, with_fdefault(iterable, fdefault))
    return unlist_fdefault(iterable, fdefault__null_iter_raise, f1)
    head, tail = head_tail(iterable)
    return f1(head, tail)


