#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py

seed.recognize.text_recognizer.ITextRecognizer__doctest
py -m nn_ns.app.debug_cmd   seed.recognize.text_recognizer.ITextRecognizer__doctest -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.ITextRecognizer__doctest:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'




%s/^\(>>> \)\(\<parse_text_\>(.*, \)None\(, '[^']*', \d*, \d*)\)$/\1_\2env\3
>>> _parse_text_ = parse_text_

_default_IOps4oresult_seq4cased_flow_txt_rgnr__using_xxx8oresult_seq = IOps4oresult_seq4cased_flow_txt_rgnr__using_list8oresult_seq
>>> env = None

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

OResult('aaabbbccc', 12)


TextRecognizer__postprocess6ok
TextRecognizer__unbox
TextRecognizer__getitem
TextRecognizer__box
TextRecognizer__to_tuple
TextRecognizer__to_finger_tree_seq
>>> TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), hex)
TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), <built-in function hex>)
>>> _parse_text_(TextRecognizer__postprocess6ok(TextRecognizer__constant_oresult(999), hex), env, '', 0, 0)
OResult('0x3e7', 0)

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
TextRecognizer__serial((TextRecognizer__constant_oresult(999), TextRecognizer__constant_text('abc123')))
>>> _parse_text_(mk_tagged_txt_rgnr_(999, TextRecognizer__constant_text('abc123')), env, 'abc123', 0, 6)
OResult((999, 'abc123'), 6)

>>> mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))])
TextRecognizer__fallback((TextRecognizer__serial((TextRecognizer__constant_oresult(666), TextRecognizer__constant_text('bbb'))), TextRecognizer__serial((TextRecognizer__constant_oresult(999), TextRecognizer__constant_text('qqq')))))
>>> _parse_text_(mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))]), env, 'bbb', 0, 3)
OResult((666, 'bbb'), 3)
>>> _parse_text_(mk_tagged_txt_rgnr_fallback_([(666, TextRecognizer__constant_text('bbb')), (999, TextRecognizer__constant_text('qqq'))]), env, 'qqq', 0, 3)
OResult((999, 'qqq'), 3)

>>> mk_ignorable_txt_rgnr_serial_([(False, TextRecognizer__constant_text('x')), (False, TextRecognizer__constant_text('y')), (True, TextRecognizer__constant_text('1')), (False, TextRecognizer__constant_text('z')), (True, TextRecognizer__constant_text('2')), (True, TextRecognizer__constant_text('3'))])
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
TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))))
>>> _parse_text_(TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))]), env, '123abcxyz', 0, 9)
OResult(('abc', 'x', 'y', 'z'), 9)

>>> TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))
>>> _parse_text_(TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123abcabcxyz', 0, 12)
OResult(('abc', 'abc', 'x', 'y', 'z'), 12)

>>> TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')))
TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))))
>>> _parse_text_(TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc'))), env, '123abcabc', 0, 9)
OResult(('abc', 'abc'), 9)


>>> TextRecognizer__end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))
>>> _parse_text_(TextRecognizer__end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123123xyz', 0, 9)
OResult(('x', 'y', 'z'), 9)

>>> TextRecognizer__many__cased(0, None, mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__many__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))
>>> _parse_text_(TextRecognizer__many__cased(0, None, mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, 'xyzxyzxyz', 0, 9)
OResult(('x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'), 9)







































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
TextRecognizer__serial__cased((TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz')))))
>>> _parse_text_(TextRecognizer__serial__cased([mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))]), env, '123abcxyz', 0, 9)
OResult(Seq(['abc', 'x', 'y', 'z']), 9)

>>> TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz')))
TextRecognizer__sep_end_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))), TextRecognizer__serial((TextRecognizer__constant_oresult(2), TextRecognizer__constant_text('xyz'))))
>>> _parse_text_(TextRecognizer__sep_end_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')), mk_tagged_txt_rgnr_(2, TextRecognizer__constant_text('xyz'))), env, '123abcabcxyz', 0, 12)
OResult(Seq(['abc', 'abc', 'x', 'y', 'z']), 12)

>>> TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc')))
TextRecognizer__sep_by__cased(0, None, TextRecognizer__serial((TextRecognizer__constant_oresult(0), TextRecognizer__constant_text('123'))), TextRecognizer__serial((TextRecognizer__constant_oresult(1), TextRecognizer__constant_text('abc'))))
>>> _parse_text_(TextRecognizer__sep_by__cased(0, None, mk_tagged_txt_rgnr_(0, TextRecognizer__constant_text('123')), mk_tagged_txt_rgnr_(1, TextRecognizer__constant_text('abc'))), env, '123abcabc', 0, 9)
OResult(Seq(['abc', 'abc']), 9)










################
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
from seed.recognize.text_recognizer.ITextRecognizer import (ITextRecognizer
,parse_text_
,   ParseResult
,       OResult
,       Errmsg
,ITextRecognizer
,   ITextRecognizer__postprocess6ok
,   ITextRecognizer__fallback
,   ITextRecognizer__flow
,       ITextRecognizer__flow__cased_oresult7child
,           ITextRecognizer__serial
,           ITextRecognizer__sep_by
,               ITextRecognizer__many
,           ITextRecognizer__sep_end_by
,               ITextRecognizer__end_by
#
,   TextRecognizer__postprocess6ok
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
)



___end_mark_of_excluded_global_names__0___ = ...



__all__
from seed.recognize.text_recognizer.ITextRecognizer__doctest import *
