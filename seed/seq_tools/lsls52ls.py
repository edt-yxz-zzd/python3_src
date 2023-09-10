#check_super_idx
#   ???TODO
#DONE?:bisearch
#    mk5???
#    super_idx2ground_rng_end
#       neednot, use super_idx2ground_offset instead
#   super_idx2ground_offset instead
#       --> GroundIdx52IndirectIdxPair__list__bisearch
#
r'''
e ../../python3_src/seed/seq_tools/lsls52ls.py
seed.seq_tools.lsls52ls
py -m seed.seq_tools.lsls52ls
py -m nn_ns.app.debug_cmd   seed.seq_tools.lsls52ls -x
from seed.seq_tools.lsls52ls import sizes_to_ground_idx2super_idx_inner_idx_pair, sizes_to_ground_idx2super_idx, sizes_to_super_idx2ground_offset
from seed.seq_tools.lsls52ls import GroundIdx5IndirectIdxPair, GroundIdx52IndirectIdxPair__list, GroundIdx52IndirectIdxPair__list__bisearch, GroundIdx52IndirectIdxPair__func
from seed.seq_tools.lsls52ls import IGroundIdx5IndirectIdxPair, IGroundIdx52IndirectIdxPair

used in:
    seed.math.matrix.solve_matrix
        view ../../python3_src/seed/math/matrix/solve_matrix.py
see also:
    nn_ns.app.crypt.involution.InvolutoryCipher::derived5idx8eqvcls2num_elements
        view ../../python3_src/nn_ns/app/crypt/involution/InvolutoryCipher.py
        (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements) = derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements)



get_state___sizes__si2go
get_state___sizes__si2go__gi2si_ni
go - ground_offset
si - super_idx
gi - ground_idx
ni - inner_idx

[[[
>>> from seed.seq_tools.lsls52ls import sizes_to_ground_idx2super_idx_inner_idx_pair, sizes_to_ground_idx2super_idx, sizes_to_super_idx2ground_offset, GroundIdx5IndirectIdxPair, GroundIdx52IndirectIdxPair__list, GroundIdx52IndirectIdxPair__list__bisearch, GroundIdx52IndirectIdxPair__func

>>> def print_dir(x, /):
...     for nm in dir(x):
...         if nm[0] != '_':
...             print(nm)
>>> g = GroundIdx5IndirectIdxPair([])
>>> {g}
{GroundIdx5IndirectIdxPair(())}
>>> print_dir(g)
get_len_ground_seq
get_len_inner_seq_at
get_len_super_seq
get_state___sizes__si2go
ground_idx5super_idx_inner_idx
ground_idx5super_idx_inner_idx_pair
ground_offset5super_idx
ground_offset_ex5super_idx_ex

>>> g.get_len_ground_seq()
0
>>> g.get_len_super_seq()
0
>>> g.get_state___sizes__si2go()
((), ())
>>> g.ground_offset_ex5super_idx_ex(0)
0

>>> g = GroundIdx52IndirectIdxPair__list([])
>>> {g}
{GroundIdx52IndirectIdxPair__list(())}
>>> print_dir(g)
get_len_ground_seq
get_len_inner_seq_at
get_len_super_seq
get_state___sizes__si2go
get_state___sizes__si2go__gi2si_ni
ground_idx2ground_offset
ground_idx2inner_idx
ground_idx2super_idx
ground_idx2super_idx_inner_idx_pair
ground_idx5super_idx_inner_idx
ground_idx5super_idx_inner_idx_pair
ground_idx_ex2super_idx_ex
ground_offset5super_idx
ground_offset_ex5super_idx_ex

>>> g.get_state___sizes__si2go__gi2si_ni()
((), (), ())
>>> g.ground_idx_ex2super_idx_ex(0)
0

>>> g = GroundIdx52IndirectIdxPair__list__bisearch([])
>>> {g}
{GroundIdx52IndirectIdxPair__list__bisearch(())}
>>> print_dir(g)
get_len_ground_seq
get_len_inner_seq_at
get_len_super_seq
get_state___sizes__si2go
ground_idx2ground_offset
ground_idx2inner_idx
ground_idx2super_idx
ground_idx2super_idx_inner_idx_pair
ground_idx5super_idx_inner_idx
ground_idx5super_idx_inner_idx_pair
ground_idx_ex2super_idx_ex
ground_offset5super_idx
ground_offset_ex5super_idx_ex

>>> g.get_state___sizes__si2go()
((), ())
>>> g.ground_idx_ex2super_idx_ex(0)
0












>>> g = GroundIdx5IndirectIdxPair([0, 5, 1])
>>> {g}
{GroundIdx5IndirectIdxPair((0, 5, 1))}
>>> g.get_len_ground_seq()
6
>>> g.get_len_inner_seq_at(1)
5
>>> g.get_len_super_seq()
3
>>> g.get_state___sizes__si2go()
((0, 5, 1), (0, 0, 5))
>>> g.ground_idx5super_idx_inner_idx(1, 4)
4
>>> g.ground_idx5super_idx_inner_idx_pair((2, 0))
5
>>> g.ground_offset5super_idx(1)
0
>>> g.ground_offset_ex5super_idx_ex(0)
0
>>> g.ground_offset_ex5super_idx_ex(1)
0
>>> g.ground_offset_ex5super_idx_ex(2)
5
>>> g.ground_offset_ex5super_idx_ex(3)
6


>>> g = GroundIdx52IndirectIdxPair__list([0, 5, 1])
>>> {g}
{GroundIdx52IndirectIdxPair__list((0, 5, 1))}
>>> g.get_state___sizes__si2go__gi2si_ni()
((0, 5, 1), (0, 0, 5), ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0)))
>>> g.ground_idx2ground_offset(3)
0
>>> g.ground_idx2inner_idx(3)
3
>>> g.ground_idx2super_idx(3)
1
>>> g.ground_idx2super_idx_inner_idx_pair(3)
(1, 3)
>>> g.ground_idx_ex2super_idx_ex(0)
1
>>> g.ground_idx_ex2super_idx_ex(3)
1
>>> g.ground_idx_ex2super_idx_ex(4)
1
>>> g.ground_idx_ex2super_idx_ex(5)
2
>>> g.ground_idx_ex2super_idx_ex(6)
3

>>> g = GroundIdx52IndirectIdxPair__list__bisearch([0, 5, 1])
>>> {g}
{GroundIdx52IndirectIdxPair__list__bisearch((0, 5, 1))}
>>> g.get_state___sizes__si2go()
((0, 5, 1), (0, 0, 5))
>>> g.ground_idx2ground_offset(3)
0
>>> g.ground_idx2inner_idx(3)
3
>>> g.ground_idx2super_idx(3)
1
>>> g.ground_idx2super_idx_inner_idx_pair(3)
(1, 3)
>>> g.ground_idx_ex2super_idx_ex(0)
1
>>> g.ground_idx_ex2super_idx_ex(3)
1
>>> g.ground_idx_ex2super_idx_ex(4)
1
>>> g.ground_idx_ex2super_idx_ex(5)
2
>>> g.ground_idx_ex2super_idx_ex(6)
3











ground_idx2super_idx__si2gre_
ground_idx2super_idx__si2go_
>>> sizes = [0, 1, 2, 3, 0, 0, 0, 2, 0, 1, 0]

>>> super_idx2ground_rng_end = sizes_to_super_idx2ground_rng_end(sizes)
>>> super_idx2ground_rng_end
[0, 1, 3, 6, 6, 6, 6, 8, 8, 9, 9]
>>> [ground_idx2super_idx__si2gre_(super_idx2ground_rng_end, ground_idx) for ground_idx in range(sum(sizes))]
[1, 2, 2, 3, 3, 3, 7, 7, 9]

>>> super_idx2ground_offset = sizes_to_super_idx2ground_offset(sizes)
>>> super_idx2ground_offset
[0, 0, 1, 3, 6, 6, 6, 6, 8, 8, 9]
>>> [ground_idx2super_idx__si2go_(super_idx2ground_offset, ground_idx) for ground_idx in range(sum(sizes))]
[1, 2, 2, 3, 3, 3, 7, 7, 9]

]]]


#'''

