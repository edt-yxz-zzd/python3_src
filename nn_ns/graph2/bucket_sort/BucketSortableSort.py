
'''
BucketSortable
    # bucket sortable key type
    # key :: Obj -> Key where Key <: BucketSortable
    # bucket_sort :: BucketSortable a => [a] -> [a]
    assume (a,b,c... <: BucketSortable a) below:
    BoundedUInt<upper_bound::UInt>
        0 <= uint < upper_bound
        if upper_bound is 0:
            there is no object at all
            or the object has no such key attribute
    Seq<a>
        [a]
        sorted in dictionary order
        a python sequence, donot consider the actual python type
    Tpl<a...>
        (...)
        sorted in dictionary order
        a python sequence, donot consider the actual python type

        allow vary length
        if len(python seq obj) > len(type Tpl) == L:
            then omit the seq[L:]
        if Lseq == len(python seq obj) < len(type Tpl):
            then omit Tpl[Lseq:]
    LenSeq<a>
    LenTpl<a...>
        like Seq/Tpl
        but sorted by len after lex sort
        i.e. LenSeq/LenTpl <==> (len, Seq/Tpl)

    -- union
    Switch<a...>
        let total_case = len(Switch)
        (case::BoundedUInt<total_case>, ~PyUnion~<a|b|c|...>)

    -- recur
    -- ?? Tree a b = Leaf a | Node b [Tree a b]
    -- Tree a b <==> (tree_structure_binary_string :: [bool], prefix_order :: [b], linear :: [a])





see also:
    UIntSeqSort
        -- convert BucketSortable key into uint seq, then use UIntSeqSort
        -- e.g. Tpl<a,b,c> --> [TplOpen, offset+a, offset+b, offset+c, Close]
    shadow_key
        -- compute BucketSortable key may not efficient, e.g. (Tree a b) would transform to more simpler form; we may want to cache the key first

example:
    >>> S = BucketSortableSort
    >>> tv_u = BoundedUIntTV(6);
    >>> S(tv_u, key=snd)([(None,3), (False, 1), ([], 2), ((), 2)])
    [(False, 1), ([], 2), ((), 2), (None, 3)]
    >>> tv_len_seq = LenSeqTV(tv_u)
    >>> S(tv_len_seq)([(3,5), (4,), (3,5,2), (3,4), ()])
    [(), (4,), (3, 4), (3, 5), (3, 5, 2)]
    >>> tv_tpl = TplTV([tv_u, tv_len_seq, tv_u])
    >>> S(tv_tpl)([(3,), (2,[3],1, None), (2, [2,3])])
    [(2, [3], 1, None), (2, [2, 3]), (3,)]
    >>> tv_sw = SwitchTV([tv_tpl, tv_len_seq])
    >>> S(tv_sw)([(1, [1,1,1]), (1, [2]), (0, [1,(3,), 3, None]), (0, [1,(1,1)])])
    [(0, [1, (3,), 3, None]), (0, [1, (1, 1)]), (1, [2]), (1, [1, 1, 1])]
    >>> tv_seq = SeqTV(tv_u)
    >>> S(tv_seq)([[1], [], [0], [2], [2, 3], [2, 1], [1, 3]])
    [[], [0], [1], [1, 3], [2], [2, 1], [2, 3]]
'''


__all__ = '''
    BucketSortableSort

    global_idx_manager
    IBucketSortableTV

    BoundedUIntTV
    SeqTV
    LenSeqTV
    TplTV
    LenTplTV
    SwitchTV
    KnownTVs

    maybeTV
    Just
    Nothing

    '''.split()

from abc import ABC, abstractmethod
from collections.abc import Sequence
from itertools import chain
from .are_instances import are_instances
from .GroupBy import unique_keys, GroupBy
from .reiterable import make_seq, is_sorted, is_seq, is_sorted_seq
from .inplace_bucket_sort import calc_upper_bound_of_seqs
from .UIntSeqSort import UIntSeqSort
from .echo import echo_ifNone, snd, fst, echo
from .ISortBase import ISortBase__ConvertNoneKey
from .IObjectPredicator import IElementEq, are_elements





class Global_BoundedUIntTV_OpenCloseIDX:
    CLOSE = 0
    tv2open_idx = {}
    @staticmethod
    def get_tv_stream_uint_offset():
        d = __class__.tv2open_idx
        return len(d) + 1
    @staticmethod
    def get_open_idx(aBucketSortable):
        d = __class__.tv2open_idx
        return d[aBucketSortable]
    @staticmethod
    def add_TV(aBucketSortable):
        if not issubclass(aBucketSortable, IBucketSortableTV): raise TypeError
        d = __class__.tv2open_idx
        default = __class__.get_tv_stream_uint_offset()

        if aBucketSortable in d: raise Exception('already existed')
        d[aBucketSortable] = default
        return
        return d.setdefault(aBucketSortable, default)

