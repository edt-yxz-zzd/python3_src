#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/machine_word.py

py -m seed.lang.machine_word
py -m nn_ns.app.debug_cmd   seed.lang.machine_word -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.lang.machine_word:__doc__ -ht # -ff -df

[[
sizeof(int)
]]

why mismatch?
    * 64bit <<==:
        platform.machine()
        sys.hash_info
    * 32bit <<==:
        ctypes.sizeof(ctypes.c_int)
        sys.int_info

>>> import platform
>>> platform.machine()
'aarch64'

>>> import ctypes
>>> ctypes.c_int
<class 'ctypes.c_int'>
>>> ctypes.sizeof(ctypes.c_int)
4
>>> ctypes.sizeof(ctypes.c_int(0))
4
>>> ctypes.sizeof(ctypes.c_int16)
2
>>> ctypes.sizeof(ctypes.c_int16(0))
2
>>> ctypes.sizeof(ctypes.c_int32)
4
>>> ctypes.sizeof(ctypes.c_int32(0))
4
>>> ctypes.sizeof(ctypes.c_int64)
8
>>> ctypes.sizeof(ctypes.c_int64(0))
8

>>> import sys
>>> sys.int_info
sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
>>> sys.hash_info
sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='fnv', hash_bits=64, seed_bits=128, cutoff=0)

py_adhoc_call   seed.lang.machine_word   @f
from seed.lang.machine_word import *
]]]'''#'''
__all__ = r'''
NUM_BYTES4WORD
NUM_BITS4WORD
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import ctypes
___end_mark_of_excluded_global_names__0___ = ...

NUM_BYTES4WORD = ctypes.sizeof(ctypes.c_int)
NUM_BITS4WORD = 8*NUM_BYTES4WORD

def _main():
    for nm in __all__:
        x = globals()[nm]
        print(f'{nm!s} = {x!r}')
if __name__ == "__main__":
    _main()


__all__
from seed.lang.machine_word import *
