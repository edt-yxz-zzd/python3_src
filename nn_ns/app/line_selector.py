#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/line_selector.py
    move some code to:
        view ../../python3_src/seed/text/avoid_py_str_literal.py


nn_ns.app.line_selector
py -m nn_ns.app.debug_cmd   nn_ns.app.line_selector -x
py -m nn_ns.app.doctest_cmd nn_ns.app.line_selector:__doc__ -ff -v
py_adhoc_call   nn_ns.app.line_selector   @f

[[
fixed:bug: _mk_lambda5body_() ::.replace('?', nm) when py_str_literal contains '?'
    replace___avoid_py_str_literal_
fixed:bug: when str-literal in directive4lineno_generator contains '. \ ' or '->'
    try update regex4directive4lineno_generator using py_str__pattern
        but cause endless loop
    replace_ex___avoid_py_str_literal_+extract_old5new_idx__re_matchobj_groupdict_

fixed:bug: when str-literal in directive4lineno_generator contains ';'
    split(';')
    regex4directive4lineno_generator
        .*[.]\\ \w+ = .* ->
    ^:NotImplementedError
    split_directives__str_
        py_str__regex

fixed:bug: keyword "lambda/if/else/in/is/and/or..." in directive4lineno_generator
    erase_spaces_
    ===
    update regex4directive4lineno_generator
    comment out:erase_spaces_

]]

[[
type:
===
#regex4directive4lineno_generator:goto
#epilog:goto

[begin4lineno :: int]
[idx5j4lineno_generator :: uint]
[lineno_generator :: sorted-Iter<lineno>]
[lineno :: int{>=begin4lineno}]
[0 <= j4lineno_generator < len(lineno_generators)]
[line :: str]
[output_formattor :: (lineno, j4lineno_generator, idx5j4lineno_generator, line) -> output]
[output_fmt == output_fmt_str | output_formattor]
[output_fmt_str :: str][output_fmt_str.format :: (*[lineno, j4lineno_generator, idx5j4lineno_generator, line], **{lineno=?, j4lineno_generator=?, idx5j4lineno_generator=?, line=?}) -> str]
]]

[[
used in:
    view ../../python3_src/seed/math/right_angled_triangle_side_length.py
        to extract data4conjecture
        ######################
        ???[coprime_ratio case][hypotenuse[k-1] ~= 2*pi*k]???
            ???[hypotenuse[2**k-1] ~= (25/4)*2**k]???
            ???[hypotenuse[10**k-1] ~= 2*pi*10**k]???
        ######################
        # data4conjecture:
        ######################
        view /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
        ######################
py -m nn_ns.app.line_selector --begin4lineno=1 --lineno_generator='2**?' -i /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
[1@0.0]:(5, 3, 4)
[2@0.1]:(13, 5, 12)
[4@0.2]:(25, 7, 24)
[8@0.3]:(53, 45, 28)
[16@0.4]:(97, 65, 72)
[32@0.5]:(197, 195, 28)
[64@0.6]:(401, 399, 40)
[128@0.7]:(797, 555, 572)
[256@0.8]:(1609, 1591, 240)
[512@0.9]:(3221, 2829, 1540)
[1024@0.10]:(6421, 3379, 5460)
[2048@0.11]:(12889, 10439, 7560)
[4096@0.12]:(25769, 25431, 4160)
[8192@0.13]:(51481, 24569, 45240)
[16384@0.14]:(102901, 22099, 100500)
[32768@0.15]:(205957, 197245, 59268)
[65536@0.16]:(411757, 60635, 407268)
[131072@0.17]:(823553, 767775, 297928)
[262144@0.18]:(1647005, 1640043, 151276)
[524288@0.19]:(3294205, 2581387, 2046516)

py -m nn_ns.app.line_selector --begin4lineno=1 --lineno_generator='10**?' -i /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
[1@0.0]:(5, 3, 4)
[10@0.1]:(65, 33, 56)
[100@0.2]:(629, 429, 460)
[1000@0.3]:(6277, 6205, 948)
[10000@0.4]:(62849, 11649, 61760)
[100000@0.5]:(628325, 334947, 531604)
[1000000@0.6]:(6283313, 5507055, 3025288)

]]