__all__ = '''
    sizes_to_ground_idx2super_idx_inner_idx_pair
    sizes_to_ground_idx2super_idx
    sizes_to_super_idx2ground_offset
        ground_idx2super_idx__si2go_
    sizes_to_super_idx2ground_rng_end
        ground_idx2super_idx__si2gre_

    IGroundIdx5IndirectIdxPair
        IGroundIdx52IndirectIdxPair
        GroundIdx5IndirectIdxPair
            GroundIdx52IndirectIdxPair__list
            GroundIdx52IndirectIdxPair__list__bisearch
            GroundIdx52IndirectIdxPair__func

    '''.split()
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

#from seed.helper.repr_input import repr_helper
from seed.tiny import mk_tuple, check_uint, check_callable
from itertools import accumulate, chain
from seed.seq_tools.bisearch import bisearch



#def sizes2offsets(sizes, /):
def sizes_to_ground_idx2super_idx_inner_idx_pair(sizes, /):
    ground_idx2super_idx_inner_idx_pair = [(super_idx, inner_idx_at) for super_idx, sz in enumerate(sizes) for inner_idx_at in range(sz)]
    return ground_idx2super_idx_inner_idx_pair
def sizes_to_ground_idx2super_idx(sizes, /):
    ground_idx2super_idx = [super_idx for super_idx, sz in enumerate(sizes) for inner_idx_at in range(sz)]
    #[*ground_idx2super_idx] = chain.from_iterable(repeat(super_idx, sz) for super_idx, sz in enumerate(sizes))
    return ground_idx2super_idx
