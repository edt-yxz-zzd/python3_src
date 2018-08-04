

__all__ = 'UIntRange IntRange'.split()


def is_uint(obj):
    return type(obj) is int and obj >= 0
def is_may_uint(obj):
    return obj is None or is_uint(obj)
def is_int(obj):
    return type(obj) is int
def is_may_int(obj):
    return obj is None or is_int(obj)
def may_int_add_int(may_int, offset):
    if may_int is None:
        return None
    return may_int + offset
def int_sub_may_int(center, may_int):
    if may_int is None:
        return None
    return center - may_int

pos_inf = float('inf')
neg_inf = float('-inf')
def pos_inf_int2may_int(pos_inf_int):
    return None if pos_inf_int == pos_inf else pos_inf_int
def neg_inf_int2may_int(neg_inf_int):
    return None if neg_inf_int == neg_inf else neg_inf_int
def may_neg_inf2pair(may_neg_inf):
    # (may_int, neg_inf_int)
    if may_neg_inf is None or may_neg_inf == neg_inf:
        return (None, neg_inf)
    i = may_neg_inf
    assert is_int(i)
    return (i, i)
def may_pos_inf2pair(may_pos_inf):
    # (may_int, pos_inf_int)
    if may_pos_inf is None or may_pos_inf == pos_inf:
        return (None, pos_inf)
    i = may_pos_inf
    assert is_int(i)
    return (i, i)

class UIntRange:
    'min <= u <= may_max'
    def __init__(self, min=0, may_max=None):
        assert is_uint(min), TypeError
        assert is_may_uint(may_max), TypeError
        assert may_max is None or may_max >= min, ValueError
        self.min = min
        self.may_max, self.inf_max = may_pos_inf2pair(may_max)
        self.range_spec = self.__range_spec()
    def is_singleton_range(self):
        return self.may_max == self.min
    def get_inf_range_size(self):
        return self.inf_max - self.min
    def get_may_range_size(self):
        return pos_inf_int2may_int(self.get_inf_range_size())
    def valid(self, L):
        return is_int(L) and self.min <= L <= self.inf_max
    def get_args(self):
        return self.min, self.may_max

    def __range_spec(self):
        M = self.may_max
        m = self.min
        if M is None:
            fmt = '{m}..'
        elif m == M:
            fmt = '{m}'
        else:
            fmt = '{m}..{M}'

        mid = fmt.format(m=m, M=M)
        return '{'+mid+'}'

    def __ne__(self, other):
        return not (self == other)
    def __eq__(self, other):
        return type(other) == __class__ and \
            self.get_args() == other.get_args()
    def __hash__(self):
        return hash((__class__, self.get_args()))
    def __repr__(self):
        return 'UIntRange({}, {})'.format(*self.get_args())


class IntRange:
    'may_min <= u <= may_max'
    def __init__(self, may_min=None, may_max=None):
        assert is_may_int(may_min), TypeError
        assert is_may_int(may_max), TypeError
        assert may_max is None or may_min is None or may_max >= may_min, ValueError
        self.may_min, self.inf_min = may_neg_inf2pair(may_min)
        self.may_max, self.inf_max = may_pos_inf2pair(may_max)
        self.range_spec = self.__range_spec()

    def is_singleton_range(self):
        return self.inf_max == self.inf_min
    def shift_range(self, offset):
        assert type(offset) is int
        may_min = may_int_add_int(self.may_min, offset)
        may_max = may_int_add_int(self.may_max, offset)
        return __class__(may_min, may_max)
    def mirror_range(self, center):
        assert type(center) is int
        may_min = int_sub_may_int(center, self.may_max)
        may_max = int_sub_may_int(center, self.may_min)
        return __class__(may_min, may_max)
    def get_inf_range_size(self):
        return self.inf_max - self.inf_min
    def get_may_range_size(self):
        return pos_inf_int2may_int(self.get_inf_range_size())
    def valid(self, L):
        return is_int(L) and self.inf_min <= L <= self.inf_max
    def get_args(self):
        return self.may_min, self.may_max

    def __range_spec(self):
        M = self.may_max
        m = self.may_min
        if m == M:
            if m is None:
                fmt = '..'
            else:
                fmt = '{m}'
        elif M is None:
            fmt = '{m}..'
        elif m is None:
            fmt = '..{M}'
        else:
            fmt = '{m}..{M}'

        mid = fmt.format(m=m, M=M)
        return '{'+mid+'}'

    def __ne__(self, other):
        return not (self == other)
    def __eq__(self, other):
        return type(other) == __class__ and \
            self.get_args() == other.get_args()
    def __hash__(self):
        return hash((__class__, self.get_args()))
    def __repr__(self):
        return 'IntRange({}, {})'.format(*self.get_args())