def line_selector_(output_fmt, begin4lineno, lineno_generator_or_str__eithers___or_str, lines, /, *, to_drop_newline):
>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
>>> lines = [f'{i:0>4}\n' for i in range(31)]

[[[
_2__mk_lineno_generator
===
py -m nn_ns.app.line_selector --begin4lineno=-100 --lineno_generator='(?-10)*(?+9)' <<here_doc
0000
0001
0002
0003
0004
0005
0006
0007
0008
0009
0010
0011
0012
0013
0014
0015
0016
0017
0018
0019
0020
0021
0022
0023
0024
0025
0026
0027
0028
0029
0030
here_doc
==>>:
[-90@0.0]:0010
[-90@0.1]:0010
[-88@0.2]:0012
[-84@0.3]:0016
[-78@0.4]:0022
[-70@0.5]:0030

===
>>> show_islice_(1000, line_selector_(default_output_fmt, -100, '(?-10)*(?+9)', lines, to_drop_newline=True))
'[-90@0.0]:0010'
'[-90@0.1]:0010'
'[-88@0.2]:0012'
'[-84@0.3]:0016'
'[-78@0.4]:0022'
'[-70@0.5]:0030'

]]]
[[[
_2__mk_lineno_generator
    with spaces:
        regex4erase_spaces
multi-line_selectors:
    (j4lineno_generator,idx5j4lineno_generator)
===
py -m nn_ns.app.line_selector --begin4lineno=-100 --lineno_generator='(?-10)*(?+9)'  --lineno_generator='(?-10)*(?+9)'  --lineno_generator='(? - 80)' <<here_doc
0000
0001
0002
0003
0004
0005
0006
0007
0008
0009
0010
0011
0012
0013
0014
0015
0016
0017
0018
0019
0020
0021
0022
0023
0024
0025
0026
0027
0028
0029
0030
here_doc
==>>:
[-90@0.0]:0010
[-90@0.1]:0010
[-90@1.0]:0010
[-90@1.1]:0010
[-88@0.2]:0012
[-88@1.2]:0012
[-84@0.3]:0016
[-84@1.3]:0016
[-80@2.0]:0020
[-79@2.1]:0021
[-78@0.4]:0022
[-78@1.4]:0022
[-78@2.2]:0022
[-77@2.3]:0023
[-76@2.4]:0024
[-75@2.5]:0025
[-74@2.6]:0026
[-73@2.7]:0027
[-72@2.8]:0028
[-71@2.9]:0029
[-70@0.5]:0030
[-70@1.5]:0030
[-70@2.10]:0030

===
>>> show_islice_(1000, line_selector_(default_output_fmt, -100, '(?-10)*(?+9) ; (?-10)*(?+9) ; ? - 80', lines, to_drop_newline=True))
'[-90@0.0]:0010'
'[-90@0.1]:0010'
'[-90@1.0]:0010'
'[-90@1.1]:0010'
'[-88@0.2]:0012'
'[-88@1.2]:0012'
'[-84@0.3]:0016'
'[-84@1.3]:0016'
'[-80@2.0]:0020'
'[-79@2.1]:0021'
'[-78@0.4]:0022'
'[-78@1.4]:0022'
'[-78@2.2]:0022'
'[-77@2.3]:0023'
'[-76@2.4]:0024'
'[-75@2.5]:0025'
'[-74@2.6]:0026'
'[-73@2.7]:0027'
'[-72@2.8]:0028'
'[-71@2.9]:0029'
'[-70@0.5]:0030'
'[-70@1.5]:0030'
'[-70@2.10]:0030'

]]]
[[[
_1__mk_lineno_generator
    regex4directive4lineno_generator
        lambda4iterate
        step
        pow
===
py -m nn_ns.app.line_selector --begin4lineno=1 --lineno_generator='\x=1 -> 2*x'  --lineno_generator='20+5*?'  --lineno_generator='10+3*2**?'  <<here_doc
0000
0001
0002
0003
0004
0005
0006
0007
0008
0009
0010
0011
0012
0013
0014
0015
0016
0017
0018
0019
0020
0021
0022
0023
0024
0025
0026
0027
0028
0029
0030
here_doc
==>>:
[1@0.0]:0000
[2@0.1]:0001
[4@0.2]:0003
[8@0.3]:0007
[13@2.0]:0012
[16@0.4]:0015
[16@2.1]:0015
[20@1.0]:0019
[22@2.2]:0021
[25@1.1]:0024
[30@1.2]:0029

===
>>> show_islice_(1000, line_selector_(default_output_fmt, 1, r'\x=1 -> 2*x ; 20+5*? ; 10+3*2**?', lines, to_drop_newline=True))
'[1@0.0]:0000'
'[2@0.1]:0001'
'[4@0.2]:0003'
'[8@0.3]:0007'
'[13@2.0]:0012'
'[16@0.4]:0015'
'[16@2.1]:0015'
'[20@1.0]:0019'
'[22@2.2]:0021'
'[25@1.1]:0024'
'[30@1.2]:0029'

]]]


