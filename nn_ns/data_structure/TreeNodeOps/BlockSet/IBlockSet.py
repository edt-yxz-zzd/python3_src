
from .abc import ABC, not_implemented
#from collections.abc import Set, MutableSet

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase

from itertools import chain
from seed.tiny import null_iter, echo
from seed.iters.handle_first_middles_last import handle_first_middles_last

from ..BlockDictOps.bd_helper import \
    (is_one_piece_block_key
    ,is_exactly_block_key
    ,block_key2iter_block_entities
    , bd_subtract
    )


entity2block_key = echo
ireplace_block_key_of_entity = lambda entity, block_key: block_key


class IBlockSet(ABC):
    '''
not (MutableSet):
    since no __len__/__iter__
        # hence no pop

dict_key :: ITotalOrderingOps
    # to using KeyOrderedTree

set_key = dict_key = basic_key = key :: Key in IBlockDictKeyOps
    # BlockSet implement details:
    # tree_key = lkey_ex = left_key_ex = left_bound :: KeyEx in IBlockDictKeyOps


block_key = (lkey_ex, rkey_ex) = range :: Range



'''


    __slots__ = ()

    def get_total_dict_key_ops(self):
        # about dict_key
        return self.block_dict_key_ops.total_key_ops
    def get_block_dict_key_ops(self):
        bdk_ops = self._get_block_dict_key_ops_()
        assert isinstance(bdk_ops, IBlockDictKeyOps)
        return bdk_ops


    @not_implemented
    def _get_block_dict_key_ops_(self):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        ...



    @not_implemented
    def get_num_block_keys(self):
        # no __len__
        ...
    @not_implemented
    def iter_block_keys(self, *, reverse=False):
        # no __iter__/keys
        ...

    @not_implemented
    def copy(self):
        ...


    @not_implemented
    def _index_block_key_at_(self, i:'UInt'):
        # -> block_key
        assert 0 <= i < self.get_num_block_keys()
        ...
    def index_block_key_at(self, i:'Int'):
        # -> block_key | IndexError
        # normally, O(log(n)), maybe O(1), should not >O(n)
        # position may not be index
        # see: IBlockDictOps__position
        L = self.get_num_block_keys()
        if i < 0:
            i += L
        if not 0 <= i < L: raise IndexError
        return self._index_block_key_at_(i)
    def get_first_or_last_block_key(self, last:bool):
        # -> block_key | IndexError
        L = self.get_num_block_keys()
        if not L: raise IndexError
        #bug:i = L-1 if L else 0
        i = L-1 if last else 0
        return self._index_block_key_at_(i)
    def get_first_block_key(self):
        # -> block_key | IndexError
        return self.get_first_or_last_block_key(False)
    def get_last_block_key(self):
        # -> block_key | IndexError
        return self.get_first_or_last_block_key(True)





    @not_implemented
    def self_make_empty_block_set(self):
        ...
    @not_implemented
    def self_make_block_set_from_dict_keys(self, dict_keys):
        ...
    @not_implemented
    def self_make_block_set_from_block_keys(self, block_keys):
        ...

    @not_implemented
    def iter_all_touch_or_overlap_block_keys(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        ...

    def self_make_block_set_from_iterable(self, iterable, is_block_keys:bool):
        if is_block_keys:
            f = self.self_make_block_set_from_block_keys
        else:
            f = self.self_make_block_set_from_dict_keys
        return f(iterable)


    def is_empty(self):
        return not self
    def is_whole_set(self):
        if self.get_num_block_keys() != 1: return False
        block_dict_key_ops = self.block_dict_key_ops

        rng = self.get_first_block_key()
        wrng = block_dict_key_ops.getWholeRange()
        return block_dict_key_ops.eqRange(rng, wrng)

    def __bool__(self):
        return bool(self.get_num_block_keys())

    @property
    def mkSingletonRange(self):
        return self.get_block_dict_key_ops().mkSingletonRange
    @property
    def block_dict_key_ops(self):
        return self.get_block_dict_key_ops()
    @property
    def total_dict_key_ops(self):
        return self.get_total_dict_key_ops()



    def block_key2block_keys(self, block_key, *, reverse=False):
        # -> [block_key]
        return list(self.block_key2iter_block_keys(block_key, reverse=reverse))





    def is_one_piece_block_key(self, block_key):
        # not empty range and inside one of iter_block_keys()
        return is_one_piece_block_key(
                block_key
                , entity2block_key
                , self.block_dict_key_ops
                , self.iter_all_touch_or_overlap_block_keys)

    def is_exactly_block_key(self, block_key):
        # be one of iter_block_keys()
        return is_exactly_block_key(
                block_key
                , entity2block_key
                , self.block_dict_key_ops
                , self.iter_all_touch_or_overlap_block_keys)

    def list_all_touch_or_overlap_block_keys(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        # block_key may be empty
        iter_all_of = self.iter_all_touch_or_overlap_block_keys
        return [*iter_all_of(block_key, overlap_only, reverse=reverse)]



    def dict_key2block_keys(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        block_keys = self.block_key2block_keys(block_key)
        return block_keys








    def __contains__(self, dict_key):
        block_keys = self.dict_key2block_keys(dict_key)
        return bool(block_keys)



    def before__le(self, other):
        # since "<=" used as issubset
        # "<="
        return self.before(other, False)
    def before__lt(self, other):
        # since "<=" used as issubset
        # "<"
        return self.before(other, True)
    def after__ge(self, other):
        # since "<=" used as issubset
        # ">="
        return self.after(other, False)
    def after__gt(self, other):
        # since "<=" used as issubset
        # ">"
        return self.after(other, True)
    def before(self, other, strict:bool):
        # since "<=" used as issubset
        # "<" if strict else "<="
        r = self.block_set_cmp(other)
        if not r:
            return not strict
        return r < 0
    def after(self, other, strict:bool):
        # since "<=" used as issubset
        # ">" if strict else ">="
        r = self.block_set_cmp(other)
        if not r:
            return not strict
        return r > 0

    def block_set_cmp(self, other):
        # -> -1/0/+1
        if self is other: return 0

        self.__check_other(other)

        block_dict_key_ops = self.block_dict_key_ops
        cmpRange = block_dict_key_ops.cmpRange
        eqRange = block_dict_key_ops.eqRange

        s_it = self.iter_block_keys()
        o_it = other.iter_block_keys()
        for s_rng, o_rng in zip(s_it, o_it):
            if eqRange(s_rng, o_rng): continue
            r = cmpRange(s_rng, o_rng) # -1/0/+1
            assert r
            return r # -1/+1
        sL = self.get_num_block_keys()
        oL = other.get_num_block_keys()
        d = sL - oL
        if not d:
            return 0
        return -1 if d < 0 else +1
    def __eq__(self, other):
        if self is other: return True

        if not isinstance(other, __class__): return NotImplemented
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        if self.get_num_block_keys() != other.get_num_block_keys():
            return False

        block_dict_key_ops = self.block_dict_key_ops
        eqRange = block_dict_key_ops.eqRange
        return all(map(eqRange, self.iter_block_keys(), other.iter_block_keys()))

    def __ne__(self, other):
        return not (self == other)

    def __check_other(self, other):
        if not isinstance(other, __class__): raise TypeError
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
    def issuperset(self, other):
        return self.__issubset(other, True)
    def issubset(self, other):
        return self.__issubset(other, False)
    def __issubset(self, other, swap:bool):
        if self is other: return True
        self.__check_other(other)

        insideRange = self.block_dict_key_ops.insideRange
        if swap:
            other, self = self, other

        if not self: return True
        if not other: return False
        iter_all_of = other.iter_all_touch_or_overlap_block_keys
        for block_key in self.iter_block_keys():
            it = iter_all_of(block_key, True)
            #if len(block_keys) != 1: return False
            for other_block_key in it:
                break
            else:
                return False
            if not insideRange(block_key, other_block_key):
                return False
        return True

    def __le__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.issubset(other)
    def __lt__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self <= other and self != other
    def __gt__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self >= other and self != other
    def __ge__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.issuperset(other)
    def __and__(self, other):
        if self is other: return self.copy()
        self.__check_other(other)
        block_keys = self.__iter_and(other)
        return self.self_make_block_set_from_block_keys(block_keys)
    def __iter_and(self, other):
        if self.get_num_block_keys() > other.get_num_block_keys():
            other, self = self, other

        block_key2iter_block_keys = other.block_key2iter_block_keys
        return chain.from_iterable(
            map(block_key2iter_block_keys, self.iter_block_keys()))
    def __or__(self, other):
        if self is other: return self.copy()
        self.__check_other(other)
        return self.self_make_block_set_from_block_keys(
            chain(self.iter_block_keys(), other.iter_block_keys())
            )
    def __sub__(self, other):
        if self is other: return self.self_make_empty_block_set()
        self.__check_other(other)
        s_block_keys = self.__sub(other, False)
        return self.self_make_block_set_from_block_keys(s_block_keys)
    def __sub(self, other, swap:bool):
        # -> [block_key]
        block_dict_key_ops = self.block_dict_key_ops
        if swap:
            other, self = self, other
        return bd_subtract(
            entity2block_key
            , ireplace_block_key_of_entity
                # :: entity -> block_key -> new_entity
            , block_dict_key_ops
            , self.iter_block_keys()
            , other.block_key2iter_block_keys
            )
        '''
        subtract = block_dict_key_ops.subtract_two_touch_or_cross_ranges
        block_key2iter_block_keys = other.block_key2iter_block_keys
        s_block_keys = []
        for s_block_key in self.iter_block_keys():
            o_block_keys = block_key2iter_block_keys(s_block_key)
            s_block_keys.append(s_block_key)
            for o_block_key in o_block_keys:
                s_block_key = s_block_keys.pop()
                s_block_keys.extend(subtract(s_block_key, o_block_key))
        return s_block_keys
        '''


    def __xor__(self, other):
        if self is other: return self.self_make_empty_block_set()
        self.__check_other(other)
        #return (self - other) | (other - self)
        s_block_keys = self.__sub(other, False)
        o_block_keys = self.__sub(other, True)
        return self.self_make_block_set_from_block_keys(
            chain(s_block_keys, o_block_keys))
    def isdisjoint(self, other):
        self.__check_other(other)
        iter_block_keys = self.__iter_and(other)
        for _ in iter_block_keys:
            return False
        return True

    ###############

    def block_key2iter_block_keys(self, block_key, *, reverse=False):
        # intput_block_key may be empty
        #
        # -> Iter (block_key, dict_value)
        #   all output_block_keys are nonempty and inside input_block_key
        return block_key2iter_block_entities(
                    block_key
                    , bool(reverse)
                    , entity2block_key
                    , ireplace_block_key_of_entity
                        # :: entity -> block_key -> new_entity
                    , self.block_dict_key_ops
                    , self.iter_all_touch_or_overlap_block_keys
                    )

    def self_make_whole_block_set(self):
        rng = self.block_dict_key_ops.getWholeRange()
        return self.self_make_block_set_from_block_keys([rng])
    def self_make_complement_block_set(self):
        block_dict_key_ops = self.block_dict_key_ops
        rng = block_dict_key_ops.getWholeRange()
        block_keys = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , [rng]
                , self.block_key2iter_block_keys
                )
        return self.self_make_block_set_from_block_keys(block_keys)
    def __neg__(self):
        return self.self_make_complement_block_set()



if __name__ == '__main__':
    XXX = IBlockSet

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)