def sizes_to_super_idx2ground_offset(sizes, /):
    offsets = super_idx2ground_offset = []
    offset = 0
    for sz in sizes:
        offsets.append(offset)
        offset += sz
    return super_idx2ground_offset
    #offsets = [*accumulate([0, *sizes])]
    offsets.pop()
    return super_idx2ground_offset
def sizes_to_super_idx2ground_rng_end(sizes, /):
    super_idx2ground_rng_end = [*accumulate(sizes)]
    return super_idx2ground_rng_end
def ground_idx2super_idx__si2gre_(super_idx2ground_rng_end, ground_idx, /):
    (eqv_begin, eqv_end) = bisearch(ground_idx, super_idx2ground_rng_end)
    super_idx = eqv_end
    return super_idx
def ground_idx2super_idx__si2go_(super_idx2ground_offset, ground_idx, /):
    (eqv_begin, eqv_end) = bisearch(ground_idx, super_idx2ground_offset)
    super_idx = eqv_end-1
    return super_idx



class IGroundIdx5IndirectIdxPair(ABC):
    r'''
ground_seq :: [a]{len_ground_seq}
    ground_idx <- [0..<len_ground_seq]
    ground_idx_ex <- [0..=len_ground_seq]
    ground_offset_ex <- [0..=len_ground_seq]
super_seq :: [[a]{len_inner_seq_at<super_idx>} | super_idx <- [0..<len_super_seq]]{len_super_seq}
    super_idx <- [0..<len_super_seq]
    super_idx_ex <- [0..=len_super_seq]
    inner_idx_at<super_idx> <- [0..<len_inner_seq_at<super_idx>]

sizes = inner_seq_sizes = super_idx2len_inner_seq :: [uint]



ground_offset_ex<super_idx_ex> = sum sizes[:super_idx_ex]
ground_offset<super_idx> = ground_offset_ex<super_idx>
ground_rng_begin<super_idx> = ground_offset<super_idx>
ground_rng_end<super_idx> = ground_offset_ex<super_idx+1>



ground_rng_begin<super_idx<ground_idx> > <= ground_idx < ground_rng_end<super_idx<ground_idx> >
super_idx<ground_idx> <- {super_idx | ground_rng_begin<super_idx> <= ground_idx < ground_rng_end<super_idx>}
inner_idx_at<ground_idx> = ground_idx - ground_offset<super_idx<ground_idx> >

memory:
        super_idx2ground_rng_end:   O(len_super_seq)
            may be huge, e.g. 2**M
                len_super_seq = 2**M
                len_inner_seq_at(any super_idx) = 2**N
                len_ground_seq = len_super_seq*len_inner_seq_at(?) = 2**(M+N)

        ground_idx2super_idx:       O(len_ground_seq)
            may be huge, e.g. 2**N
                len_ground_seq = 2**N
                len_inner_seq_at(super_idx) = C(N, super_idx)
                len_super_seq = N+1
query:
    -> len_ground_seq
        super_idx2ground_rng_end:   O(1)
            .[-1] if . else 0
        ground_idx_ex2super_idx_ex: O(1)
            len(.)-1
    -> len_super_seq
        super_idx2ground_rng_end:   O(1)
            len(.)
        ground_idx_ex2super_idx_ex: O(1)
            .[-1] if . else 0
    -> len_inner_seq_at<super_idx>
        super_idx2ground_rng_end:   O(1)
            super_idx2ground_rng_end<super_idx> - (super_idx2ground_rng_end<super_idx-1> if super_idx else 0)
        ground_idx_ex2super_idx_ex: O(log len_ground_seq)
            bisearch rng eq to super_idx

    -> ground_idx
        <<==:
        (super_idx, inner_idx_at)
            super_idx2ground_rng_end:   O(1)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
            !!! 1 vs log
        (ground_offset/ground_rng_begin, inner_idx_at)
            O(1)
                ground_offset + inner_idx_at
        (ground_rng_end, inner_idx_at)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
            !!! log vs log

    -> super_idx
        <<==:
        (ground_idx)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(1)
            !!! log vs 1
    -> inner_idx_at<super_idx>
        <<==:
        (ground_idx)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)

    #no:-> ground_idx_ex
    -> ground_offset_ex
        <<==:
        (super_idx_ex)
            super_idx2ground_rng_end:   O(1)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
        (ground_idx_ex)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)

    -> ground_offset/ground_rng_begin
        <<==:
        # vivi. floor
        (super_idx)
            super_idx2ground_rng_end:   O(1)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
        (ground_idx)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
    -> ground_rng_end
        <<==:
        # vivi. cei
        (super_idx)
            super_idx2ground_rng_end:   O(1)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)
        (ground_idx)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(log len_ground_seq)

    -> super_idx_ex
        <<==:
        (ground_idx_ex)
            super_idx2ground_rng_end:   O(log len_super_seq)
            ground_idx_ex2super_idx_ex: O(1)


super_idx2len_inner_seq :: [uint]{len_super_seq}
<==> super_idx2ground_rng_end :: sorted[uint]{len_super_seq}
<==> ground_idx_ex2super_idx_ex :: sorted[uint]{len_ground_seq+1}
<==> ground_idx_ex2super_idx_ex_increment :: [uint]{len_ground_seq+1}




why split GroundIdx5IndirectIdxPair out from GroundIdx52IndirectIdxPair__list?
    since len_ground_seq may be huge
        see: nn_ns.app.crypt.involution.InvolutoryCipher::derived5idx8eqvcls2num_elements
        eg. super_idx == eqvcls == num_1s in bin(UIint)
            sizes = [C(N, i) for i in range(N+1)]
            ground_seq = [0..2**N -1]
    #'''
    __slots__ = ()
    @abstractmethod
    def _get_len_ground_seq_(sf, /):
        '-> len_ground_seq'
    @abstractmethod
    def _get_len_super_seq_(sf, /):
        '-> len_super_seq'
    @abstractmethod
    def _get_len_inner_seq_at_(sf, super_idx, /):
        'super_idx/uint%len_super_seq -> len_inner_seq_at@super_idx = len(super_seq[super_idx]'
    @abstractmethod
    def _ground_offset5super_idx_(sf, super_idx, /):
        'super_idx/uint%len_super_seq -> ground_offset'

    def _ground_idx5super_idx_inner_idx_(sf, super_idx, inner_idx_at, /):
        ground_offset = sf.ground_offset5super_idx(super_idx)
        ground_idx = ground_offset + inner_idx_at
        return ground_idx
    def ground_idx5super_idx_inner_idx(sf, super_idx, inner_idx_at, /):
        check_uint(super_idx)#necessary
        check_uint(inner_idx_at)#necessary
        if not super_idx < sf.get_len_super_seq(): raise TypeError#!!!unnecessary
        if not inner_idx_at < sf.get_len_inner_seq_at(super_idx): raise TypeError#necessary

        ground_idx = sf._ground_idx5super_idx_inner_idx_(super_idx, inner_idx_at)

        check_uint(ground_idx)
        if not ground_idx < sf.get_len_ground_seq(): raise TypeError
        return ground_idx
    def ground_idx5super_idx_inner_idx_pair(sf, super_idx_inner_idx_pair, /):
        (super_idx, inner_idx_at) = super_idx_inner_idx_pair
        ground_idx = sf.ground_idx5super_idx_inner_idx(super_idx, inner_idx_at)
        return ground_idx



    def get_len_ground_seq(sf, /):
        '-> len_ground_seq'
        len_ground_seq = sf._get_len_ground_seq_()
        check_uint(len_ground_seq)
        return len_ground_seq

    def get_len_super_seq(sf, /):
        '-> len_super_seq'
        len_super_seq = sf._get_len_super_seq_()
        check_uint(len_super_seq)
        return len_super_seq




    def get_len_inner_seq_at(sf, super_idx, /):
        '-> len_inner_seq_at@super_idx = len(super_seq[super_idx]'
        check_uint(super_idx)#necessary
        if not super_idx < sf.get_len_super_seq(): raise TypeError#!!!unnecessary
        len_inner_seq_at = sf._get_len_inner_seq_at_(super_idx)
        check_uint(len_inner_seq_at)
        return len_inner_seq_at



    def ground_offset_ex5super_idx_ex(sf, super_idx_ex, /):
        if super_idx_ex == sf.get_len_super_seq():
            ground_offset_ex = sf.get_len_ground_seq()
        else:
            super_idx = super_idx_ex
            ground_offset = sf.ground_offset5super_idx(super_idx)
            ground_offset_ex = ground_offset
        return ground_offset_ex
    def ground_offset5super_idx(sf, super_idx, /):
        '-> ground_offset'
        check_uint(super_idx)#necessary
        if not super_idx < sf.get_len_super_seq(): raise TypeError#!!!unnecessary

        ground_offset = sf._ground_offset5super_idx_(super_idx)
        check_uint(ground_offset)
        if not ground_offset < sf.get_len_ground_seq(): raise TypeError
        return ground_offset
