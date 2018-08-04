
'''
0) XInt[L] <-> XInt[0..L]
    # by remove tail 0s
    # L = 3:
    #   (7,5,3) <-> (7,5,3-1)
    #   (7,5,0) <-> (7,5-1)
    #   (7,0,0) <-> (7-1,)
    #   (0,0,0) <-> ()
    # or by remove init 0s

1) (XInt[L] <-> XInt[0..L]) -> (XInt[m+L] <-> XInt[m..m+L])
    XInt[m+L]
        <-> (XInt[m], XInt[L])     #SplitArrayPrefixAt
        <-> (XInt[m], XInt[0..L])  #use input
        <-> XInt[m..m+L]           #SplitArrayPrefixAt^-1
2) (XInt[L] <-> XInt[0..L]) -> (XInt[m+L..M] <-> XInt[m..M])
    XInt[m+L..M]
        <-> <XInt[m+L]             | XInt[m+L+1..M]> #ArrayUnion2Choices
        <-> <XInt[m..m+L]          | XInt[m+L+1..M]> #use 1)
        <-> XInt[m..M]                               #ArrayUnion2Choices^-1
'''

# main output: XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs
__all__ = '''
    XIntLLs2XInt0Ls_by_remove_headMINs
    XIntLLs2XInt0Ls_by_remove_tailMINs
    XIntNLMs2XIntNMs_by_alter_shortest_array_suffix
    XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs

    aUIntLLs2UInt0Ls_by_remove_head0s__L3
    aUIntNLNLs2UIntNNLs__L3N1
    aUIntNLMs2UIntNMs__L3N1M5
    '''.split()

from ..Bijection import Bijection
from ..IdBijection import id_of
from ..InverseBijection import inverse_bijection
from ..ChainedBijection import ChainedBijection
from ..TupleBijection import TupleBijection, pair_bijection
from ..ChoiceBijection import choice_bijection
from ..SeqBJ import SplitArrayPrefixAt, ArrayUnion2Choices, reverse_arrayBJ

from ..ArrayTV import ArrayTV, ArrayJust
from ..NumberTVs import is_IntGeTV # IntGeTV, IntGeLeTV
from ..abbr import UInt

from itertools import chain, repeat

def XIntLLs2XInt0Ls_by_remove_tailMINs(XInt, max_len):
    L = max_len
    return +(reverse_arrayBJ(XInt[L,L])
            >> XIntLLs2XInt0Ls_by_remove_headMINs(XInt, L)
            >> reverse_arrayBJ(XInt[0,L])
            )
class XIntLLs2XInt0Ls_by_remove_headMINs(Bijection):
    '[a]{L} <-> [a]{0..L}'
    def __init__(self, XInt, max_len):
        assert is_IntGeTV(XInt)
        self.max_len = max_len
        self.XInt = XInt
        self.InputType = ArrayTV(XInt, max_len, max_len)
        self.OutputType = ArrayTV(XInt, 0, max_len)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        minXInt = self.XInt.int_range.may_min
        it = iter(input)
        for u in it:
            if u != minXInt: break
        else:
            return () # all 0s
        return tuple(chain([u-1], it))
    def untypechecked_backward(self, output):
        minXInt = self.XInt.int_range.may_min
        it = iter(output)
        for u in it:
            break
        else:
            return (minXInt,) * self.max_len

        return tuple(chain
            ( repeat(minXInt, self.max_len - len(output))
            , [u+1]
            , it
            ))
    def get_construct_info(self):
        return self.make_args_kwargs(self.max_len, self.XInt)


def XIntNLNLs2XIntNNLs_by_remove_suffix_headMINs(XInt, minO, maxO):
    'XInt[m+L] <-> XInt[m..m+L]'
    m = minO
    L = maxO - minO
    aXIntLs2XInt0Ls = XIntLLs2XInt0Ls_by_remove_headMINs(XInt, L)
    return XIntNLNLs2XIntNNLs_by_alter_suffix(XInt, L, aXIntLs2XInt0Ls, minO)
def XIntNLNLs2XIntNNLs_by_alter_suffix(XInt, maxI, aXIntLs2XInt0Ls, minO):
    '(XInt[L] <-> XInt[0..L]) -> (XInt[m+L] <-> XInt[m..m+L])'
    assert 0 <= minO
    if minO == 0:
        return aXIntLs2XInt0Ls
    m = minO
    # L = aXIntLs2XInt0Ls.max_len
    # XInt = aXIntLs2XInt0Ls.XInt
    L = maxI

    InputType = ArrayJust(XInt, m+L)
    b1 = SplitArrayPrefixAt(InputType, m)
    b2 = pair_bijection(id_of(ArrayJust(XInt, m)), aXIntLs2XInt0Ls)
    OutputType = ArrayTV(XInt, m, m+L)
    b3 = inverse_bijection(SplitArrayPrefixAt(OutputType, m))
    return ChainedBijection(b1, b2, b3)


def XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs(XInt, minI, minO, may_max):
    'XInt[m+L..M] <-> XInt[m..M]'
    m = minO
    mL = minI
    L = mL - m
    aXIntLs2XInt0Ls = XIntLLs2XInt0Ls_by_remove_headMINs(XInt, L)
    return XIntNLMs2XIntNMs_by_alter_shortest_array_suffix(
        XInt, L, aXIntLs2XInt0Ls, minO, may_max)
def XIntNLMs2XIntNMs_by_alter_shortest_array_suffix(
    XInt, maxI, aXIntLs2XInt0Ls, minO, may_maxO):
    '(XInt[L] <-> XInt[0..L]) -> (XInt[m+L..M] <-> XInt[m..M])'
    m, M = minO, may_maxO
    #L = aXIntLs2XInt0Ls.max_len
    #XInt = aXIntLs2XInt0Ls.XInt
    L = maxI
    if M is None: assert 0 <= m <= m + L
    else:         assert 0 <= m <= m + L <= M
    aXIntNLNLs2XIntNNLs = XIntNLNLs2XIntNNLs_by_alter_suffix(XInt, L, aXIntLs2XInt0Ls, minO)
    if M is not None and m + L == M:
        return aXIntNLNLs2XIntNNLs

    InputType = ArrayTV(XInt, m+L, M)
    b1 = ArrayUnion2Choices(InputType, m+L)

    b2_left = aXIntNLNLs2XIntNNLs
    b2_right = id_of(ArrayTV(XInt, m+L+1, M))
    b2 = choice_bijection(left=b2_left, right=b2_right)

    OutputType = ArrayTV(XInt, m, M)
    b3 = inverse_bijection(ArrayUnion2Choices(OutputType, m+L))
    return ChainedBijection(b1, b2, b3)



aUIntLLs2UInt0Ls_by_remove_head0s__L3 = XIntLLs2XInt0Ls_by_remove_headMINs(UInt, 3)
aUIntNLNLs2UIntNNLs__L3N1\
    = XIntNLNLs2XIntNNLs_by_alter_suffix(UInt, 3, aUIntLLs2UInt0Ls_by_remove_head0s__L3, 1)
aUIntNLMs2UIntNMs__L3N1M5\
    = XIntNLMs2XIntNMs_by_alter_shortest_array_suffix(
        UInt, 3, aUIntLLs2UInt0Ls_by_remove_head0s__L3, 1, 5)

