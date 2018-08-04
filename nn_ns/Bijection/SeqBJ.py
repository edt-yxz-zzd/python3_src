

__all__ = '''
    SplitArrayLast
    ArrayUnion2Choices
    MakeSingletonArray
    SplitArrayPrefixAt
    SplitArraySuffixAt
    Array2Tuple

    reverse_tuple_prefixBJ
    reverse_arrayBJ
    reverse_array_max_prefixBJ
    left_rotate_tupleBJ
    left_rotate_arrayBJ

    tuple2tuple_by_unpackBJ
    unpack_tupleBJ
    remove_tuple_singleton_elemBJ
    permute_tupleBJ
    permute_tuple_omit_singletonBJ
    '''.split()

from .Bijection import Bijection
from .ArrayTV import ArrayTV
from .TupleTV import PairTV, TupleTV
from .ChoiceTV import ChoiceTV, make_choice
from .TypeVerifier import TypeVerifier
from .seq_ops import may_seq_len2len\
    , left_rotate_seq__strict, reverse_seq_prefix__strict
from itertools import chain

class SplitHead(Bijection):
    '[a] <-> (a, [a])'
    def __init__(self, InputType):
        assert isinstance(InputType, ArrayTV)
        a = self.type_verifier = InputType.type_verifier
        self.min_lenI = InputType.size_range.min
        self.may_max_lenI = InputType.size_range.may_max
        self.min_lenO = self.min_lenI - 1
        if self.may_max_lenI is None:
            self.may_max_lenO = None
        else:
            self.may_max_lenO = self.may_max_lenI - 1
        OutputArray = ArrayTV(a, self.min_lenO, self.may_max_lenO)

        self.InputType = InputType
        self.OutputType = PairTV(a, OutputArray)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input[0], input[1:]
    def untypechecked_backward(self, output):
        a, tail = output
        return tuple(chain([a], tail))
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType)

class SplitArrayLast(Bijection):
    '[a] <-> ([a], a)'
    def __init__(self, InputType):
        assert isinstance(InputType, ArrayTV)
        a = self.type_verifier = InputType.type_verifier
        self.min_lenI = InputType.size_range.min
        self.may_max_lenI = InputType.size_range.may_max
        self.min_lenO = self.min_lenI - 1
        if self.may_max_lenI is None:
            self.may_max_lenO = None
        else:
            self.may_max_lenO = self.may_max_lenI - 1
        OutputArray = ArrayTV(a, self.min_lenO, self.may_max_lenO)

        self.InputType = InputType
        self.OutputType = PairTV(OutputArray, a)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input[:-1], input[-1]
    def untypechecked_backward(self, output):
        init, a = output
        return tuple(chain(init, [a]))
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType)



'''
error!
class UnionArray(Bijection):
    '([a]{m..L}, [a]{L+1..M}) <-> [a]{m..M}'
    # m-1 <= L <= M
    # if m-1 == L: ([], _) <-> _
    # if L == M: (_, []) <-> _
    # Note: [] == [a]{0..0}, will lost information
    # so, we, require '[a]{m..M}' and 'L' instead of just InputType

    # normally, m <= L < L+1 <= M, i.e. m <= L < M
    # usually, m == L
'''
class ArrayUnion2Choices(Bijection):
    '[a]{m..M} <-> <left=[a]{m..L}, right=[a]{L+1..M}>'
    # m <= L < L+1 <= M, i.e. m <= L < M
    # usually, m == L
    def __init__(self, InputType, left_max_len):
        assert isinstance(InputType, ArrayTV)
        assert type(left_max_len) is int and left_max_len >= 0
        L = left_max_len
        a = self.type_verifier = InputType.type_verifier

        m = self.min_lenI = InputType.size_range.min
        M = self.may_max_lenI = InputType.size_range.may_max
        if M is None:   assert m <= L
        else:           assert m <= L < M

        self.left_min_lenO = m
        self.left_max_lenO = L
        self.right_min_lenO = L+1
        self.right_max_lenO = M

        leftO = ArrayTV(a, self.left_min_lenO, self.left_max_lenO)
        rightO = ArrayTV(a, self.right_min_lenO, self.right_max_lenO)

        self.InputType = InputType
        self.OutputType = ChoiceTV(left=leftO, right=rightO)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return make_choice(left=input) if len(input) < self.right_min_lenO else\
                make_choice(right=input)
    def untypechecked_backward(self, output):
        tag, array = output # choice is a pair
        return array
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.left_max_lenO)


