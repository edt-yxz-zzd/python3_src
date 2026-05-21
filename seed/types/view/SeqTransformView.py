

__all__ = '''
    SeqTransformView
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import Sequence
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.funcs import echo
#from .View import SeqView
___end_mark_of_excluded_global_names__0___ = ...


class SeqTransformView(Sequence):
    '''(a->b) -> [a] -> [b]

example:
    >>> ls = SeqTransformView(lambda a: -a, [1,2,3])
    >>> ls[0]
    -1
    >>> -2 in ls[1:]
    True
    >>> ls[1:]                      # doctest: +ELLIPSIS
    SeqTransformView(..., [2, 3])
    >>> list(ls)
    [-1, -2, -3]
    >>> list(reversed(ls))
    [-3, -2, -1]

see: SeqSliceView
'''
    __slots__ = ('__f', '__seq', '__smay_repr')

    def __init__(self, transform, seq, *, smay_repr=''):
        ':: (a->b) -> [a] -> [b]'
        if not (transform is None or callable): raise TypeError
        if not isinstance(seq, Sequence): raise TypeError
        if not type(smay_repr) is str: raise TypeError
        self.__f = transform if transform is not None else echo
        self.__seq = seq
        self.__smay_repr = smay_repr

    def __getitem__(self, i):
        r = self.__seq[i]
        if type(i) is not slice:
            r = self.__f(r)
        else:
            ls = r
            r = type(self).from_tranform_sequence(self.__f, ls)
        return r
    '''
    def ___get_args_kwargs___(self):
        # for repr
        args, kwargs = super().__get_args_kwargs__()
        return (self.__f,) + args, kwargs
    '''

    def __repr__(self):
        if self.__smay_repr:
            return self.__smay_repr
        return repr_helper(self, self.__f, self.__seq) # ? list(self.__seq)

    @classmethod
    def from_sequence(cls, seq): return cls.from_tranform_sequence(None, seq)
    @classmethod
    def from_tranform_sequence(cls, f, seq): return cls(f, seq)

    def __len__(self):
        return len(self.__seq)

    def __iter__(self):
        return map(self.__f, self.__seq)
    def __reversed__(self):
        return map(self.__f, reversed(self.__seq))





if __name__ == "__main__":
    import doctest
    doctest.testmod()



