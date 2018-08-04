
from .Bijection import Bijection
from .abbr import UInt, UInts
import itertools
from itertools import islice, accumulate
from abc import abstractmethod
from .import_choose import C
from .import_LinkedList import from_LinkedList_to_list

def fst(ab):
    return ab[0]
def snd(ab):
    return ab[1]
def at(pos, it):
    assert pos >= 0
    obj, = islice(it, pos, pos+1)
    return obj
def index_by(f, iterable):
    for i, y in enumerate(iterable):
        if f(y): return i
    raise IndexError
def index(x, iterable):
    f = lambda y: x == y
    return index_by(f, iterable)
'''
class (UInts2UInt_by_layers):
    def uints2level(self, uints):
    def level2sorted_len_count_pairs(self, level):
    def iter_ordered_uints_of_len(self, len):
'''
class UInts2UInt_by_layers(Bijection):
    def get_InputType(self):
        return UInts
    def get_OutputType(self):
        return UInt
    def untypechecked_forward(self, input):
        uints = input
        level = self.uints2level(uints)
        level_offset = self.level_offset(level)
        level_pos = self.index_uints_in_level(level, uints)
        return level_offset + level_pos
    def untypechecked_backward(self, output):
        uint = output
        level, len, idx = self.uint2level_len_idx(uint)
        it = self.iter_ordered_uints_in_level_len(level, len)
        return at(idx, it)

    # uints -> uint  # maynot injection
    @abstractmethod
    def uints2level(self, uints):pass
    # uint -> [(uint, pint)] # finite; uint not equal; sorted
    @abstractmethod
    def level2sorted_len_count_pairs(self, level):pass
    # uint -> [uints]  # len(uints) == uint; ordered by index
    @abstractmethod
    def iter_ordered_uints_of_len(self, len):pass
    # uint -> uint -> [uints] # ordered by index
    def iter_ordered_uints_in_level_len(self, level, len):
        it = self.iter_ordered_uints_of_len(len)
        return (uints for uints in it if self.uints2level(uints) == level)
    # uint -> uint -> uints -> uint   # len(uints) == len
    def index_uints_in_level_len(self, level, len, uints):
        assert len(uints) == len
        it = self.iter_ordered_uints_in_level_len(level, len)
        return index(uints, it)
    def index_uints_in_level(self, level, uints):
        L = len(uints)
        f = lambda len_count: len_count[0] == L
        pairs = self.level2sorted_len_count_pairs(level)
        i = index_by(f, pairs)
        offset = sum(count for _, count in pairs[:i])
        pos = self.index_uints_in_level_len(level, L, uints)
        return offset + pos
    # uint -> uint
    #   level2count level = |{uints | uints2level uints == level}|
    def level2count(self, level):
        pairs = self.level2sorted_len_count_pairs(level)
        total = sum(count for _, count in pairs)
        return total
    def level_offset(self, level):
        return sum(self.level2count(small_level)
                    for small_level in range(0, level))
    def iter_level_offsets(self):
        counts = chain([0], map(self.level2count, itertools.count()))
        return accumulate(counts)
    def iter_len_offset_pairs_in_level(self, level):
        pairs = self.level2sorted_len_count_pairs(level)
        counts = chain([0], map(snd, pairs))
        offsets = accumulate(counts)
        return zip(map(fst, pairs), offsets)
    def uint2level(self, uint):
        f = lambda offset: uint < offset
        i = index_by(f, self.iter_level_offsets())
        level = i - 1
        return level
    def uint2level_len_idx(self, uint):
        level = self.uint2level(uint)
        level_offset = self.level_offset(level)
        level_pos = uint - level_offset
        *pairs, = self.iter_len_offset_pairs_in_level(level)
        f = lambda len_offset: level_pos < snd(len_offset)
        i = index_by(f, pairs)
        len, len_offset = pairs[i-1]
        idx = level_pos - len_offset
        return level, len, idx


def num_of_n_UInt_of_sum(sum_:'UInt', len:'PInt'):
    # uint -> pint -> uint
    # num_of_n_UInt_of_sum(sum, len) = |{uints in UInt^len | sum(uints)==sum}|
    assert len > 0
    if sum_ == 0: return 1
    if len == 1: return 1
    return sum(num_of_n_UInt_of_sum(sum_-head, len-1) for head in range(0, sum_+1))
def num_of_n_UInt_of_sum(sum_:'UInt', len:'PInt'):
    return C(sum_+len-1, len-1)
class UInts2UInt_by_layers__sum(UInts2UInt_by_layers):
    def uints2level(self, uints):
        return sum(uints)+len(uints)
    '''
    total_per_level level
        = sum C(level-1, len-1) {len=1..level} + [level==0]
        = sum C(level-1, len-1) {len=-oo..+oo} + [level==0]
        = sum C(level-1, i) {i <- Int} + [level==0]
        = [level>0]2^(level-1) + [level==0]
    totol_before_level level
        = sum total_per_level i {i=0->level}
        = [level>0]sum total_per_level i {i=0->level}
        + [level==0]sum total_per_level i {i=0->level}
        = [level>0](1 + sum total_per_level i {i=1..level-1})
        = [level>0](1 + sum 2^(i-1) {i=1..level-1})
        = [level>0]2^(level-1)
    total_per_len_in_level level len
        = [level==0][len==0] + [level>0]C(level-1, len-1)
    total_before_len_in_level level len
        = sum total_per_len_in_level level i {i=0->len}
        = [level==0]sum total_per_len_in_level level i {i=0->len}
        + [level>0]sum total_per_len_in_level level i {i=0->len}
        = [level==0][len==0]0
        + [level==0][len>0]sum total_per_len_in_level level i {i=0..len-1}
        + [level>0]sum total_per_len_in_level level i {i=0->len}
        = [level==0][len>0]total_per_len_in_level level 0
        + [level>0]sum total_per_len_in_level level i {i=0->len}
        = 1 + [level>0]sum total_per_len_in_level level i {i=0->len}
        = 1 + [level>0]sum C(level-1, i-1) {i=0->len}
        = ?????????
    '''
    def level2iter_sorted_len_count_pairs(self, level):
        if level == 0:
            yield (0, 1)
            return
        for len in range(1, level+1):
            sum = level - len
            count = num_of_n_UInt_of_sum(sum, len)
            if count > 0:
                yield len, count
    def level2sorted_len_count_pairs(self, level):
        return tuple(self.level2iter_sorted_len_count_pairs(level))
    def iter_ordered_LinkedUInts_of_len_sum(self, len:'PInt', sum_:'UInt'):
        assert len > 0
        if len == 1:
            yield (sum_, ())
        this_func = self.iter_ordered_LinkedUInts_of_len_sum
        for head in range(0, sum_+1):
            for tail in this_func(len-1, sum_-head):
                yield (head, tail)
    def iter_ordered_uints_of_len(self, len):
        if len == 0:
            yield ()
            return
        f = self.iter_ordered_LinkedUInts_of_len_sum
        for sum_ in itertools.count():
            for ll in f(len, sum_):
                yield tuple(from_LinkedList_to_list(ll))