#class IGroundIdx5IndirectIdxPair(ABC):

class IGroundIdx52IndirectIdxPair(IGroundIdx5IndirectIdxPair):
    __slots__ = ()
    @abstractmethod
    def _ground_idx2super_idx_inner_idx_pair_(sf, ground_idx, /):
        'ground_idx/uint%len_ground_seq -> (super_idx, inner_idx_at)'
    def ground_idx2super_idx_inner_idx_pair(sf, ground_idx, /):
        '-> (super_idx, inner_idx_at)'
        check_uint(ground_idx)
        if not ground_idx < sf.get_len_ground_seq(): raise TypeError
        (super_idx, inner_idx_at) = sf._ground_idx2super_idx_inner_idx_pair_(ground_idx)
        if not ground_idx == sf.ground_idx5super_idx_inner_idx(super_idx, inner_idx_at): raise TypeError
        return (super_idx, inner_idx_at)

    def ground_idx2super_idx(sf, ground_idx, /):
        (super_idx, inner_idx_at) = sf.ground_idx2super_idx_inner_idx_pair(ground_idx)
        return super_idx

    def ground_idx_ex2super_idx_ex(sf, ground_idx_ex, /):
        if ground_idx_ex == sf.get_len_ground_seq():
            super_idx_ex = sf.get_len_super_seq()
        else:
            ground_idx = ground_idx_ex
            super_idx = sf.ground_idx2super_idx(ground_idx)
            super_idx_ex = super_idx
        return super_idx_ex


    def ground_idx2inner_idx(sf, ground_idx, /):
        (super_idx, inner_idx_at) = sf.ground_idx2super_idx_inner_idx_pair(ground_idx)
        return inner_idx_at
    def ground_idx2ground_offset(sf, ground_idx, /):
        (super_idx, inner_idx_at) = sf.ground_idx2super_idx_inner_idx_pair(ground_idx)
        ground_offset = ground_idx - inner_idx_at
        assert ground_offset == sf.ground_offset5super_idx(super_idx)
        return ground_offset