class MakeSingletonArray(Bijection):
    'a <-> [a]{1}'
    def __init__(self, type_verifier):
        assert isinstance(type_verifier, TypeVerifier)
        self.InputType = type_verifier
        self.OutputType = ArrayTV(type_verifier, 1, 1)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return (input,)
    def untypechecked_backward(self, output):
        a, = output
        return a
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType)



class SplitArrayPrefixAt(Bijection):
    '[a]{L+m..L+M} <-> ([a]{L}, [a]{m..M})'
    def __init__(self, InputType, prefix_len):
        assert isinstance(InputType, ArrayTV)
        assert type(prefix_len) is int and prefix_len >= 0
        L = self.prefix_len = prefix_len
        a = self.type_verifier = InputType.type_verifier

        self.min_lenI = InputType.size_range.min
        self.may_max_lenI = InputType.size_range.may_max
        self.min_lenO = self.min_lenI - L
        if self.may_max_lenI is None:
            self.may_max_lenO = None
        else:
            self.may_max_lenO = self.may_max_lenI - L
        fstOutputArray = ArrayTV(a, L, L)
        sndOutputArray = ArrayTV(a, self.min_lenO, self.may_max_lenO)

        self.InputType = InputType
        self.OutputType = PairTV(fstOutputArray, sndOutputArray)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input[:self.prefix_len], input[self.prefix_len:]
    def untypechecked_backward(self, output):
        fst, snd = output
        return fst + snd
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.prefix_len)



class SplitArraySuffixAt(Bijection):
    '[a]{m+L..M+L} <-> ([a]{m..M}, [a]{L})'
    def __init__(self, InputType, suffix_len):
        assert isinstance(InputType, ArrayTV)
        assert type(suffix_len) is int and suffix_len >= 0
        L = self.suffix_len = suffix_len
        a = self.type_verifier = InputType.type_verifier

        self.min_lenI = InputType.size_range.min
        self.may_max_lenI = InputType.size_range.may_max
        self.min_lenO = self.min_lenI - L
        if self.may_max_lenI is None:
            self.may_max_lenO = None
        else:
            self.may_max_lenO = self.may_max_lenI - L
        fstOutputArray = ArrayTV(a, self.min_lenO, self.may_max_lenO)
        sndOutputArray = ArrayTV(a, L, L)

        self.InputType = InputType
        self.OutputType = PairTV(fstOutputArray, sndOutputArray)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        prefix_len = len(input)-self.suffix_len
        return input[:prefix_len], input[prefix_len:]
    def untypechecked_backward(self, output):
        fst, snd = output
        return fst + snd
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.suffix_len)



class Array2Tuple(Bijection):
    'a[L] <-> (a,)*L'
    def __init__(self, type_verifier, size):
        assert isinstance(type_verifier, TypeVerifier)
        assert size >= 0
        self.type_verifier = type_verifier
        self.size = size

        self.InputType = type_verifier[size, size]
        self.OutputType = type_verifier.TupleTV(*[type_verifier]*size)

    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input
    def untypechecked_backward(self, output):
        return output
    def get_construct_info(self):
        return self.make_args_kwargs(self.type_verifier, self.size)




###########################################

def reverse_tuple_prefixBJ(InputType, may_prefix_len=None):
    assert isinstance(InputType, TupleTV), TypeError
    assert may_prefix_len is None or type(may_prefix_len) is int, TypeError
    ts = InputType.type_verifiers
    L = len(ts)
    prefix_len = may_seq_len2len(may_prefix_len, L)
    assert 0 <= prefix_len <= L
    if prefix_len < 2:
        return InputType.idBJ
    return ReverseTuplePrefix(InputType, prefix_len)
class ReverseTuplePrefix(Bijection):
    '(a, b, ...) <-[2]-> (b, a, ...)'
    def __init__(self, InputType, prefix_len):
        assert isinstance(InputType, TupleTV), TypeError
        assert type(prefix_len) is int, TypeError
        ts = InputType.type_verifiers
        L = len(ts)
        assert L >= 2, TypeError
        assert 2 <= prefix_len <= L, ValueError
        self.prefix_len = prefix_len

        self.InputType = InputType
        self.OutputType = InputType.TupleTV(
            *reverse_seq_prefix__strict(prefix_len, ts))

    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return reverse_seq_prefix__strict(self.prefix_len, input)
    def untypechecked_backward(self, output):
        return reverse_seq_prefix__strict(self.prefix_len, output)
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'reverse_tuple_prefixBJ', self.InputType, self.prefix_len)


