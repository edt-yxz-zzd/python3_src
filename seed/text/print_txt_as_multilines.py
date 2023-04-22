#__all__:goto
r"""[[[
e ../../python3_src/seed/text/print_txt_as_multilines.py

used in:
    view ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简.py
    py -m   nn_ns.CJK.CJK_data.汉字繁简 -sz 16 -py

seed.text.print_txt_as_multilines
py -m nn_ns.app.debug_cmd   seed.text.print_txt_as_multilines -x
py -m nn_ns.app.doctest_cmd seed.text.print_txt_as_multilines:__doc__ -ff -v
py_adhoc_call   seed.text.print_txt_as_multilines   @f



>>> from seed.text.print_txt_as_multilines import print_txt_without_space_as_py_src_varable_, print_txt_as_multilines_

>>> print_txt_as_multilines_(None, -1, '012345678901234567890123456789')
012345678901234567890123456789
>>> print_txt_as_multilines_(None, 0, '012345678901234567890123456789')
012345678901234567890123456789
>>> print_txt_as_multilines_(None, 10, '012345678901234567890123456789')
0123456789
0123456789
0123456789
>>> print_txt_as_multilines_(None, 1, '012')
0
1
2
>>> print_txt_as_multilines_(None, 20, '012345678901234567890123456789')
01234567890123456789
0123456789







>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'a')
a = ''.join(r'''
0
1
2
'''.split())#'''
assert len(a) == 3
#end:a:3
<BLANKLINE>
>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'b')
b = ''.join(r'''
3
4
5
'''.split())#'''
assert len(b) == 3
#end:b:3
<BLANKLINE>
>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'c')
Traceback (most recent call last):
    ...
ValueError: contains spaces
>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'a', 'z')
z = ''.join(r'''
0
1
2
'''.split())#'''
assert len(z) == 3
#end:z:3
<BLANKLINE>
>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'a', 'b')
b = ''.join(r'''
0
1
2
'''.split())#'''
assert len(b) == 3
#end:b:3
<BLANKLINE>
>>> print_txt_without_space_as_py_src_varable_(None, 1, dict(a='012', b='345', c='6 8'), 'a', 'b', to_show_assert_len=False)
b = ''.join(r'''
0
1
2
'''.split())#'''
#end:b:3
<BLANKLINE>



>>> b = ''.join(r'''
... 0
... 1
... 2
... '''.split())#'''
>>> assert len(b) == 3
>>> b
'012'



#]]]"""
__all__ = r'''
    print_txt_without_space_as_py_src_varable_
    print_txt_as_multilines_
'''.split()#'''
__all__


from seed.iters.icut_to import icut_to, icut_seq_to
from seed.text.contains_spaces import contains_spaces, check_contains_no_spaces
from seed.tiny import check_type_is, mk_fprint#, ifNone


def print_txt_without_space_as_py_src_varable_(ofile, sz4row, nm2var, nm4txt, alias=None, /, *, to_show_assert_len=True):
    fprint = mk_fprint(ofile)

    if not alias:
        alias = nm4txt

    txt = nm2var[nm4txt]
    check_contains_no_spaces(txt)

    nm = alias
    fprint(f"{nm} = ''.join(r'''")
    print_txt_as_multilines_(ofile, sz4row, txt)
    fprint(f"'''.split())#'''")
    if to_show_assert_len:
        fprint(f'assert len({nm}) == {len(txt)}')

    fprint(f"#end:{nm}:{len(txt)}\n")
    return
    fprint(f"{nm} = r'''")
    print_txt_as_multilines_(ofile, sz4row, txt)
    fprint(f"'''#'''")
    fprint(f"{nm} = ''.join({nm}.split())\n\n")
    return
def print_txt_as_multilines_(ofile, sz4row, txt, /):
    fprint = mk_fprint(ofile)

    if sz4row > 0:
        irows = icut_seq_to(txt, sz4row)
    else:
        irows = [txt]

    for row in irows:
        fprint(row)



from seed.text.print_txt_as_multilines import print_txt_without_space_as_py_src_varable_, print_txt_as_multilines_
from seed.text.print_txt_as_multilines import *
