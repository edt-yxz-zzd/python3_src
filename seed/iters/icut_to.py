
'''

usage:
    def bits2vbytes(bits, padding_bits):
        assert padding_bits is None or len(padding_bits) == 7
        for bits in icut_to(bits):
            if len(bits) < 8:
                if padding_bits is None:
                    raise LenError('len(bits) % 8 != 0')
                bits.extend(padding_bits[:8-len(bits)])
            yield bits2vbyte(bits)
        
'''


__all__ = ['icut_to', 'icut_seq_to']
from itertools import islice
from collections import Sequence
from seed.helper.check_utils import to_pint

def icut_seq_to(seq, block_size, begin=None, end=None):
    block_size = to_pint(block_size, 'block_size')

    if begin is None:
        begin = 0
    if end is None:
        end = len(seq)
        
    for i in range(begin, end, block_size):
        yield seq[i:i+block_size]


def icut_to(iterable, block_size, may_use_container=None):
    if isinstance(iterable, Sequence):
        return icut_seq_to(iterable, block_size)
    return _icut_to(iterable, block_size, may_use_container)

def _icut_to(iterable, block_size, container):
    block_size = to_pint(block_size, 'block_size')
    if container is None:
        container = list
    
    it = iter(iterable)
    while True:
        c = container(islice(it, block_size))
        if not c:
            break
        yield c


    
