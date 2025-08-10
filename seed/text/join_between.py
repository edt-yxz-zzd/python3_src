#__all__:goto
r'''[[[
e ../../python3_src/seed/text/join_between.py

seed.text.join_between
py -m nn_ns.app.debug_cmd   seed.text.join_between -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.text.join_between:__doc__ -ht # -ff -df

[[
used by:
view ../lots/NOTE/unicode/cjk/汉字区分区表.txt
]]


>>> join_between(*'一丨')
'一丁丂七丄丅丆万丈三上下丌不与丏丐丑丒专且丕世丗丘丙业丛东丝丞丟丠両丢丣两严並丧丨'
>>> join_between_ex(*'一丨')
((19968, 20008), '一丁丂七丄丅丆万丈三上下丌不与丏丐丑丒专且丕世丗丘丙业丛东丝丞丟丠両丢丣两严並丧丨')


py_adhoc_call   seed.text.join_between   @join_between  :一 :龥
py_adhoc_call   seed.text.join_between   @join_between  :一 :丨

]]]'''#'''
__all__ = r'''
join_between
    join_between_ex
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


def join_between(c0, c1, /):
    (j01, cs) = join_between_ex(c0, c1)
    return cs
def join_between_ex(c0, c1, /):
    j0 = ord(c0)
    j1 = ord(c1)
    ws = range(j0,j1+1)
    cs = ''.join(map(chr,ws))
    return ((j0, j1), cs)

__all__
from seed.text.join_between import join_between, join_between_ex
from seed.text.join_between import *