#class IGroundIdx52IndirectIdxPair(IGroundIdx5IndirectIdxPair):






class GroundIdx5IndirectIdxPair(IGroundIdx5IndirectIdxPair, IReprImmutableHelper, ABC__no_slots):
    def __init__(sf, sizes, /):
        sizes = mk_tuple(sizes)
        for sz in sizes: check_uint(sz)
        super_idx2ground_offset = sizes_to_super_idx2ground_offset(sizes)
        sf._sizes = mk_tuple(sizes) #super_idx2len_inner_seq
        sf._si2goffset = mk_tuple(super_idx2ground_offset)
        sf._len_ground_seq = super_idx2ground_offset[-1] + sizes[-1] if sizes else 0
        assert sf._len_ground_seq == sum(sizes)
    def get_state___sizes__si2go(sf, /):
        return (sf._sizes, sf._si2goffset)

    @override
    def ___get_args_kwargs___(sf, /):
        # -> (args:Seq, kwargs:Mapping)
        #bug:return (sf._sizes, {})
        return ([sf._sizes], {})

    @override
    def _get_len_ground_seq_(sf, /):
        '-> len_ground_seq'
        return sf._len_ground_seq
        #return len(sf._gi2si_ni)#sum(sf._sizes)
    @override
    def _get_len_super_seq_(sf, /):
        '-> len_super_seq'
        return len(sf._si2goffset)#len(sf._sizes)
    @override
    def _get_len_inner_seq_at_(sf, super_idx, /):
        'super_idx/uint%len_super_seq -> len_inner_seq_at@super_idx = len(super_seq[super_idx]'
        len_inner_seq_at = sf._sizes[super_idx]#super_idx2len_inner_seq
        return len_inner_seq_at
    @override
    def _ground_offset5super_idx_(sf, super_idx, /):
        'super_idx/uint%len_super_seq -> ground_offset'
        ground_offset = sf._si2goffset[super_idx]
        return ground_offset
