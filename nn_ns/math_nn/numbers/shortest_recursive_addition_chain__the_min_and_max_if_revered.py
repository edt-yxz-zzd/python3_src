#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_recursive_addition_chain__the_min_and_max_if_revered.py
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py

nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered:__doc__ -ht # -ff -df

[[
[shortest_recursive_addition_chain <: shortest_addition_chain]
but:
    [MAY_NOT:[revmin_shortest_recursive_addition_chain == revmin_shortest_addition_chain]]
    [MAY_NOT:[revmax_shortest_recursive_addition_chain == revmax_shortest_addition_chain]]

===
注意:已有更新版:
    这里是:无缺版
    已有:无缺深一版，无缺精深版...
===
view script/min_add_ver4__pseudo_addition_chain.py
    =>:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_recursive_addition_chain__the_min_and_max_if_revered.py
        le12021
        最短短程加链:反向最小+反向最大
        注意:『短程』
        [最短短程加链 <: 最短加链]
        但 相应反向极值 则不一定等同

vs:
view script/搜索冫最短加链长度.py
    =>:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py
        le4333
        最短加链:正向最大

===
prepare:
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(30,30)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.min_add_ver4__pseudo_addition_chain   ,12022:枚举冫相关信息纟最短短程加链牜简并态算法扌  +rename_NonTouchRanges +尝试补充缺失 --path:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,str._提取另档冫加链扌 --路径纟无缺版:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt  > script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
tar -cvf script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
cp -iv script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma   ../../python3_src/nn_ns/math_nn/numbers/shortest_recursive_addition_chain__the_min_and_max_if_revered.py..data.le12021.tar.lzma

===
]]

py_adhoc_call   nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered   @f
]]]'''#'''
__all__ = r'''
pint2revmin_shortest_recursive_addition_chain
pint2revmax_shortest_recursive_addition_chain

pint2revmin_shortest_recursive_addition_chain__first_12021_terms
pint2revmax_shortest_recursive_addition_chain__first_12021_terms

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
from io import BytesIO
from ast import literal_eval

from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
___end_mark_of_excluded_global_names__0___ = ...



_pint2revmin_revmax = tuple(tuple(us)
for us in map(literal_eval, iter_read_solo_tarfile_
    (BytesIO(read_under_pkg_
        (__package__
        , 'shortest_recursive_addition_chain__the_min_and_max_if_revered.py..data.le12021.tar.lzma'
        , xencoding=None
        ))
    , xencoding4data='ascii'
    ))
)
pint2revmin_shortest_recursive_addition_chain__first_12021_terms = (None, *_pint2revmin_revmax[2::2])
pint2revmax_shortest_recursive_addition_chain__first_12021_terms = (None, *_pint2revmin_revmax[3::2])
del _pint2revmin_revmax

assert len(pint2revmin_shortest_recursive_addition_chain__first_12021_terms) == 1+12021
assert len(pint2revmax_shortest_recursive_addition_chain__first_12021_terms) == 1+12021

assert pint2revmin_shortest_recursive_addition_chain__first_12021_terms[1][-1] == 1
assert pint2revmin_shortest_recursive_addition_chain__first_12021_terms[12021][-1] == 12021

assert pint2revmax_shortest_recursive_addition_chain__first_12021_terms[1][-1] == 1
assert pint2revmax_shortest_recursive_addition_chain__first_12021_terms[12021][-1] == 12021

pint2revmin_shortest_recursive_addition_chain = pint2revmin_shortest_recursive_addition_chain__first_12021_terms
pint2revmax_shortest_recursive_addition_chain = pint2revmax_shortest_recursive_addition_chain__first_12021_terms

#view others/数学/最小加法链.txt
    #[存在反例382==191*2,最少加法(382)==11==最少加法(191)]
    #[存在反例513=171*3,最少加法(513)==10==最少加法(171)]

assert len(pint2revmin_shortest_recursive_addition_chain[191*2]) == 1+11 ==  len(pint2revmin_shortest_recursive_addition_chain[191])
assert len(pint2revmin_shortest_recursive_addition_chain[171*3]) == 1+10 ==  len(pint2revmin_shortest_recursive_addition_chain[171])
assert pint2revmin_shortest_recursive_addition_chain[191*2] == (1, 2, 4, 8, 16, 17, 33, 50, 83, 166, 332, 382)
assert pint2revmin_shortest_recursive_addition_chain[191] == (1, 2, 4, 8, 16, 18, 34, 52, 53, 87, 139, 191)
assert pint2revmin_shortest_recursive_addition_chain[171*3] == (1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513)
assert pint2revmin_shortest_recursive_addition_chain[171] == (1, 2, 3, 5, 10, 11, 21, 42, 84, 87, 171)

assert pint2revmax_shortest_recursive_addition_chain[191*2] == (1, 2, 4, 5, 9, 14, 23, 46, 92, 184, 368, 382)
assert pint2revmax_shortest_recursive_addition_chain[191] == (1, 2, 4, 6, 10, 20, 40, 46, 92, 184, 190, 191)
assert pint2revmax_shortest_recursive_addition_chain[171*3] == (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513)
assert pint2revmax_shortest_recursive_addition_chain[171] == (1, 2, 4, 8, 10, 20, 40, 80, 160, 170, 171)

__all__
from nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered import pint2revmin_shortest_recursive_addition_chain, pint2revmax_shortest_recursive_addition_chain

from nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered import pint2revmin_shortest_recursive_addition_chain__first_12021_terms, pint2revmax_shortest_recursive_addition_chain__first_12021_terms

from nn_ns.math_nn.numbers.shortest_recursive_addition_chain__the_min_and_max_if_revered import *
