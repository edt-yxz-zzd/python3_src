


r'''

why not using dict_key2basic_key?
    since block_key = range = (lkey_ex, rkey_ex)
    key/basic_key is compressed, it should be some very prime data type
        we should not have dict_key2basic_key
        hence basic_key is dict_key

    key = dict_key = basic_key
        ==>> will become (TheKey key)
    lkey_ex = left_key_ex = left_bound = tree_key
        entity = (block_key, dict_value) = ((lkey_ex, rkey_ex), dict_value)
        entity2key = entity2lkey_ex = lambda e: e[0][0]
            # here key means tree key
            #   in the KeyOrderedRedBlackTree context

    dict_value is using IEqOps instead of (==)
    dict_key is using ITotalOrderingOps instead of (<=)



Key
KeyEx = TheMinKeyEx | TheMaxKeyEx | TheKey Key | More Key | Less Key
    TheMinKeyEx = TheKey the_min_key | VirtualMoreMinKeyEx
    TheMaxKeyEx = TheKey the_max_key | VirtualLessMaxKeyEx
    More key = TheKey (succ key) | VirtualMoreKey key if TheKey key < TheMaxKeyEx
    Less key = TheKey (prec key) | VirtualLessKey key if TheKey key > TheMinKeyEx


example:
    * byte:
        TheMinKeyEx = TheKey 0
        TheMaxKeyEx = TheKey 255
        More key = TheKey (key+1) if key < 255
        Less key = TheKey (key-1) if key > 0
    * uint
        TheMinKeyEx = TheKey 0
        TheMaxKeyEx = VirtualLessMaxKeyEx # i.e. (..., +oo)
        More key = TheKey (key+1) if key < +oo
        Less key = TheKey (key-1) if key > 0
    * int
        TheMinKeyEx = VirtualMoreMinKeyEx # i.e. (-oo, ...)
        TheMaxKeyEx = VirtualLessMaxKeyEx # i.e. (..., +oo)
        More key = TheKey (key+1) if key < +oo
        Less key = TheKey (key-1) if key > -oo
    * Fraction
        TheMinKeyEx = VirtualMoreMinKeyEx # i.e. (-oo, ...)
        TheMaxKeyEx = VirtualLessMaxKeyEx # i.e. (..., +oo)
        More key = VirtualMoreKey key # i.e. (key, ...)
        Less key = VirtualLessKey key # i.e. (..., key)
    * bytes in dictionary-order
        TheMinKeyEx = TheKey b''
        TheMaxKeyEx = VirtualLessMaxKeyEx # i.e. (..., b'\xFF' * +oo)
        More key = TheKey (key + b'\x0')
        Less key = VirtualLessKey key if key > b'' and key[-1] > 0
                 | TheKey key[:-1] if key > b'' and key[-1] == 0
                # i.e.
                #   if key[-1] > 0:
                #       (..., key[:-1] ++ [key[-1]-1] ++ b'\xFF' * +oo)
                #   else:
                #       [..., key[:-1]]
    * bytes in (len, dictionary-order)
        TheMinKeyEx = TheKey b''
        TheMaxKeyEx = VirtualLessMaxKeyEx # i.e. (..., b'\xFF' * +oo)
        More key = TheKey (key + b'\x0') if key == b'\xFF'*len(key)
                | TheKey (key[:i] ++ [key[i]+1] ++ key[i+1:])
                    where key[i] < 255 and key[i+1:] == b'\xFF'*?
        Less key = TheKey ??? if key > b''

    * uints in dictionary-order
    * uints in (len, dictionary-order)
    * ints in dictionary-order
    * ints in (len, dictionary-order)






data KeyEx = (KeyExCase, payload)
    payload :: Key      if case = TheKey | VirtualMoreKey | VirtualLessKey
    payload is None     if case = VirtualMoreMinKeyEx | VirtualLessMaxKeyEx

LeftBound = LeftKeyEx = VirtualMoreMinKeyEx | VirtualMoreKey key | TheKey Key
RightBound = RightKeyEx = VirtualLessMaxKeyEx | VirtualLessKey key | TheKey Key
Range = (LeftKeyEx, RightKeyEx) = (LeftBound, RightBound)

'''




















__all__ = '''
    IBlockDictKeyOps
    KeyExCase
    not_strict_range_before

    has_key_ex_payload
    cmpKeyEx
    ltKeyEx
    eqKeyEx
    leKeyEx

    cmpRange
    eqRange
    '''.split()




from .abc import ABC, not_implemented, abstractmethod
import enum
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..OtherOps.TotalOrderingOps import TotalOrderingOps, python_total_key_ops