[[[
_1__mk_lineno_generator
    finalizer
    _mk_lambda5body_
===
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'?[0] . \x=(0,1) -> (x[1], sum(x))', lines, to_drop_newline=True))
'[0@0.0]:0000'
'[1@0.1]:0001'
'[1@0.2]:0001'
'[2@0.3]:0002'
'[3@0.4]:0003'
'[5@0.5]:0005'
'[8@0.6]:0008'
'[13@0.7]:0013'
'[21@0.8]:0021'

]]]


[[[
debug: erase_spaces_ * keyword
===
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'\x=23 -> x+1 if x<25 else x+2', lines, to_drop_newline=True))
'[23@0.0]:0023'
'[24@0.1]:0024'
'[25@0.2]:0025'
'[27@0.3]:0027'
'[29@0.4]:0029'

]]]

[[[
debug: str literal * split ';'
===
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'\x=27 -> x + len(";")', lines, to_drop_newline=True))
'[27@0.0]:0027'
'[28@0.1]:0028'
'[29@0.2]:0029'
'[30@0.3]:0030'

]]]
[[[
debug: str literal * '. \ '
debug: str literal * '->'
===
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'\x=23 -> x + len("->1")', lines, to_drop_newline=True))
'[23@0.0]:0023'
'[26@0.1]:0026'
'[29@0.2]:0029'
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'\x=21 -> x + len(".\y=0->1")', lines, to_drop_newline=True))
'[21@0.0]:0021'
'[29@0.1]:0029'

]]]
[[[
debug: str literal * '?'
===
>>> show_islice_(1000, line_selector_(default_output_fmt, 0, r'20+len("??")*? +?', lines, to_drop_newline=True))
'[20@0.0]:0020'
'[23@0.1]:0023'
'[26@0.2]:0026'
'[29@0.3]:0029'

]]]




#]]]'''
__all__ = r'''
main
    epilog
    default_output_fmt

line_selector_
    drop_newline_
    mk_output_formattor_
    select_lines_ex_
        iter_lineno_generator_
    mk_lineno_generators_
        iter_mk_lineno_generators5str_
            mk_lineno_generator5directive_str_
                regex4directive4lineno_generator
                split_directives__str_
                replace___avoid_py_str_literal_
                    split___avoid_py_str_literal_
                        split_out__py_str_literals_
                replace_ex___avoid_py_str_literal_
                    extract_old5new_idx__re_matchobj_groupdict_



'''.split()#'''
                            #regex4split_out__py_str_literal
            #erase_spaces_
            #    regex4erase_spaces
__all__

import re
from itertools import count

from seed.for_libs.for_heapq import Heap
    #def __init__(sf, heap, /, *, item5obj_, item2val_, key, __le__, reverse, obj_vs_item, applied__heapify):
from seed.iters.PeekableIterator import PeekableIterator

from seed.tiny_.check import check_int_ge
from seed.tiny import check_type_is, echo, mk_fprint, print_err
from seed.helper.safe_eval import safe_eval
from seed.text.useful_regex_patterns import py_str__pattern, py_str__regex

