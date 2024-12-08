#__all__:goto
r'''[[[
e ../../python3_src/seed/math/combination__stated.py
prev:
view ../../python3_src/seed/math/combination.py
later:
view ../../python3_src/seed/for_libs/for_itertools.py
view ../../python3_src/seed/math/combination__stated__radix_repr_uint.py

[[
源起:作为进制数避免零开头:
    view script/搜索冫无重复十进制位数字型素数乊位数.py

NOTE:
    kw:avoid_leading_zero@(product_|permutations_|combinations_|combinations_with_replacement_|combinations__descending_|combinations_with_replacement__descending_)
    iterator.tell()&iterator.seek()
]]


seed.math.combination__stated
py -m nn_ns.app.debug_cmd   seed.math.combination__stated -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.combination__stated:__doc__ -ht # -ff -df


[[

>>> def list_show_(it, /):
...     assert iter(it) is it
...     for x in it:print(x)

>>> list_show_(permutations_(4, 3))
(0, 1, 2)
(0, 1, 3)
(0, 2, 1)
(0, 2, 3)
(0, 3, 1)
(0, 3, 2)
(1, 0, 2)
(1, 0, 3)
(1, 2, 0)
(1, 2, 3)
(1, 3, 0)
(1, 3, 2)
(2, 0, 1)
(2, 0, 3)
(2, 1, 0)
(2, 1, 3)
(2, 3, 0)
(2, 3, 1)
(3, 0, 1)
(3, 0, 2)
(3, 1, 0)
(3, 1, 2)
(3, 2, 0)
(3, 2, 1)
>>> list_show_(permutations_(4, 3, avoid_leading_zero=True))
(1, 0, 2)
(1, 0, 3)
(1, 2, 0)
(1, 2, 3)
(1, 3, 0)
(1, 3, 2)
(2, 0, 1)
(2, 0, 3)
(2, 1, 0)
(2, 1, 3)
(2, 3, 0)
(2, 3, 1)
(3, 0, 1)
(3, 0, 2)
(3, 1, 0)
(3, 1, 2)
(3, 2, 0)
(3, 2, 1)


>>> list_show_(combinations_(4, 3))
(0, 1, 2)
(0, 1, 3)
(0, 2, 3)
(1, 2, 3)

>>> list_show_(combinations_(4, 3, avoid_leading_zero=True))
(1, 2, 3)

>>> list_show_(combinations_with_replacement_(4, 3))
(0, 0, 0)
(0, 0, 1)
(0, 0, 2)
(0, 0, 3)
(0, 1, 1)
(0, 1, 2)
(0, 1, 3)
(0, 2, 2)
(0, 2, 3)
(0, 3, 3)
(1, 1, 1)
(1, 1, 2)
(1, 1, 3)
(1, 2, 2)
(1, 2, 3)
(1, 3, 3)
(2, 2, 2)
(2, 2, 3)
(2, 3, 3)
(3, 3, 3)

>>> list_show_(combinations_with_replacement_(4, 3, avoid_leading_zero=True))
(1, 1, 1)
(1, 1, 2)
(1, 1, 3)
(1, 2, 2)
(1, 2, 3)
(1, 3, 3)
(2, 2, 2)
(2, 2, 3)
(2, 3, 3)
(3, 3, 3)

>>> list_show_(product_(3, repeat=2))
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)

>>> list_show_(product_(3, repeat=2, avoid_leading_zero=True))
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)

>>> list_show_(product_(3))
(0,)
(1,)
(2,)
>>> list_show_(product_(3, avoid_leading_zero=True))
(1,)
(2,)

>>> list_show_(product_(3, 2))
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
>>> list_show_(product_(3, 2, avoid_leading_zero=True))
(1, 0)
(1, 1)
(2, 0)
(2, 1)

>>> list_show_(product_(3, 2, repeat=2))
(0, 0, 0, 0)
(0, 0, 0, 1)
(0, 0, 1, 0)
(0, 0, 1, 1)
(0, 0, 2, 0)
(0, 0, 2, 1)
(0, 1, 0, 0)
(0, 1, 0, 1)
(0, 1, 1, 0)
(0, 1, 1, 1)
(0, 1, 2, 0)
(0, 1, 2, 1)
(1, 0, 0, 0)
(1, 0, 0, 1)
(1, 0, 1, 0)
(1, 0, 1, 1)
(1, 0, 2, 0)
(1, 0, 2, 1)
(1, 1, 0, 0)
(1, 1, 0, 1)
(1, 1, 1, 0)
(1, 1, 1, 1)
(1, 1, 2, 0)
(1, 1, 2, 1)
(2, 0, 0, 0)
(2, 0, 0, 1)
(2, 0, 1, 0)
(2, 0, 1, 1)
(2, 0, 2, 0)
(2, 0, 2, 1)
(2, 1, 0, 0)
(2, 1, 0, 1)
(2, 1, 1, 0)
(2, 1, 1, 1)
(2, 1, 2, 0)
(2, 1, 2, 1)
>>> list_show_(product_(3, 2, repeat=2, avoid_leading_zero=True))
(1, 0, 0, 0)
(1, 0, 0, 1)
(1, 0, 1, 0)
(1, 0, 1, 1)
(1, 0, 2, 0)
(1, 0, 2, 1)
(1, 1, 0, 0)
(1, 1, 0, 1)
(1, 1, 1, 0)
(1, 1, 1, 1)
(1, 1, 2, 0)
(1, 1, 2, 1)
(2, 0, 0, 0)
(2, 0, 0, 1)
(2, 0, 1, 0)
(2, 0, 1, 1)
(2, 0, 2, 0)
(2, 0, 2, 1)
(2, 1, 0, 0)
(2, 1, 0, 1)
(2, 1, 1, 0)
(2, 1, 1, 1)
(2, 1, 2, 0)
(2, 1, 2, 1)


>>> def not_leading_zero_(us, /):
...     return not (us and us[0] == 0)
>>> def check_avoid_leading_zero_(f, /, *args, **kwds):
...     it0 = f(*args, avoid_leading_zero=False, **kwds)
...     it1 = f(*args, avoid_leading_zero=True, **kwds)
...     it2 = filter(not_leading_zero_, it0)
...     assert [*it1] == [*it2]
>>> def check_tell_seek_(f, /, *args, **kwds):
...     it = f(*args, **kwds)
...     st = it.tell()
...     ls0 = [*it]
...     assert not [*it]
...     it.seek(st)
...     ls1 = [*it]
...     assert not [*it]
...     it.seek(st)
...     ls2 = [*it]
...     assert not [*it]
...     assert ls1 == ls0
...     assert ls2 == ls0

>>> def check_cmp_std_(std_f, f, radixes, /, *args, ascending_vs_descending, **kwds):
...     it0 = f(*radixes, *args, avoid_leading_zero=False, **kwds)
...     it1 = std_f(*map(range, radixes), *args, **kwds)
...     if ascending_vs_descending:
...         it1 = sorted(us[::-1] for us in it1)
...     assert [*it1] == [*it0]
>>> def check_cmp_std_ex_(std_f, f, radixes, /, *args, ascending_vs_descending, **kwds):
...     check_cmp_std_(std_f, f, radixes, *args, ascending_vs_descending=ascending_vs_descending, **kwds)
...     check_avoid_leading_zero_(f, *radixes, *args, **kwds)
...     check_tell_seek_(f, *radixes, *args, avoid_leading_zero=False, **kwds)
...     check_tell_seek_(f, *radixes, *args, avoid_leading_zero=True, **kwds)
>>> def check_cmp_std_ex__via_std_name_(std_nm4f, radixes, /, *args, **kwds):
...     std_f = globals()[std_nm4f]
...     f_ = globals()[f'{std_nm4f}_']
...     check_cmp_std_ex_(std_f, f_, radixes, *args, ascending_vs_descending=False, **kwds)
...     if std_nm4f.startswith('combinations'):
...         f__descending_ = globals()[f'{std_nm4f}__descending_']
...         check_cmp_std_ex_(std_f, f__descending_, radixes, *args, ascending_vs_descending=True, **kwds)

>>> from itertools import product, permutations, combinations, combinations_with_replacement

######################
>>> check_cmp_std_ex__via_std_name_('product', [4,3], repeat=2)

######################
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 0)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 1)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 2)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 3)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 4)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 5)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 6)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 7)
>>> check_cmp_std_ex__via_std_name_('permutations', [7], 8)

######################
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 0)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 1)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 2)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 3)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 4)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 5)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 6)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 7)
>>> check_cmp_std_ex__via_std_name_('combinations', [7], 8)

######################
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 0)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 1)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 2)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 3)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 4)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 5)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 6)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 7)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [7], 8)


######################
######################
######################
>>> check_cmp_std_ex__via_std_name_('permutations', [0], 0)
>>> check_cmp_std_ex__via_std_name_('permutations', [0], 1)
>>> check_cmp_std_ex__via_std_name_('permutations', [1], 0)
>>> check_cmp_std_ex__via_std_name_('permutations', [1], 1)
>>> check_cmp_std_ex__via_std_name_('permutations', [1], 2)
>>> check_cmp_std_ex__via_std_name_('permutations', [2], 0)
>>> check_cmp_std_ex__via_std_name_('permutations', [2], 1)
>>> check_cmp_std_ex__via_std_name_('permutations', [2], 2)
>>> check_cmp_std_ex__via_std_name_('permutations', [2], 3)
>>> check_cmp_std_ex__via_std_name_('permutations', [3], 0)
>>> check_cmp_std_ex__via_std_name_('permutations', [3], 1)
>>> check_cmp_std_ex__via_std_name_('permutations', [3], 2)
>>> check_cmp_std_ex__via_std_name_('permutations', [3], 3)
>>> check_cmp_std_ex__via_std_name_('permutations', [3], 4)

######################
>>> check_cmp_std_ex__via_std_name_('combinations', [0], 0)
>>> check_cmp_std_ex__via_std_name_('combinations', [0], 1)
>>> check_cmp_std_ex__via_std_name_('combinations', [1], 0)
>>> check_cmp_std_ex__via_std_name_('combinations', [1], 1)
>>> check_cmp_std_ex__via_std_name_('combinations', [1], 2)
>>> check_cmp_std_ex__via_std_name_('combinations', [2], 0)
>>> check_cmp_std_ex__via_std_name_('combinations', [2], 1)
>>> check_cmp_std_ex__via_std_name_('combinations', [2], 2)
>>> check_cmp_std_ex__via_std_name_('combinations', [2], 3)
>>> check_cmp_std_ex__via_std_name_('combinations', [3], 0)
>>> check_cmp_std_ex__via_std_name_('combinations', [3], 1)
>>> check_cmp_std_ex__via_std_name_('combinations', [3], 2)
>>> check_cmp_std_ex__via_std_name_('combinations', [3], 3)
>>> check_cmp_std_ex__via_std_name_('combinations', [3], 4)

######################
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [0], 0)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [0], 1)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [1], 0)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [1], 1)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [1], 2)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [2], 0)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [2], 1)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [2], 2)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [2], 3)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [3], 0)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [3], 1)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [3], 2)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [3], 3)
>>> check_cmp_std_ex__via_std_name_('combinations_with_replacement', [3], 4)


######################
######################
######################
>>> def show_(it, /):
...     print(it)
...     print(it.tell())

######################
>>> show_(product_(1,3,4, repeat=3))
ProductIterator(Mutable_st4prod((1, 3, 4, 1, 3, 4, 1, 3, 4), [0, 0, 0, 0, 0, 0, 0, 0, 0]))
((1, 3, 4, 1, 3, 4, 1, 3, 4), (0, 0, 0, 0, 0, 0, 0, 0, 0))
>>> show_(product_(1,3,4, repeat=3, avoid_leading_zero=True))
ProductIterator(None)
False

######################
>>> show_(permutations_(1, 1))
PermutationIterator(SinglyLinkedList4idx([0], [-1, -1]))
((0,), (-1, -1))
>>> show_(permutations_(1, 1, avoid_leading_zero=True))
PermutationIterator(None)
False
>>> show_(permutations_(7, 7))
PermutationIterator(SinglyLinkedList4idx([0, 1, 2, 3, 4, 5, 6], [-1, -1, -1, -1, -1, -1, -1, -1]))
((0, 1, 2, 3, 4, 5, 6), (-1, -1, -1, -1, -1, -1, -1, -1))
>>> show_(permutations_(7, 7, avoid_leading_zero=True))
PermutationIterator(SinglyLinkedList4idx([1, 0, 2, 3, 4, 5, 6], [-1, 0, -1, -1, -1, -1, -1, -1]))
((1, 0, 2, 3, 4, 5, 6), (-1, 0, -1, -1, -1, -1, -1, -1))
>>> show_(permutations_(7, 8))
PermutationIterator(None)
False
>>> show_(permutations_(7, 4))
PermutationIterator(SinglyLinkedList4idx([0, 1, 2, 3], [-1, -1, -1, -1, 5, 6, -1, 4]))
((0, 1, 2, 3), (-1, -1, -1, -1, 5, 6, -1, 4))
>>> show_(permutations_(7, 4, avoid_leading_zero=True))
PermutationIterator(SinglyLinkedList4idx([1, 0, 2, 3], [-1, 0, -1, -1, 5, 6, -1, 4]))
((1, 0, 2, 3), (-1, 0, -1, -1, 5, 6, -1, 4))

######################
>>> show_(combinations_(1, 1))
CombinationIterator(Mutable_st4comb(1, [0]))
(1, (0,))
>>> show_(combinations_(1, 1, avoid_leading_zero=True))
CombinationIterator(None)
False
>>> show_(combinations_(7, 7))
CombinationIterator(Mutable_st4comb(7, [0, 1, 2, 3, 4, 5, 6]))
(7, (0, 1, 2, 3, 4, 5, 6))
>>> show_(combinations_(7, 7, avoid_leading_zero=True))
CombinationIterator(None)
False
>>> show_(combinations_(7, 8))
CombinationIterator(None)
False
>>> show_(combinations_(7, 4))
CombinationIterator(Mutable_st4comb(7, [0, 1, 2, 3]))
(7, (0, 1, 2, 3))
>>> show_(combinations_(7, 4, avoid_leading_zero=True))
CombinationIterator(Mutable_st4comb(7, [1, 2, 3, 4]))
(7, (1, 2, 3, 4))

######################
>>> show_(combinations_with_replacement_(1, 1))
CombinationIterator__with_replacement(Mutable_st4comb(1, [0]))
(1, (0,))
>>> show_(combinations_with_replacement_(1, 1, avoid_leading_zero=True))
CombinationIterator__with_replacement(None)
False
>>> show_(combinations_with_replacement_(7, 7))
CombinationIterator__with_replacement(Mutable_st4comb(7, [0, 0, 0, 0, 0, 0, 0]))
(7, (0, 0, 0, 0, 0, 0, 0))
>>> show_(combinations_with_replacement_(7, 7, avoid_leading_zero=True))
CombinationIterator__with_replacement(Mutable_st4comb(7, [1, 1, 1, 1, 1, 1, 1]))
(7, (1, 1, 1, 1, 1, 1, 1))
>>> show_(combinations_with_replacement_(7, 8))
CombinationIterator__with_replacement(Mutable_st4comb(7, [0, 0, 0, 0, 0, 0, 0, 0]))
(7, (0, 0, 0, 0, 0, 0, 0, 0))
>>> show_(combinations_with_replacement_(7, 4))
CombinationIterator__with_replacement(Mutable_st4comb(7, [0, 0, 0, 0]))
(7, (0, 0, 0, 0))
>>> show_(combinations_with_replacement_(7, 4, avoid_leading_zero=True))
CombinationIterator__with_replacement(Mutable_st4comb(7, [1, 1, 1, 1]))
(7, (1, 1, 1, 1))



######################
>>> show_(combinations__descending_(1, 1))
CombinationIterator__descending(Mutable_st4comb__descending(1, [0]))
(1, (0,))
>>> show_(combinations__descending_(1, 1, avoid_leading_zero=True))
CombinationIterator__descending(None)
False
>>> show_(combinations__descending_(7, 7))
CombinationIterator__descending(Mutable_st4comb__descending(7, [6, 5, 4, 3, 2, 1, 0]))
(7, (6, 5, 4, 3, 2, 1, 0))
>>> show_(combinations__descending_(7, 7, avoid_leading_zero=True))
CombinationIterator__descending(Mutable_st4comb__descending(7, [6, 5, 4, 3, 2, 1, 0]))
(7, (6, 5, 4, 3, 2, 1, 0))
>>> show_(combinations__descending_(7, 8))
CombinationIterator__descending(None)
False
>>> show_(combinations__descending_(7, 4))
CombinationIterator__descending(Mutable_st4comb__descending(7, [3, 2, 1, 0]))
(7, (3, 2, 1, 0))
>>> show_(combinations__descending_(7, 4, avoid_leading_zero=True))
CombinationIterator__descending(Mutable_st4comb__descending(7, [3, 2, 1, 0]))
(7, (3, 2, 1, 0))

######################
>>> show_(combinations_with_replacement__descending_(1, 1))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(1, [0]))
(1, (0,))
>>> show_(combinations_with_replacement__descending_(1, 1, avoid_leading_zero=True))
CombinationIterator__with_replacement__descending(None)
False
>>> show_(combinations_with_replacement__descending_(7, 7))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(7, [0, 0, 0, 0, 0, 0, 0]))
(7, (0, 0, 0, 0, 0, 0, 0))
>>> show_(combinations_with_replacement__descending_(7, 7, avoid_leading_zero=True))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(7, [1, 0, 0, 0, 0, 0, 0]))
(7, (1, 0, 0, 0, 0, 0, 0))
>>> show_(combinations_with_replacement__descending_(7, 8))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(7, [0, 0, 0, 0, 0, 0, 0, 0]))
(7, (0, 0, 0, 0, 0, 0, 0, 0))
>>> show_(combinations_with_replacement__descending_(7, 4))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(7, [0, 0, 0, 0]))
(7, (0, 0, 0, 0))
>>> show_(combinations_with_replacement__descending_(7, 4, avoid_leading_zero=True))
CombinationIterator__with_replacement__descending(Mutable_st4comb__descending(7, [1, 0, 0, 0]))
(7, (1, 0, 0, 0))





######################
######################

]]




py_adhoc_call   seed.math.combination__stated   @f
#]]]'''
__all__ = r'''
permutations_
product_    permutations_with_replacement_
combinations_
combinations_with_replacement_
combinations__descending_
combinations_with_replacement__descending_


PermutationIterator
ProductIterator     PermutationIterator__with_replacement
CombinationIterator
CombinationIterator__with_replacement
CombinationIterator__descending
CombinationIterator__with_replacement__descending











IBase4TellSeekState
    PermutationIterator
        next_ex4permutation_
        Mutable_st4perm    SinglyLinkedList4idx
    ProductIterator     PermutationIterator__with_replacement
        next_ex4product_
        Mutable_st4prod
    CombinationIterator
        next_ex4combination_
        Mutable_st4comb
    CombinationIterator__with_replacement
        next_ex4combination__with_replacement_
        Mutable_st4comb
    CombinationIterator__descending
        next_ex4combination__descending_
        Mutable_st4comb__descending
    CombinationIterator__with_replacement__descending
        next_ex4combination__with_replacement__descending_
        Mutable_st4comb__descending

SinglyLinkedList4idx
    mk_js4off_slist_
    validate_js4off_slist_
    pop_imay_jnext_
    put_back_last_j4off_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny_._Base4repr import _Base4repr
from seed.helper.repr_input import repr_helper

from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC
___end_mark_of_excluded_global_names__0___ = ...

######################
class IBase4TellSeekState(ABC):
    __slots__ = ()
    @abstractmethod
    def __getstate__(sf, /):
        '-> may st # [None=>skip __setstate__]'
    @abstractmethod
    def __setstate__(sf, st, /):
        'st{not None} -> None'

    @classmethod
    def mk5st_(cls, st, /):
        sf = object.__new__(cls)
        sf.seek(st)
        return sf
    def tell(sf, /):
        st = sf.__getstate__()
        return st
    def seek(sf, st, /):
        sf.__setstate__(st)
        return
class SinglyLinkedList4idx(IBase4TellSeekState, _Base4repr):
    r'''[[[
    #here is SinglyLinkedList<idx> over list{len=L+1}
    #   not:view ../../python3_src/seed/types/linked_list.py
    #
    [L :: uint]
    [idx <- [0..<L]]
    [slist :: [imay idx]{L+1}]

    [slist[-1] == imay_jhead]

    [-1 <= imay_j < L]:
        [[imay_j <~*~ slist] =[def]= [[imay_j == -1]or[?k. [[k <~*~ slist][imay_j == slist[k]]]]]]
        [[imay_j <~+~ slist] =[def]= [[imay_j =!= -1][imay_j <~*~ slist]]]

    [imay_j <~*~ slist]:
        [imay_jnext_(slist; imay_j) =[def]= [slist[imay_j]]]

    [0 <= j < L][not [j <~*~ slist]]:
        [imay_original_jprev_(slist; j) =[def]= [slist[j]]]
            #merely required by this module::(product_|permutations_|combinations_|combinations_with_replacement_|combinations__descending_|combinations_with_replacement__descending_)

    ==>>:
    [[imay_j <- [-1..<L]] -> [slist[imay_j] == (if [imay_j <~*~ slist] then imay_jnext_(slist; imay_j) else imay_original_jprev_(slist; imay_j))]]


    #]]]'''#'''
    ___no_slots_ok___ = True
    @override
    def __getstate__(sf, /):
        #bug:return sf._args4sy
        return (tuple(sf.js4off), tuple(sf.slist))
    @override
    def __setstate__(sf, st, /):
        ([*js4off], [*slist]) = st
        sf.__init__(js4off, slist)
    def __init__(sf, js4off, slist, /):
        check_type_is(list, js4off)
        check_type_is(list, slist)
        #sf.js4off = js4off
        #sf.slist = slist
        sf._args4sy = (js4off, slist)
        sf._reset4repr(sf._args4sy)
    @property
    def js4off(sf, /):
        return sf._args4sy[0]
    @property
    def slist(sf, /):
        return sf._args4sy[1]
    @property
    def L(sf, /):
        return len(sf.slist) - 1
    @property
    def sz4off(sf, /):
        return len(sf.js4off)

    @classmethod
    def mk5L_(cls, L, /):
        (js4off, slist) = mk_js4off_slist_(L)
        return cls(js4off, slist)
    def validate(sf, /):
        validate_js4off_slist_(*sf._args4sy)
    def pop_imay_jnext_(sf, imay_j, /):
        return pop_imay_jnext_(*sf._args4sy, imay_j)
    def put_back_last_j4off_(sf, /):
        return put_back_last_j4off_(*sf._args4sy)
######################
def mk_js4off_slist_(L, /):
    'L/uint -> (js4off, slist)/([uint%L]{len==0}, [imay uint%L]{len==L+1}) # == ([], [idx+1.., -1, 0]{len==L+1} if L > 0 else [-1])'
    check_int_ge(0, L)
    if L == 0:
        slist = [-1]
    else:
        slist = list(range(1, L+2))
        assert slist[-2:] == [L, L+1]
        slist[-1] = 0
        slist[L-1] = -1
        assert slist[-2:] == [-1, 0]
    slist
    assert 0 <= L == len(slist) - 1
    js4off = []
    return (js4off, slist)
def validate_js4off_slist_(js4off, slist, /):
    #assert len(slist) > 0
    assert len(js4off) < len(slist)
    (_js4off, _slist) = (js4off.copy(), slist.copy())
    ls = []
    while _js4off:
        imay_j = put_back_last_j4off_(_js4off, _slist)
        ls.append(imay_j)
    L = len(slist) - 1
    #check_int_ge(0, L)
    assert (_js4off, _slist) == mk_js4off_slist_(L)
    while ls:
        imay_j = ls.pop()
        imay_jnext = pop_imay_jnext_(_js4off, _slist, imay_j)
    assert (_js4off, _slist) == (js4off, slist)
def pop_imay_jnext_(js4off, slist, imay_j, /):
    '[imay_j <~*~ slist] => js4off -> slist -> imay_j -> imay_jnext # postcondition:[[imay_jnext =!= -1] -> [[not [jnext <~*~ slist]][slist[jnext] == imay_original_jprev_(slist; jnext) == imay_j][slist[imay_j] == imay_jnext_(slist; imay_j) == original jnextnext][js4off := [*js4off, jnext]]]]'
    assert -1 <= imay_j < len(slist) - 1 # == L
    imay_jnext = slist[imay_j]
    if not imay_jnext == -1:
        # to maintain: [[imay_j <- [-1..<L]] -> [slist[imay_j] == (if [imay_j <~*~ slist] then imay_jnext_(slist; imay_j) else imay_original_jprev_(slist; imay_j))]]
        # => [[jnext <- [0..<L]] -> [slist[jnext] == (if [jnext <~+~ slist] then imay_jnext_(slist; jnext) else imay_original_jprev_(slist; jnext))]]
        #
        # !! [imay_j <~*~ slist]
        # [imay_jnext <~*~ slist]
        # !! [imay_jnext =!= -1]
        # [jnext <~+~ slist]
        # [slist[imay_j] == imay_jnext_(slist; imay_j) == jnext]
        # [slist[jnext] == imay_jnext_(slist; jnext) == jnextnext]
        jnext = imay_jnext
        slist[imay_j] = slist[jnext]
        slist[jnext] = imay_j
        # [not [jnext <~*~ slist]]
        # [slist[jnext] == imay_original_jprev_(slist; jnext) == imay_j]
        # [slist[imay_j] == imay_jnext_(slist; imay_j) == original jnextnext]
        js4off.append(jnext)
    return imay_jnext
def put_back_last_j4off_(js4off, slist, /):
    '[len(js4off) > 0] => js4off -> slist -> imay_j # [put_back_last_j4off_ ~= inv{pop_imay_jnext_} when [-1 =!= imay_jnext{from pop_imay_jnext_}]] #see:validate_js4off_slist_()'
    jnext = js4off.pop()
    #assert not jnext == -1
    assert 0 <= jnext < len(slist) - 1 # == L
    imay_j = slist[jnext]
        # == imay_original_jprev_(slist; jnext)
    slist[jnext] = slist[imay_j]
        # == imay_original_jnextnext
        # == original-imay_jnext_(slist; jnext) 
        # == new-imay_jnext_(slist; imay_j)
    slist[imay_j] = jnext
    return imay_j

#end-class SinglyLinkedList4idx:
######################

class _IBaseRecordIterator(IBase4TellSeekState, ABC):
    #__slots__ = ()
    ___no_slots_ok___ = True
    @property#@classmethod
    @abstractmethod
    def _type4mutable_st_(sf, /):
        '-> type(mutable_st) <: IBase4TellSeekState'
    @abstractmethod
    def _next_ex4record_(sf, mutable_st, /):
        'mutable_st -> (record4sz{len==.sz4record}, known_stop/bool)|^StopIteration'
    @classmethod
    @abstractmethod
    def mk5params_(cls, radix, sz4record, /, *, avoid_leading_zero:bool):
        '-> sf/__class__'
    @override
    def __getstate__(sf, /):
        may_mutable_st = sf._m
        if None is may_mutable_st:
            return False
        mutable_st = may_mutable_st
        return mutable_st.tell()
    @override
    def __setstate__(sf, st, /):
        if st is False:
            may_mutable_st = None
        else:
            mutable_st = type(sf)._type4mutable_st_.mk5st_(st)
            may_mutable_st = mutable_st
        sf.__init__(may_mutable_st)
    def __repr__(sf, /):
        return repr_helper(sf, sf._m)
    def __init__(sf, may_mutable_st, /):
        if not None is may_mutable_st:
            mutable_st = may_mutable_st
            check_type_is(type(sf)._type4mutable_st_, mutable_st)
        sf._m = may_mutable_st
    #.@property
    #.def sz4record(sf, /):
    #.    return sf._mutable_st.sz4off#<<==no:『._mutable_st』
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        may_mutable_st = sf._m
        if None is may_mutable_st:
            raise StopIteration
        mutable_st = may_mutable_st
        try:
            r = sf._next_ex4record_(mutable_st)
        except StopIteration:
            sf._m = None
            raise
        (record4sz, known_stop) = r
        if known_stop:
            sf._m = None
        return record4sz

class _IBaseRecordIterator__using_SinglyLinkedList4idx(_IBaseRecordIterator):
    '[mutable_st == syls :: SinglyLinkedList4idx]'
    ___no_slots_ok___ = True
    #@override
    _type4mutable_st_ = SinglyLinkedList4idx
    #.@abstractmethod
    #.@override#re-declare
    #.def _next_ex4record_(sf, syls, /):
    #.    'SinglyLinkedList4idx -> (record4sz{len==.sz4record}, known_stop/bool)|^StopIteration'
    #.    next_ex4permutation_
class PermutationIterator(_IBaseRecordIterator__using_SinglyLinkedList4idx):
    r'''[[[
    [sz4perm == sz4record]
    [permutation4sz == record4sz]
    [arg4perm :: SinglyLinkedList4idx]
    #]]]'''#'''
    @classmethod
    @override
    def mk5params_(cls, radix, sz4perm, /, *, avoid_leading_zero:bool):
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, sz4perm)
        #check_int_ge(sz4perm, radix)
        check_int_ge(0, radix)
        if not sz4perm <= radix:
            may_mutable_st = None
        elif not sz4perm == 0 and avoid_leading_zero and radix == 1:
            may_mutable_st = None
        else:
            syls = SinglyLinkedList4idx.mk5L_(radix)
            #.if 0:
            #.    #bug:
            #.    #   uint%4 => avoid 012 --> 102 not 123
            #.    imay_j = 0 if avoid_leading_zero and sz4perm > 0 else -1
            #.    for _ in range(sz4perm):
            #.        syls.pop_imay_jnext_(imay_j)
            if avoid_leading_zero and sz4perm > 0:
                syls.pop_imay_jnext_(0)
                for _ in range(sz4perm-1):
                    syls.pop_imay_jnext_(-1)
            else:
                for _ in range(sz4perm):
                    syls.pop_imay_jnext_(-1)
            assert radix == syls.L
            assert sz4perm == syls.sz4off, (radix, sz4perm, avoid_leading_zero, syls)
            may_mutable_st = mutable_st = syls
        may_mutable_st
        return cls(may_mutable_st)


    @override
    def _next_ex4record_(sf, syls, /):
        return next_ex4permutation_(syls)
def next_ex4permutation_(syls, /):
    'SinglyLinkedList4idx -> (permutation4sz{len==.sz4perm}, known_stop/bool)|^StopIteration'
    sz4perm = syls.sz4off
    permutation4sz = tuple(syls.js4off)
    #if not sz4perm: return (null_tuple, True)
    ######################
    # vivi: 666999+1-->667000
    # eg: inc4perm(selected_perm[1,2,6,5],sorted_remain[0,3,4])-->([1,3,0,2],[4,5,6])
    while syls.sz4off:
        imay_j = syls.put_back_last_j4off_()
        # [new1-syls.sz4off == old-syls.sz4off-1]
        jnext = syls.slist[imay_j]
        imay_jnextnext = syls.pop_imay_jnext_(jnext)
        if not imay_jnextnext == -1:
            # [new2-syls.sz4off == new1-syls.sz4off+1 == old-syls.sz4off]
            known_stop = False
            break
        # [new1-syls.sz4off == old-syls.sz4off-1]
    else:
        known_stop = True
    known_stop
    for _ in range(sz4perm - syls.sz4off):
        syls.pop_imay_jnext_(-1)
    assert sz4perm == syls.sz4off
    ######################
    return (permutation4sz, known_stop)


######################
# !! CombinationIterator neednot SinglyLinkedList4idx, simply [mutable_st == (radix, selected_sorted_comb[uint%radix]{len==sz4comb})] is ok.
######################
#.class CombinationIterator(_IBaseRecordIterator__using_SinglyLinkedList4idx):
#.    r'''[[[
#.    [sz4comb == sz4record]
#.    [combination4sz == record4sz]
#.    #]]]'''#'''
#.    @override
#.    def _next_ex4record_(sf, syls, /):
#.        return next_ex4combination_(syls)
#.def next_ex4combination_(syls, /):
#.    'SinglyLinkedList4idx -> (combination4sz{len==.sz4comb}, known_stop/bool)|^StopIteration'
#.    sz4comb = syls.sz4off
#.    combination4sz = tuple(syls.js4off)
#.    #if not sz4comb: return (null_tuple, True)
#.    ######################
#.    # vivi: 666999+1-->667000
#.    # eg: inc4comb(selected_sorted_comb[1,2,5,6],sorted_remain[0,3,4])-->([1,3,4,5],[0,2,6])
#.    avoid = syls.L - 1
#.    js4off = syls.js4off
#.    while js4off and js4off[-1] == avoid:
#.        imay_j = syls.put_back_last_j4off_()
#.        # [new1-syls.sz4off == old-syls.sz4off-1]
#.        avoid -= 1
#.
#.    while js4off:
#.        imay_j = syls.put_back_last_j4off_()
#.        # [new1-syls.sz4off == old-syls.sz4off-1]
#.        jnext = syls.slist[imay_j]
#.        imay_jnextnext = syls.pop_imay_jnext_(jnext)
#.        if not imay_jnextnext == -1:
#.            # [new2-syls.sz4off == new1-syls.sz4off+1 == old-syls.sz4off]
#.            known_stop = False
#.            j0 = jnext
#.            break
#.        # [new1-syls.sz4off == old-syls.sz4off-1]
#.        raise 000
#.    else:
#.        known_stop = True
#.        j0 = -1
#.    known_stop
#.    j0
#.    for _ in range(sz4comb - syls.sz4off):
#.        syls.pop_imay_jnext_(j0)
#.    assert sz4comb == syls.sz4off
#.    ######################
#.    return (combination4sz, known_stop)
#.

class Mutable_st4comb(IBase4TellSeekState, _Base4repr):
    ___no_slots_ok___ = True

    @override
    def __getstate__(sf, /):
        return (sf.radix, tuple(sf.sorted_js))
    @override
    def __setstate__(sf, st, /):
        (radix, [*sorted_js]) = st
        sf.__init__(radix, sorted_js)
    def __init__(sf, radix, sorted_js, /):
        check_int_ge(0, radix)
        check_type_is(list, sorted_js)
        sf._args4mst = (radix, sorted_js)
        sf._reset4repr(sf._args4mst)
    @property
    def radix(sf, /):
        return sf._args4mst[0]
    @property
    def sorted_js(sf, /):
        return sf._args4mst[1]
    @property
    def sz4comb(sf, /):
        return len(sf.sorted_js)
class CombinationIterator(_IBaseRecordIterator):
    r'''[[[
    [sz4comb == sz4record]
    [combination4sz == record4sz]
    [mutable_st :: Mutable_st4comb]
    #]]]'''#'''

    #@override
    _type4mutable_st_ = Mutable_st4comb
    @classmethod
    @override
    def mk5params_(cls, radix, sz4comb, /, *, avoid_leading_zero:bool):
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, sz4comb)
        #check_int_ge(sz4comb, radix)
        check_int_ge(0, radix)
        j0 = 1 if avoid_leading_zero else 0
        #check_int_ge(j0+sz4comb, radix)
        if not (sz4comb == 0 or j0+sz4comb <= radix):
            may_mutable_st = None
        else:
            sorted_js = list(range(j0, j0+sz4comb))
            mutable_st = Mutable_st4comb(radix, sorted_js)
            assert radix == mutable_st.radix
            assert sz4comb == mutable_st.sz4comb
            may_mutable_st = mutable_st
        may_mutable_st
        return cls(may_mutable_st)
    @override
    def _next_ex4record_(sf, mutable_st, /):
        return next_ex4combination_(mutable_st)
def next_ex4combination_(mutable_st, /):
    'Mutable_st4comb -> (combination4sz{len==.sz4comb}, known_stop/bool)|^StopIteration'
    radix = mutable_st.radix
    sz4comb = mutable_st.sz4comb
    sorted_js = mutable_st.sorted_js
    combination4sz = tuple(sorted_js)
    ######################
    # vivi: 666999+1-->667000
    # eg: inc4comb(selected_sorted_comb[1,2,5,6],sorted_remain[0,3,4])-->([1,3,4,5],[0,2,6])
    for k4j, j, avoid in zip(reversed(range(sz4comb)), reversed(sorted_js), reversed(range(radix))):
        if not j == avoid:
            assert j < avoid, (radix, sz4comb, sorted_js, k4j, j, avoid)
            known_stop = False
            break
    else:
        known_stop = True
    known_stop
    if not known_stop:
        k4j, j
        j1 = j+1
        sorted_js[k4j:sz4comb] = range(j1, j1+(sz4comb-k4j))
    ######################
    return (combination4sz, known_stop)




#combinations_with_replacement_
class CombinationIterator__with_replacement(_IBaseRecordIterator):
    r'''[[[
    [sz4comb == sz4record]
    [wr_combination4sz == record4sz]
    [mutable_st :: Mutable_st4comb]
    #]]]'''#'''

    #@override
    _type4mutable_st_ = Mutable_st4comb
    @classmethod
    @override
    def mk5params_(cls, radix, sz4comb, /, *, avoid_leading_zero:bool):
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, sz4comb)
        check_int_ge(0, radix)
        j0 = 1 if avoid_leading_zero else 0
        #check_int_ge(j0+1, radix)
        if not (sz4comb == 0 or j0 < radix):
            may_mutable_st = None
        else:
            sorted_js = [j0]*sz4comb
            mutable_st = Mutable_st4comb(radix, sorted_js)
            assert radix == mutable_st.radix
            assert sz4comb == mutable_st.sz4comb
            may_mutable_st = mutable_st
        may_mutable_st
        return cls(may_mutable_st)
    @override
    def _next_ex4record_(sf, mutable_st, /):
        return next_ex4combination__with_replacement_(mutable_st)