global_idx_manager = Global_BoundedUIntTV_OpenCloseIDX()






class IBucketSortableTV(IElementEq):
    # TV: type verifier
    @abstractmethod
    def tv_local_upper_bound(self):...
    @abstractmethod
    def element_local_upper_bound(self, element):...

    @abstractmethod
    def stream(self, element):
        # element -> iter<uint>
        ...

    '''
    @abstractmethod
    def local_collect_ptr_uint_pairs(self, ptr, element, output):
        # ptr = () | (ptr, location::uint)
        #   location is case for Switch
        #   location is idx for [Len]Seq/Tpl
        # elements :: [element]
        # output::[(ptr, uint)]
        # return None
        ...

    #def bucket_sort(self, elements):...
    @abstractmethod
    def is_sort_info(self, obj):...
    @abstractmethod
    def collect_info(self, elements):...
    def global_collect_ptr_uint_pairs(self, elements):
        ptr = ()
        output = []
        for a in elements:
            self.local_collect_ptr_uint_pairs(ptr, a, output)
        return output
    '''




class BoundedUIntTV(IBucketSortableTV):
    def __init__(self, upper_bound):
        assert isinstance(upper_bound, int) and upper_bound >= 0
        self.upper_bound = upper_bound
    def element_eq(self, a, b):
        return a == b
    def is_element(self, obj):
        return isinstance(obj, int) and 0 <= obj < self.upper_bound
    def local_collect_ptr_uint_pairs(self, ptr, element, output):
        output.append((ptr, element))
    def tv_local_upper_bound(self):
        return self.upper_bound
    def element_local_upper_bound(self, element):
        return element+1

    def is_sort_info(self, obj):
        return is_seq(obj) and are_elements(obj, self) and is_sorted(obj)
    def collect_info(self, elements):
        return unique_keys(elements)
    def stream(self, element):
        yield global_idx_manager.get_tv_stream_uint_offset() + element

class IOpenCloseTV(IBucketSortableTV):
    @abstractmethod
    def stream_between_open_close(self, element):
        return
        yield
    def stream(self, element):
        open = global_idx_manager.get_open_idx(type(self))
        close = global_idx_manager.CLOSE
        yield open
        yield from self.stream_between_open_close(element)
        yield close

#class ISeqTplBaseTV(IBucketSortableTV):
class IWith_TV(IBucketSortableTV):
    def __init__(self, tv):
        if not isinstance(tv, IBucketSortableTV): raise TypeError
        self.tv = tv
class ISeqBaseTV(IWith_TV, IOpenCloseTV):
    def element_eq(self, a, b):
        return all(map(self.tv.element_eq, a, b))
    def is_element(self, obj):
        return isinstance(obj, Sequence) and all(map(self.tv.is_element, obj))
    def local_collect_ptr_uint_pairs(self, ptr, element, output):
        collect = self.tv.local_collect_ptr_uint_pairs
        for idx, a in enumerate(element):
            collect((ptr, idx), a, output)
        return
    def tv_local_upper_bound(self):
        return self.tv.tv_local_upper_bound()
    def element_local_upper_bound(self, element):
        return max(map(self.tv.element_local_upper_bound, element), default=0)

    @abstractmethod
    def stream_after_open(self, element):
        # bug: miss "return" will 'yield' a 'None'!!!
        return
        yield
    def stream_between_open_close(self, element):
        yield from self.stream_after_open(element)
        tv = self.tv
        yield from chain.from_iterable(map(tv.stream, element))

class SeqTV(ISeqBaseTV):
    def stream_after_open(self, element):
        return
        yield
    pass

class LenSeqTV(ISeqBaseTV):
    def stream_after_open(self, element):
        yield len(element)
    pass

class IWith_TV_Size(IBucketSortableTV):
    def __init__(self, tvs):
        tvs = tuple(tvs)
        if not are_instances(tvs, IBucketSortableTV): raise TypeError
        self.tvs = tvs
        self.tv_sizeTV= BoundedUIntTV(len(tvs))
    def tv_local_upper_bound(self):
        return max((tv.tv_local_upper_bound() for tv in self.tvs), default=0)