from seed.text.avoid_py_str_literal import (
str_ops4avoid_py_str_literal
,replace___avoid_py_str_literal_
,    split___avoid_py_str_literal_
,        split_out__py_str_literals_
,replace_ex___avoid_py_str_literal_
,    extract_old5new_idx__re_matchobj_groupdict_
)
if 0:
    from seed.text.avoid_py_str_literal import erase_spaces_, regex4erase_spaces

#class LinenoGenerator:


def iter_lineno_generator_(begin4lineno, j4lineno_generator, lineno_generator, /):
    '-> sorted-Iter (lineno, j4lineno_generator, idx5j4lineno_generator) # [lineno_generator :: sorted-Iter<lineno>][lineno :: int{>=begin4lineno}]'
    lineno_generator = iter(lineno_generator)
    pre_lineno = begin4lineno
    for idx5j4lineno_generator, lineno in enumerate(lineno_generator):
        check_int_ge(pre_lineno, lineno)
        yield (lineno, j4lineno_generator, idx5j4lineno_generator)
        pre_lineno = lineno

def _sorted_iter5lineno_generators_(begin4lineno, lineno_generators, /):
    '-> sorted-Iter (lineno, j4lineno_generator, idx5j4lineno_generator) # [lineno_generator :: sorted-Iter<lineno>][lineno :: int{>=begin4lineno}]'
    ls = [PeekableIterator(iter_lineno_generator_(begin4lineno, j4lineno_generator, g)) for j4lineno_generator, g in enumerate(lineno_generators)]
    # [heap_item =[def]= PeekableIterator<(lineno, j4lineno_generator, idx5j4lineno_generator)>]
    # [key =[def]= PeekableIterator.peek_le(1)]
    heap = Heap(ls, item5obj_=None, item2val_=None, key=lambda it:it.peek_le(1), __le__=None, reverse=False, obj_vs_item=True, applied__heapify=False)
    while ls:
        it = heap.heappop()
        if it.is_empty():
            continue
        (lineno, j4lineno_generator, idx5j4lineno_generator) = it.read1()
        yield (lineno, j4lineno_generator, idx5j4lineno_generator)
        heap.heappush(it)

def select_lines_ex_(begin4lineno, lineno_generators, lines, /):
    '-> sorted-Iter (lineno, j4lineno_generator, idx5j4lineno_generator, line) # lineno_generators[j4lineno_generator]'

    it = PeekableIterator(_sorted_iter5lineno_generators_(begin4lineno, lineno_generators))
    lineno_generators = None

    if it.is_empty():
        return
    (lineno5head, j4lineno_generator, idx5j4lineno_generator) = it.read1()
    # [lineno5head >= begin4lineno]
    assert lineno5head >= begin4lineno
    for lineno5input, line in enumerate(lines, begin4lineno):
        # [lineno5head >= lineno5input]
        assert lineno5head >= lineno5input
        while lineno5head == lineno5input:
            # [lineno5head == lineno5input]
            lineno = lineno5input
            yield (lineno, j4lineno_generator, idx5j4lineno_generator, line)
            if it.is_empty():
                return
            (lineno5head, j4lineno_generator, idx5j4lineno_generator) = it.read1()
            # [new_lineno5head >= old_lineno5head == lineno5input]
            # [lineno5head >= lineno5input]
            assert lineno5head >= lineno5input
        # [lineno5head > lineno5input]
        assert lineno5head > lineno5input
    return

def mk_output_formattor_(output_fmt, /):
    if callable(output_fmt):
        output_formattor = output_fmt
    else:
        check_type_is(str, output_fmt)
        def output_formattor(lineno, j4lineno_generator, idx5j4lineno_generator, line, /):
            return output_fmt.format(lineno, j4lineno_generator, idx5j4lineno_generator, line, lineno=lineno, j4lineno_generator=j4lineno_generator, idx5j4lineno_generator=idx5j4lineno_generator, line=line)
    return output_formattor