def left_rotate_tupleBJ(InputType, may_prefix_len=None):
    assert isinstance(InputType, TupleTV), TypeError
    assert may_prefix_len is None or type(may_prefix_len) is int, TypeError
    ts = InputType.type_verifiers
    L = len(ts)
    prefix_len = may_seq_len2len(may_prefix_len, L)
    assert 0 <= prefix_len <= L
    if prefix_len == 0 or prefix_len == L:
        return InputType.idBJ
    return LeftRotateTuple(InputType, prefix_len)
    b1 = reverse_tuple_prefixBJ(InputType, prefix_len)
    b2 = reverse_tuple_prefixBJ(b1.get_OutputType())
    b3 = reverse_tuple_prefixBJ(b2.get_OutputType(), L-prefix_len)
    return +(b1 >> b2 >> b3)

class LeftRotateTuple(Bijection):
    '(a, b, ...) <-[2]-> (..., a, b)'
    def __init__(self, InputType, prefix_len):
        assert isinstance(InputType, TupleTV), TypeError
        assert type(prefix_len) is int, TypeError
        ts = InputType.type_verifiers
        L = len(ts)
        assert L >= 2, TypeError
        assert 1 <= prefix_len <= L-1, ValueError
        self.prefix_len = prefix_len

        self.InputType = InputType
        self.OutputType = InputType.TupleTV(
            *left_rotate_seq__strict(self.prefix_len, ts))

    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return left_rotate_seq__strict(self.prefix_len, input)
    def untypechecked_backward(self, output):
        return left_rotate_seq__strict(self.prefix_len, output)
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'left_rotate_tupleBJ', self.InputType, self.prefix_len)



def reverse_arrayBJ(io_type):
    assert isinstance(io_type, ArrayTV), TypeError
    if io_type.size_range.inf_max < 2:
        return io_type.idBJ
    return ReverseArray(io_type)

class ReverseArray(Bijection):
    '[1,2,3] <-> [3,2,1]; mainly for Array[:None]'
    def __init__(self, io_type):
        assert isinstance(io_type, ArrayTV), TypeError
        assert io_type.size_range.inf_max >= 2, TypeError
        self.io_type = io_type

    def __map(self, array):
        L = len(array)
        return reverse_seq_prefix__strict(L, array)

    def get_InputType(self):
        return self.io_type
    def get_OutputType(self):
        return self.io_type
    def untypechecked_forward(self, input):
        return self.__map(input)
    def untypechecked_backward(self, output):
        return self.__map(output)
    def get_construct_info(self):
        return self.make_name_args_kwargs('reverse_arrayBJ', self.io_type)


class ReverseArrayMaxPrefix(Bijection):
    '[1,2,3] <-[2]-> [2,1,3]; [1,2,3]<-[4]->[3,2,1]'
    def __init__(self, io_type, max_prefix_len):
        assert isinstance(io_type, ArrayTV), TypeError
        assert type(max_prefix_len) is int, TypeError
        rng = io_type.size_range
        # not: max_prefix_len <= inf_max
        #       if ==, then ReverseArray
        assert 2 <= max_prefix_len < rng.inf_max, ValueError
        self.max_prefix_len = max_prefix_len

        self.io_type = io_type

    def __map(self, array):
        L = min(len(array), self.max_prefix_len)
        return reverse_seq_prefix__strict(L, array)

    def get_InputType(self):
        return self.io_type
    def get_OutputType(self):
        return self.io_type
    def untypechecked_forward(self, input):
        return self.__map(input)
    def untypechecked_backward(self, output):
        return self.__map(output)
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'reverse_array_max_prefixBJ', self.io_type, self.max_prefix_len)


