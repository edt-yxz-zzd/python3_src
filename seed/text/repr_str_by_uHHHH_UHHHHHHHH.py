
def repr_str_by_uHHHH_UHHHHHHHH(s, /):
    r = ''.join(fr'\u{u:0>4X}' if u < 0x1_00_00 else fr'\U{u:0>8X}' for u in map(ord, s))
    return f"'{r!s}'"


from seed.text.repr_str_by_uHHHH_UHHHHHHHH import repr_str_by_uHHHH_UHHHHHHHH
from seed.text.repr_str_by_uHHHH_UHHHHHHHH import *