def drop_newline_(line, /):
    line = line.replace('\r', '\n')
    imay = line.find('\n')
    if imay >= 0:
        i = imay
        L = len(line)
        if not line[i:] == '\n'*(L-i): raise ValueError(f'bad line:multiline:{line!r}')
        line = line[:i]
    assert not '\n' in line
    return line
def line_selector_(output_fmt, begin4lineno, lineno_generator_or_str__eithers___or_str, lines, /, *, to_drop_newline):
    '-> Iter output<output_fmt>'
    output_formattor = mk_output_formattor_(output_fmt)
    lineno_generators = mk_lineno_generators_(lineno_generator_or_str__eithers___or_str)
    lines = iter(lines)

    it = select_lines_ex_(begin4lineno, lineno_generators, lines)
    lines = None
    lineno_generators = None
    begin4lineno = None
    for (lineno, j4lineno_generator, idx5j4lineno_generator, line) in it:
        if to_drop_newline:
            line = drop_newline_(line)
        yield output_formattor(lineno, j4lineno_generator, idx5j4lineno_generator, line)

#epilog:goto
if 0:
    # since 『erase_spaces_(directive4lineno_generator)』is logic-err
    ######################
    regex4directive4lineno_generator = re.compile(r'(?P<lambda4iterate>(?:(?P<finalizer>.*)[.])?[\\](?P<nm4param>\w+)=(?P<x0>.*)->(?P<body_expr>.*))|(?P<step>\d+[+]\d+[*][?])|(?P<pow>-?\d+[+]\d+[*]\d+[*][*][?])')
if 1:
    #fixed:by:replace_ex___avoid_py_str_literal_
    #bug: when str-literal in directive4lineno_generator contains '. \ ' or '->'
    ######################
    #(?x) re.X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    regex4directive4lineno_generator = re.compile(r'''(?x)
(?P<lambda4iterate>
    (?:(?P<finalizer>.*)[.])?
     \s* [\\] \s* (?P<nm4param>\w+)
        \s* = \s* (?P<x0>.*)
        \s* -> \s* (?P<body_expr>.*)
    )
|(?P<step>\d+
    \s* [+] \s* \d+
    \s* [*] \s* [?]
    )
|(?P<pow>-? \s* \d+
    \s* [+] \s* \d+
    \s* [*] \s* \d+
    \s* [*][*] \s* [?]
    )
''')#'''

if 0:
    #why dead??? whats wrong???
    ######################
    #(?x) re.X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    _unit__pattern = fr'''(?:[^'"]+|{py_str__pattern})'''
    _unit__pattern = fr'''(?:(?:[^'".]|[.](?!\s*[\\]))+|{py_str__pattern})'''
    regex4directive4lineno_generator = re.compile(fr'''(?x)
(?P<lambda4iterate>
    (?:(?P<finalizer>{_unit__pattern}+)[.])?
     \s* [\\] \s* (?P<nm4param>\w+)
        \s* = \s* (?P<x0>{_unit__pattern}+)
        \s* -> \s* (?P<body_expr>.*)
    )
|(?P<step>\d+
    \s* [+] \s* \d+
    \s* [*] \s* [?]
    )
|(?P<pow>-? \s* \d+
    \s* [+] \s* \d+
    \s* [*] \s* \d+
    \s* [*][*] \s* [?]
    )
''')#'''
    if 1:
        print_err(regex4directive4lineno_generator.pattern)
        print_err(py_str__regex.split(r'?[0] . \x=(0,1) -> (x[1], sum(x))'))
            # ok
        regex4directive4lineno_generator.fullmatch(r'?[0] . \x=(0,1) -> (x[1], sum(x))')
            # ???endless loop???
            # dead here, why?


def _1__mk_lineno_generator(x0, f, finalizer, /):
    x = x0
    while 1:
        yield finalizer(x)
        x = f(x)
def _2__mk_lineno_generator(s, /):
    f = _mk_lambda5body_(s)
    return map(f, count(0))
def _find_unused_nm_(s, /):
    for i in count(0):
        nm = f'_{i}'
        if not nm in s:
            break
    return nm