#class GroundIdx5IndirectIdxPair(IGroundIdx5IndirectIdxPair, IReprImmutableHelper, ABC__no_slots):



class GroundIdx52IndirectIdxPair__list(GroundIdx5IndirectIdxPair, IGroundIdx52IndirectIdxPair):
    def __init__(sf, sizes, /):
        sizes = mk_tuple(sizes)
        super().__init__(sizes)
        ground_idx2super_idx_inner_idx_pair = sizes_to_ground_idx2super_idx_inner_idx_pair(sizes)
        sf._gi2si_ni = mk_tuple(ground_idx2super_idx_inner_idx_pair)
    def get_state___sizes__si2go__gi2si_ni(sf, /):
        _sizes, _si2goffset = sf.get_state___sizes__si2go()
        return (_sizes, _si2goffset, sf._gi2si_ni)
    @override
    def _ground_idx2super_idx_inner_idx_pair_(sf, ground_idx, /):
        '-> (super_idx, inner_idx_at)'
        (super_idx, inner_idx_at) = sf._gi2si_ni[ground_idx]
        return (super_idx, inner_idx_at)
#class GroundIdx52IndirectIdxPair__list(GroundIdx5IndirectIdxPair, IGroundIdx52IndirectIdxPair):
class GroundIdx52IndirectIdxPair__list__bisearch(GroundIdx5IndirectIdxPair, IGroundIdx52IndirectIdxPair):
    @override
    def _ground_idx2super_idx_inner_idx_pair_(sf, ground_idx, /):
        '-> (super_idx, inner_idx_at)'
        _sizes, _si2goffset = sf.get_state___sizes__si2go()
        super_idx = ground_idx2super_idx__si2go_(_si2goffset, ground_idx)
        inner_idx_at = ground_idx -_si2goffset[super_idx]
        return (super_idx, inner_idx_at)


class GroundIdx52IndirectIdxPair__func(GroundIdx5IndirectIdxPair, IGroundIdx52IndirectIdxPair):
    def __init__(sf, sizes, ground_idx2super_idx_inner_idx_pair__callable, /):
        check_callable(ground_idx2super_idx_inner_idx_pair__callable)
        sizes = mk_tuple(sizes)
        super().__init__(sizes)
        sf._f4gi2si_ni = ground_idx2super_idx_inner_idx_pair__callable
    @override
    def ___get_args_kwargs___(sf, /):
        # -> (args:Seq, kwargs:Mapping)
        #bug:return (sf._sizes, {})
        _sizes, _si2goffset = sf.get_state___sizes__si2go()
        return ([_sizes, sf._f4gi2si_ni], {})

    @override
    def _ground_idx2super_idx_inner_idx_pair_(sf, ground_idx, /):
        '-> (super_idx, inner_idx_at)'
        (super_idx, inner_idx_at) = sf._f4gi2si_ni(ground_idx)
        return (super_idx, inner_idx_at)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