def next_ex4combination__with_replacement_(mutable_st, /):
    'Mutable_st4comb -> (wr_combination4sz{len==.sz4comb}, known_stop/bool)|^StopIteration'
    radix = mutable_st.radix
    sz4comb = mutable_st.sz4comb
    sorted_js = mutable_st.sorted_js
    wr_combination4sz = tuple(sorted_js)
    ######################
    # vivi: 666999+1-->667000
    # eg: inc4comb(selected_sorted_comb[1,2,6,6],sorted_remain[0,3,4,5])-->([1,3,3,3],[0,2,4,5,6])
    avoid = radix -1
    for k4j, j in zip(reversed(range(sz4comb)), reversed(sorted_js)):
        if not j == avoid:
            assert j < avoid
            known_stop = False
            break
    else:
        known_stop = True
    known_stop
    if not known_stop:
        k4j, j
        sorted_js[k4j:sz4comb] = [j+1]*(sz4comb-k4j)
    ######################
    return (wr_combination4sz, known_stop)






class Mutable_st4prod(IBase4TellSeekState, _Base4repr):
    ___no_slots_ok___ = True

    @override
    def __getstate__(sf, /):
        return (sf.radixes, tuple(sf.js))
    @override
    def __setstate__(sf, st, /):
        (radixes, [*js]) = st
        sf.__init__(radixes, js)
    def __init__(sf, radixes, js, /):
        check_type_is(tuple, radixes)
        check_type_is(list, js)
        if not len(radixes) == len(js):raise TypeError
        for radix, j in zip(radixes, js):
            check_int_ge(0, j)
            check_int_ge(j+1, radix)
        sf._args4mst = (radixes, js)
        sf._reset4repr(sf._args4mst)
    @property
    def radixes(sf, /):
        return sf._args4mst[0]
    @property
    def js(sf, /):
        return sf._args4mst[1]
    @property
    def sz4prod(sf, /):
        #return len(sf.radixes)
        return len(sf.js)
