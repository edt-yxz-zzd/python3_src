#__all__:goto
r'''[[[
e ../../python3_src/seed/math/is_prime__le_pow2_81.py
see:
    view ../../python3_src/seed/math/is_prime__le_pow2_64.py
    view ../../python3_src/seed/math/is_prime__le_pow2_81.py
    view ../../python3_src/seed/math/primality_test/strong_probable_prime.py

seed.math.is_prime__le_pow2_81
py -m nn_ns.app.debug_cmd   seed.math.is_prime__le_pow2_81 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.is_prime__le_pow2_81:__doc__ -ht # -ff -df

[[
>>> from seed.math.is_prime__le_pow2_81 import is_prime__le_pow2_81_
>>> from seed.math.is_prime__le_pow2_81 import is_prime__le_pow2_81 #to match is_prime__le_pow2_64
>>> from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64
>>> from math import *
>>> is_prime__le_pow2_81_.upperbound
3317044064679887385962123
>>> log(3317044064679887385962123, 10)
24.520751240865337
>>> 3*10**24 < 3317044064679887385962123 < 4*10**24
True
>>> log(3317044064679887385962123, 2)
81.45617245477473

]]



[[
===
echo $PATH
/data/data/com.termux/files/usr/bin/my_sh/:/data/data/com.termux/files/usr/bin
===
ls $my_git_sh/my_sh/ -1 | grep prim
filter4prime
is_prime
next_probable_prime
prev_probable_prime
===
for nm in $(ls $my_git_sh/my_sh/ -1 | grep prim) ; do which ${nm} ; done
/data/data/com.termux/files/usr/bin/my_sh/filter4prime
/data/data/com.termux/files/usr/bin/my_sh/is_prime
/data/data/com.termux/files/usr/bin/my_sh/next_probable_prime
/data/data/com.termux/files/usr/bin/my_sh/prev_probable_prime
===
for nm in $(ls $my_git_sh/my_sh/ -1 | grep prim) ; do cat $(which ${nm}) ; echo ; done
bash $my_git_sh/app/filter4prime "$@"
bash $my_git_sh/app/is_prime "$@"
bash $my_git_sh/app/next_probable_prime "$@"
bash $my_git_sh/app/prev_probable_prime "$@"
===
for nm in $(ls $my_git_sh/my_sh/ -1 | grep prim) ; do cat $my_git_sh/app/${nm} | grep '^[^#]' ; done
py -m nn_ns.app.filter4prime "$@"
py_adhoc_call   seed.math.primality_test.strong_probable_prime   @is_prime__le_pow2_81_  "$@"
py_adhoc_call   seed.math.primality_test.strong_probable_prime   @next_probable_prime__ge_  "$@"
py_adhoc_call   seed.math.primality_test.strong_probable_prime   @prev_may_probable_prime__lt_  "$@"
===
]]


py_adhoc_call   seed.math.is_prime__le_pow2_81   @is_prime__le_pow2_81  =17401
py_adhoc_call   seed.math.is_prime__le_pow2_81   @is_prime__le_pow2_81  =643879
py_adhoc_call   seed.math.is_prime__le_pow2_81   @is_prime__le_pow2_81  =648379


]]]'''#'''
__all__ = r'''
is_prime__le_pow2_81_
    is_prime__le_pow2_81
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...



from seed.math.primality_test.strong_probable_prime import is_prime__le_pow2_81_
assert is_prime__le_pow2_81_.upperbound == 3317044064679887385962123
is_prime__le_pow2_81 = is_prime__le_pow2_81_ #to match is_prime__le_pow2_64



__all__
from seed.math.is_prime__le_pow2_81 import is_prime__le_pow2_81
from seed.math.is_prime__le_pow2_81 import *