KeyExCase = enum.Enum('KeyExCase', '''
    VirtualLessKey
    TheKey
    VirtualMoreKey

    VirtualMoreMinKeyEx
    VirtualLessMaxKeyEx
    '''.split()
    )

def has_key_ex_payload(key_ex_case):
    return not (key_ex_case == KeyExCase.VirtualMoreMinKeyEx
        or key_ex_case == KeyExCase.VirtualLessMaxKeyEx)

LT = -1
EQ = 0
GT = +1
def cmp(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<Key>
    # lhs, rhs :: Key
    #
    # total_key_ops :: ITotalOrderingOps<KeyExCase>
    #   python_total_key_ops
    # lhs, rhs :: int
    #   #lhs, rhs :: KeyExCase
    #
    if total_key_ops.eq(lhs, rhs):
        return EQ
    return LT if total_key_ops.lt(lhs, rhs) else GT
def cmpKeyEx(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<Key>
    # lhs, rhs :: KeyEx
    #
    lhs_case, lhs_payload = lhs
    rhs_case, rhs_payload = rhs
    if lhs_case == rhs_case:
        if has_key_ex_payload(lhs_case):
            return cmp(total_key_ops, lhs_payload, rhs_payload)
        return EQ

    # lhs_case != rhs_case
    if not has_key_ex_payload(lhs_case):
        return LT if lhs_case == KeyExCase.VirtualMoreMinKeyEx else GT
    if not has_key_ex_payload(rhs_case):
        return GT if rhs_case == KeyExCase.VirtualMoreMinKeyEx else LT


    # lhs_case != rhs_case
    # has_key_ex_payload(lhs_case)
    # has_key_ex_payload(rhs_case)
    # return cmp((lhs_payload, lhs_case), (rhs_payload, rhs_case))
    r = cmp(total_key_ops, lhs_payload, rhs_payload)
    if r == EQ:
        #return cmp(python_total_key_ops, lhs_case, rhs_case)
        # Enum has no __lt__
        return cmp(python_total_key_ops, lhs_case.value, rhs_case.value)
    return r

def ltKeyEx(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<Key>
    # lhs, rhs :: KeyEx
    #
    return cmpKeyEx(total_key_ops, lhs, rhs) == LT
def leKeyEx(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<Key>
    # lhs, rhs :: KeyEx
    #
    return not ltKeyEx(total_key_ops, rhs, lhs)
    return cmpKeyEx(total_key_ops, lhs, rhs) != GT

def eqKeyEx(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<Key>
    # lhs, rhs :: KeyEx
    #
    lhs_case, lhs_payload = lhs
    rhs_case, rhs_payload = rhs
    return lhs_case == rhs_case and total_key_ops.eq(lhs_payload, rhs_payload)


def cmpRange(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<key>
    # lhs, rhs :: Range
    #
    lhs_left_bound, lhs_right_bound = lhs
    rhs_left_bound, rhs_right_bound = rhs

    r = cmpKeyEx(total_key_ops, lhs_left_bound, rhs_left_bound)
    if r == LT: return LT
    if r == GT: return GT

    # r == EQ
    return cmpKeyEx(total_key_ops, lhs_right_bound, rhs_right_bound)

def eqRange(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<key>
    # lhs, rhs :: Range
    #
    lhs_left_bound, lhs_right_bound = lhs
    rhs_left_bound, rhs_right_bound = rhs
    return all(map(eqKeyEx, [total_key_ops, total_key_ops], lhs, rhs))


def not_strict_range_before(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<key>
    # lhs, rhs :: Range
    #
    # a range before another, to mean is_sorted
    # not strict: (<=)
    #   =[def]= lift leKeyEx (lhs.left_bound, lhs.right_bound) (rhs.left_bound, rhs.right_bound)
    #
    return GT != cmpRange(total_key_ops, lhs, rhs)

def isEmptyRange(total_key_ops, rng):
    # total_key_ops :: ITotalOrderingOps<key>
    # lhs, rhs :: Range
    #
    left_bound, right_bound = rng
    # bug???: return ops.leKeyEx(left_bound, right_bound)
    return not leKeyEx(total_key_ops, left_bound, right_bound)
def insideRange(total_key_ops, lhs, rhs):
    # total_key_ops :: ITotalOrderingOps<key>
    # lhs, rhs :: Range
    #
    assert not isEmptyRange(total_key_ops, lhs)

    lhs_left_bound, lhs_right_bound = lhs
    rhs_left_bound, rhs_right_bound = rhs
    return (leKeyEx(total_key_ops, rhs_left_bound, lhs_left_bound)
        and leKeyEx(total_key_ops, lhs_right_bound, rhs_right_bound)
        )
    # bug: should be leKeyEx instead of ltKeyEx
    return (ltKeyEx(total_key_ops, rhs_left_bound, lhs_left_bound)
        and ltKeyEx(total_key_ops, lhs_right_bound, rhs_right_bound)
        )



def is_pair(x):
    return type(x) is tuple and len(x) == 2

class IBlockDictKeyOps(ABC):
    '''

take care of Key and KeyEx
    key :: Key
    getTheMinKeyEx :: ops -> KeyEx

    key is tree_key not dict_key
        # see: IBlockDict

key :: Ord Key => Key
KeyEx = (KeyExCase, payload)
    payload :: Key if case = TheKey | VirtualMoreKey | VirtualLessKey
    payload is None if case = VirtualMoreMinKeyEx | VirtualLessMaxKeyEx




assume range is both-side-closed range
    i.e. [a,b] not [a,b), (a,b], (a,b)
    Virtual... ==>> "()" # left-open / right-open
    TheKey ==>> "[]" # left-close / right-close
assume (the_min_key_ex, the_max_key_ex) is not empty
    # assume range=[getTheMinKeyEx(), getTheMaxKeyEx()] is not empty


to distinguish Key and KeyEx:
    'getTheMinKeyEx' instead of 'get_min_key' or 'get_min_key_ex'
    'isKeyEx' instead of 'is_key_ex'
    'mkRange' instead of 'mk_range'
    'isRange' instead of 'is_range'
    'isEmptyRange' instead of 'is_empty_range'


see:
    OtherOps.ITotalOrderingOps
    OtherOps.TotalOrderingOps
    OtherOps.TotalOrderingOps.python_total_key_ops

example:
    theUInt_as_BlockDictKeyOps
    theInt_as_BlockDictKeyOps
    theFraction_as_BlockDictKeyOps

    >>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
    >>> from ..BlockDictOps__concrete.theInt_as_BlockDictKeyOps import theInt_as_BlockDictKeyOps
    >>> from ..BlockDictOps__concrete.theFraction_as_BlockDictKeyOps import theFraction_as_BlockDictKeyOps
'''
    __slots__ = ()


    @abstractmethod
    def _get_total_key_ops_(ops):
        # -> ITotalOrderingOps
        return python_total_key_ops
    def get_total_key_ops(ops):
        total_key_ops = ops._get_total_key_ops_()
        assert isinstance(total_key_ops, ITotalOrderingOps)
        return total_key_ops

    def make_total_left_bound_ops(ops):
        # use left_bound/lkey_ex/left_key_ex as tree_key
        return TotalOrderingOps(ops.leKeyEx, ops.eqKeyEx)

    def isKeyEx(ops, kx):
        if not is_pair(kx): return False
        case, payload = kx
        if not ops.is_key_ex_case(case): return False
        if has_key_ex_payload(case):
            return ops.is_key(payload)
        else:
            return payload is None

    @abstractmethod
    def is_key_ex_case(ops, case):
        # normally, the concrete subclass doesnot use all KeyExCase instances
        #   so, we can refine the method
        return type(case) is KeyExCase

    @not_implemented
    def is_key(ops, key):
        pass
    @not_implemented
    def getTheMinKeyEx(ops):
        # () -> KeyEx
        pass
    @not_implemented
    def getTheMaxKeyEx(ops):
        # () -> KeyEx
        pass


    @not_implemented
    def mkMore(ops, key):
        # Key -> KeyEx
        assert ops.key_ltTheMaxKeyEx(key)
        pass
    @not_implemented
    def mkLess(ops, key):
        # Key -> KeyEx
        assert ops.key_gtTheMinKeyEx(key)
        pass

    @not_implemented
    def key_gtTheMinKeyEx(ops, key):
        # cmp Key with KeyEx
        # cmp (TheKey key) with TheMinKeyEx
        pass
    @not_implemented
    def key_ltTheMaxKeyEx(ops, key):
        # cmp Key with KeyEx
        # cmp (TheKey key) with TheMaxKeyEx
        pass


    def getWholeRange(ops):
        return ops.mkRange(ops.getTheMinKeyEx(), ops.getTheMaxKeyEx())
    def isTheMinKeyEx(ops, key_ex):
        return ops.eqKeyEx(ops.getTheMinKeyEx(), key_ex)
    def isTheMaxKeyEx(ops, key_ex):
        return ops.eqKeyEx(ops.getTheMaxKeyEx(), key_ex)

    def left_bound2right_bound_less(ops, left_bound):
        # [a, ...) -> (..., a)
        # (a, ...) -> (..., a]
        if ops.isTheMinKeyEx(left_bound): raise ValueError('should not be TheMinKeyEx')

        key_ex_case, lkey = left_bound
        if key_ex_case == KeyExCase.TheKey:
            return ops.mkLess(lkey)
        elif key_ex_case == KeyExCase.VirtualMoreKey:
            return ops.mkTheKey(lkey)
        assert not ops.isLeftBound(left_bound)
        raise TypeError('not isLeftBound')
        raise logic-error
    def right_bound2left_bound_more(ops, right_bound):
        # (..., a] -> (a, ...)
        # (..., a) -> [a, ...)
        if ops.isTheMaxKeyEx(right_bound): raise ValueError('should not be TheMaxKeyEx')

        key_ex_case, rkey = right_bound
        if key_ex_case == KeyExCase.TheKey:
            return ops.mkMore(rkey)
        if key_ex_case == KeyExCase.VirtualLessKey:
            return ops.mkTheKey(rkey)
        assert not ops.isRightBound(right_bound)
        raise TypeError('not isRightBound')
        raise logic-error



    @property
    def total_key_ops(ops):
        return ops.get_total_key_ops()
    def ltKeyEx(ops, lhs, rhs):
        # call global ltKeyEx
        return ltKeyEx(ops.total_key_ops, lhs, rhs)
    def gtKeyEx(ops, lhs, rhs):
        return ops.ltKeyEx(rhs, lhs)
    def geKeyEx(ops, lhs, rhs):
        return not ops.ltKeyEx(lhs, rhs)
    def leKeyEx(ops, lhs, rhs):
        return not ops.ltKeyEx(rhs, lhs)

    def eqKeyEx(ops, lhs, rhs):
        # call global eqKeyEx
        return eqKeyEx(ops.total_key_ops, lhs, rhs)
    def neKeyEx(ops, lhs, rhs):
        return not ops.eqKeyEx(lhs, rhs)


    def cmpRange(ops, lhs, rhs):
        # -> -1/0/+1
        return cmpRange(ops.total_key_ops, lhs, rhs)
    def leRange(ops, lhs, rhs):
        # call global not_strict_range_before
        return not_strict_range_before(ops.total_key_ops, lhs, rhs)
    def eqRange(ops, lhs, rhs):
        # call global eqRange
        return eqRange(ops.total_key_ops, lhs, rhs)
    def neRange(ops, lhs, rhs):
        return not ops.eqRange(lhs, rhs)
    def geRange(ops, lhs, rhs):
        return ops.leRange(rhs, lhs)
    def gtRange(ops, lhs, rhs):
        return not ops.leRange(lhs, rhs)
    def ltRange(ops, lhs, rhs):
        return not ops.leRange(rhs, lhs)


    def subtract_two_touch_or_cross_ranges(ops, lhs, rhs):
        # NonEmptyRange -> NonEmptyRange -> [NonEmptyRange]
        # lhs and rhs are touch_or_cross
        # len(result) == 0|1|2
        (lhs_left_bound, lhs_right_bound) = lhs
        rhs_left_bound, rhs_right_bound = rhs

        may_empty_rngs = []
        if not ops.isTheMinKeyEx(rhs_left_bound):
            rng1 = lhs_left_bound, ops.left_bound2right_bound_less(rhs_left_bound)
            may_empty_rngs.append(rng1)
        if not ops.isTheMaxKeyEx(rhs_right_bound):
            rng2 = ops.right_bound2left_bound_more(rhs_right_bound), lhs_right_bound
            may_empty_rngs.append(rng2)
        rngs = [rng for rng in may_empty_rngs if not ops.isEmptyRange(rng)]
        return rngs



    def union_touch_or_cross_ranges1(ops, rng, *ranges):
        # return (min(left_bounds), max(right_bounds))
        # input must be nonempty ranges
        isEmptyRange = ops.isEmptyRange
        if isEmptyRange(rng) or any(map(isEmptyRange, ranges)): raise ValueError

        min_left_bound, max_right_bound = rng
        ltKeyEx = ops.ltKeyEx
        for left_bound, right_bound in ranges:
            if ltKeyEx(left_bound, min_left_bound):
                min_left_bound = left_bound
            if ltKeyEx(max_right_bound, right_bound):
                max_right_bound = right_bound
        return min_left_bound, max_right_bound


    def intersection_ranges1(ops, rng, *ranges):
        # return (max(left_bounds), min(right_bounds))
        # maybe empty range
        max_left_bound, min_right_bound = rng
        ltKeyEx = ops.ltKeyEx
        for left_bound, right_bound in ranges:
            if ltKeyEx(max_left_bound, left_bound):
                max_left_bound = left_bound
            if ltKeyEx(right_bound, min_right_bound):
                min_right_bound = right_bound
        return max_left_bound, min_right_bound

    def mkTheKey(ops, key):
        return (KeyExCase.TheKey, key)

    def isTheKey(ops, key_ex):
        case, _ = key_ex
        return case == KeyExCase.TheKey

    def insideRange(ops, lhs, rhs):
        return insideRange(ops.total_key_ops, lhs, rhs)
    def isEmptyRange(ops, rng):
        # assume (the_min_key_ex, the_max_key_ex) is not empty
        # assume range is both-side-closed range
        #   i.e. [a,b] not [a,b), (a,b], (a,b)
        return isEmptyRange(ops.total_key_ops, rng)
        left_bound, right_bound = rng
        # bug???: return ops.leKeyEx(left_bound, right_bound)
        return not ops.leKeyEx(left_bound, right_bound)
        return ops.ltKeyEx(right_bound, left_bound)

    def isRange(ops, rng):
        if not is_pair(rng): return False

        left_bound, right_bound = rng
        return (ops.isKeyEx(left_bound)
            and ops.isKeyEx(right_bound)
            and ops.isLeftBound(left_bound)
            and ops.isRightBound(right_bound)
            )

    def mkSingletonRange(ops, key):
        key_ex = ops.mkTheKey(key)
        return key_ex, key_ex
        return ops.mkRange(key_ex, key_ex)
    def mkRange(ops, left_bound, right_bound):
        assert ops.isKeyEx(left_bound)
        assert ops.isKeyEx(right_bound)

        assert ops.isLeftBound(left_bound)
        assert ops.isRightBound(right_bound)

        return (left_bound, right_bound)



    def cross(ops, right_bound, left_bound):
        # one_rng.right_bound cross another_rng.left_bound?
        rng = ops.mkRange(left_bound, right_bound)
        return not ops.isEmptyRange(rng)

        assert ops.isKeyEx(left_bound)
        assert ops.isKeyEx(right_bound)

        assert ops.isLeftBound(left_bound)
        assert ops.isRightBound(right_bound)
        return not ops.isEmptyRange((left_bound, right_bound))
        return ops.leKeyEx(left_bound, right_bound)
        if ops.isTheKey(right_bound):
            _, rkey = right_bound
            right_bound_more = ops.mkMore(rkey)
            return ops.ltKeyEx(left_bound, right_bound_more)
        if ops.isTheKey(left_bound):
            _, lkey = left_bound
            left_bound_less = ops.mkLess(lkey)
            return ops.ltKeyEx(left_bound_less, right_bound)
        return ops.ltKeyEx(left_bound, right_bound)



    def touch_or_cross(ops, right_bound, left_bound):
        # one_rng.right_bound touch or cross another_rng.left_bound?
        return (ops.cross(right_bound, left_bound)
                or ops.touch(right_bound, left_bound)
                )
    def touch(ops, right_bound, left_bound):
        # one_rng.right_bound touch another_rng.left_bound?
        assert ops.isKeyEx(left_bound)
        assert ops.isKeyEx(right_bound)

        assert ops.isLeftBound(left_bound)
        assert ops.isRightBound(right_bound)
        if ops.isTheKey(right_bound):
            _, rkey = right_bound
            right_bound_more = ops.mkMore(rkey)
            return ops.eqKeyEx(right_bound_more, left_bound)
        if ops.isTheKey(left_bound):
            _, lkey = left_bound
            left_bound_less = ops.mkLess(lkey)
            return ops.eqKeyEx(right_bound, left_bound_less)
        return False

    def isLeftBound(ops, key_ex):
        # assert ops.isKeyEx(key_ex)
        case, _ = key_ex
        return id(case) in left_case_ids
    def isRightBound(ops, key_ex):
        # assert ops.isKeyEx(key_ex)
        case, _ = key_ex
        return id(case) in right_case_ids
left_cases = (KeyExCase.TheKey, KeyExCase.VirtualMoreKey, KeyExCase.VirtualMoreMinKeyEx)
right_cases = (KeyExCase.TheKey, KeyExCase.VirtualLessKey, KeyExCase.VirtualLessMaxKeyEx)

left_case_ids = tuple(map(id, left_cases))
right_case_ids = tuple(map(id, right_cases))




if __name__ == '__main__':
    XXX = IBlockDictKeyOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)




if __name__ == "__main__":
    import doctest
    doctest.testmod()



