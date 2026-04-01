#__all__:goto
#TODO:goto
r'''[[[
e ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py

seed.recognize.text_recognizer.ITextRecognizer__doctest
#py -m nn_ns.app.debug_cmd   seed.recognize.text_recognizer.ITextRecognizer__doctest -x # -off_defs
py -m nn_ns.app.debug_cmd   seed.recognize.text_recognizer.ITextRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.ITextRecognizer__doctest:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'




%s/^\(>>> \)\(\<parse_text_\>(.*, \)None\(, '[^']*', \d*, \d*)\)$/\1_\2env\3
>>> _parse_text_ = parse_text_

_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq = IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
#>>> env = None

_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq = IOps4oresult_seq4cased_flow_txt_rgnr__using_env_ops4oresult_seq__env_is_mapping
env4ops4oresult_seq__ftSeq
env4ops4oresult_seq__list
>>> env = env4ops4oresult_seq__ftSeq
>>> env = env4ops4oresult_seq__list

################




################

>>> OResult(oresult=999, end=666)
OResult(999, 666)
>>> OResult(999, 666)
OResult(999, 666)
>>> match OResult(999, 666):
...     case OResult():
...         print('ok')
ok
>>> match OResult(999, 666):
...     case OResult(end=x):
...         print(x)
666
>>> match OResult(999, 666):
...     case OResult(x):
...         print(x)
999
>>> match OResult(999, 666):
...     case OResult(x, y):
...         print((x, y))
(999, 666)
>>> match 1:
...     case True:
...         print('bad')
...     case 1:
...         print('o....k')
o....k
>>> match True:
...     case 1:
...         print('ok')
ok
>>> match 1:
...     case bool(x):
...         print('bad')
...     case int(x):
...         print('ok')
ok
>>> match True:
...     case int(x):
...         print('oooo!!!!!')
oooo!!!!!
>>> match True:
...     case bool(x):
...         print('ok')
ok

>>> Errmsg(errmsg='eof', end=666, severe=False)
Errmsg('eof', 666, False)
>>> Errmsg('eof', 666, False)
Errmsg('eof', 666, False)


>>> OResult(999, 666).ok
True
>>> Errmsg('eof', 666, True).ok
False
>>> Errmsg('eof', 666, True).severe
True
>>> Errmsg('eof', 666, True)._replace(severe=False, end=555)
Errmsg('eof', 555, False)

>>> isinstance(OResult(999, 666), ParseResult)
True
>>> isinstance(Errmsg('eof', 666, False), ParseResult)
True


################
#see:mk_txt_rgnr__regex_/TextRecognizer__regex
xget_groups5re_match_
check_may_group_or_groups_
>>> import re
>>> rgx = re.compile(r'(aa)(?P<xx>bb)')
>>> rgx
re.compile('(aa)(?P<xx>bb)')
>>> check_may_group_or_groups_(rgx, None)
>>> check_may_group_or_groups_(rgx, '1..')
>>> check_may_group_or_groups_(rgx, 'xx')
>>> check_may_group_or_groups_(rgx, 0)
>>> check_may_group_or_groups_(rgx, 1)
>>> check_may_group_or_groups_(rgx, 2)
>>> check_may_group_or_groups_(rgx, 3)
Traceback (most recent call last):
    ...
TypeError: 3
>>> check_may_group_or_groups_(rgx, -1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> check_may_group_or_groups_(rgx, '')
Traceback (most recent call last):
    ...
TypeError: (mappingproxy({'xx': 2}), '', re.compile('(aa)(?P<xx>bb)'))
>>> check_may_group_or_groups_(rgx, 'yy')
Traceback (most recent call last):
    ...
TypeError: (mappingproxy({'xx': 2}), 'yy', re.compile('(aa)(?P<xx>bb)'))
>>> check_may_group_or_groups_(rgx, ())
>>> check_may_group_or_groups_(rgx, (0, 1, 2, (None, 'xx', '1..', ())))
>>> m = rgx.match('aabbcc')
>>> m
<re.Match object; span=(0, 4), match='aabb'>
>>> xget_groups5re_match_(m, None) is m
True
>>> xget_groups5re_match_(m, '1..')
('aa', 'bb')
>>> xget_groups5re_match_(m, 'xx')
'bb'
>>> xget_groups5re_match_(m, 2)
'bb'
>>> xget_groups5re_match_(m, 1)
'aa'
>>> xget_groups5re_match_(m, 0)
'aabb'
>>> xget_groups5re_match_(m, ())
()
>>> xget_groups5re_match_(m, (0, 1, 2, (None, 'xx', '1..', ())))
('aabb', 'aa', 'bb', (<re.Match object; span=(0, 4), match='aabb'>, 'bb', ('aa', 'bb'), ()))

################
>>> env = env4ops4oresult_seq__list

TextRecognizer__constant_oresult
TextRecognizer__constant_errmsg
TextRecognizer__constant_text
TextRecognizer__regex
>>> TextRecognizer__constant_oresult(999)
TextRecognizer__constant_oresult(999)
>>> _parse_text_(TextRecognizer__constant_oresult(999), env, 'xxx', 0, 3)
OResult(999, 0)

>>> TextRecognizer__constant_errmsg('fail', True)
TextRecognizer__constant_errmsg('fail', True)
>>> _parse_text_(TextRecognizer__constant_errmsg('fail', True), env, 'xxx', 0, 3)
Errmsg('fail', 0, True)


>>> TextRecognizer__constant_text('aaabbbccc')
TextRecognizer__constant_text('aaabbbccc')
>>> _parse_text_(TextRecognizer__constant_text('aaabbbccc'), env, 'aaabbbccc', 0, 9)
OResult('aaabbbccc', 9)
>>> _parse_text_(TextRecognizer__constant_text('aaabbbccc'), env, 'aaabbbcccxxx', 0, 12)
OResult('aaabbbccc', 9)
>>> _parse_text_(TextRecognizer__constant_text('aaabbbccc'), env, 'xxxaaabbbcccxxx', 0, 15)
Errmsg(('unmatched:NE', 'aaabbbccc', 'xxxaaabbb'), 0, False)
>>> _parse_text_(TextRecognizer__constant_text('aaabbbccc'), env, 'xxxaaabbbcccxxx', 3, 15)
OResult('aaabbbccc', 12)

>>> TextRecognizer__regex('a+b+c+')
TextRecognizer__regex(re.compile('a+b+c+'))
>>> _parse_text_(TextRecognizer__regex('a+b+c+'), env, 'xxxaaabbbcccxxx', 0, 15)
Errmsg(('unmatched:', re.compile('a+b+c+')), 0, False)
>>> _parse_text_(TextRecognizer__regex('a+b+c+'), env, 'xxxaaabbbcccxxx', 3, 15)
OResult(<re.Match object; span=(3, 12), match='aaabbbccc'>, 12)

>>> TextRecognizer__regex('a+b+c+', 0)
TextRecognizer__regex(re.compile('a+b+c+'), 0)
>>> _parse_text_(TextRecognizer__regex('a+b+c+', 0), env, 'xxxaaabbbcccxxx', 3, 15)
OResult('aaabbbccc', 12)


TextRecognizer__postprocess6ok
    TextRecognizer__postprocess6oresult
    TextRecognizer__tag
TextRecognizer__postprocess6ko
    TextRecognizer__postprocess6errmsg
    TextRecognizer__named
TextRecognizer__unbox
TextRecognizer__getitem
TextRecognizer__box
TextRecognizer__to_tuple
TextRecognizer__to_finger_tree_seq
>>> TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), hex)
TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), <built-in function hex>)
>>> _parse_text_(TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), hex), env, '', 0, 0)
OResult('0x3e7', 0)

>>> TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 1, hex)
TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 1, <built-in function hex>)
>>> _parse_text_(TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 1, hex), env, '', 0, 0)
OResult('0x3e7', 0)
>>> TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 0, lambda:666)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 0, <function <lambda> at 0x...>)
>>> _parse_text_(TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), 0, lambda:666), env, '', 0, 0)
OResult(666, 0)
>>> TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), -1, 666)
TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), -1, 666)
>>> _parse_text_(TextRecognizer__postprocess6oresult(TextRecognizer__constant_oresult(999), -1, 666), env, '', 0, 0)
OResult(666, 0)

>>> TextRecognizer__tag(666, TextRecognizer__constant_oresult(999))
TextRecognizer__tag(666, TextRecognizer__constant_oresult(999))
>>> _parse_text_(TextRecognizer__tag(666, TextRecognizer__constant_oresult(999)), env, '', 0, 0)
OResult((666, 999), 0)

>>> TextRecognizer__postprocess6ko(TextRecognizer__constant_errmsg(999, True), lambda errmsg, severe, /:((666, errmsg, severe), False))  #doctest: +ELLIPSIS
TextRecognizer__postprocess6ko(TextRecognizer__constant_errmsg(999, True), <function <lambda> at 0x...>)
>>> _parse_text_(TextRecognizer__postprocess6ko(TextRecognizer__constant_errmsg(999, True), lambda errmsg, severe, /:((666, errmsg, severe), False)), env, '', 0, 0)
Errmsg((666, 999, True), 0, False)

>>> TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), 2, lambda errmsg, severe, /:(666, errmsg, severe))  #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), 2, <function <lambda> at 0x...>)
>>> _parse_text_(TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), 2, lambda errmsg, severe, /:(666, errmsg, severe)), env, '', 0, 0)
Errmsg((666, 999, True), 0, True)
>>> _parse_text_(TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), 1, lambda errmsg, /:(666, errmsg)), env, '', 0, 0)
Errmsg((666, 999), 0, True)
>>> _parse_text_(TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), 0, lambda:666), env, '', 0, 0)
Errmsg(666, 0, True)
>>> _parse_text_(TextRecognizer__postprocess6errmsg(TextRecognizer__constant_errmsg(999, True), -1, 666), env, '', 0, 0)
Errmsg(666, 0, True)

>>> TextRecognizer__named(True, '[33]', TextRecognizer__constant_errmsg(999, True))
TextRecognizer__named(True, '[33]', ...)
>>> TextRecognizer__named(True, '.attr', TextRecognizer__constant_errmsg(999, True))
TextRecognizer__named(True, '.attr', ...)
>>> TextRecognizer__named(False, 'anm', TextRecognizer__constant_errmsg(999, True))
TextRecognizer__named(False, 'anm', ...)
>>> print(TextRecognizer__named(False, 'anm', TextRecognizer__constant_errmsg(999, True)))
TextRecognizer__named(False, 'anm', TextRecognizer__constant_errmsg(999, True))
>>> _parse_text_(TextRecognizer__named(False, 'anm', TextRecognizer__constant_errmsg(999, True)), env, '', 0, 0)
Errmsg((False, 'anm', 999), 0, True)

>>> TextRecognizer__unbox(TextRecognizer__constant_oresult((999,)))
TextRecognizer__unbox(TextRecognizer__constant_oresult((999,)))
>>> _parse_text_(TextRecognizer__unbox(TextRecognizer__constant_oresult((999,))), env, '', 0, 0)
OResult(999, 0)

>>> TextRecognizer__getitem(TextRecognizer__constant_oresult(range(999)), slice(77, 99))
TextRecognizer__getitem(TextRecognizer__constant_oresult(range(0, 999)), slice(77, 99, None))
>>> _parse_text_(TextRecognizer__getitem(TextRecognizer__constant_oresult(range(999)), slice(77, 99)), env, '', 0, 0)
OResult(range(77, 99), 0)


>>> TextRecognizer__box(TextRecognizer__constant_oresult(999))
TextRecognizer__box(TextRecognizer__constant_oresult(999))
>>> _parse_text_(TextRecognizer__box(TextRecognizer__constant_oresult(999)), env, '', 0, 0)
OResult((999,), 0)

>>> TextRecognizer__to_tuple(TextRecognizer__constant_oresult('678'))
TextRecognizer__to_tuple(TextRecognizer__constant_oresult('678'))
>>> _parse_text_(TextRecognizer__to_tuple(TextRecognizer__constant_oresult('678')), env, '', 0, 0)
OResult(('6', '7', '8'), 0)

>>> TextRecognizer__to_finger_tree_seq(TextRecognizer__constant_oresult('678'))
TextRecognizer__to_finger_tree_seq(TextRecognizer__constant_oresult('678'))
>>> _parse_text_(TextRecognizer__to_finger_tree_seq(TextRecognizer__constant_oresult('678')), env, '', 0, 0)
OResult(Seq(['6', '7', '8']), 0)


TextRecognizer__trial
TextRecognizer__fallback
TextRecognizer__enclosed
>>> TextRecognizer__trial(TextRecognizer__constant_errmsg('fail', True))
TextRecognizer__trial(TextRecognizer__constant_errmsg('fail', True))
>>> _parse_text_(TextRecognizer__trial(TextRecognizer__constant_errmsg('fail', True)), env, 'xxx', 0, 3)
Errmsg('fail', 0, False)

>>> TextRecognizer__fallback([TextRecognizer__constant_errmsg('fail', True), TextRecognizer__constant_oresult(999)])
TextRecognizer__fallback((TextRecognizer__constant_errmsg('fail', True), TextRecognizer__constant_oresult(999)))
>>> _parse_text_(TextRecognizer__fallback([TextRecognizer__constant_errmsg('fail', True), TextRecognizer__constant_oresult(999)]), env, 'xxx', 0, 3)
Errmsg('fail', 0, True)
>>> _parse_text_(TextRecognizer__fallback([TextRecognizer__constant_oresult(999), TextRecognizer__constant_errmsg('fail', True)]), env, 'xxx', 0, 3)
OResult(999, 0)
>>> _parse_text_(TextRecognizer__fallback([TextRecognizer__trial(TextRecognizer__constant_errmsg('fail', True)), TextRecognizer__constant_oresult(999)]), env, 'xxx', 0, 3)
OResult(999, 0)
>>> _parse_text_(TextRecognizer__fallback([TextRecognizer__constant_errmsg('fail', False), TextRecognizer__constant_oresult(999)]), env, 'xxx', 0, 3)
OResult(999, 0)
>>> _parse_text_(TextRecognizer__fallback([TextRecognizer__constant_errmsg('fail', False), TextRecognizer__constant_errmsg('eof', False)]), env, 'xxx', 0, 3)
Errmsg((Errmsg('fail', 0, False), Errmsg('eof', 0, False)), 0, False)
>>> _parse_text_(TextRecognizer__fallback([]), env, 'xxx', 0, 3)
Errmsg((), 0, False)


>>> TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
>>> _parse_text_(TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '66', 0, 2)
Errmsg(('unmatched:EOF', '666', 3, 2), 0, False)
>>> _parse_text_(TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '665', 0, 3)
Errmsg(('unmatched:NE', '666', '665'), 0, False)
>>> _parse_text_(TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666', 0, 3)
Errmsg(('unmatched:EOF', '111', 3, 0), 3, True)
>>> _parse_text_(TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult('111', 9)
>>> _parse_text_(TextRecognizer__enclosed(TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111997', 0, 9)
Errmsg(('unmatched:NE', '999', '997'), 6, True)


TextRecognizer__serial
TextRecognizer__sep_end_by
TextRecognizer__sep_by
TextRecognizer__end_by
TextRecognizer__many
>>> TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')])
TextRecognizer__serial((TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')))
>>> _parse_text_(TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')]), env, '666999', 0, 6)
OResult(('666', '999'), 6)
>>> _parse_text_(TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')]), env, '666997', 0, 6)
Errmsg(('unmatched:NE', '999', '997'), 3, True)

>>> TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
OResult(('666', '999'), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '999666', 0, 6)
OResult(('999',), 3)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 6)
Errmsg(('unmatched:EOF', '111', 3, 0), 6, True)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(('666', '111', '999'), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111111999', 0, 15)
OResult(('666', '111', '111', '111', '999'), 15)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '999666', 0, 6)
Errmsg(('unmatched:NE', '666', '999'), 0, False)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
OResult(('666', '999'), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
Errmsg(('unmatched:NE', '111', '999'), 3, True)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(('666', '111', '999'), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(2, 2, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(('666', '111', '999'), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(2, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(('666', '111', '111', '999'), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(3, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(('666', '111', '111', '999'), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(0, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(('666', '111', '111', '999'), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(0, 2, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
Errmsg(('unmatched:NE', '999', '111'), 6, True)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('6')), env, '666111999', 0, 9)
OResult(('6',), 1)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('1')), env, '666111999', 0, 9)
OResult(('666', '1'), 4)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('1119')), env, '666111999', 0, 9)
OResult(('666', '1119'), 7)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('111')), env, '666111999', 0, 9)
OResult(('666', '111'), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(('123',), 3)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(('123', '123'), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(('123', '123', '123'), 9)

>>> TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1'))
TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1'))
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1', '1', '1'), 4)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(('6', '1'), 2)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
OResult(('6',), 1)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, 'x111', 0, 4)
OResult((), 0)
>>> _parse_text_(TextRecognizer__sep_by(1, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, 'x111', 0, 4)
Errmsg(('unmatched:NE', '6', 'x'), 0, False)
>>> _parse_text_(TextRecognizer__sep_by(1, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
OResult(('6',), 1)
>>> _parse_text_(TextRecognizer__sep_by(2, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
Errmsg(('unmatched:NE', '1', 'x'), 1, True)
>>> _parse_text_(TextRecognizer__sep_by(2, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(('6', '1'), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(('6', '1'), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1'), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1', '1'), 3)
>>> _parse_text_(TextRecognizer__sep_by(3, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1', '1'), 3)
>>> _parse_text_(TextRecognizer__sep_by(0, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1', '1'), 3)
>>> _parse_text_(TextRecognizer__sep_by(0, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6', '1'), 2)
>>> _parse_text_(TextRecognizer__sep_by(0, 1, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(('6',), 1)
>>> _parse_text_(TextRecognizer__sep_by(0, 0, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult((), 0)


>>> TextRecognizer__end_by(0, None, TextRecognizer__constant_text('a'), TextRecognizer__constant_text('b'))
TextRecognizer__end_by(0, None, TextRecognizer__constant_text('a'), TextRecognizer__constant_text('b'))
>>> _parse_text_(TextRecognizer__end_by(0, None, TextRecognizer__constant_text('a'), TextRecognizer__constant_text('b')), env, 'aaab', 0, 4)
OResult(('a', 'a', 'a', 'b'), 4)


>>> TextRecognizer__many(0, None, TextRecognizer__constant_text('a'))
TextRecognizer__many(0, None, TextRecognizer__constant_text('a'))
>>> _parse_text_(TextRecognizer__many(0, None, TextRecognizer__constant_text('a')), env, 'aaab', 0, 4)
OResult(('a', 'a', 'a'), 3)


mk_tagged_txt_rgnr_
mk_tagged_txt_rgnr_fallback_
mk_ignorable_txt_rgnr_serial_
>>> mk_tagged_txt_rgnr_(999, TextRecognizer__constant_text('abc123'))
TextRecognizer__tag(999, TextRecognizer__constant_text('abc123'))

TextRecognizer__serial((TextRecognizer__constant_oresult(999), TextRecognizer__constant_text('abc123')))

>>> _parse_text_(mk_tagged_txt_rgnr_(999, TextRecognizer__constant_text('abc123')), env, 'abc123', 0, 6)
OResult((999, 'abc123'), 6)

>>> mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))])
TextRecognizer__fallback((TextRecognizer__tag(666, TextRecognizer__constant_text('bbb')), TextRecognizer__tag(999, TextRecognizer__constant_text('qqq'))))

TextRecognizer__fallback((TextRecognizer__serial((TextRecognizer__constant_oresult(666), TextRecognizer__constant_text('bbb'))), TextRecognizer__serial((TextRecognizer__constant_oresult(999), TextRecognizer__constant_text('qqq')))))

>>> _parse_text_(mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))]), env, 'bbb', 0, 3)
OResult((666, 'bbb'), 3)
>>> _parse_text_(mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))]), env, 'qqq', 0, 3)
OResult((999, 'qqq'), 3)

>>> mk_ignorable_txt_rgnr_serial_([(False, TextRecognizer__constant_text('x')), (False, TextRecognizer__constant_text('y')), (True, TextRecognizer__constant_text('1')), (False, TextRecognizer__constant_text('z')), (True, TextRecognizer__constant_text('2')), (True, TextRecognizer__constant_text('3'))])
TextRecognizer__serial__cased((TextRecognizer__tag(1, TextRecognizer__constant_text('x')), TextRecognizer__tag(1, TextRecognizer__constant_text('y')), TextRecognizer__tag(0, TextRecognizer__constant_text('1')), TextRecognizer__tag(1, TextRecognizer__constant_text('z')), TextRecognizer__tag(0, TextRecognizer__constant_text('2')), TextRecognizer__tag(0, TextRecognizer__constant_text('3'))))

TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('x'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('y'))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('1'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('z'))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('2'))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('3')))))

>>> _parse_text_(mk_ignorable_txt_rgnr_serial_([(False, TextRecognizer__constant_text('x')), (False, TextRecognizer__constant_text('y')), (True, TextRecognizer__constant_text('1')), (False, TextRecognizer__constant_text('z')), (True, TextRecognizer__constant_text('2')), (True, TextRecognizer__constant_text('3'))]), env, 'xy1z23', 0, 6)
OResult(('x', 'y', 'z'), 6)
>>> mk_ignorable_txt_rgnr_serial_([(False, TextRecognizer__constant_text('x')), (False, TextRecognizer__constant_text('y')), (False, TextRecognizer__constant_text('z'))])
TextRecognizer__serial((TextRecognizer__constant_text('x'), TextRecognizer__constant_text('y'), TextRecognizer__constant_text('z')))
>>> _parse_text_(mk_ignorable_txt_rgnr_serial_([(False, TextRecognizer__constant_text('x')), (False, TextRecognizer__constant_text('y')), (False, TextRecognizer__constant_text('z'))]), env, 'xyz', 0, 3)
OResult(('x', 'y', 'z'), 3)
>>> mk_ignorable_txt_rgnr_serial_([(True, TextRecognizer__constant_text('1')), (True, TextRecognizer__constant_text('2')), (True, TextRecognizer__constant_text('3'))])
TextRecognizer__enclosed(TextRecognizer__serial((TextRecognizer__constant_text('1'), TextRecognizer__constant_text('2'), TextRecognizer__constant_text('3'))), TextRecognizer__constant_oresult(()), TextRecognizer__constant_oresult(()))
>>> _parse_text_(mk_ignorable_txt_rgnr_serial_([(True, TextRecognizer__constant_text('1')), (True, TextRecognizer__constant_text('2')), (True, TextRecognizer__constant_text('3'))]), env, '123', 0, 3)
OResult((), 3)


TextRecognizer__serial__cased
TextRecognizer__sep_end_by__cased
TextRecognizer__sep_by__cased
TextRecognizer__end_by__cased
TextRecognizer__many__cased
>>> TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))])
TextRecognizer__serial__cased((TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')), TextRecognizer__tag(2, TextRecognizer__constant_text('xyz'))))

TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))))

>>> _parse_text_(TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))]), env, '123abcxyz', 0, 9)
OResult(('abc', 'x', 'y', 'z'), 9)

>>> TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')), TextRecognizer__tag(2, TextRecognizer__constant_text('xyz')))

TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))

>>> _parse_text_(TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123abcabcxyz', 0, 12)
OResult(('abc', 'abc', 'x', 'y', 'z'), 12)

>>> TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')))
TextRecognizer__sep_by__cased(0, None, TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')))

TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))))

>>> _parse_text_(TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc'))), env, '123abcabc', 0, 9)
OResult(('abc', 'abc'), 9)


>>> TextRecognizer__end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__end_by__cased(0, None, TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(2, TextRecognizer__constant_text('xyz')))

TextRecognizer__end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))

>>> _parse_text_(TextRecognizer__end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123123xyz', 0, 9)
OResult(('x', 'y', 'z'), 9)

>>> TextRecognizer__many__cased(0, None, mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__many__cased(0, None, TextRecognizer__tag(2, TextRecognizer__constant_text('xyz')))

TextRecognizer__many__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))

>>> _parse_text_(TextRecognizer__many__cased(0, None, mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, 'xyzxyzxyz', 0, 9)
OResult(('x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'), 9)




TextRecognizer__fullmatched
TextRecognizer__span6regex
TextRecognizer__span
TextRecognizer__inside
TextRecognizer__repr
TextRecognizer__ref

>>> TextRecognizer__fullmatched(TextRecognizer__constant_text('xyz'))
TextRecognizer__fullmatched(TextRecognizer__constant_text('xyz'))
>>> _parse_text_(TextRecognizer__fullmatched(TextRecognizer__constant_text('xyz')), env, 'xyz-', 0, 3)
OResult('xyz', 3)
>>> _parse_text_(TextRecognizer__fullmatched(TextRecognizer__constant_text('xyz')), env, 'xyz-', 0, 4)
Errmsg((OResult('xyz', 3), 1, '-'), 3, False)

>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1)
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1)
>>> _parse_text_(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1), env, 'aabbccdd', 0, 8)
OResult((2, 4), 6)
>>> _parse_text_(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx'), env, 'aabbccdd', 0, 8)
OResult((2, 4), 6)

>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 'span')
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1)
>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 'end')
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1, 1)
>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 'start')
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1, 0)
>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 2)
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1)
>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 1)
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1, 1)
>>> TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 1, 0)
TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 1, 0)
>>> _parse_text_(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 2), env, 'aabbccdd', 0, 8)
OResult((2, 4), 6)
>>> _parse_text_(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 1), env, 'aabbccdd', 0, 8)
OResult(4, 6)
>>> _parse_text_(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 0), env, 'aabbccdd', 0, 8)
OResult(2, 6)

>>> TextRecognizer__span(None, None, True)
TextRecognizer__span(None, None, True)
>>> TextRecognizer__span(None, None)
TextRecognizer__span(None, None)
>>> _parse_text_(TextRecognizer__span(None, None), env, 'aabbccdd', 0, 8)
OResult((0, 8), 8)
>>> _parse_text_(TextRecognizer__span(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 0), TextRecognizer__span6regex(r'dd(?P<xx>ee)ff', 'xx', 1)), env, 'aabbccddeeffgg', 0, 14)
OResult((2, 10), 12)
>>> _parse_text_(TextRecognizer__span(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 0), TextRecognizer__span6regex(r'.{6}dd(?P<xx>ee)ff', 'xx', 1), True), env, 'aabbccddeeffgg', 0, 14)
OResult((2, 10), 12)

>>> _parse_text_(TextRecognizer__span(TextRecognizer__span6regex(r'a*', 0, 1), TextRecognizer__span6regex(r'[^a]*(a+)', 1, 0)), env, 'aaaabbbbaaaa', 0, 12)
OResult((4, 8), 12)
>>> _parse_text_(TextRecognizer__span(TextRecognizer__span6regex(r'a*', 0, 1), TextRecognizer__span6regex(r'[^a]*(a+)', 1, 0), True), env, 'aaaabbbbaaaa', 0, 12)
OResult((0, 0), 4)


>>> TextRecognizer__inside(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 2), TextRecognizer__constant_text('bb'), True)
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 'xx'), TextRecognizer__constant_text('bb'), True)
>>> TextRecognizer__inside(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 2), TextRecognizer__constant_text('bb'))
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('aa(?P<xx>bb)cc'), 'xx'), TextRecognizer__constant_text('bb'))
>>> _parse_text_(TextRecognizer__inside(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 2), TextRecognizer__constant_text('bb')), env, 'aabbccdd', 0, 8)
OResult('bb', 4)
>>> _parse_text_(TextRecognizer__inside(TextRecognizer__span6regex(r'aa(?P<xx>bb)cc', 'xx', 2), TextRecognizer__constant_text('bb'), True), env, 'aabbccdd', 0, 8)
OResult('bb', 6)




>>> TextRecognizer__repr(mk_txt_rgnr__span6regex_(r'\s+', 0, method=1), mk_txt_rgnr__span6regex_, r'\s+', 0, method=1)
mk_txt_rgnr__span6regex_('\\s+', 0, method = 1)
>>> print(TextRecognizer__repr(mk_txt_rgnr__span6regex_(r'\s+', 0, method=1), mk_txt_rgnr__span6regex_, r'\s+', 0, method=1))  #doctest: +ELLIPSIS
TextRecognizer__repr(TextRecognizer__span6regex(re.compile('\\s+'), 0, 1), <function mk_txt_rgnr__span6regex_ at 0x...>, '\\s+', 0, method = 1)
>>> _parse_text_(TextRecognizer__repr(mk_txt_rgnr__span6regex_(r'\s+', 0, method=1), mk_txt_rgnr__span6regex_, r'\s+', 0, method=1), env, '\t'*4, 0, 4)
OResult(4, 4)

>>> name5or_named_obj_('xxx yyy')
'xxx yyy'
>>> name5or_named_obj_(999)
'int'
>>> name5or_named_obj_(lambda:0)
'<lambda>'
>>> name5or_named_obj_(name5or_named_obj_)
'name5or_named_obj_'
>>> name5or_named_obj_(mk_txt_rgnr__text_(''))
'TextRecognizer__constant_text'
>>> name5or_named_obj_(TextRecognizer__repr)
'TextRecognizer__repr'




>>> TextRecognizer__ref(666)
TextRecognizer__ref(666)
>>> nm2txt_rgnr = {666:mk_txt_rgnr__text_(r'xyz')}
>>> _env = {TextRecognizer__ref:nm2txt_rgnr, **env4ops4oresult_seq__list}
>>> _parse_text_(TextRecognizer__ref(666), _env, 'xyzaaa', 0, 6)
OResult('xyz', 3)

>>> nm2txt_rgnr = {}
>>> mk_txt_rgnr__text_(r'xyz').ref_as_(nm2txt_rgnr, 666)
TextRecognizer__ref(666)
>>> _env = mk_env5nm2txt_rgnr_(nm2txt_rgnr, case4ops4flow_txt_rgnr='list')
>>> _env = mk_env5nm2txt_rgnr_(nm2txt_rgnr, case4ops4flow_txt_rgnr='ftSeq')
>>> _env = mk_env5nm2txt_rgnr_(nm2txt_rgnr)
>>> _parse_text_(TextRecognizer__ref(666), _env, 'xyzaaa', 0, 6)
OResult('xyz', 3)
>>> nm2txt_rgnr
{666: TextRecognizer__constant_text('xyz')}
>>> #_env

























################
affect{_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq}:
    TextRecognizer__serial
    TextRecognizer__sep_by
    TextRecognizer__sep_end_by
    但:考虑到 cased 明显不同:
    TextRecognizer__serial__cased
    TextRecognizer__sep_end_by__cased
    TextRecognizer__sep_by__cased
>>> env = env4ops4oresult_seq__ftSeq

.,$s/^\(OResult(\)(\(.*\))\(, \d*)\)$/\1Seq([\2])\3
.,$s/,\]/]
.,$s/Seq(\[\])/Seq()

    TextRecognizer__serial
    TextRecognizer__sep_end_by
    TextRecognizer__sep_by
>>> TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')])
TextRecognizer__serial((TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')))
>>> _parse_text_(TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')]), env, '666999', 0, 6)
OResult(Seq(['666', '999']), 6)
>>> _parse_text_(TextRecognizer__serial([TextRecognizer__constant_text('666'), TextRecognizer__constant_text('999')]), env, '666997', 0, 6)
Errmsg(('unmatched:NE', '999', '997'), 3, True)

>>> TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999'))
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
OResult(Seq(['666', '999']), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '999666', 0, 6)
OResult(Seq(['999']), 3)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 6)
Errmsg(('unmatched:EOF', '111', 3, 0), 6, True)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(Seq(['666', '111', '999']), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111111999', 0, 15)
OResult(Seq(['666', '111', '111', '111', '999']), 15)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '999666', 0, 6)
Errmsg(('unmatched:NE', '666', '999'), 0, False)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
OResult(Seq(['666', '999']), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666999', 0, 6)
Errmsg(('unmatched:NE', '111', '999'), 3, True)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(Seq(['666', '111', '999']), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(2, 2, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111999', 0, 9)
OResult(Seq(['666', '111', '999']), 9)
>>> _parse_text_(TextRecognizer__sep_end_by(2, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(Seq(['666', '111', '111', '999']), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(3, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(Seq(['666', '111', '111', '999']), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(0, 3, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
OResult(Seq(['666', '111', '111', '999']), 12)
>>> _parse_text_(TextRecognizer__sep_end_by(0, 2, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('999')), env, '666111111999', 0, 12)
Errmsg(('unmatched:NE', '999', '111'), 6, True)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('6')), env, '666111999', 0, 9)
OResult(Seq(['6']), 1)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('1')), env, '666111999', 0, 9)
OResult(Seq(['666', '1']), 4)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('1119')), env, '666111999', 0, 9)
OResult(Seq(['666', '1119']), 7)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('666'), TextRecognizer__constant_text('111'), TextRecognizer__constant_text('111')), env, '666111999', 0, 9)
OResult(Seq(['666', '111']), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(0, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(Seq(['123']), 3)
>>> _parse_text_(TextRecognizer__sep_end_by(1, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(Seq(['123', '123']), 6)
>>> _parse_text_(TextRecognizer__sep_end_by(2, None, TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123'), TextRecognizer__constant_text('123')), env, '123123123', 0, 9)
OResult(Seq(['123', '123', '123']), 9)

>>> TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1'))
TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1'))
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1', '1', '1']), 4)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(Seq(['6', '1']), 2)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
OResult(Seq(['6']), 1)
>>> _parse_text_(TextRecognizer__sep_by(0, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, 'x111', 0, 4)
OResult(Seq(), 0)
>>> _parse_text_(TextRecognizer__sep_by(1, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, 'x111', 0, 4)
Errmsg(('unmatched:NE', '6', 'x'), 0, False)
>>> _parse_text_(TextRecognizer__sep_by(1, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
OResult(Seq(['6']), 1)
>>> _parse_text_(TextRecognizer__sep_by(2, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6x11', 0, 4)
Errmsg(('unmatched:NE', '1', 'x'), 1, True)
>>> _parse_text_(TextRecognizer__sep_by(2, None, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(Seq(['6', '1']), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '61x1', 0, 4)
OResult(Seq(['6', '1']), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1']), 2)
>>> _parse_text_(TextRecognizer__sep_by(2, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1', '1']), 3)
>>> _parse_text_(TextRecognizer__sep_by(3, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1', '1']), 3)
>>> _parse_text_(TextRecognizer__sep_by(0, 3, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1', '1']), 3)
>>> _parse_text_(TextRecognizer__sep_by(0, 2, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6', '1']), 2)
>>> _parse_text_(TextRecognizer__sep_by(0, 1, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(['6']), 1)
>>> _parse_text_(TextRecognizer__sep_by(0, 0, TextRecognizer__constant_text('6'), TextRecognizer__constant_text('1')), env, '6111', 0, 4)
OResult(Seq(), 0)


    TextRecognizer__serial__cased
    TextRecognizer__sep_end_by__cased
    TextRecognizer__sep_by__cased
>>> TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))])
TextRecognizer__serial__cased((TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')), TextRecognizer__tag(2, TextRecognizer__constant_text('xyz'))))

TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))))

>>> _parse_text_(TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))]), env, '123abcxyz', 0, 9)
OResult(Seq(['abc', 'x', 'y', 'z']), 9)

>>> TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')), TextRecognizer__tag(2, TextRecognizer__constant_text('xyz')))

TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))

>>> _parse_text_(TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123abcabcxyz', 0, 12)
OResult(Seq(['abc', 'abc', 'x', 'y', 'z']), 12)

>>> TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')))
TextRecognizer__sep_by__cased(0, None, TextRecognizer__tag(0, TextRecognizer__constant_text('123')), TextRecognizer__tag(1, TextRecognizer__constant_text('abc')))

TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))))

>>> _parse_text_(TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc'))), env, '123abcabc', 0, 9)
OResult(Seq(['abc', 'abc']), 9)









################
mk_txt_rgnr__span_
mk_txt_rgnr__span6regex_
mk_txt_rgnr__regex_
mk_txt_rgnr__text_
mk_txt_rgnr__oresult_
mk_txt_rgnr__errmsg_
mk_txt_rgnr__ref_
>>> mk_txt_rgnr__span_(None, None)
TextRecognizer__span(None, None)
>>> mk_txt_rgnr__span_(None, None, backward=True)
TextRecognizer__span(None, None, True)

>>> mk_txt_rgnr__span6regex_(r'\s+', 0)
TextRecognizer__span6regex(re.compile('\\s+'), 0)
>>> mk_txt_rgnr__span6regex_(r'\s+', 0, method='end')
TextRecognizer__span6regex(re.compile('\\s+'), 0, 1)
>>> mk_txt_rgnr__span6regex_(r'\s+', 0, method=1)
TextRecognizer__span6regex(re.compile('\\s+'), 0, 1)

>>> mk_txt_rgnr__regex_(r'\s+', None)
TextRecognizer__regex(re.compile('\\s+'))
>>> mk_txt_rgnr__regex_(r'\s+', 0)
TextRecognizer__regex(re.compile('\\s+'), 0)
>>> mk_txt_rgnr__text_(r'xyz')
TextRecognizer__constant_text('xyz')
>>> mk_txt_rgnr__oresult_(999)
TextRecognizer__constant_oresult(999)
>>> mk_txt_rgnr__errmsg_(666)
TextRecognizer__constant_errmsg(666, False)
>>> mk_txt_rgnr__errmsg_(666, True)
TextRecognizer__constant_errmsg(666, True)

>>> mk_txt_rgnr__ref_(666)
TextRecognizer__ref(666)

################
all methods of _BaseTextRecognizer__ops4mkr:
    .else_
    .else_trial_
    .enclosed_by_
    .end_by_
    .many0_
    .many1_
    .many_
    .on_ok_
    .on_ko_
    .on_errmsg6ko_
    .named_
    .tagnamed_
    .optional_
    .sep_by_
    .sep_end_by_
    .tag7echo_
    .tag7ignore_
    .tag7unpack_
    .__neg__ = tag7ignore_
    .__pos__ = tag7echo_
    .__invert__ = tag7unpack_
    .__matmul__ = then_tag_
    .then_
    .then_box_
    .then_getitem_
    .then_tag_
    .then_to_finger_tree_seq_
    .then_to_tuple_
    .then_unbox_
    .fullmatched_
    .inside_
    .insideR_
    .insideV_
    .span_
    .spanB_
    .repr_as_
    .ref_as_
>>> mk_txt_rgnr__text_(r'xyz').else_(mk_txt_rgnr__text_(r'012'), mk_txt_rgnr__errmsg_(r'fail:ko'))
TextRecognizer__fallback((TextRecognizer__constant_text('xyz'), TextRecognizer__constant_text('012'), TextRecognizer__constant_errmsg('fail:ko', False)))
>>> mk_txt_rgnr__text_(r'xyz').else_trial_()
TextRecognizer__trial(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').else_trial_().else_trial_()
TextRecognizer__trial(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').enclosed_by_('(', ')')
TextRecognizer__enclosed(TextRecognizer__constant_text('('), TextRecognizer__constant_text('xyz'), TextRecognizer__constant_text(')'))
>>> mk_txt_rgnr__text_(r'xyz').enclosed_by_(r'[(]', r'[)]', as_regex=True)
TextRecognizer__enclosed(TextRecognizer__regex(re.compile('[(]')), TextRecognizer__constant_text('xyz'), TextRecognizer__regex(re.compile('[)]')))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().end_by_(mk_txt_rgnr__text_(r',').tag7ignore_(), cased=True)
TextRecognizer__end_by__cased(0, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')), TextRecognizer__tag(0, TextRecognizer__constant_text(',')))

TextRecognizer__end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text(','))))

>>> mk_txt_rgnr__text_(r'xyz').end_by_(mk_txt_rgnr__text_(r','), 2, 4)
TextRecognizer__end_by(2, 4, TextRecognizer__constant_text('xyz'), TextRecognizer__constant_text(','))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().many0_(cased=True)
TextRecognizer__many__cased(0, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')))

TextRecognizer__many__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))

>>> mk_txt_rgnr__text_(r'xyz').many0_(4)
TextRecognizer__many(0, 4, TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().many1_(cased=True)
TextRecognizer__many__cased(1, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')))

TextRecognizer__many__cased(1, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))

>>> mk_txt_rgnr__text_(r'xyz').many1_(4)
TextRecognizer__many(1, 4, TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().many_(cased=True)
TextRecognizer__many__cased(0, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')))

TextRecognizer__many__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))

>>> mk_txt_rgnr__text_(r'xyz').many_(2, 4)
TextRecognizer__many(2, 4, TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').on_ok_(repr)
TextRecognizer__postprocess6ok(TextRecognizer__constant_text('xyz'), <built-in function repr>)
>>> mk_txt_rgnr__text_(r'xyz').on_ok_(repr, 1)
TextRecognizer__postprocess6ok(TextRecognizer__constant_text('xyz'), <built-in function repr>)
>>> mk_txt_rgnr__text_(r'xyz').on_ok_(lambda:666, 0)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6oresult(TextRecognizer__constant_text('xyz'), 0, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ok_(666, -1)
TextRecognizer__postprocess6oresult(TextRecognizer__constant_text('xyz'), -1, 666)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_(lambda errmsg, severe, /:('xxx', severe))   #doctest: +ELLIPSIS
TextRecognizer__postprocess6ko(TextRecognizer__constant_text('xyz'), <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_(lambda errmsg, severe, /:('xxx', severe), None)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6ko(TextRecognizer__constant_text('xyz'), <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_(lambda errmsg, severe, /:f'xxx{severe}', 2)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 2, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_(lambda errmsg, /:'xxx', 1)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 1, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_(lambda:'xxx', 0)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 0, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_ko_('xxx', -1)   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), -1, 'xxx')
>>> mk_txt_rgnr__text_(r'xyz').on_errmsg6ko_(2, lambda errmsg, severe, /:f'xxx{severe}')   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 2, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_errmsg6ko_(1, lambda errmsg, /:'xxx')   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 1, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_errmsg6ko_(0, lambda:'xxx')   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), 0, <function <lambda> at 0x...>)
>>> mk_txt_rgnr__text_(r'xyz').on_errmsg6ko_(-1, 'xxx')   #doctest: +ELLIPSIS
TextRecognizer__postprocess6errmsg(TextRecognizer__constant_text('xyz'), -1, 'xxx')
>>> mk_txt_rgnr__text_(r'xyz').named_('anm')
TextRecognizer__named(False, 'anm', ...)
>>> print(mk_txt_rgnr__text_(r'xyz').named_('anm'))
TextRecognizer__named(False, 'anm', TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').named_('.attr', global_vs_local=True, to_tag=True)
TextRecognizer__named(True, '.attr', ...)
>>> print(mk_txt_rgnr__text_(r'xyz').named_('.attr', global_vs_local=True, to_tag=True))
TextRecognizer__named(True, '.attr', TextRecognizer__tag('.attr', TextRecognizer__constant_text('xyz')))
>>> print(mk_txt_rgnr__text_(r'xyz').tagnamed_('anm'))
TextRecognizer__named(False, 'anm', TextRecognizer__tag('anm', TextRecognizer__constant_text('xyz')))
>>> print(mk_txt_rgnr__text_(r'xyz').tagnamed_('.attr', global_vs_local=True))
TextRecognizer__named(True, '.attr', TextRecognizer__tag('.attr', TextRecognizer__constant_text('xyz')))
>>> print(mk_txt_rgnr__text_(r'xyz').tagnamed_('.attr', global_vs_local=True, to_tag=False))
TextRecognizer__named(True, '.attr', TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().optional_(cased=True)
TextRecognizer__many__cased(0, 1, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')))

TextRecognizer__many__cased(0, 1, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))

>>> mk_txt_rgnr__text_(r'xyz').optional_()
TextRecognizer__many(0, 1, TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().sep_by_(mk_txt_rgnr__text_(r',').tag7ignore_(), cased=True)
TextRecognizer__sep_by__cased(0, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')), TextRecognizer__tag(2, TextRecognizer__serial__cased((TextRecognizer__tag(0, TextRecognizer__constant_text(',')), TextRecognizer__tag(1, TextRecognizer__constant_text('xyz'))))))

TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text(','))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))))))

bug:TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text(','))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))))
    !! ++mk_txt_rgnr7sep_item_()

>>> mk_txt_rgnr__text_(r'xyz').sep_by_(mk_txt_rgnr__text_(r','), 2, 4)
TextRecognizer__sep_by(2, 4, TextRecognizer__constant_text('xyz'), TextRecognizer__serial((TextRecognizer__constant_text(','), TextRecognizer__constant_text('xyz'))))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().sep_end_by_(mk_txt_rgnr__text_(r',').tag7ignore_(), mk_txt_rgnr__text_(r';').tag7ignore_(), cased=True)
TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')), TextRecognizer__tag(2, TextRecognizer__serial__cased((TextRecognizer__tag(0, TextRecognizer__constant_text(',')), TextRecognizer__tag(1, TextRecognizer__constant_text('xyz'))))), TextRecognizer__tag(0, TextRecognizer__constant_text(';')))

TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__serial__cased((TextRecognizer__constant_text(','), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text(';'))))

bug:TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial__cased((TextRecognizer__constant_text(','), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text(';'))))
    !! ++mk_txt_rgnr7sep_item_()

>>> mk_txt_rgnr__text_(r'xyz').sep_end_by_(mk_txt_rgnr__text_(r','), mk_txt_rgnr__text_(r';'), 2, 4)
TextRecognizer__sep_end_by(2, 4, TextRecognizer__constant_text('xyz'), TextRecognizer__serial((TextRecognizer__constant_text(','), TextRecognizer__constant_text('xyz'))), TextRecognizer__constant_text(';'))
>>> mk_txt_rgnr__text_(r'xyz').tag7ignore_()
TextRecognizer__tag(0, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('xyz')))

>>> mk_txt_rgnr__text_(r'xyz').tag7echo_()
TextRecognizer__tag(1, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz')))

>>> mk_txt_rgnr__text_(r'xyz').tag7unpack_()
TextRecognizer__tag(2, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))

>>> -mk_txt_rgnr__text_(r'xyz')
TextRecognizer__tag(0, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('xyz')))

>>> +mk_txt_rgnr__text_(r'xyz')
TextRecognizer__tag(1, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz')))

>>> ~mk_txt_rgnr__text_(r'xyz')
TextRecognizer__tag(2, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))

>>> mk_txt_rgnr__text_(r'xyz') @ 777
TextRecognizer__tag(777, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(777), TextRecognizer__constant_text('xyz')))

>>> mk_txt_rgnr__text_(r'xyz').then_(mk_txt_rgnr__text_(r'012'), mk_txt_rgnr__oresult_(999))
TextRecognizer__serial((TextRecognizer__constant_text('xyz'), TextRecognizer__constant_text('012'), TextRecognizer__constant_oresult(999)))
>>> mk_txt_rgnr__text_(r'xyz').tag7echo_().then_(-mk_txt_rgnr__text_(r'012'), +mk_txt_rgnr__oresult_(999), cased=True)
TextRecognizer__serial__cased((TextRecognizer__tag(1, TextRecognizer__constant_text('xyz')), TextRecognizer__tag(0, TextRecognizer__constant_text('012')), TextRecognizer__tag(1, TextRecognizer__constant_oresult(999))))

TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('xyz'))), TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('012'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_oresult(999)))))

>>> mk_txt_rgnr__text_(r'xyz').then_box_()
TextRecognizer__box(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').then_getitem_(-2)
TextRecognizer__getitem(TextRecognizer__constant_text('xyz'), -2)
>>> mk_txt_rgnr__text_(r'xyz').then_tag_(777)
TextRecognizer__tag(777, TextRecognizer__constant_text('xyz'))

TextRecognizer__serial((TextRecognizer__constant_oresult(777), TextRecognizer__constant_text('xyz')))

>>> mk_txt_rgnr__text_(r'xyz').then_to_finger_tree_seq_()
TextRecognizer__to_finger_tree_seq(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').then_to_finger_tree_seq_().then_to_finger_tree_seq_()
TextRecognizer__to_finger_tree_seq(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').then_to_tuple_()
TextRecognizer__to_tuple(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').then_to_tuple_().then_to_tuple_()
TextRecognizer__to_tuple(TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').then_box_().then_unbox_()
TextRecognizer__unbox(TextRecognizer__box(TextRecognizer__constant_text('xyz')))



################
    .fullmatched_
    .inside_
    .insideR_
    .insideV_
    .span_
    .spanB_
    .repr_as_
    .ref_as_

>>> mk_txt_rgnr__text_(r'xyz').fullmatched_()
TextRecognizer__fullmatched(TextRecognizer__constant_text('xyz'))

>>> mk_txt_rgnr__text_(r'xyz').inside_(mk_txt_rgnr__span6regex_(r'\w+', 0))
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('\\w+'), 0), TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').inside_(mk_txt_rgnr__span6regex_(r'\w+', 0), no_seekback=True)
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('\\w+'), 0), TextRecognizer__constant_text('xyz'), True)

>>> mk_txt_rgnr__text_(r'xyz').insideR_(r'\w+', 0)
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('\\w+'), 0), TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').insideR_(r'\w+', 0, no_seekback=True)
TextRecognizer__inside(TextRecognizer__span6regex(re.compile('\\w+'), 0), TextRecognizer__constant_text('xyz'), True)

>>> mk_txt_rgnr__text_(r'xyz').insideV_(mk_txt_rgnr__span6regex_(r'\w+', 0, method=0), mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1))
TextRecognizer__inside(TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1)), TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').insideV_(mk_txt_rgnr__span6regex_(r'\w+', 0, method=0), mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1), backward=True)
TextRecognizer__inside(TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1), True), TextRecognizer__constant_text('xyz'))
>>> mk_txt_rgnr__text_(r'xyz').insideV_(mk_txt_rgnr__span6regex_(r'\w+', 0, method=0), mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1), no_seekback=True)
TextRecognizer__inside(TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1)), TextRecognizer__constant_text('xyz'), True)
>>> mk_txt_rgnr__text_(r'xyz').insideV_(mk_txt_rgnr__span6regex_(r'\w+', 0, method=0), mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1), backward=True, no_seekback=True)
TextRecognizer__inside(TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1), True), TextRecognizer__constant_text('xyz'), True)

>>> mk_txt_rgnr__span6regex_(r'\w+', 0, method=0).span_(None)
TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), None)
>>> mk_txt_rgnr__span6regex_(r'\w+', 0, method=0).span_(None, backward=True)
TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), None, True)
>>> mk_txt_rgnr__span6regex_(r'\w+', 0, method=0).span_(mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1))
TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1))

>>> mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1).spanB_(None)
TextRecognizer__span(None, TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1), True)
>>> mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1).spanB_(None, backward=False)
TextRecognizer__span(None, TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1))
>>> mk_txt_rgnr__span6regex_(r'\W*\w+', 0, method=1).spanB_(mk_txt_rgnr__span6regex_(r'\w+', 0, method=0))
TextRecognizer__span(TextRecognizer__span6regex(re.compile('\\w+'), 0, 0), TextRecognizer__span6regex(re.compile('\\W*\\w+'), 0, 1), True)

>>> mk_txt_rgnr__text_(r'xyz').repr_as_(mk_txt_rgnr__text_, r'xyz')
mk_txt_rgnr__text_('xyz')
>>> print(mk_txt_rgnr__text_(r'xyz').repr_as_(mk_txt_rgnr__text_, r'xyz'))   #doctest: +ELLIPSIS
TextRecognizer__repr(TextRecognizer__constant_text('xyz'), <function mk_txt_rgnr__text_ at 0x...>, 'xyz')
>>> mk_txt_rgnr__span6regex_(r'\s+', 0, method=1).repr_as_(mk_txt_rgnr__span6regex_, r'\s+', 0, method=1)
mk_txt_rgnr__span6regex_('\\s+', 0, method = 1)
>>> print(mk_txt_rgnr__span6regex_(r'\s+', 0, method=1).repr_as_(mk_txt_rgnr__span6regex_, r'\s+', 0, method=1))   #doctest: +ELLIPSIS
TextRecognizer__repr(TextRecognizer__span6regex(re.compile('\\s+'), 0, 1), <function mk_txt_rgnr__span6regex_ at 0x...>, '\\s+', 0, method = 1)

>>> nm2txt_rgnr = {}
>>> mk_txt_rgnr__text_(r'xyz').ref_as_(nm2txt_rgnr, 666)
TextRecognizer__ref(666)
>>> nm2txt_rgnr
{666: TextRecognizer__constant_text('xyz')}
>>> mk_txt_rgnr__text_(r'xyz').ref_as_(nm2txt_rgnr, 666)
Traceback (most recent call last):
    ...
KeyError: ('existed:', 666)

>>> nm2txt_rgnr = {}
>>> mk_txt_rgnr__text_(r'xyz').ref_as_(nm2txt_rgnr, 666, to_name=True)
TextRecognizer__ref(666)
>>> nm2txt_rgnr
{666: TextRecognizer__named(False, 666, ...)}
>>> print(nm2txt_rgnr[666])
TextRecognizer__named(False, 666, TextRecognizer__constant_text('xyz'))

################
parse_text_
parse_text7full_
parse_text7raise_
parse_text7exact_

>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4)
OResult('xyz', 3)
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4, fullmatched=True)
Errmsg((OResult('xyz', 3), 1, '-'), 3, False)
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 3, fullmatched=True)
OResult('xyz', 3)
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4, to_raise_if_fail=True)
('xyz', 3)
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 2, to_raise_if_fail=True)
Traceback (most recent call last):
    ...
seed.recognize.text_recognizer.ITextRecognizer.ParseFail: (Errmsg(('unmatched:EOF', 'xyz', 3, 2), 0, False), 'xy')
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4, fullmatched=True, to_raise_if_fail=True)
Traceback (most recent call last):
    ...
seed.recognize.text_recognizer.ITextRecognizer.ParseFail: (Errmsg((OResult('xyz', 3), 1, '-'), 3, False), '-')
>>> parse_text_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 3, fullmatched=True, to_raise_if_fail=True)
'xyz'

>>> parse_text7full_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4)
Errmsg((OResult('xyz', 3), 1, '-'), 3, False)
>>> parse_text7full_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 3)
OResult('xyz', 3)
>>> parse_text7raise_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4)
('xyz', 3)
>>> parse_text7raise_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 2)
Traceback (most recent call last):
    ...
seed.recognize.text_recognizer.ITextRecognizer.ParseFail: (Errmsg(('unmatched:EOF', 'xyz', 3, 2), 0, False), 'xy')
>>> parse_text7exact_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 4)
Traceback (most recent call last):
    ...
seed.recognize.text_recognizer.ITextRecognizer.ParseFail: (Errmsg((OResult('xyz', 3), 1, '-'), 3, False), '-')
>>> parse_text7exact_(mk_txt_rgnr__text_('xyz'), env, 'xyz-', 0, 3)
'xyz'





################
>>> 

TODO
>>> 










py_adhoc_call   seed.recognize.text_recognizer.ITextRecognizer__doctest   @f
from seed.recognize.text_recognizer.ITextRecognizer__doctest import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from seed.recognize.text_recognizer.ITextRecognizer import name5or_named_obj_
from seed.recognize.text_recognizer.ITextRecognizer import xget_groups5re_match_, check_may_group_or_groups_
from seed.recognize.text_recognizer.ITextRecognizer import (ITextRecognizer
,BaseError
,   ParseFail
,parse_text_
,   parse_text7full_
,   parse_text7raise_
,   parse_text7exact_
,   check_parse_result__between_
,       check_parse_result_
,   ParseResult
,       OResult
,       Errmsg
,ITextRecognizer
,   ITextRecognizer__postprocess
,   ITextRecognizer__postprocess6ok
,       ITextRecognizer__postprocess6oresult
,   ITextRecognizer__postprocess6ko
,       ITextRecognizer__postprocess6errmsg
,   ITextRecognizer__fallback
,   ITextRecognizer__flow
,       ITextRecognizer__flow__cased_oresult7child
,           ITextRecognizer__serial
,           ITextRecognizer__sep_by
,               ITextRecognizer__many
,           ITextRecognizer__sep_end_by
,               ITextRecognizer__end_by
#
,   TextRecognizer__inside
,   TextRecognizer__span
,   TextRecognizer__span6regex
,   TextRecognizer__repr
,   TextRecognizer__ref
#
,   ITextRecognizer__postprocess
,       TextRecognizer__fullmatched
,   TextRecognizer__postprocess6ok
,       TextRecognizer__postprocess6oresult
,       TextRecognizer__tag
,   TextRecognizer__postprocess6ko
,       TextRecognizer__postprocess6errmsg
,       TextRecognizer__named
,   TextRecognizer__unbox
,   TextRecognizer__getitem
,   TextRecognizer__box
,   TextRecognizer__to_tuple
,   TextRecognizer__to_finger_tree_seq
,   TextRecognizer__constant_oresult
,   TextRecognizer__constant_errmsg
,   TextRecognizer__constant_text
,   TextRecognizer__regex
,   TextRecognizer__trial
,   TextRecognizer__fallback
,   TextRecognizer__enclosed
#
,   TextRecognizer__serial
,   TextRecognizer__sep_end_by
,   TextRecognizer__sep_by
,   TextRecognizer__end_by
,   TextRecognizer__many
#
,   TextRecognizer__serial__cased
,   TextRecognizer__sep_end_by__cased
,   TextRecognizer__sep_by__cased
,   TextRecognizer__end_by__cased
,   TextRecognizer__many__cased
#
,   mk_tagged_txt_rgnr_
,   mk_tagged_txt_rgnr_fallback_
,   mk_ignorable_txt_rgnr_serial_
#
,   env4ops4oresult_seq__ftSeq
,   env4ops4oresult_seq__list
,   mk_env5nm2txt_rgnr_
)


#from seed.recognize.text_recognizer.ITextRecognizer import parse_text_, env4ops4oresult_seq__ftSeq, env4ops4oresult_seq__list
    #def parse_text_(txt_rgnr, env, txt, begin, end, /):
from seed.recognize.text_recognizer.ITextRecognizer import parse_text_, parse_text7full_, parse_text7raise_, parse_text7exact_, ParseFail, env4ops4oresult_seq__ftSeq, env4ops4oresult_seq__list, mk_env5nm2txt_rgnr_
    #def mk_env5nm2txt_rgnr_(nm2txt_rgnr, /, *, case4ops4flow_txt_rgnr:'list|ftSeq'=None):
    #def parse_text_(txt_rgnr, env, txt, begin, end, /, *, fullmatched=False, to_raise_if_fail=False):
    #   'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> ParseResult/(OResult|Errmsg)'
    #   Errmsg(errmsg,end,severe){ok:=False}{ko:=True}
    #   OResult(oresult,end){ok:=True}{ko:=False}
from seed.recognize.text_recognizer.ITextRecognizer import (
#after:_BaseTextRecognizer__ops4mkr
#   other_mkrs:goto
ITextRecognizer
,mk_tagged_txt_rgnr_fallback_
,mk_ignorable_txt_rgnr_serial_
,mk_txt_rgnr__span_#kw:backward
,mk_txt_rgnr__span6regex_#kw:method
,mk_txt_rgnr__regex_#kw:as_regex
,mk_txt_rgnr__text_#kw:as_regex
,mk_txt_rgnr__oresult_
,mk_txt_rgnr__errmsg_
,mk_txt_rgnr__ref_
#_BaseTextRecognizer__ops4mkr::
#   .on_ok_
#   .on_ko_
#   .on_errmsg6ko_
#   .named_#kw:global_vs_local,to_tag
#   .tagnamed_#kw:global_vs_local,to_tag
#
#   .fullmatched_
#   .inside_#kw:no_seekback
#   .insideR_#kw:no_seekback
#   .insideV_#kw:backward,no_seekback
#   .span_#kw:backward
#   .spanB_#kw:backward
#   .repr_as_
#   .ref_as_
#
#   .enclosed_by_#kw:as_regex
#   .end_by_#kw:cased
#   .many0_#kw:cased
#   .many1_#kw:cased
#   .many_#kw:cased
#   .optional_#kw:cased
#   .sep_by_#kw:cased
#   .sep_end_by_#kw:cased
#
#   #tag for kw:cased
#   .tag7echo_
#   .tag7ignore_
#   .tag7unpack_
#   .__neg__ = tag7ignore_
#   .__pos__ = tag7echo_
#   .__invert__ = tag7unpack_
#   .__matmul__ = then_tag_
#
#   .then_#kw:cased
#   .then_box_
#   .then_getitem_
#   .then_tag_
#   .then_to_finger_tree_seq_
#   .then_to_tuple_
#   .then_unbox_#see:enclosed_by_
#
#   .else_
#   .else_trial_
)

from seed.types.LazyObj import mk_lazy_, mk_lazy5obj_, mk_lazy5func_

___end_mark_of_excluded_global_names__0___ = ...



__all__
from seed.recognize.text_recognizer.ITextRecognizer__doctest import *