class ProductIterator(_IBaseRecordIterator):
    r'''[[[
    [sz4prod == sz4record]
    [product4sz == record4sz]
    [mutable_st :: Mutable_st4prod]
    #]]]'''#'''

    #@override
    _type4mutable_st_ = Mutable_st4prod
    @classmethod
    @override
    def mk5params_(cls, radix, sz4prod, /, *, avoid_leading_zero:bool):
        return cls.mk5radixes_(radix, repeat=sz4prod, avoid_leading_zero=avoid_leading_zero)
    @classmethod
    def mk5radixes_(cls, /, *radixes, repeat:int, avoid_leading_zero:bool):
        #see:mk5params_
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, repeat)
        for radix in radixes:
            check_int_ge(0, radix)
        may_mutable_st = ...
        if repeat and radixes:
            if not all(radixes):
                may_mutable_st = None
            elif avoid_leading_zero and radixes[0] == 1:
                may_mutable_st = None
        if may_mutable_st is ...:
            radixes *= repeat
            repeat = 1
            sz4prod = len(radixes)
            js = [0]*sz4prod
            if avoid_leading_zero and js:
                assert 1 < radixes[0]
                js[0] = 1
            mutable_st = Mutable_st4prod(radixes, js)
            assert radixes is mutable_st.radixes
            assert js is mutable_st.js
            assert sz4prod == mutable_st.sz4prod
            may_mutable_st = mutable_st
        may_mutable_st
        return cls(may_mutable_st)
    @override
    def _next_ex4record_(sf, mutable_st, /):
        return next_ex4product_(mutable_st)