def reverse_array_max_prefixBJ(io_type, may_max_prefix_len=None):
    assert isinstance(io_type, ArrayTV), TypeError
    assert may_max_prefix_len is None or type(may_max_prefix_len) is int, TypeError
    rng = io_type.size_range
    if may_max_prefix_len is None or may_max_prefix_len >= rng.inf_max:
        return reverse_arrayBJ(io_type)
    max_prefix_len = may_max_prefix_len
    if max_prefix_len < 0: raise ValueError
    if max_prefix_len < 2:
        return io_type.idBJ
    assert 2 < max_prefix_len < rng.inf_max
    return ReverseArrayMaxPrefix(io_type, max_prefix_len)





def left_rotate_arrayBJ(io_type, may_prefix_len=None):
    assert isinstance(io_type, ArrayTV), TypeError
    assert may_prefix_len is None or type(may_prefix_len) is int, TypeError
    rng = io_type.size_range
    L = rng.inf_max
    if may_prefix_len in [None, 0, L]:
        return io_type.idBJ
    prefix_len = may_prefix_len
    if prefix_len < 0: raise ValueError
    if prefix_len > rng.inf_max: raise ValueError
    assert 0 < prefix_len < L
    return LeftRotateArray(io_type, prefix_len)

class LeftRotateArray(Bijection):
    '[a, b, ...] <-[2]-> [..., a, b]'
    # RightRotateArray == LeftRotateArray^-1
    def __init__(self, io_type, prefix_len):
        assert isinstance(io_type, ArrayTV), TypeError
        assert type(prefix_len) is int, TypeError
        rng = io_type.size_range
        assert 0 < prefix_len < rng.inf_max, ValueError
        self.prefix_len = prefix_len

        self.io_type = io_type

    def get_InputType(self):
        return self.io_type
    def get_OutputType(self):
        return self.io_type
    def untypechecked_forward(self, input):
        return left_rotate_seq__strict(self.prefix_len, input)
    def untypechecked_backward(self, output):
        return left_rotate_seq__strict(self.prefix_len, output)
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'left_rotate_arrayBJ', self.io_type, self.prefix_len)

######################################


def tuple2tuple_by_unpackBJ(InputType, OutputType):
    assert isinstance(InputType, TupleTV)
    if InputType == OutputType:
        return InputType.idBJ
    b1 = unpack_tupleBJ(InputType)
    b2_inv = unpack_tupleBJ(OutputType)
    return +(b1 >> ~b2_inv)
def unpack_tupleBJ(InputType):
    if isinstance(InputType, TupleTV) and \
        any(isinstance(tv, TupleTV) for tv in InputType.type_verifiers):
        return UnpackTuple(InputType)
    return InputType.idBJ
class UnpackTuple(Bijection):
    '(a, ((b, c), d)) <-> (a, b, c, d)'
    def __init__(self, InputType):
        assert isinstance(InputType, TupleTV), TypeError
        assert any(isinstance(tv, TupleTV) for tv in InputType.type_verifiers)
        type_verifiers = InputType.type_verifiers
        idx2isTupleTV = tuple(isinstance(tv, TupleTV) for tv in type_verifiers)
        assert any(idx2isTupleTV)

        self.__bijection = TupleTV(*map(unpack_tupleBJ, type_verifiers))
        self.InputType = InputType
        self.idx2isTupleTV = idx2isTupleTV
        self.idx2may_len = \
            tuple(len(tv.type_verifiers) if is_tpl else None
                    for is_tpl, tv in zip(idx2isTupleTV, type_verifiers))
        tvsO_mid = self.__bijection.OutputType.type_verifiers
        tvsO = []
        for is_tpl, tv in zip(idx2isTupleTV, type_verifiers):
            if is_tpl:
                tvsO.extend(tv.type_verifiers)
            else:
                tvsO.append(tv)
        self.OutputType = TupleTV(*tvsO)
        assert self.InputType != self.OutputType


    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        mid = self.__bijection.untypechecked_forward(input)
        out = []
        for is_tpl, x in zip(self.idx2isTupleTV, mid):
            if is_tpl:
                out.extend(x)
            else:
                out.append(x)
        out = tuple(out)
        return out
    def untypechecked_backward(self, output):
        i = 0
        input = []
        for may_len in self.idx2may_len:
            if may_len is None:
                input.append(output[i])
                i += 1
            else:
                L = may_len
                input.append(output[i:i+L])
                i += L
        assert i == len(output)
        input = tuple(input)
        return input
    def get_construct_info(self):
        return self.make_name_args_kwargs('unpack_tupleBJ', self.InputType)


