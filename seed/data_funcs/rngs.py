

'''
rngs = [rng]
rng = (begin:int, end:int)
begin < end
'''
import bisect

def all_map(pred, iterable):
    return all(map(pred, iterable))
def sorted_unique_ints_to_ranges(ints):
    return tuple(sorted_unique_ints_to_iter_ranges(ints))
def sorted_unique_ints_to_iter_ranges(ints):
    it = iter(ints)
    for begin in it:
        break
    else:
        return
    end = begin + 1

    for last in it:
        if last == end:
            end += 1
        elif last > end:
            yield begin, end
            begin = last
            end = begin + 1
        else:
            raise ValueError('not sorted_unique_ints: {} {}'.format(end-1, last))
    yield begin, end
    pass

assert sorted_unique_ints_to_ranges([0,1,3]) == ((0,2), (3,4))
assert sorted_unique_ints_to_ranges([0]) == ((0,1),)
assert sorted_unique_ints_to_ranges([]) == ()

def valid_range(range):
    if type(range) is not tuple:
        return False
    begin, end = range
    if not type(begin) is int is type(end):
        return False
    return begin < end
def check_range(rng):
    if not valid_range(rng):
        raise ValueError('not valid_range({})'.format(rng))


from operator import lt, le
def valid_nontouch_ranges(ranges):
    return _valid_ranges(ranges, lt)
def valid_touch_ranges(ranges):
    return _valid_ranges(ranges, le)
def _valid_ranges(ranges, lt):
    if type(ranges) is not tuple:
        return False
    if not all_map(valid_range, ranges):
        return False
    for i in range(len(ranges) - 1):
        a, b = ranges[i:i+2]
        if not lt(a[-1], b[0]):
            return False
    return True

def is_subrange_of(sub_rng, super_rng):
    check_range(sub_rng)
    check_range(super_rng)

    begin, end = sub_rng
    lower, upper = super_rng
    return lower <= begin and end <= upper
assert is_subrange_of((0,3), (0,3))
assert not is_subrange_of((0,3), (0,2))
assert not is_subrange_of((0,3), (1,3))
assert is_subrange_of((0,2), (0,3))

def make_NonTouchRanges(iterable):
    return NonTouchRanges(tuple(iterable))
def make_TouchRanges(iterable):
    return TouchRanges(tuple(iterable))
class Ranges:
    @classmethod
    def valid_ranges(cls, ranges):
        raise NotImplementedError
        return valid_ranges(ranges)
    def __init__(self, ranges):
        #ranges = tuple(ranges)
        if not type(self).valid_ranges(ranges):
            raise ValueError('not valid_ranges(ranges)')
        self.ranges = ranges
    def maybe_range_contained(self, i):
        # None | rng
        return self.maybe_range_contained_ex(i)[0]
    def maybe_range_contained_ex(self, i):
        rngs = self.ranges
        L = len(rngs)

        j = i + 1
        idx = bisect.bisect_left(rngs, (j,j)) - 1
        if idx < 0:
            assert not L or rngs[0][0] > i
            return None, idx

        begin, end = rng = rngs[idx]
        assert begin <= i
        if not i < end:
            assert idx + 1 == L or rngs[idx+1][0] > i
            return None, idx
        return rng, idx

    def __contains__(self, int_or_rng):
        if isinstance(int_or_rng, int):
            begin = int_or_rng
            end = begin + 1
            sub_rng = begin, end
        else:
            sub_rng = int_or_rng
        return self.contains_range(sub_rng)
    def contains_range(self, sub_rng):
        check_range(sub_rng)
        rngs = self.ranges
        begin, end = sub_rng
        may_rng, idx = self.maybe_range_contained_ex(begin)
        if may_rng is None:
            return False

        pre_end = may_rng[0]
        for idx in range(idx, len(rngs)):
            begin_, end_ = rngs[idx]
            if pre_end != begin_:
                return False
            pre_end = end_
            if end <= end_:
                return True
        assert end > rngs[-1][-1]
        return False
        #return is_subrange_of(sub_rng, may_rng)
        pass

    def contains_all(self, iterable):
        return all_map(self.__contains__, iterable)
    def __hash__(self):
        return hash(self.ranges)
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.ranges)

    def __bool__(self):
        return len(self.ranges)
    def gaps(self):
        return tuple(self.iter_gaps())
    def iter_gaps(self):
        rngs = self.ranges
        for pre_end, _ in rngs:
            break
        for begin, end in rngs:
            if begin != pre_end:
                yield pre_end, begin
            pre_end = end
class TouchRanges(Ranges):
    @classmethod
    def valid_ranges(cls, ranges):
        return valid_touch_ranges(ranges)
class NonTouchRanges(Ranges):
    @classmethod
    def valid_ranges(cls, ranges):
        return valid_nontouch_ranges(ranges)

assert make_NonTouchRanges([(0,2), (3,4), (5,7)]).contains_all([(0,1), 3, 6, (0,2), (6,7)])
assert 2 not in make_NonTouchRanges([(0,2), (3,4), (5,7)])
assert make_TouchRanges([(0,2), (3,4), (5,7)]).gaps() == ((2,3), (4,5),)

assert make_TouchRanges([(0,3), (3,4), (5,7)]).contains_all([(0,4), 3, 6, (0,2), (6,7),])
assert 4 not in make_TouchRanges([(0,3), (3,4), (5,7)])
assert make_TouchRanges([(0,3), (3,4), (5,7)]).gaps() == ((4,5),)