def next_ex4product_(mutable_st, /):
    'Mutable_st4prod -> (product4sz{len==.sz4prod}, known_stop/bool)|^StopIteration'
    radixes = mutable_st.radixes
    sz4prod = mutable_st.sz4prod
    js = mutable_st.js
    product4sz = tuple(js)
    ######################
    # vivi: 666999+1-->667000
    for k4j, j, radix in zip(reversed(range(sz4prod)), reversed(js), reversed(radixes)):
        if not j+1 == radix:
            known_stop = False
            break
    else:
        known_stop = True
    known_stop
    if not known_stop:
        k4j, j
        js[k4j] = j+1
        js[k4j+1:sz4prod] = [0]*(sz4prod-k4j-1)
    ######################
    return (product4sz, known_stop)







#ascending --> descending
#Mutable_st4comb --> Mutable_st4comb__descending
class Mutable_st4comb__descending(IBase4TellSeekState, _Base4repr):
    ___no_slots_ok___ = True

    @override
    def __getstate__(sf, /):
        return (sf.radix, tuple(sf.rvsorted_js))
    @override
    def __setstate__(sf, st, /):
        (radix, [*rvsorted_js]) = st
        sf.__init__(radix, rvsorted_js)
    def __init__(sf, radix, rvsorted_js, /):
        check_int_ge(0, radix)
        check_type_is(list, rvsorted_js)
        sf._args4mst = (radix, rvsorted_js)
        sf._reset4repr(sf._args4mst)
    @property
    def radix(sf, /):
        return sf._args4mst[0]
    @property
    def rvsorted_js(sf, /):
        return sf._args4mst[1]
    @property
    def sz4comb(sf, /):
        return len(sf.rvsorted_js)
