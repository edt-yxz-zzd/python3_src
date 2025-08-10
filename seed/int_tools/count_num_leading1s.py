#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/count_num_leading1s.py

seed.int_tools.count_num_leading1s
py -m nn_ns.app.debug_cmd   seed.int_tools.count_num_leading1s -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.count_num_leading1s:__doc__ -ht # -ff -df

[[
]]

>>> for j in range(8):
...     count_num_leading1s_ex_(3,7,j)
(0, 2)
(0, 2)
(0, 2)
(0, 2)
(1, 1)
(1, 1)
(2, 0)
(3, -1)
>>> for j in range(8):
...     count_num_leading1s_(3,7,j)
0
0
0
0
1
1
2
3


>>> for j in range(8):
...     count_num_leading0s_ex_(3,j)
(3, -1)
(2, 0)
(1, 1)
(1, 1)
(0, 2)
(0, 2)
(0, 2)
(0, 2)
>>> for j in range(8):
...     count_num_leading0s_(3,j)
3
2
1
1
0
0
0
0


py_adhoc_call   seed.int_tools.count_num_leading1s   @count_num_leading1s_ =3 =7 =0
0
py_adhoc_call   seed.int_tools.count_num_leading1s   @count_num_leading1s_ =3 =7 =7
3

]]]'''#'''
__all__ = r'''
count_num_leading1s_
count_num_leading1s_ex_
count_num_leading0s_
count_num_leading0s_ex_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def count_num_leading1s_(num_bits4digit, max_digit, digit, /):
    'num_bits4digit/uint -> max_digit/uint{==2**num_bits4digit-1} -> digit/uint%2**num_bits4digit -> num_leading1s/uint%(1+num_bits4digit)'
    return count_num_leading1s_ex_(num_bits4digit, max_digit, digit)[0]
def count_num_leading1s_ex_(num_bits4digit, max_digit, digit, /):
    'num_bits4digit/uint -> max_digit/uint{==2**num_bits4digit-1} -> digit/uint%2**num_bits4digit -> (num_leading1s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading1s+1[#(maybe nonexist) the "0" bit#]+imay_num_bits4payload]'
    # [num_bits4digit==num_leading1s+1[#可能不存在的阴爻#]+imay_num_bits4payload]
    u = max_digit^digit
    return count_num_leading0s_ex_(num_bits4digit, u)
    #.u = max_digit^digit
    #.assert u >= 0
    #.n = u.bit_length()
    #.r = (num_leading1s, imay_num_bits4payload) = (num_bits4digit-n, n-1)
    #.assert num_leading1s >= 0
    #.assert imay_num_bits4payload >= -1
    #.return r

def count_num_leading0s_(num_bits4digit, digit, /):
    'num_bits4digit/uint -> digit/uint%2**num_bits4digit -> num_leading0s/uint%(1+num_bits4digit)'
    return count_num_leading0s_ex_(num_bits4digit, digit)[0]
def count_num_leading0s_ex_(num_bits4digit, digit, /):
    'num_bits4digit/uint -> digit/uint%2**num_bits4digit -> (num_leading0s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading0s+1[#(maybe nonexist) the "1" bit#]+imay_num_bits4payload]'
    #assert 0 <= digit <= max_digit
    assert 0 <= digit
    n = digit.bit_length()
    #assert 0 <= n <= num_bits4digit
    num_leading0s = num_bits4digit-n
    assert num_leading0s >= 0
    return (num_leading0s, n-1)
    #.r = (num_leading0s, imay_num_bits4payload) = (num_bits4digit-n, n-1)
    #.assert num_leading0s >= 0
    #.assert imay_num_bits4payload >= -1
    #.return r

if __name__ == "__main__":
    assert (0,2) == count_num_leading1s_ex_(3,7,0)
    assert (0,2) == count_num_leading1s_ex_(3,7,1)
    assert (0,2) == count_num_leading1s_ex_(3,7,2)
    assert (0,2) == count_num_leading1s_ex_(3,7,3)
    assert (1,1) == count_num_leading1s_ex_(3,7,4)
    assert (1,1) == count_num_leading1s_ex_(3,7,5)
    assert (2,0) == count_num_leading1s_ex_(3,7,6)
    assert (3,-1) == count_num_leading1s_ex_(3,7,7)


__all__
from seed.int_tools.count_num_leading1s import count_num_leading1s_, count_num_leading1s_ex_
    #(num_leading1s, imay_num_bits4payload) = count_num_leading1s_ex_(num_bits4digit, max_digit, digit)
from seed.int_tools.count_num_leading1s import count_num_leading0s_, count_num_leading0s_ex_
    #(num_leading0s, imay_num_bits4payload) = count_num_leading0s_ex_(num_bits4digit, digit)
from seed.int_tools.count_num_leading1s import *
