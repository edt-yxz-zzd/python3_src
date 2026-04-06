
__all__ = '''
flag_eq
flag_le

get_flag
set_flag
clear_flag
flip_flag

'''.split()#'''

def flag_eq(state1, state2):
    return state1 == state2
def flag_le(state1, state2):
    return state1 == (state1 & state2)

def get_flag(state, flag):
    return state & flag

def set_flag(state, flag):
    return state | flag
def clear_flag(state, flag):
    return state ^ (state & flag)
    return state & ~flag
def flip_flag(state, flag):
    return state ^ flag

from seed.types.int_like_flag import flag_eq, flag_le

from seed.types.int_like_flag import get_flag, set_flag, clear_flag, flip_flag

from seed.types.int_like_flag import *
