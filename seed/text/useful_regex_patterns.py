#__all__:goto
r'''[[[
e ../../python3_src/seed/text/useful_regex_patterns.py


seed.text.useful_regex_patterns
py -m nn_ns.app.debug_cmd   seed.text.useful_regex_patterns -x
py -m nn_ns.app.doctest_cmd seed.text.useful_regex_patterns:__doc__ -ff
py -m nn_ns.app.doctest_cmd seed.text.useful_regex_patterns!
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.text.useful_regex_patterns   @f




:%s/^>>> \(\w*\)[.]fullmatch(\([^)]*\))$/>>> not_match_(\1, \2)
>>> import re
>>> def match_(regex, s, /):
...    return None if not None is regex.fullmatch(s) else False
>>> def not_match_(regex, s, /):
...    return None if None is regex.fullmatch(s) else False

>>> from seed.text.useful_regex_patterns import nm__pattern, qnm__pattern, nm__regex, qnm__regex

>>> match_(nm__regex, 'a')
>>> match_(nm__regex, '_')
>>> match_(nm__regex, '的')
>>> match_(nm__regex, '_a的')
>>> match_(nm__regex, '_a的09')

>>> not_match_(nm__regex, '0a')
>>> not_match_(nm__regex, '0')
>>> not_match_(nm__regex, '')
>>> not_match_(nm__regex, 'a.a')
>>> not_match_(nm__regex, '$')
>>> not_match_(nm__regex, '%')





>>> match_(qnm__regex, 'a')
>>> match_(qnm__regex, '_')
>>> match_(qnm__regex, '的')
>>> match_(qnm__regex, '_a的')
>>> match_(qnm__regex, '_a的09')
>>> match_(qnm__regex, 'a.a')

>>> not_match_(qnm__regex, '0a')
>>> not_match_(qnm__regex, '0')
>>> not_match_(qnm__regex, '')
>>> not_match_(qnm__regex, 'a..a')
>>> not_match_(qnm__regex, 'a.')
>>> not_match_(qnm__regex, '.a')
>>> not_match_(qnm__regex, 'a.0')
>>> not_match_(qnm__regex, '0.a')
>>> not_match_(qnm__regex, '$')
>>> not_match_(qnm__regex, '%')


>>> 0_x
Traceback (most recent call last):
    ...
SyntaxError: invalid decimal literal
>>> 0_x1
Traceback (most recent call last):
    ...
SyntaxError: invalid decimal literal



>>> 0x
Traceback (most recent call last):
    ...
SyntaxError: invalid hexadecimal literal
>>> 0x_
Traceback (most recent call last):
    ...
SyntaxError: invalid hexadecimal literal
>>> 0x1_
Traceback (most recent call last):
    ...
SyntaxError: invalid hexadecimal literal
>>> 0x__1
Traceback (most recent call last):
    ...
SyntaxError: invalid hexadecimal literal
>>> 0x1__1
Traceback (most recent call last):
    ...
SyntaxError: invalid hexadecimal literal



>>> 0x_1
1
>>> 0x_0_0
0
>>> 0x00000
0
>>> 0x00001
1



>>> match_(decimal_int__regex, '0')
>>> match_(decimal_int__regex, '1')
>>> match_(decimal_int__regex, '9')
>>> match_(decimal_int__regex, '1000')
>>> match_(decimal_int__regex, '9999')
>>> match_(decimal_int__regex, '+0')
>>> match_(decimal_int__regex, '+1')
>>> match_(decimal_int__regex, '+9')
>>> match_(decimal_int__regex, '+1000')
>>> match_(decimal_int__regex, '+9999')
>>> match_(decimal_int__regex, '-0')
>>> match_(decimal_int__regex, '-1')
>>> match_(decimal_int__regex, '-9')
>>> match_(decimal_int__regex, '-1000')
>>> match_(decimal_int__regex, '-9999')

>>> not_match_(decimal_int__regex, '')
>>> not_match_(decimal_int__regex, 'a')
>>> not_match_(decimal_int__regex, '00')
>>> not_match_(decimal_int__regex, '01')
>>> not_match_(decimal_int__regex, '1_1')
>>> not_match_(decimal_int__regex, '1.1')
>>> not_match_(decimal_int__regex, '1.')
>>> not_match_(decimal_int__regex, '.1')

>>> not_match_(decimal_int__regex, '+ 1')
>>> not_match_(decimal_int__regex, '- 1')

>>> not_match_(decimal_int__regex, '+')
>>> not_match_(decimal_int__regex, '+a')
>>> not_match_(decimal_int__regex, '+00')
>>> not_match_(decimal_int__regex, '+01')
>>> not_match_(decimal_int__regex, '+1_1')
>>> not_match_(decimal_int__regex, '+1.1')
>>> not_match_(decimal_int__regex, '+1.')
>>> not_match_(decimal_int__regex, '+.1')

>>> not_match_(decimal_int__regex, '-')
>>> not_match_(decimal_int__regex, '-a')
>>> not_match_(decimal_int__regex, '-00')
>>> not_match_(decimal_int__regex, '-01')
>>> not_match_(decimal_int__regex, '-1_1')
>>> not_match_(decimal_int__regex, '-1.1')
>>> not_match_(decimal_int__regex, '-1.')
>>> not_match_(decimal_int__regex, '-.1')









>>> match_(hex_int__regex, '0x0')
>>> match_(hex_int__regex, '0x1')
>>> match_(hex_int__regex, '0X9')
>>> match_(hex_int__regex, '0xa')
>>> match_(hex_int__regex, '0Xf')
>>> match_(hex_int__regex, '0xA')
>>> match_(hex_int__regex, '0XF')
>>> match_(hex_int__regex, '0X0000')
>>> match_(hex_int__regex, '0xffff')
>>> match_(hex_int__regex, '+0x0')
>>> match_(hex_int__regex, '+0x1')
>>> match_(hex_int__regex, '+0X9')
>>> match_(hex_int__regex, '+0xa')
>>> match_(hex_int__regex, '+0Xf')
>>> match_(hex_int__regex, '+0xA')
>>> match_(hex_int__regex, '+0XF')
>>> match_(hex_int__regex, '+0X0000')
>>> match_(hex_int__regex, '+0xffff')
>>> match_(hex_int__regex, '-0x0')
>>> match_(hex_int__regex, '-0x1')
>>> match_(hex_int__regex, '-0X9')
>>> match_(hex_int__regex, '-0xa')
>>> match_(hex_int__regex, '-0Xf')
>>> match_(hex_int__regex, '-0xA')
>>> match_(hex_int__regex, '-0XF')
>>> match_(hex_int__regex, '-0X0000')
>>> match_(hex_int__regex, '-0xffff')


>>> not_match_(hex_int__regex, '')
>>> not_match_(hex_int__regex, '0')
>>> not_match_(hex_int__regex, '9')
>>> not_match_(hex_int__regex, 'a')
>>> not_match_(hex_int__regex, 'A')
>>> not_match_(hex_int__regex, '0xg')
>>> not_match_(hex_int__regex, '0xG')
>>> not_match_(hex_int__regex, '0x1_1')
>>> not_match_(hex_int__regex, '0x1.1')
>>> not_match_(hex_int__regex, '0x1.')
>>> not_match_(hex_int__regex, '0x.1')

>>> not_match_(hex_int__regex, '+ 0x1')
>>> not_match_(hex_int__regex, '- 0x1')

>>> not_match_(hex_int__regex, '+')
>>> not_match_(hex_int__regex, '+0')
>>> not_match_(hex_int__regex, '+9')
>>> not_match_(hex_int__regex, '+a')
>>> not_match_(hex_int__regex, '+A')
>>> not_match_(hex_int__regex, '+0xg')
>>> not_match_(hex_int__regex, '+0xG')
>>> not_match_(hex_int__regex, '+0x1_1')
>>> not_match_(hex_int__regex, '+0x1.1')
>>> not_match_(hex_int__regex, '+0x1.')
>>> not_match_(hex_int__regex, '+0x.1')

>>> not_match_(hex_int__regex, '-')
>>> not_match_(hex_int__regex, '-0')
>>> not_match_(hex_int__regex, '-9')
>>> not_match_(hex_int__regex, '-a')
>>> not_match_(hex_int__regex, '-A')
>>> not_match_(hex_int__regex, '-0xg')
>>> not_match_(hex_int__regex, '-0xG')
>>> not_match_(hex_int__regex, '-0x1_1')
>>> not_match_(hex_int__regex, '-0x1.1')
>>> not_match_(hex_int__regex, '-0x1.')
>>> not_match_(hex_int__regex, '-0x.1')












    underscored_decimal_int__regex
    underscored_
>>> match_(underscored_decimal_int__regex, '0')
>>> match_(underscored_decimal_int__regex, '1')
>>> match_(underscored_decimal_int__regex, '9')
>>> match_(underscored_decimal_int__regex, '1_0_000_0')
>>> match_(underscored_decimal_int__regex, '9_9_999_9')
>>> match_(underscored_decimal_int__regex, '1_0')
>>> match_(underscored_decimal_int__regex, '+0')
>>> match_(underscored_decimal_int__regex, '+1')
>>> match_(underscored_decimal_int__regex, '+9')
>>> match_(underscored_decimal_int__regex, '+1_0_000_0')
>>> match_(underscored_decimal_int__regex, '+9_9_999_9')
>>> match_(underscored_decimal_int__regex, '+1_0')
>>> match_(underscored_decimal_int__regex, '-0')
>>> match_(underscored_decimal_int__regex, '-1')
>>> match_(underscored_decimal_int__regex, '-9')
>>> match_(underscored_decimal_int__regex, '-1_0_000_0')
>>> match_(underscored_decimal_int__regex, '-9_9_999_9')
>>> match_(underscored_decimal_int__regex, '-1_0')

>>> not_match_(underscored_decimal_int__regex, '')
>>> not_match_(underscored_decimal_int__regex, 'a')
>>> not_match_(underscored_decimal_int__regex, '_')
>>> not_match_(underscored_decimal_int__regex, '00')
>>> not_match_(underscored_decimal_int__regex, '01')
>>> not_match_(underscored_decimal_int__regex, '0_0')
>>> not_match_(underscored_decimal_int__regex, '0_1')
>>> not_match_(underscored_decimal_int__regex, '1__1')
>>> not_match_(underscored_decimal_int__regex, '_1')
>>> not_match_(underscored_decimal_int__regex, '1_')
>>> not_match_(underscored_decimal_int__regex, '1.1')
>>> not_match_(underscored_decimal_int__regex, '1.')
>>> not_match_(underscored_decimal_int__regex, '.1')

>>> not_match_(underscored_decimal_int__regex, '+ 1')
>>> not_match_(underscored_decimal_int__regex, '- 1')

>>> not_match_(underscored_decimal_int__regex, '+')
>>> not_match_(underscored_decimal_int__regex, '+a')
>>> not_match_(underscored_decimal_int__regex, '+_')
>>> not_match_(underscored_decimal_int__regex, '+00')
>>> not_match_(underscored_decimal_int__regex, '+01')
>>> not_match_(underscored_decimal_int__regex, '+0_0')
>>> not_match_(underscored_decimal_int__regex, '+0_1')
>>> not_match_(underscored_decimal_int__regex, '+1__1')
>>> not_match_(underscored_decimal_int__regex, '+_1')
>>> not_match_(underscored_decimal_int__regex, '+1_')
>>> not_match_(underscored_decimal_int__regex, '+1.1')
>>> not_match_(underscored_decimal_int__regex, '+1.')
>>> not_match_(underscored_decimal_int__regex, '+.1')

>>> not_match_(underscored_decimal_int__regex, '-')
>>> not_match_(underscored_decimal_int__regex, '-a')
>>> not_match_(underscored_decimal_int__regex, '-_')
>>> not_match_(underscored_decimal_int__regex, '-00')
>>> not_match_(underscored_decimal_int__regex, '-01')
>>> not_match_(underscored_decimal_int__regex, '-0_0')
>>> not_match_(underscored_decimal_int__regex, '-0_1')
>>> not_match_(underscored_decimal_int__regex, '-1__1')
>>> not_match_(underscored_decimal_int__regex, '-_1')
>>> not_match_(underscored_decimal_int__regex, '-1_')
>>> not_match_(underscored_decimal_int__regex, '-1.1')
>>> not_match_(underscored_decimal_int__regex, '-1.')
>>> not_match_(underscored_decimal_int__regex, '-.1')





    underscored_hex_int__regex
    underscored_
>>> match_(underscored_hex_int__regex, '0x0')
>>> match_(underscored_hex_int__regex, '0x1')
>>> match_(underscored_hex_int__regex, '0X9')
>>> match_(underscored_hex_int__regex, '0xa')
>>> match_(underscored_hex_int__regex, '0Xf')
>>> match_(underscored_hex_int__regex, '0xA')
>>> match_(underscored_hex_int__regex, '0XF')
>>> match_(underscored_hex_int__regex, '0X0000')
>>> match_(underscored_hex_int__regex, '0xffff')
>>> match_(underscored_hex_int__regex, '0X0_000_0_0_0')
>>> match_(underscored_hex_int__regex, '0xfff_f_f_f_f')
>>> match_(underscored_hex_int__regex, '0x1_1')
>>> match_(underscored_hex_int__regex, '+0x0')
>>> match_(underscored_hex_int__regex, '+0x1')
>>> match_(underscored_hex_int__regex, '+0X9')
>>> match_(underscored_hex_int__regex, '+0xa')
>>> match_(underscored_hex_int__regex, '+0Xf')
>>> match_(underscored_hex_int__regex, '+0xA')
>>> match_(underscored_hex_int__regex, '+0XF')
>>> match_(underscored_hex_int__regex, '+0X0000')
>>> match_(underscored_hex_int__regex, '+0xffff')
>>> match_(underscored_hex_int__regex, '+0X0_000_0_0_0')
>>> match_(underscored_hex_int__regex, '+0xfff_f_f_f_f')
>>> match_(underscored_hex_int__regex, '+0x1_1')
>>> match_(underscored_hex_int__regex, '-0x0')
>>> match_(underscored_hex_int__regex, '-0x1')
>>> match_(underscored_hex_int__regex, '-0X9')
>>> match_(underscored_hex_int__regex, '-0xa')
>>> match_(underscored_hex_int__regex, '-0Xf')
>>> match_(underscored_hex_int__regex, '-0xA')
>>> match_(underscored_hex_int__regex, '-0XF')
>>> match_(underscored_hex_int__regex, '-0X0000')
>>> match_(underscored_hex_int__regex, '-0xffff')
>>> match_(underscored_hex_int__regex, '-0X0_000_0_0_0')
>>> match_(underscored_hex_int__regex, '-0xfff_f_f_f_f')
>>> match_(underscored_hex_int__regex, '-0x1_1')

>>> not_match_(underscored_hex_int__regex, '')
>>> not_match_(underscored_hex_int__regex, '0')
>>> not_match_(underscored_hex_int__regex, '9')
>>> not_match_(underscored_hex_int__regex, 'a')
>>> not_match_(underscored_hex_int__regex, 'A')
>>> not_match_(underscored_hex_int__regex, '0xg')
>>> not_match_(underscored_hex_int__regex, '0xG')
>>> not_match_(underscored_hex_int__regex, '0x1__1')
>>> not_match_(underscored_hex_int__regex, '0x1_')
>>> not_match_(underscored_hex_int__regex, '0x_1')
>>> not_match_(underscored_hex_int__regex, '0_x1')
>>> not_match_(underscored_hex_int__regex, '_0x1')
>>> not_match_(underscored_hex_int__regex, '0x1.1')
>>> not_match_(underscored_hex_int__regex, '0x1.')
>>> not_match_(underscored_hex_int__regex, '0x.1')

>>> not_match_(underscored_hex_int__regex, '+ 0x1')
>>> not_match_(underscored_hex_int__regex, '- 0x1')

>>> not_match_(underscored_hex_int__regex, '+')
>>> not_match_(underscored_hex_int__regex, '+0')
>>> not_match_(underscored_hex_int__regex, '+9')
>>> not_match_(underscored_hex_int__regex, '+a')
>>> not_match_(underscored_hex_int__regex, '+A')
>>> not_match_(underscored_hex_int__regex, '+0xg')
>>> not_match_(underscored_hex_int__regex, '+0xG')
>>> not_match_(underscored_hex_int__regex, '+0x1__1')
>>> not_match_(underscored_hex_int__regex, '+0x1_')
>>> not_match_(underscored_hex_int__regex, '+0x_1')
>>> not_match_(underscored_hex_int__regex, '+0_x1')
>>> not_match_(underscored_hex_int__regex, '+_0x1')
>>> not_match_(underscored_hex_int__regex, '+0x1.1')
>>> not_match_(underscored_hex_int__regex, '+0x1.')
>>> not_match_(underscored_hex_int__regex, '+0x.1')

>>> not_match_(underscored_hex_int__regex, '-')
>>> not_match_(underscored_hex_int__regex, '-0')
>>> not_match_(underscored_hex_int__regex, '-9')
>>> not_match_(underscored_hex_int__regex, '-a')
>>> not_match_(underscored_hex_int__regex, '-A')
>>> not_match_(underscored_hex_int__regex, '-0xg')
>>> not_match_(underscored_hex_int__regex, '-0xG')
>>> not_match_(underscored_hex_int__regex, '-0x1__1')
>>> not_match_(underscored_hex_int__regex, '-0x1_')
>>> not_match_(underscored_hex_int__regex, '-0x_1')
>>> not_match_(underscored_hex_int__regex, '-0_x1')
>>> not_match_(underscored_hex_int__regex, '-_0x1')
>>> not_match_(underscored_hex_int__regex, '-0x1.1')
>>> not_match_(underscored_hex_int__regex, '-0x1.')
>>> not_match_(underscored_hex_int__regex, '-0x.1')






>>> match_(space__regex, ' ')
>>> match_(space__regex, '\t')
>>> match_(space__regex, '\r')
>>> match_(space__regex, '\n')
>>> match_(space__regex, '\u3000')
>>> match_(space__regex, '\u2000')
>>> not_match_(space__regex, '')
>>> not_match_(space__regex, '  ')
>>> not_match_(space__regex, ' \n')
>>> not_match_(space__regex, '\r\n')
>>> not_match_(space__regex, '1')
>>> not_match_(space__regex, '+')
>>> not_match_(space__regex, 'a')
>>> not_match_(space__regex, '_')
>>> not_match_(space__regex, 'A')




>>> match_(spaces0__regex, ' ')
>>> match_(spaces0__regex, '\t')
>>> match_(spaces0__regex, '\r')
>>> match_(spaces0__regex, '\n')
>>> match_(spaces0__regex, '\u3000')
>>> match_(spaces0__regex, '\u2000')
>>> match_(spaces0__regex, '  ')
>>> match_(spaces0__regex, ' \n')
>>> match_(spaces0__regex, '\r\n')
>>> match_(spaces0__regex, '')
>>> not_match_(spaces0__regex, '1')
>>> not_match_(spaces0__regex, '+')
>>> not_match_(spaces0__regex, 'a')
>>> not_match_(spaces0__regex, '_')
>>> not_match_(spaces0__regex, 'A')








>>> match_(spaces1__regex, ' ')
>>> match_(spaces1__regex, '\t')
>>> match_(spaces1__regex, '\r')
>>> match_(spaces1__regex, '\n')
>>> match_(spaces1__regex, '\u3000')
>>> match_(spaces1__regex, '\u2000')
>>> match_(spaces1__regex, '  ')
>>> match_(spaces1__regex, ' \n')
>>> match_(spaces1__regex, '\r\n')
>>> not_match_(spaces1__regex, '')
>>> not_match_(spaces1__regex, '1')
>>> not_match_(spaces1__regex, '+')
>>> not_match_(spaces1__regex, 'a')
>>> not_match_(spaces1__regex, '_')
>>> not_match_(spaces1__regex, 'A')






#]]]'''
__all__ = r'''
nm__pattern
qnm__pattern


digit__pattern
digit_nonzero__pattern
decimal_ge1__pattern
decimal_ge0__pattern
decimal_int__pattern

underscored_digit__pattern
underscored_decimal_ge1__pattern
underscored_decimal_ge0__pattern
underscored_decimal_int__pattern

hexdigit__pattern
hexdigit_nonzero__pattern
hex_ge1__pattern
hex_ge0__pattern
hex_int__pattern

underscored_hexdigit__pattern
underscored_hex_body__pattern
underscored_hex_ge1__pattern
underscored_hex_ge0__pattern
underscored_hex_int__pattern


space__pattern
spaces0__pattern
spaces1__pattern

nonspace__pattern
nonspaces0__pattern
nonspaces1__pattern








nm__regex
qnm__regex

digit__regex
digit_nonzero__regex
decimal_ge0__regex
decimal_ge1__regex
decimal_int__regex

underscored_digit__regex
underscored_decimal_ge1__regex
underscored_decimal_ge0__regex
underscored_decimal_int__regex

hexdigit__regex
hexdigit_nonzero__regex
hex_ge1__regex
hex_ge0__regex
hex_int__regex

underscored_hexdigit__regex
underscored_hex_body__regex
underscored_hex_ge1__regex
underscored_hex_ge0__regex
underscored_hex_int__regex


space__regex
spaces0__regex
spaces1__regex

nonspace__regex
nonspaces0__regex
nonspaces1__regex






'''.split()#'''
__all__

