
'''
seed.seq_tools.seq_index_if
py -m seed.seq_tools.seq_index_if
from seed.seq_tools.seq_index_if import seq_index, seq_index_if, seq_find, seq_find_if


see:
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator
    seed.text.StepDecoder
        #def&search "line"
        #using step_builder,step_predicator




example:
    >>> from seed.tiny import expectError
    >>> ls = '0123456789'

    # XXX success
    >>> seq_index(ls, '5')
    5
    >>> seq_find(ls, '5')
    (5, '5')

    # XXX fail
    >>> assert expectError(IndexError, lambda:seq_index(ls, 'a'))
    >>> seq_find(ls, 'a')
    (-1, None)


    # XXX_if success
    >>> ge4 = lambda x: x > '4'
    >>> seq_index_if(ls, ge4)
    5
    >>> seq_find_if(ls, ge4)
    (5, '5')
    >>> seq_index_if(ls, ge4, 6)
    6
    >>> seq_find_if(ls, ge4, 6)
    (6, '6')

    # XXX_if fail
    >>> assert expectError(IndexError, lambda:seq_index_if(ls, ge4, 0, 3))
    >>> seq_find_if(ls, ge4, 0, 3)
    (-1, None)
    >>> geA = lambda x: x > 'A'
    >>> assert expectError(IndexError, lambda:seq_index_if(ls, geA))
    >>> seq_find_if(ls, geA)
    (-1, None)


    # reverse
    >>> seq_index_if(ls, ge4, reverse=True)
    9
    >>> seq_find_if(ls, ge4, reverse=True)
    (9, '9')

    # fthen
    >>> seq_index_if(ls, ge4, fthen=lambda idx:-idx, fthen_case=0)
    -5
    >>> seq_index_if(ls, ge4, fthen=lambda a:a*3, fthen_case=1)
    '555'
    >>> seq_index_if(ls, ge4, fthen=lambda i, a:a*i, fthen_case=2)
    '55555'

    # felse
    >>> seq_index(ls, 'a', felse=lambda:[])
    []
'''



__all__ = '''
    seq_index
    seq_index_if
    seq_find
    seq_find_if
    '''.split()

from .iter_seq_range import iter_seq_range, enumerate_seq
from seed.tiny import ifNone


def seq_find(__seq, __a, *args, **kwargs):
    # seq_find :: [a] -> a -> ((uint, a)|(-1, None))
    # see: seq_index_if # but no "fthen_case/fthen/felse/pred_case/__pred"
    if "pred_case" in kwargs: raise TypeError
    def __pred_ex(i, b):
        return __a == b
    return seq_find_if(__seq, __pred_ex, *args, pred_case=2, **kwargs)
def seq_find_if(__seq, __pred, *args, **kwargs):
    # seq_find :: [a] -> (a->bool) -> ((uint, a)|(-1, None))
    # see: seq_index_if # but no "fthen_case/fthen/felse"
    if "fthen_case" in kwargs: raise TypeError
    if "fthen" in kwargs: raise TypeError
    if "felse" in kwargs: raise TypeError
    return seq_index_if(__seq, __pred, *args
        , fthen=None, fthen_case=2, felse=lambda: (-1,None), **kwargs)

def seq_index(__seq, __a, *args, **kwargs):
    # seq_index :: [a] -> a -> uint
    # see: seq_index_if # but no "__pred", no "pred_case"
    if "pred_case" in kwargs: raise TypeError
    def __pred_ex(i, b):
        return __a == b
    return seq_index_if(__seq, __pred_ex, *args, pred_case=2, **kwargs)






def get_args0(a, b):
    return a
def get_args1(a, b):
    return b
def get_args(a, b):
    return a, b

def make_fthen_ex(fthen_case, fthen):
    # see: seq_index_if
    if fthen_case == 0:
        fthen_i = fthen
        if fthen is None:
            return get_args0
        def fthen_ex(i, a):
            return fthen_i(i)
    elif fthen_case == 1:
        fthen_a = fthen
        if fthen is None:
            return get_args1
        def fthen_ex(i, a):
            return fthen_a(a)
    elif fthen_case == 2:
        fthen_ia = fthen
        if fthen_ia is not None:
            return fthen_ia
        def fthen_ex(i, a):
            return i, a
    else:
        raise ValueError('fthen_case not in [0,1,2]')
    return fthen_ex
def make_pred_ex(pred_case, pred):
    # see: seq_index_if
    if pred_case == 1:
        def pred_ex(i, a):
            return pred(a)
    elif pred_case == 2:
        pred_ex = pred
    else:
        raise ValueError('fthen_case not in [0,1,2]')
    return pred_ex


def seq_index_if(__seq, __pred
        , begin=None, end=None, step=None
        , *, reverse=False
        , fthen=None    # echo
        , felse=None    # raise IndexError
        , pred_case=1   # a->bool
        , fthen_case=0  # return idx
        ):
    '''
    # seq_index_if :: [a] -> (uint->a->bool) -> (uint->a->x) -> (()->y) -> (x|y)

__seq :: [a]
__pred :: a->bool | uint -> a -> bool
begin, end, step :: None|int

reverse :: bool
fthen :: None | uint -> x | a -> x | uint -> a -> x
felse :: None | () -> y
    None ==>> raise IndexError
    # see: seed.tiny.lazy_raise
pred_case :: 1 | 2
    pred_case == 1:
        __pred :: a->bool
    pred_case == 2:
        __pred :: uint -> a -> bool

fthen_case = 0 | 1 | 2
    fthen_case == 0:
        # .index
        fthen :: None | uint -> x
            None ==>> uint -> uint
    fthen_case == 1:
        # .find
        fthen :: None | a -> x
            None ==>> a -> a
    fthen_case == 2:
        fthen :: None | uint -> a -> x
            None ==>> uint -> a -> (uint, a)
'''

    pred_ex = make_pred_ex(pred_case, __pred)
    it = enumerate_seq(__seq, begin, end, step, reverse=reverse)
    for i, a in it:
        if pred_ex(i, a):
            fthen_ex = make_fthen_ex(fthen_case, fthen)
            return fthen_ex(i, a)
    else:
        if felse is None:
            raise IndexError
        return felse()
    pass






if __name__ == "__main__":
    import doctest
    doctest.testmod()