class ITplBaseTV(IWith_TV_Size, IOpenCloseTV):
    def element_eq(self, a, b):
        tvs = self.tvs
        La = len(a)
        Lb = len(b)
        L = len(tvs)
        if La == Lb or (La > L and Lb > L):
            return all(tv.element_eq(a, b) for tv, a, b in zip(tvs, a, b))
        return False

    def is_element(self, obj):
        if not isinstance(obj, Sequence):
            return False
        tvs = self.tvs
        # L = min(len(tvs), len(obj))
        # the shorter
        return all(tv.is_element(a) for tv, a in zip(tvs, obj))
    def local_collect_ptr_uint_pairs(self, ptr, element, output):
        tvs = self.tvs
        for idx, (tv, a) in enumerate(zip(tvs, element)):
            tv.local_collect_ptr_uint_pairs((ptr, idx), a, output)
        return
    def element_local_upper_bound(self, element):
        return max((tv.element_local_upper_bound(a) for tv, a in zip(self.tvs, element)), default=0)
    @abstractmethod
    def stream_after_open(self, element):
        return
        yield
    def stream_between_open_close(self, element):
        yield from self.stream_after_open(element)
        tvs = self.tvs
        yield from chain.from_iterable(tv.stream(a) for tv, a in zip(tvs, element))

class TplTV(ITplBaseTV):
    def stream_after_open(self, element):
        return
        yield
class LenTplTV(ITplBaseTV):
    def stream_after_open(self, element):
        yield len(element)

class SwitchTV(IWith_TV_Size, IOpenCloseTV):
    def element_eq(self, a, b):
        caseA, A = a
        caseB, B = b
        return caseA == caseB and self.tvs[caseA].element_eq(A, B)

    def is_element(self, obj):
        if not (isinstance(obj, Sequence) and len(obj) == 2):
            return False
        case, a = obj
        return (self.tv_sizeTV.is_element(case)
            and self.tvs[case].is_element(a))
    def local_collect_ptr_uint_pairs(self, ptr, element, output):
        case, a = element
        tv = self.tvs[case]
        tv.local_collect_ptr_uint_pairs((ptr, case), a, output)
        return
    def element_local_upper_bound(self, element):
        case, a = element
        tv = self.tvs[case]
        return tv.element_local_upper_bound(a)
    def stream_between_open_close(self, element):
        case, a = element
        tv = self.tvs[case]
        offset = global_idx_manager.get_tv_stream_uint_offset()
        yield offset+case
        yield from tv.stream(a)






def maybeTV(tv):
    return TplTV([tv])
def Just(a):
    return (a,)
Nothing = ()



####################
KnownTVs = (BoundedUIntTV, SeqTV, TplTV, LenSeqTV, LenTplTV, SwitchTV)
list(map(global_idx_manager.add_TV, KnownTVs))


if False:
    def ptr2list(ptr):
        output = []
        while ptr:
            ptr, a = ptr
            output.append(a)
        output.reverse()
        return output
    def sort(tv, elements):
        if not is_seq(elements): raise TypeError
        pairs = tv.global_collect_ptr_uint_pairs(elements)  # [(ptr, uint)]
        pairs = [(ptr2list(ptr), u) for ptr, u in pairs]    # [(lsptr, uint)]
        snd_upper_bound = max(map(snd, pairs), default=-1) + 1
        fst_upper_bound = max(map(fst, pairs), default=-1) + 1
        pairs = bucket_sort(snd_upper_bound, pairs, key=snd)
        pairs = seq_bucket_sort(fst_upper_bound, pairs, key=fst) # sorted [(lsptr, uint)]
        lsptr_uints_pairs = group_by(pairs) # sorted [(unique_lsptr, sorted [uint])]
        lsptr_uints_pairs = [(lsptr, unique_keys(uints)) for lsptr, uints in lsptr_uints_pairs] # sorted [(unique_lsptr, sorted [unique_uint])]
        raise ...


class BucketSortableSort(ISortBase__ConvertNoneKey):
    def __init__(self, tv, *, key=None, reverse=False):
        assert isinstance(tv, KnownTVs), TypeError
        self.tv = tv
        ISortBase__ConvertNoneKey.__init__(self, key=key, reverse=reverse)
        self.group_by = GroupBy(key=self.key, eq=tv.element_eq)
    def sort_and_groups(self, __objs):
        # [obj] -> [[obj]]
        objs = self.sort(__objs)
        return self.group_by.groups(objs)
    def __call__(self, __objs):
        return self.sort(__objs)
    def sort(self, __objs):
        objs = __objs
        key = self.key
        reverse = self.reverse
        tv = self.tv

        f = lambda obj: list(tv.stream(key(obj)))
        uints_obj_pairs = [(f(obj), obj) for obj in objs]
        upper_bound = calc_upper_bound_of_seqs(map(fst, uints_obj_pairs), echo)
        sort = UIntSeqSort(upper_bound, key=fst, reverse=reverse)
        uints_obj_pairs = sort(uints_obj_pairs)
        return list(map(snd, uints_obj_pairs))



if __name__ == "__main__":
    import doctest, sys
    def show(*args):
        print(*args, file=sys.stderr)
    doctest.testmod()
    for k in list(globals()): print(k)

