

'''
LeftBiasListAsStack

LeftBiasList a = () | (LeftBiasList a, a)
SizedLeftBiasList a = (Size, LeftBiasList a)

'''
__all__ = '''
    the_left_bias_list_as_stack_ops
    the_sized_left_bias_list_as_stack_ops
'''.split()

from .IPseudoImmutableStackOps import\
    (IPseudoImmutableCompleteStackOps
    ,IStackOps__factory
    ,IPseudoImmutableTopStackOps
    )
class LeftBiasListAsStackOps(IPseudoImmutableTopStackOps, IStackOps__factory):
    # `is_empty, `top, top_or_fdefault, ipop_None, `ipop, `ipush, ipop_or_fdefault;
    #   `from_iterable
    __slots__ = ()

    def from_iterable(self, iterable):
        s = ()
        for x in iterable:
            s = s, x
        return s
    def ipush(self, s, x):
        return s, x
    def ipop(self, s):
        return s
        s, x = s
        return s, x
    def is_empty(self, s):
        # bug: return bool(s)
        return not s

    def top(self, s):
        # if empty then raise
        return s[-1]
    def reversed(self, s):
        while s:
            s, x = s
            yield x
the_left_bias_list_as_stack_ops = LeftBiasListAsStackOps()



class SizedLeftBiasListAsStackOps(IPseudoImmutableCompleteStackOps):
    # is_empty, `top, top_or_fdefault, ipop_None, `ipop, `ipush, ipop_or_fdefault;
    #   `len; `from_iterable
    __slots__ = ()
    def from_iterable(self, iterable):
        s = ()
        size = 0
        for size, x in enumerate(iterable, 1):
            s = s, x
        return size, s
    def ipush(self, ss, x):
        size, s = ss
        return size+1, (s,x)
    def ipop(self, ss):
        size, (s, x) = ss
        return (size-1, s), x
    def len(self, ss):
        return ss[0]

    def top(self, ss):
        # if empty then raise
        size, (s, x) = ss
        return x
    def reversed(self, ss):
        size, s = ss
        return the_left_bias_list_as_stack_ops.reversed(s)
the_sized_left_bias_list_as_stack_ops = SizedLeftBiasListAsStackOps()

def t():
    opss = [the_left_bias_list_as_stack_ops, the_sized_left_bias_list_as_stack_ops]
    [*map(t1, opss)]
def t1(ops):
    #ops = the_left_bias_list_as_stack_ops
    im = ops.from_iterable([1,2,3])
    assert not ops.is_empty(im)
    if False:
        print(im)
        print(ops.is_empty)
        print(type(ops).is_empty)
t()