def _mk_lambda5body_(s, /):
    nm = _find_unused_nm_(s)
    ss = 'lambda ?:'+s
    if 0:
        #bug: when py_str_literal contains '?'
        expr = ss.replace('?', nm)
    else:
        expr = replace___avoid_py_str_literal_('?', nm, ss)
    expr
    f = safe_eval(expr)
    return f

def mk_lineno_generators_(lineno_generator_or_str__eithers___or_str, /):
    '(Iter (lineno_generator|str)|str) -> Iter lineno_generator'
    if type(lineno_generator_or_str__eithers___or_str) is str:
        directives__str = lineno_generator_or_str__eithers___or_str
        lineno_generator_or_str__eithers = [directives__str]
    else:
        lineno_generator_or_str__eithers = lineno_generator_or_str__eithers___or_str
    lineno_generator_or_str__eithers

    for either in lineno_generator_or_str__eithers:
        if type(either) is str:
            directives__str = either
            yield from iter_mk_lineno_generators5str_(directives__str)
        else:
            lineno_generator = either
            yield lineno_generator
    return

##def split_directives__str_(directives__str, /):
##    directive_or_blank__strs = []
##    ls4last_segment = []
##    pre_end4str = 0
##    for m in py_str__regex.finditer(directives__str):
##        begin4str, end4str = m.span(0)
##        begin4gap, end4gap = pre_end4str, begin4str
##        py_str_literal = directives__str[begin4str:end4str]
##        gap = directives__str[begin4gap:end4gap]
##        if ';' in gap:
##            tail4prev, *segment_strs4mid, init4next = gap.split(';')
##            ls4last_segment.append(tail4prev)
##            last_segment4prev = ''.join(ls4last_segment)
##            directive_or_blank__strs.append(last_segment4prev)
##            directive_or_blank__strs.extend(segment_strs4mid)
##            ls4last_segment = [init4next]
##        else:
##            ls4last_segment.append(gap)
##        ls4last_segment.append(py_str_literal)
##        ######################
##        pre_end4str = end4str
##        ######################
##    else:
##        last_gap = directives__str[pre_end4str:]
##        ls4last_segment.append(last_gap)
##        last_segment = ''.join(ls4last_segment)
##        directive_or_blank__strs.append(last_segment)
##    return directive_or_blank__strs

def split_directives__str_(directives__str, /):
    directive_or_blank__strs = split___avoid_py_str_literal_(';', directives__str)
    return directive_or_blank__strs
def iter_mk_lineno_generators5str_(directives__str, /):
    check_type_is(str, directives__str)
    if ';' in directives__str and ('"' in directives__str or "'" in directives__str):
        #fixed:raise NotImplementedError('bug: str-literal in directive4lineno_generator')
        directive_or_blank__strs = split_directives__str_(directives__str)
    else:
        directive_or_blank__strs = directives__str.split(';')
    directive_or_blank__strs

    for spaces_or_directive in directive_or_blank__strs:
        if 0:
            # bug: 『(x is y)』『(x in y)』『(x if z else y)』『(lambda x:x)』『(x and y)』『(x or y)』『(x for x in y)』
            smay_directive = erase_spaces_(spaces_or_directive)
        else:
            smay_directive = spaces_or_directive.strip()
        smay_directive

        if smay_directive:
            directive4lineno_generator = smay_directive
            lineno_generator = mk_lineno_generator5directive_str_(directive4lineno_generator)
            yield lineno_generator
    return