class CombinationIterator__descending(_IBaseRecordIterator):
    r'''[[[
    [sz4comb == sz4record]
    [des_combination4sz == record4sz]
    [mutable_st :: Mutable_st4comb__descending]
    #]]]'''#'''

    #@override
    _type4mutable_st_ = Mutable_st4comb__descending
    @classmethod
    @override
    def mk5params_(cls, radix, sz4comb, /, *, avoid_leading_zero:bool):
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, sz4comb)
        #check_int_ge(sz4comb, radix)
        check_int_ge(0, radix)
        #if not (sz4comb == 0 or (2 <= radix if avoid_leading_zero and sz4comb == 1 else sz4comb <= radix)):
        if not (2 <= radix if avoid_leading_zero and sz4comb == 1 else sz4comb <= radix):
            may_mutable_st = None
        else:
            rvsorted_js = list(range(sz4comb)[::-1])
            if avoid_leading_zero and sz4comb == 1:
                rvsorted_js[0] = 1
                assert rvsorted_js == [1]
            if avoid_leading_zero:
                assert not (rvsorted_js and rvsorted_js[0] == 0)
                assert not rvsorted_js[:1] == [0]
            mutable_st = Mutable_st4comb__descending(radix, rvsorted_js)
            assert radix == mutable_st.radix
            assert sz4comb == mutable_st.sz4comb
            may_mutable_st = mutable_st
        may_mutable_st
        return cls(may_mutable_st)
    @override
    def _next_ex4record_(sf, mutable_st, /):
        return next_ex4combination__descending_(mutable_st)
