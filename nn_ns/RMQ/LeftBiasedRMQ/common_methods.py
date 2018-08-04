
__all__ = '''
    floor_log2
    ceil_log2
    ceil_div
    calc_num_blocks
    is_sorted
    '''.split()

from seed.iters.is_sorted import is_sorted
from seed.math.floor_ceil import floor_log2, ceil_log2, ceil_div

def calc_num_blocks(array_length, block_size):
    '''calc_num_blocks array_length block_size = ceil(array_length/block_size)

def num_normal_blocks = calc_num_blocks(p, complete_normal_block_size)
def num_super_blocks = calc_num_blocks(p, complete_super_block_size)

example:
    >>> calc_num_blocks(0, 1)
    0
    >>> calc_num_blocks(0, 2)
    0
    >>> calc_num_blocks(1, 1)
    1
    >>> calc_num_blocks(1, 2)
    1
    >>> calc_num_blocks(2, 1)
    2
    >>> calc_num_blocks(2, 2)
    1
    >>> calc_num_blocks(2, 3)
    1
    >>> calc_num_blocks(3, 1)
    3
    >>> calc_num_blocks(3, 2)
    2
    >>> calc_num_blocks(3, 3)
    1
    >>> calc_num_blocks(3, 4)
    1
    >>> calc_num_blocks(3, 5)
    1
    >>> calc_num_blocks(3, 6)
    1
'''
    assert array_length >= 0
    assert block_size > 0
    return ceil_div(array_length, block_size)
    return (array_length+block_size-1) // block_size



if __name__ == "__main__":
    import doctest
    doctest.testmod()