def mk_lineno_generator5directive_str_(directive4lineno_generator, /):
    check_type_is(str, directive4lineno_generator)
    #xxx:str-literal:assert not ';' in directive4lineno_generator
    if 0:
        s = erase_spaces_(directive4lineno_generator)
            #.replace(' ', '')
            # bug: 『(x is y)』『(x in y)』『(x if z else y)』『(lambda x:x)』『(x and y)』『(x or y)』『(x for x in y)』
    else:
        s = directive4lineno_generator
            #using new regex4directive4lineno_generator inserted『\s*』
    s = s.strip()

    #print_err(s)
    if 0:
        # bug: when py_str_literal contains '.\ ' or '->'
        m = regex4directive4lineno_generator.fullmatch(s)
    else:
        old_s = s
        s = None
        (new_idx2old_idx, new_s) = replace_ex___avoid_py_str_literal_(old_s)
        m = regex4directive4lineno_generator.fullmatch(new_s)
        if m:
            d = extract_old5new_idx__re_matchobj_groupdict_(old_s, new_idx2old_idx, m)
            m = d
            assert m
        s = old_s


    if not m:
        if '?' in s:
            # superset of "step/pow"
            return _2__mk_lineno_generator(s)
        raise ValueError(f'bad format:directive4lineno_generator:{directive4lineno_generator!r}')

    if m['lambda4iterate']:
        finalizer = m['finalizer']
        nm4param = m['nm4param']
        x0 = m['x0']
        body_expr = m['body_expr']
        x0 = safe_eval(f'{x0}')
        f = safe_eval(f'lambda {nm4param}: {body_expr}')
        finalizer = echo if not finalizer else _mk_lambda5body_(finalizer)
    elif m['step']:
        s_, t = s.split('*')
        assert t == '?'
        x0, step = s_.split('+')
        x0 = int(x0)
        step = int(step)
        f = step.__add__
        finalizer = echo
    elif m['pow']:
        s_, t = s.split('**')
        assert t == '?'
        s__, base = s_.split('*')
        offset, scale = s__.split('+')
        base = int(base)
        scale = int(scale)
        offset = int(offset)
        x0 = scale
        f = base.__mul__
        finalizer = offset.__add__
    else:
        raise 000
    x0, f, finalizer
    return _1__mk_lineno_generator(x0, f, finalizer)


#regex4directive4lineno_generator:goto
epilog = r'''
example<lineno_generator>:
    #######################
    # iterate f x0
    #   f(f(...f(x0)))
    '\x=1 -> 10*x'
        => [1, 10, 100, 1000, ...]
    #######################
    # map finalizer $ iterate f x0
    #   finalizer(f(f(...f(x0))))
    '?[0] . \x=(0,1) -> (x[1], sum(x))'
        => [0, 1, 1, 2, 3, 5, 8, 13, 21, ...]
    #######################
    # map lineno5idx_ [0..]
    '1+2*?'
        => [1, 3, 5, 7, ...]
    '-1+2*3**?'
        => [1, 5, 17, 53, ...]
    '(?+1) * ?'
        => [0, 2, 6, 12, ...]
    #######################

'''#'''
#output_fmt
default_output_fmt = '[{lineno}@{j4lineno_generator}.{idx5j4lineno_generator}]:{line!s}'
def main(args=None, /):
    import argparse
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='select lines from given lineno'
        , epilog=epilog
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--begin4lineno', type=int, default=0
                        , help='set lineno<start_line>')
    parser.add_argument('--output_fmt', type=str, default=default_output_fmt
                        , help='output format #[output_fmt_str.format :: (*[lineno, j4lineno_generator, idx5j4lineno_generator, line], **{lineno=?, j4lineno_generator=?, idx5j4lineno_generator=?, line=?}) -> str]')
    parser.add_argument('--lineno_generator', type=str, action='append', default=[]
                        , help='directive to indicate howto generate linenos of selected lines; multi-directive can be seperated by ";"')


    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    begin4lineno = args.begin4lineno
    output_fmt = args.output_fmt
    strs8lineno_generators = args.lineno_generator
    str8lineno_generators = ';'.join(strs8lineno_generators)
    strs8lineno_generators = None

    may_ifname = args.input
    with open4r(may_ifname, xencoding=iencoding) as fin:
        lines = iter(fin)
        it = line_selector_(output_fmt, begin4lineno, str8lineno_generators, lines, to_drop_newline=True)

        may_ofname = args.output
        with open4w(may_ofname, force=force, xencoding=oencoding) as fout:
            fprint = mk_fprint(fout)
            for r in it:
                fprint(r)
                #fprint(repr(r)) ==>> +to_drop_newline

__all__



from nn_ns.app.line_selector import *
if __name__ == "__main__":
    main()