def next_ex4combination__descending_(mutable_st, /):
    'Mutable_st4comb__descending -> (des_combination4sz{len==.sz4comb}, known_stop/bool)|^StopIteration'
    radix = mutable_st.radix
    sz4comb = mutable_st.sz4comb
    rvsorted_js = mutable_st.rvsorted_js
    des_combination4sz = tuple(rvsorted_js)
    ######################
    # vivi: 666999+1-->667000
    # eg: inc4comb(selected_rvsorted_comb[6,5,2,1],sorted_remain[0,3,4])-->([6,5,3,0],[1,2,4])
    for k4j, j in zip(reversed(range(sz4comb)), reversed(rvsorted_js)):
        avoid = (rvsorted_js[k4j-1] if k4j else radix) -1
        if not j == avoid:
            assert j < avoid, (radix, sz4comb, rvsorted_js, k4j, j, avoid)
            known_stop = False
            break
    else:
        known_stop = True
    known_stop
    if not known_stop:
        k4j, j
        rvsorted_js[k4j] = j+1
        rvsorted_js[k4j+1:sz4comb] = range(sz4comb-k4j-1)[::-1]
    ######################
    return (des_combination4sz, known_stop)




#combinations_with_replacement_
class CombinationIterator__with_replacement__descending(_IBaseRecordIterator):
    r'''[[[
    [sz4comb == sz4record]
    [des_wr_combination4sz == record4sz]
    [mutable_st :: Mutable_st4comb__descending]
    #]]]'''#'''

    #@override
    _type4mutable_st_ = Mutable_st4comb__descending
    @classmethod
    @override
    def mk5params_(cls, radix, sz4comb, /, *, avoid_leading_zero:bool):
        check_type_is(bool, avoid_leading_zero)
        check_int_ge(0, sz4comb)
        check_int_ge(0, radix)
        j0 = 1 if avoid_leading_zero else 0
        #check_int_ge(j0+1, radix)
        if not (sz4comb == 0 or j0 < radix):
            may_mutable_st = None
        else:
            rvsorted_js = [0]*sz4comb
            if j0 and sz4comb:
                rvsorted_js[0] = j0
            mutable_st = Mutable_st4comb__descending(radix, rvsorted_js)
            assert radix == mutable_st.radix
            assert sz4comb == mutable_st.sz4comb
            may_mutable_st = mutable_st
        may_mutable_st
        return cls(may_mutable_st)
    @override
    def _next_ex4record_(sf, mutable_st, /):
        return next_ex4combination__with_replacement__descending_(mutable_st)
