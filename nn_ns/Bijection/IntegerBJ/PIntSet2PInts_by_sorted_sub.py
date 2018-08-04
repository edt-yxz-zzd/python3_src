
__all__ = ['aPIntSet2PInts_by_sorted_sub']
from ..Bijection import Bijection
from ..abbr import PIntSet, PInts
from itertools import accumulate

class PIntSet2PInts_by_sorted_sub(Bijection):
    def get_InputType(self):
        return PIntSet
    def get_OutputType(self):
        return PInts
    def untypechecked_forward(self, input):
        if not input: return ()
        ps = sorted(input)
        head, *tail = ps
        return (head,) + tuple(a-b for a,b in zip(tail, ps))
    def untypechecked_backward(self, output):
        return frozenset(accumulate(output))
    def get_construct_info(self):
        return 'aPIntSet2PInts_by_sorted_sub'
aPIntSet2PInts_by_sorted_sub = PIntSet2PInts_by_sorted_sub()
