__all__ = '''
    is_uint_sequence
    '''.split()

from seed.verify.common_verify import (
    is_UInt, is_Sequence
    )

def is_uint_sequence(obj):
    return is_Sequence.of(obj, is_UInt)