def next_ex4combination__with_replacement__descending_(mutable_st, /):
    'Mutable_st4comb__descending -> (des_wr_combination4sz{len==.sz4comb}, known_stop/bool)|^StopIteration'
    radix = mutable_st.radix
    sz4comb = mutable_st.sz4comb
    rvsorted_js = mutable_st.rvsorted_js
    des_wr_combination4sz = tuple(rvsorted_js)
    ######################
    # vivi: 666999+1-->667000
    # eg: inc4comb(selected_rvsorted_comb[6,5,2,2],sorted_remain[0,1,3,4])-->([6,5,3,0],[1,2,4])
    for k4j, j in zip(reversed(range(sz4comb)), reversed(rvsorted_js)):
        avoid = rvsorted_js[k4j-1] if k4j else (radix -1)
        if not j == avoid:
            assert j < avoid
            known_stop = False
            break
    else:
        known_stop = True
    known_stop
    if not known_stop:
        k4j, j
        rvsorted_js[k4j] = j+1
        rvsorted_js[k4j+1:sz4comb] = [0]*(sz4comb-k4j-1)
    ######################
    return (des_wr_combination4sz, known_stop)









Mutable_st4perm = SinglyLinkedList4idx
PermutationIterator__with_replacement = ProductIterator

check_non_ABC(Mutable_st4perm)
check_non_ABC(SinglyLinkedList4idx)
check_non_ABC(Mutable_st4prod)
check_non_ABC(Mutable_st4comb)
check_non_ABC(Mutable_st4comb__descending)