import re
nm__pattern = r'(?:(?!\d)\w+)'
qnm__pattern = fr'(?:{nm__pattern}(?:[.]{nm__pattern})*)'


digit__pattern = r'[0-9]'
digit_nonzero__pattern = r'[1-9]'

decimal_ge1__pattern = fr'(?:{digit_nonzero__pattern}{digit__pattern}*)'
decimal_ge0__pattern = fr'(?:0|{decimal_ge1__pattern})'
decimal_int__pattern = fr'(?:[+-]?{decimal_ge0__pattern})'


underscored_digit__pattern = r'[_0-9]'
#underscored_decimal_ge1__pattern = fr'(?:{digit_nonzero__pattern}{underscored_digit__pattern}*)'
#underscored_decimal_ge0__pattern = fr'(?:0_*|{underscored_decimal_ge1__pattern})'
underscored_decimal_ge1__pattern = fr'(?:{decimal_ge1__pattern}(?:_{digit__pattern}+)*)'
underscored_decimal_ge0__pattern = fr'(?:0|{underscored_decimal_ge1__pattern})'
underscored_decimal_int__pattern = fr'(?:[+-]?{underscored_decimal_ge0__pattern})'






#hexadecimal
hexdigit__pattern = r'[0-9a-fA-F]'
hexdigit_nonzero__pattern = r'[1-9a-fA-F]'
hex_ge1__pattern = fr'(?:0[xX]0*{hexdigit_nonzero__pattern}{hexdigit__pattern}*)'
#hex_ge0__pattern = fr'(?:0|0[xX]{hexdigit__pattern}+)'
hex_ge0__pattern = fr'(?:0[xX]{hexdigit__pattern}+)'
hex_int__pattern = fr'(?:[+-]?{hex_ge0__pattern})'


