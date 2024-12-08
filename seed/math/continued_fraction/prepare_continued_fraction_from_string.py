#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/prepare_continued_fraction_from_string.py

seed.math.continued_fraction.prepare_continued_fraction_from_string
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.prepare_continued_fraction_from_string -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.prepare_continued_fraction_from_string:__doc__ -ht # -ff -df

[[
[regular_continued_fraction <: simple_continued_fraction <: generalized_continued_fraction]
generalized_continued_fraction
    partial numerators and denominators can be anything
simple_continued_fraction
    partial numerators are all one
regular_continued_fraction
    partial numerators are all one
    partial denominators are all integer
    partial denominators except first one are all positive integer

generalized continued fraction
[gcf[d0; n1$d1, n2$d2, ..., nN$dN, z[N+1]] =[def]= (d0 + n1/(d1 + n2/(d2 + ... + nN/(dN+z[N+1]))))]
[n/d _+ z =[def]= n/(d+z)]
  partial numerators and denominators
[gcf[d0; n1$d1, n2$d2, ..., nN$dN, z] == (d0 + n1/d1 _+ n2/d2 _+ ... _+ nN/dN _+ z[N+1])]
]]


>>> prepare_continued_fraction_from_string_(' - 3_4 ')
-34
>>> prepare_continued_fraction_from_string_(' + 3_4 ')
34
>>> prepare_continued_fraction_from_string_(' 3_4 ')
34
>>> prepare_continued_fraction_from_string_('34')
34

>>> prepare_continued_fraction_from_string_(' [ - 3_4 ; ] ')
[-34]
>>> prepare_continued_fraction_from_string_(' [ - 3_4 ; 5 , + 0b01_0 , - 0o07 , 0x0_f ] ') # not regular_continued_fraction <<== "-0o07"
Traceback (most recent call last):
    ...
seed.math.continued_fraction.prepare_continued_fraction_from_string.FormatError: ('expected: "[-1;3,4]", "-3/-4", "-4", "3 + -3/5 _+2/5 _+7/6"', ' [ -3_4 ; 5 , +0b01_0 , -0o07 , 0x0_f ] ')
>>> prepare_continued_fraction_from_string_(' [ - 3_4 ; 5 , + 0b01_0 , + 0o07 , 0x0_f ] ')
[-34, 5, 2, 7, 15]

>>> prepare_continued_fraction_from_string_(' - 3_4 / - 5_7 ')
Fraction(34, 57)
>>> prepare_continued_fraction_from_string_(' + 3_4 / + 5_7 ')
Fraction(34, 57)
>>> prepare_continued_fraction_from_string_(' 3_4 / 5_7 ')
Fraction(34, 57)
>>> prepare_continued_fraction_from_string_(' 34 / 57 ')
Fraction(34, 57)
>>> prepare_continued_fraction_from_string_('34/57')
Fraction(34, 57)



py_adhoc_call   seed.math.continued_fraction.prepare_continued_fraction_from_string   @f
#]]]'''
__all__ = r'''
prepare_continued_fraction_from_string_


FormatError

cf_digits_list_repr__pattern
    cf_digits_list_repr__regex
py_Fraction_repr__pattern
    py_Fraction_repr__regex
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.tiny_.check import check_type_is, check_int_ge

from seed.text.useful_regex_patterns import py_uint__pattern, py_uint__regex
from seed.text.useful_regex_patterns import py_int__pattern, py_int__regex
from seed.text.useful_regex_patterns import space__regex

import re
from fractions import Fraction

___end_mark_of_excluded_global_names__0___ = ...

cf_digits_list_repr__pattern = fr'(?:\s*\[\s*{py_int__pattern}\s*;\s*(?:{py_uint__pattern}\s*(?:,\s*{py_uint__pattern}\s*)*)?\]\s*)'
py_int__pattern
py_int_repr__pattern = fr'(?:\s*{py_int__pattern}\s*?)'
py_Fraction_repr__pattern = fr'(?:\s*{py_int__pattern}\s*(?:/\s*{py_int__pattern}\s*)?)'




cf_digits_list_repr__regex = re.compile(cf_digits_list_repr__pattern)
py_int__regex
py_int_repr__regex = re.compile(py_int_repr__pattern)
py_Fraction_repr__regex = re.compile(py_Fraction_repr__pattern)

_regex4spaces_followed_sign = re.compile('(?<=[+-])\s+')
assert _regex4spaces_followed_sign.sub('', '+   ') == '+'
assert py_int__regex.fullmatch('-3_4')
assert py_int__regex.fullmatch('-0b01_0')
assert py_int__regex.fullmatch('-0o07')
assert py_int__regex.fullmatch('-0x0_f')

class FormatError(Exception):pass
def prepare_continued_fraction_from_string_(s, /):
    'str/(cf_digits_list_repr|Fraction_repr) -> cf_digits__or__int__or__Fraction/(cf_digits|int|Fraction)'
    check_type_is(str, s)
    s = _regex4spaces_followed_sign.sub('', s)
        # !! '+ 3' fail

    if '_+' in s:
        raise NotImplementedError('partial quotients repr')
    elif ';' in s:
        regex = cf_digits_list_repr__regex
    elif '/' in s:
        regex = py_Fraction_repr__regex
    else:
        regex = py_int_repr__regex
    regex
    m = regex.fullmatch(s)
    if m is None:
        raise FormatError('expected: "[-1;3,4]", "-3/-4", "-4", "3 + -3/5 _+2/5 _+7/6"', s)

    s = space__regex.sub('', s)
    if regex is cf_digits_list_repr__regex:
        cf_digits = eval(s.replace(';', ','))
        return cf_digits
    if regex is py_Fraction_repr__regex:
        sN, sD = s.split('/')
        N = eval(sN)
        D = eval(sD)
        return Fraction(N, D)
    if regex is py_int_repr__regex:
        i = eval(s)
        return i
    raise 000

__all__
from seed.math.continued_fraction.prepare_continued_fraction_from_string import prepare_continued_fraction_from_string_
from seed.math.continued_fraction.prepare_continued_fraction_from_string import *