check_non_ABC(PermutationIterator)
check_non_ABC(ProductIterator)
check_non_ABC(PermutationIterator__with_replacement)

check_non_ABC(CombinationIterator)
check_non_ABC(CombinationIterator__with_replacement)
check_non_ABC(CombinationIterator__descending)
check_non_ABC(CombinationIterator__with_replacement__descending)




#this module::(product_|permutations_|combinations_|combinations_with_replacement_|combinations__descending_|combinations_with_replacement__descending_)
#   vivi:itertools::(product|permutations|combinations|combinations_with_replacement)

def permutations_(radix, sz4perm, /, *, avoid_leading_zero:bool=False):
    return PermutationIterator.mk5params_(radix, sz4perm, avoid_leading_zero=avoid_leading_zero)

def product_(*radixes, repeat=1, avoid_leading_zero:bool=False):
    return ProductIterator.mk5radixes_(*radixes, repeat=repeat, avoid_leading_zero=avoid_leading_zero)
permutations_with_replacement_ = product_

def combinations_(radix, sz4comb, /, *, avoid_leading_zero:bool=False):
    return CombinationIterator.mk5params_(radix, sz4comb, avoid_leading_zero=avoid_leading_zero)

def combinations_with_replacement_(radix, sz4comb, /, *, avoid_leading_zero:bool=False):
    return CombinationIterator__with_replacement.mk5params_(radix, sz4comb, avoid_leading_zero=avoid_leading_zero)

def combinations__descending_(radix, sz4comb, /, *, avoid_leading_zero:bool=False):
    return CombinationIterator__descending.mk5params_(radix, sz4comb, avoid_leading_zero=avoid_leading_zero)

def combinations_with_replacement__descending_(radix, sz4comb, /, *, avoid_leading_zero:bool=False):
    return CombinationIterator__with_replacement__descending.mk5params_(radix, sz4comb, avoid_leading_zero=avoid_leading_zero)







__all__
from seed.math.combination__stated import permutations_, product_, permutations_with_replacement_, combinations_, combinations_with_replacement_, combinations__descending_, combinations_with_replacement__descending_

from seed.math.combination__stated import PermutationIterator, ProductIterator, PermutationIterator__with_replacement, CombinationIterator, CombinationIterator__with_replacement, CombinationIterator__descending, CombinationIterator__with_replacement__descending

from seed.math.combination__stated import SinglyLinkedList4idx, Mutable_st4perm, Mutable_st4comb, Mutable_st4comb__descending, Mutable_st4prod

from seed.math.combination__stated import *
