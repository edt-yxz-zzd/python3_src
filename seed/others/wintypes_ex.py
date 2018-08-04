
import ctypes
from ctypes.wintypes import LPVOID
from constant_nn.c_constant_ex import CHAR_BIT

sizeof_ULONG_PTR = ctypes.sizeof(LPVOID)
bit_len_of_ULONG_PTR = CHAR_BIT * sizeof_ULONG_PTR
ULONG_PTR = eval('ctypes.c_uint' + str(bit_len_of_ULONG_PTR))
#print(ctypes.c_long)
#strange!!

ULONG_PTR = ctypes.c_ulong
sizeof_ULONG_PTR = ctypes.sizeof(ULONG_PTR)
bit_len_of_ULONG_PTR = CHAR_BIT * sizeof_ULONG_PTR


del ctypes, LPVOID, CHAR_BIT

#ULONG_PTR = ctypes.c_void_p