#py hexadecimal literal donot allow '__', '_$', '^0_x', '0x$'
underscored_hexdigit__pattern = r'[_0-9a-fA-F]'
#underscored_hex_body__pattern = fr'(?:{underscored_hexdigit__pattern}*)'
underscored_hex_body__pattern = fr'(?:{hexdigit__pattern}+(?:_{hexdigit__pattern}+)*)'
underscored_hex_ge1__pattern = fr'(?:0[xX](?:0+_?)*{hexdigit_nonzero__pattern}(?:_?{underscored_hex_body__pattern})?)'
underscored_hex_ge0__pattern = fr'(?:0[xX]{underscored_hex_body__pattern})'
underscored_hex_int__pattern = fr'(?:[+-]?{underscored_hex_ge0__pattern})'






######################
######################
######################
######################
######################
######################
######################
######################
######################
r'''
1. generate __all__ by debug_cmd:
    py -m nn_ns.app.debug_cmd   seed.text.useful_regex_patterns -x

2. copy __all__ then:
    :.,$s/^    \(\w*\)__pattern$/\1__regex = re.compile(\1__pattern)

'''#'''
######################
######################
######################
######################
######################

nm__regex = re.compile(nm__pattern)
qnm__regex = re.compile(qnm__pattern)

digit__regex = re.compile(digit__pattern)
digit_nonzero__regex = re.compile(digit_nonzero__pattern)
decimal_ge1__regex = re.compile(decimal_ge1__pattern)
decimal_ge0__regex = re.compile(decimal_ge0__pattern)
decimal_int__regex = re.compile(decimal_int__pattern)
underscored_digit__regex = re.compile(underscored_digit__pattern)
underscored_decimal_ge1__regex = re.compile(underscored_decimal_ge1__pattern)
underscored_decimal_ge0__regex = re.compile(underscored_decimal_ge0__pattern)
underscored_decimal_int__regex = re.compile(underscored_decimal_int__pattern)
hexdigit__regex = re.compile(hexdigit__pattern)
hexdigit_nonzero__regex = re.compile(hexdigit_nonzero__pattern)
hex_ge1__regex = re.compile(hex_ge1__pattern)
hex_ge0__regex = re.compile(hex_ge0__pattern)
hex_int__regex = re.compile(hex_int__pattern)
underscored_hexdigit__regex = re.compile(underscored_hexdigit__pattern)
underscored_hex_body__regex = re.compile(underscored_hex_body__pattern)
underscored_hex_ge1__regex = re.compile(underscored_hex_ge1__pattern)
underscored_hex_ge0__regex = re.compile(underscored_hex_ge0__pattern)
underscored_hex_int__regex = re.compile(underscored_hex_int__pattern)



space__pattern = r'(?:\s)'
spaces0__pattern = r'(?:\s*)'
spaces1__pattern = r'(?:\s+)'
space__regex = re.compile(space__pattern)
spaces0__regex = re.compile(spaces0__pattern)
spaces1__regex = re.compile(spaces1__pattern)

nonspace__pattern = r'(?:\S)'
nonspaces0__pattern = r'(?:\S*)'
nonspaces1__pattern = r'(?:\S+)'
nonspace__regex = re.compile(nonspace__pattern)
nonspaces0__regex = re.compile(nonspaces0__pattern)
nonspaces1__regex = re.compile(nonspaces1__pattern)


del re
from seed.text.useful_regex_patterns import nm__pattern, qnm__pattern, nm__regex, qnm__regex
from seed.text.useful_regex_patterns import *
