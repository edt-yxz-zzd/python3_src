
__all__ = '''
    SeqAsStackOpsBase
        basic_seq_as_stack_ops
        SeqAsCompleteStackOps
            the_list_as_stack_ops
            SeqAsStackOps
    '''.split()
from .IMutableStackOps import (
        IMutableSizedTopStackOps
        , IStackOps__reversed
        , ISizedStackOps
        , IStackOps__factory
        , IMutableCompleteStackOps)

class SeqAsStackOpsBase(
        IMutableSizedTopStackOps
        , IStackOps__reversed
        , ISizedStackOps
        #, IStackOps__factory
        ):
    # no constructor
    __slots__ = ()
    def push(self, s, x):
        s.append(x)
        pass
    def pop(self, s):
        return s.pop()
    def is_empty(self, s):
        return bool(s)
    def len(self, s):
        return len(s)

    def top(self, s):
        # if empty then raise
        return s[-1]
    def reversed(self, s):
        return reversed(s)
# without constructor
basic_seq_as_stack_ops = SeqAsStackOpsBase()

class SeqAsCompleteStackOps(SeqAsStackOpsBase, IMutableCompleteStackOps):
    def from_iterable(self, iterable):
        return list(iterable)
the_list_as_stack_ops = SeqAsCompleteStackOps()

class SeqAsStackOps(SeqAsCompleteStackOps):
    __slots__ = ['_from_iterable']
    def __init__(self, from_iterable = list):
        self._from_iterable = from_iterable
    def from_iterable(self, iterable):
        return self._from_iterable(iterable)