##
def remove_tuple_singleton_elemBJ(InputType):
    assert isinstance(InputType, TupleTV), TypeError
    if any(tv.is_singletonTV() for tv in InputType.type_verifiers):
        return RemoveSingletonTupleElem(InputType)
    return InputType.idBJ
class RemoveSingletonTupleElem(Bijection):
    '(a, (), TheNone, b) <-> (a, b)'
    # see also: UniqueBJ.py
    def __init__(self, InputType):
        assert isinstance(InputType, TupleTV), TypeError
        assert any(tv.is_singletonTV() for tv in InputType.type_verifiers)
        type_verifiers = InputType.type_verifiers
        idx2not_singletonTV = tuple(not tv.is_singletonTV() for tv in type_verifiers)
        idx2is_singletonTV = tuple(map(lambda b: not b, idx2not_singletonTV))
        assert any(idx2is_singletonTV)

        self.InputType = InputType
        self.OutputType = TupleTV(*compress(type_verifiers, idx2not_singletonTV))
        self.idx2not_singletonTV = idx2not_singletonTV
        self.singletons = tuple(tv1.get_the_single_elem()
                for tv1 in compress(type_verifiers, idx2is_singletonTV))
        assert self.InputType != self.OutputType


    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return tuple(compress(input, self.idx2not_singletonTV))
    def untypechecked_backward(self, output):
        out_idx = 0
        sigleton_idx = 0
        singletons = self.singletons
        input = []
        for not1 in self.idx2not_singletonTV:
            if not1:
                x = output[out_idx]
                out_idx += 1
            else:
                x = singletons[sigleton_idx]
                sigleton_idx += 1
            input.append(x)
        assert out_idx == len(output)
        assert sigleton_idx == len(singletons)
        input = tuple(input)
        return input
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'remove_tuple_singleton_elemBJ', self.InputType)



def iter_permute_seq(seq, out_idx2seq_idx):
    L = len(seq)
    return (seq[out_idx2seq_idx[i]] for i in range(L))
def permute_tupleBJ(InputType, OutputType):
    assert isinstance(InputType, TupleTV), TypeError
    assert isinstance(OutputType, TupleTV), TypeError
    if InputType == OutputType:
        return InputType.idBJ
    return PermuteTuple(InputType, OutputType)
def permute_tuple_omit_singletonBJ(InputType, OutputType):
    assert isinstance(InputType, TupleTV), TypeError
    assert isinstance(OutputType, TupleTV), TypeError
    if InputType == OutputType:
        return InputType.idBJ
    bI = remove_tuple_singleton_elemBJ(InputType)
    bO = ~remove_tuple_singleton_elemBJ(OutputType)
    bM = permute_tupleBJ(bI.get_OutputType(), bO.get_InputType())
    return +(bI >> bM >> bO)
class PermuteTuple(Bijection):
    '(a, b, c) <-[?]-> (c, b, a)'
    def __init__(self, InputType, OutputType):
        assert isinstance(InputType, TupleTV), TypeError
        assert isinstance(OutputType, TupleTV), TypeError
        assert InputType != OutputType
        type_verifiersI = InputType.type_verifiers
        type_verifiersO = OutputType.type_verifiers
        tvsI = set(type_verifiersI)
        tvsO = set(type_verifiersO)
        assert len(tvsI) == len(type_verifiersI), TypeError('not distinguish')
        assert tvsI == tvsO, TypeError('not permutation')
        # assert InputType != OutputType
        L = len(type_verifiersI)
        tv2idxI = dict(zip(type_verifiersI, range(L)))
        tv2idxO = dict(zip(type_verifiersO, range(L)))
        idxI2idxO = tuple(tv2idxO[tv] for tv in type_verifiersI)
        idxO2idxI = tuple(tv2idxI[tv] for tv in type_verifiersO)

        self.InputType = InputType
        self.OutputType = OutputType
        self.idxI2idxO = idxI2idxO
        self.idxO2idxI = idxO2idxI


    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return tuple(iter_permute_seq(input, self.idxO2idxI))
    def untypechecked_backward(self, output):
        return tuple(iter_permute_seq(output, self.idxI2idxO))
    def get_construct_info(self):
        return self.make_name_args_kwargs(
            'permute_tupleBJ', self.InputType, self.OutputType)



