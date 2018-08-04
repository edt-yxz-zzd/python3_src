

__all__ = '''
    BytesTV StrTV
    Bytes Byte0s Byte1s
    Str Char0s Char1s
    '''.split()
from .TypeVerifier import TypeVerifier
from .IntRange import UIntRange

class BytesTV(TypeVerifier):
    def __init__(self, min_len = 0, max_len = None):
        self.size_range = UIntRange(min_len, max_len)

    def is_singletonTV(self):
        return self.size_range.may_max == 0
    def get_construct_info(self):
        rng = self.size_range
        return self.make_args_kwargs(*rng.get_args())
    def get_TypeSpec(self):
        rng = self.size_range
        return 'Bytes{}'.format(rng.range_spec)

    def get_TypeName(self):
        rng = self.size_range
        return 'Bytes{{{}<=len(.)<={}}}'.format(*rng.get_args())
    def has_instance(self, obj):
        return type(obj) == bytes and self.size_range.valid(len(obj))
    def iter_examples(self):
        rng = self.size_range
        m = rng.min
        prefix = b'\0'*m
        ls = [prefix, prefix + b'-', prefix + b'\0', prefix + b'1a,)\0\3']
        return (bs for bs in ls if rng.valid(len(bs)))

    def __hash__(self):
        return hash((__class__, self.size_range))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.size_range == other.size_range
Bytes = Byte0s = BytesTV()
Byte1s = BytesTV(1)



class StrTV(TypeVerifier):
    def __init__(self, min_len = 0, max_len = None):
        self.size_range = UIntRange(min_len, max_len)
    def is_singletonTV(self):
        return self.size_range.may_max == 0

    def get_construct_info(self):
        rng = self.size_range
        return self.make_args_kwargs(*rng.get_args())
    def get_TypeSpec(self):
        rng = self.size_range
        return 'Str{}'.format(rng.range_spec)


    def get_TypeName(self):
        rng = self.size_range
        return 'Str{{{}<=len(.)<={}}}'.format(*rng.get_args())
    def has_instance(self, obj):
        return type(obj) == str and self.size_range.valid(len(obj))
    def iter_examples(self):
        rng = self.size_range
        m = rng.min
        prefix = '\0'*m
        ls = [prefix, prefix + '一', prefix + '\0', prefix + '1a,)\0\3一']
        return (bs for bs in ls if rng.valid(len(bs)))

    def __hash__(self):
        return hash((__class__, self.size_range))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.size_range == other.size_range
Str = Char0s = StrTV()
Char1s = StrTV(1)


