#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/example__arithmetic_expression.py
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py


seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression:__doc__ -ht


[[
atom_expr =:
    | 'number'
    | '(' arith_expr ')'
pow_expr = atom_expr ( '**' sign* pow_expr)?
mul_expr = pow_expr ( ('*' | '/' | '//' | '%') sign* mul_expr)?
#bug:add_expr = sign* mul_expr ( ('+' | '-') add_expr)?
add_expr = sign* mul_expr ( ('+' | '-') sign* mul_expr)*
arith_expr = add_expr
sign = ('+' | '-')

tkey:
    ** // % * / + - ( ) number
]]












#not_using:tkey2tdat2tdat4tknz__7arith
#not_using:name2may_gpostprocess6ok4parse__7arith
>>> parse7arith__pseudo_fname_('xyzabc_file', iter('( 999 + 666 )'), {}, {}) #doctest: +ELLIPSIS
Reply(Either(True, ((), ((Cased('group', ((), ((Cased('number', ('9', '9', '9')), ()), ()), (('+', (), ((Cased('number', ('6', '6', '6')), ()), ())),))), ()), ()), ())), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)))


#not_using:tkey2tdat2tdat4tknz__7arith
>>> istream7arith = tokenize7arith__pseudo_fname_('xyzabc_file', iter('( 999 + 666 )'), {})
>>> for x in istream7arith.peek_ext_iter():
...     print(x) #doctest: +ELLIPSIS
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(0, PositionInfo4Gap__text_file('xyzabc_file', None, 0, LinenoColumn(1, 1), 0), None), PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2))), Cased('(', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2)), PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6))), Cased('number', ('9', '9', '9'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6)), PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8))), Cased('+', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8)), PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12))), Cased('number', ('6', '6', '6'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12)), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)), Cased(')', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)))



















#using:tkey2tdat2tdat4tknz__7arith
#not_using:name2may_gpostprocess6ok4parse__7arith
>>> parse7arith__pseudo_fname_('xyzabc_file', iter('( 999 + 666 )'), None, {}) #doctest: +ELLIPSIS
Reply(Either(True, ((), ((Cased('group', ((), ((Cased('number', 999), ()), ()), (('+', (), ((Cased('number', 666), ()), ())),))), ()), ()), ())), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)))


>>> istream7arith = tokenize7arith__pseudo_fname_('xyzabc_file', iter('( 999 + 666 )'))
>>> for x in istream7arith.peek_ext_iter():
...     print(x) #doctest: +ELLIPSIS
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(0, PositionInfo4Gap__text_file('xyzabc_file', None, 0, LinenoColumn(1, 1), 0), None), PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2))), Cased('(', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(1, PositionInfo4Gap__text_file('xyzabc_file', None, 1, LinenoColumn(1, 2), 1), PositionInfo4Gap__text_file('xyzabc_file', None, 2, LinenoColumn(1, 3), 2)), PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6))), Cased('number', 999)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(2, PositionInfo4Gap__text_file('xyzabc_file', None, 5, LinenoColumn(1, 6), 5), PositionInfo4Gap__text_file('xyzabc_file', None, 6, LinenoColumn(1, 7), 6)), PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8))), Cased('+', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(3, PositionInfo4Gap__text_file('xyzabc_file', None, 7, LinenoColumn(1, 8), 7), PositionInfo4Gap__text_file('xyzabc_file', None, 8, LinenoColumn(1, 9), 8)), PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12))), Cased('number', 666)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12))))
(Token__keyed(PositionInfo4Span(PositionInfo4Gap__noisy(4, PositionInfo4Gap__text_file('xyzabc_file', None, 11, LinenoColumn(1, 12), 11), PositionInfo4Gap__text_file('xyzabc_file', None, 12, LinenoColumn(1, 13), 12)), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)), Cased(')', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)))
















#using:tkey2tdat2tdat4tknz__7arith
#using:name2may_gpostprocess6ok4parse__7arith
>>> parse7arith__pseudo_fname_('xyzabc_file', iter('( 999 + 666 )')) #doctest: +ELLIPSIS
Reply(Either(True, 1665), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__noisy(5, PositionInfo4Gap__text_file('xyzabc_file', None, 13, LinenoColumn(1, 14), 13), None)))


>>> parse7arith__pseudo_fname_('xyzabc_file', iter('( 9*3**2 + 6*-(1+2)**2 )')) #doctest: +ELLIPSIS
Reply(Either(True, 27), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 18), PositionInfo4Gap__noisy(18, PositionInfo4Gap__text_file('xyzabc_file', None, 24, LinenoColumn(1, 25), 24), None)))













>>> eval7arith('7/9')
Fraction(7, 9)
>>> eval7arith('(7/9 +11/9)')
2
>>> eval7arith('-1-3+4') #found:grammar-error@add_expr
0


py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression   @eval7arith :77%9
    5
py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression   @eval7arith :7/9
    Fraction(7, 9)
py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression   @eval7arith :'(7/9 +11/9)'
    2
py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression   @eval7arith :'-1-3+4'
    0

#]]]'''
__all__ = r'''
eval7arith
parse7arith__pseudo_fname_
    parse7arith__istream_
    tokenize7arith__pseudo_fname_





prepare4parse4arith_
    grp4nm4rgnr4parse__7arith
    name2may_gpostprocess6ok4parse__7arith
    name2rgnr4parse__7arith
    nmd__arith_expr
    max_num_tokens6backward4parse__7arith
    env4parse__7arith





prepare4tokenize4arith_
    tkey2tdat2tdat4tknz__7arith
    tkeys8noise4tknz__7arith
    rgnr4tknz__7arith
    max_num_tokens6backward4tknz__7arith
    may_env4tknz__7arith




'''.split()#'''
#prepare4parse4arith_
#    name2rgnr4parse__7arith
#    nmd__arith_expr
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from fractions import Fraction
#from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import collect_namess5locals_, mk_group_pair4rgnr_ref, Makers4IRecognizerLLoo
#from seed.types.IToken import TokenKeyQuerySet5xqset
#from seed.types.Tester import Tester__eq_obj

___end_mark_of_excluded_global_names__0___ = ...

def _signed(signs, b, /):
    e = signs.count('-')
    if e&1:
        b = -b
    return b
def _spost__atom_expr(oresult, /):
    #atom_expr = mkrs.priority_parallel_([mkrs.tag_(number, 'number'), mkrs.tag_(mkrs.between_(sym6, sym9, ref__arith_expr), 'group')])
    return oresult.payload
def _spost__pow_expr(oresult, /):
    #pow_expr = atom_expr ( '**' sign* pow_expr)?
    a, tmay_op_signs_b = oresult
    match tmay_op_signs_b:
        case [('**', signs, b)]:
            b = _signed(signs, b)
            s = a**b
        case []:
            s = a
        case _:
            raise 000
    return s

def _spost__mul_expr(oresult, /):
    #mul_expr = pow_expr ( ('*' | '/' | '//' | '%') sign* mul_expr)?
    a, tmay_op_signs_b = oresult
    match tmay_op_signs_b:
        case [(op, signs, b)]:
            b = _signed(signs, b)
            match op:
                case '*':
                    s = a*b
                case '/':
                    s = Fraction(a)/b
                case '//':
                    s = a//b
                case '%':
                    s = a%b
                case _:
                    raise 000
        case []:
            s = a
        case _:
            raise 000
    return s


def _spost__add_expr(oresult, /):
    # !! bug:add_expr = sign* mul_expr ( ('+' | '-') add_expr)?
    # => add_expr = mkrs.serial_([ref__signs, ref__mul_expr, mkrs.many_(mkrs.serial_([op8add, ref__signs, ref__mul_expr]))])
    signs, a, ls4op_signs_b = oresult
    a = _signed(signs, a)
    for (op, signs, b) in ls4op_signs_b:
        b = _signed(signs, b)
        match op:
            case '+':
                a += b
            case '-':
                a -= b
            case _:
                raise 000
    return a


def prepare4parse4arith_():
    '-> (grp4nm4rgnr4parse__7arith, name2may_gpostprocess6ok4parse__7arith, name2rgnr4parse__7arith, nmd__arith_expr, max_num_tokens6backward4parse__7arith, env4parse__7arith)'
    ######################
    from seed.tiny import fmap4dict_value, MapView
    ######################
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import collect_namess5locals_, mk_group_pair4rgnr_ref, Makers4IRecognizerLLoo
    from seed.types.IToken import TokenKeyQuerySet5xqset
    from seed.types.Tester import Tester__eq_obj
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import Environment, mk_gpostprocess6ok__5spost_
    ######################
    tkn_qset5xqset_ = TokenKeyQuerySet5xqset
    mkrs = Makers4IRecognizerLLoo
    ######################
    number = mkrs.spost__tkn2tdat_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('number'))))
        # tkn -> tdat
    ######################
    # tkn -> tkey
    sym6 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('('))))
    sym9 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(')'))))
    sym_pow = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('**'))))
    sym_mul = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('*'))))
    sym_true_div = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('/'))))
    sym_floor_div = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('//'))))
    sym_mod = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('%'))))
    sym_plus = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('+'))))
    sym_diff = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('-'))))
    ######################
    sign = mkrs.priority_parallel_([sym_plus, sym_diff])
    op8pow = sym_pow
    op8mul = mkrs.priority_parallel_([sym_mul, sym_true_div, sym_floor_div, sym_mod])
    op8add = sign
    signs = mkrs.many_(sign)
    ######################

    ######################
    (grp4nm4rgnr, grp4rgnr_ref) = mk_group_pair4rgnr_ref()
    ######################
    ref__atom_expr = grp4rgnr_ref.atom_expr
    ref__pow_expr = grp4rgnr_ref.pow_expr
    ref__mul_expr = grp4rgnr_ref.mul_expr
    ref__add_expr = grp4rgnr_ref.add_expr
    ref__arith_expr = grp4rgnr_ref.arith_expr
    ref__sign = grp4rgnr_ref.sign
    ref__signs = grp4rgnr_ref.signs
    ######################
    atom_expr = mkrs.priority_parallel_([mkrs.tag_(number, 'number'), mkrs.tag_(mkrs.between_(sym6, sym9, ref__arith_expr), 'group')])
    pow_expr = mkrs.serial_([ref__atom_expr, mkrs.optional__strict_(mkrs.serial_([op8pow, ref__signs, ref__pow_expr]))])
    mul_expr = mkrs.serial_([ref__pow_expr, mkrs.optional__strict_(mkrs.serial_([op8mul, ref__signs, ref__mul_expr]))])
    #bug-1:add_expr = mkrs.serial_([ref__signs, ref__mul_expr, mkrs.optional__strict_(mkrs.serial_([op8add, ref__signs, ref__add_expr]))])
    #   should remove snd ref__signs
    #bug-2:grammar-error:add_expr = mkrs.serial_([ref__signs, ref__mul_expr, mkrs.optional__strict_(mkrs.serial_([op8add, ref__add_expr]))])
    #   !! bug:add_expr = sign* mul_expr ( ('+' | '-') add_expr)?
    #   => add_expr = sign* mul_expr ( ('+' | '-') sign* mul_expr)*
    add_expr = mkrs.serial_([ref__signs, ref__mul_expr, mkrs.many_(mkrs.serial_([op8add, ref__signs, ref__mul_expr]))])
    arith_expr = ref__add_expr
    ######################
    #:.,.+9s/^\( *\)ref__\(\w*\) = grp4rgnr_ref.\2$/\1nmd__\2 = ref__\2.mk_named_rgnr_(\2)
    nmd__atom_expr = ref__atom_expr.mk_named_rgnr_(atom_expr)
    nmd__pow_expr = ref__pow_expr.mk_named_rgnr_(pow_expr)
    nmd__mul_expr = ref__mul_expr.mk_named_rgnr_(mul_expr)
    nmd__add_expr = ref__add_expr.mk_named_rgnr_(add_expr)
    nmd__arith_expr = ref__arith_expr.mk_named_rgnr_(arith_expr)
    nmd__sign = ref__sign.mk_named_rgnr_(sign)
    nmd__signs = ref__signs.mk_named_rgnr_(signs)
    ######################
    (name2rgnr, nms4ref, nms6ref) = collect_namess5locals_(locals(), _no_check__vs__ge__vs__eq_=2)
    ######################
    name2may_gpostprocess6ok = MapView(fmap4dict_value(mk_gpostprocess6ok__5spost_, {**{}
    ,nmd__atom_expr._may_name4ref_:_spost__atom_expr
        #fixed-bug:miss postprocess<atom_expr>
    ,nmd__pow_expr._may_name4ref_:_spost__pow_expr
    ,nmd__mul_expr._may_name4ref_:_spost__mul_expr
    ,nmd__add_expr._may_name4ref_:_spost__add_expr
        #fixed-bug:miss 『._may_name4ref_』
    }))
    ######################
    name2rgnr4parse__7arith = name2rgnr
    max_num_tokens6backward4parse__7arith = 0
    name2may_gpostprocess6ok4parse__7arith = name2may_gpostprocess6ok
    grp4nm4rgnr4parse__7arith = grp4nm4rgnr
    ######################
    env4parse__7arith = Environment(param2setting:={}, name2rgnr:=name2rgnr4parse__7arith, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:=name2may_gpostprocess6ok4parse__7arith)
    ######################
    return (grp4nm4rgnr4parse__7arith, name2may_gpostprocess6ok4parse__7arith, name2rgnr4parse__7arith, nmd__arith_expr, max_num_tokens6backward4parse__7arith, env4parse__7arith)
    ######################
#end-def prepare4parse4arith_():

def prepare4tokenize4arith_():
    '-> (tkey2tdat2tdat4tknz__7arith, tkeys8noise4tknz__7arith, rgnr4tknz__7arith, max_num_tokens6backward4tknz__7arith, may_env4tknz__7arith)'
    'tkeys = ** // % * / + - ( ) number'
    from seed.tiny import MapView
    from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import mk_rgnr4words_
    ######################

    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import Makers4IRecognizerLLoo
    from seed.types.IToken import TokenKeyQuerySet5xqset
    from seed.types.IToken import char_qset__isdecimal, char_qset__isspace
    from seed.types.Tester import Tester__eq_obj
    from seed.types.Either import Cased, Either
    from seed.types.Either import mk_Left, mk_Right
    ######################
    tkn_qset5xqset_ = TokenKeyQuerySet5xqset
    mkrs = Makers4IRecognizerLLoo
    ######################

    op = mk_rgnr4words_('** // % * / + - ( )'.split())
    rgnr8digit = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(char_qset__isdecimal)))
    digits1 = mkrs.many_(rgnr8digit, 1)
    spaces1 = mkrs.many_(mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(char_qset__isspace))), 1)
    rgnr4tknz__7arith = mkrs.priority_parallel_([mkrs.tag_(spaces1, 'space'), mkrs.tag_(digits1, 'number'), mkrs.spostprocess_(op, None, lambda op:Cased(op, None), _force_postprocess_when_ignore_:=True)])
    tkeys8noise4tknz__7arith = frozenset(['space'])
    max_num_tokens6backward4tknz__7arith = 0
    may_env4tknz__7arith = None
    tkey2tdat2tdat4tknz__7arith = MapView({'number':lambda cs:int(''.join(cs))})
    return (tkey2tdat2tdat4tknz__7arith, tkeys8noise4tknz__7arith, rgnr4tknz__7arith, max_num_tokens6backward4tknz__7arith, may_env4tknz__7arith)
#end-def prepare4tokenize4arith_():
if 1:
  #def __():
    (grp4nm4rgnr4parse__7arith, name2may_gpostprocess6ok4parse__7arith, name2rgnr4parse__7arith, nmd__arith_expr, max_num_tokens6backward4parse__7arith, env4parse__7arith) = prepare4parse4arith_()
    (tkey2tdat2tdat4tknz__7arith, tkeys8noise4tknz__7arith, rgnr4tknz__7arith, max_num_tokens6backward4tknz__7arith, may_env4tknz__7arith) = prepare4tokenize4arith_()

if 1:
  def __():
    from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__core_, tokenize__args8chars_
    from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__chars_, tokenize__file_, tokenize__path_
    from seed.types.IToken import mk_gap_position_info_at_ifile_begin
def tokenize7arith__pseudo_fname_(pseudo_fname, src, may_tkey2tdat2tdat=None, /):
    'str -> Iter char -> istream7arith'
    from seed.recognize.recognizer_LLoo__ver2_.tokenize_utils import tokenize__chars_
    from seed.types.IToken import mk_gap_position_info_at_ifile_begin
    #def tokenize__chars_(may_tkey2tdat2tdat, may_tkeys8noise4tknz, rgnr4tknz, chr_tgbegin, chars, /, *, to_flatten:bool, max_num_tokens6backward4low_lvl=0, max_num_tokens6backward4high_lvl=0, may_env4tknz=None):
    chr_tgbegin6pseudo_fname = mk_gap_position_info_at_ifile_begin(pseudo_fname)

    tkey2tdat2tdat4tknz__7arith
    tkeys8noise4tknz__7arith
    rgnr4tknz__7arith
    max_num_tokens6backward4tknz__7arith
    max_num_tokens6backward4parse__7arith
    may_env4tknz__7arith

    if may_tkey2tdat2tdat is None:
        may_tkey2tdat2tdat = tkey2tdat2tdat4tknz__7arith
    return tokenize__chars_(may_tkey2tdat2tdat, tkeys8noise4tknz__7arith, rgnr4tknz__7arith, chr_tgbegin6pseudo_fname, src, to_flatten=False, max_num_tokens6backward4low_lvl=max_num_tokens6backward4tknz__7arith, max_num_tokens6backward4high_lvl=max_num_tokens6backward4parse__7arith, may_env4tknz=may_env4tknz__7arith)
def parse7arith__pseudo_fname_(pseudo_fname, src, may_tkey2tdat2tdat=None, may_name2may_gpostprocess6ok4parse=None, /):
    'str -> Iter char -> Reply'
    istream7arith = tokenize7arith__pseudo_fname_(pseudo_fname, src, may_tkey2tdat2tdat)
    return parse7arith__istream_(istream7arith, may_name2may_gpostprocess6ok4parse)
def parse7arith__istream_(istream7arith, may_name2may_gpostprocess6ok4parse=None, /):
    'istream7arith -> Reply'
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import recognize_, Environment
    #used to create new may_name2may_gpostprocess6ok4parse:grp4nm4rgnr4parse__7arith
    #used@env4parse__7arith:name2may_gpostprocess6ok4parse__7arith
    #used@env4parse__7arith:name2rgnr4parse__7arith
    nmd__arith_expr
    #used@istream7arith:max_num_tokens6backward4parse__7arith
    env4parse__7arith

    ######################
    env4parse = env4parse__7arith if may_name2may_gpostprocess6ok4parse is None or may_name2may_gpostprocess6ok4parse == name2may_gpostprocess6ok4parse__7arith else Environment(param2setting:={}, name2rgnr:=name2rgnr4parse__7arith, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:=may_name2may_gpostprocess6ok4parse)
    ######################
    if 0b0000:
        from seed.tiny import print_err
        print_err(env4parse._nm2mpost6ok)
    ######################
    reply = recognize_(nmd__arith_expr, env4parse, gctx:={}, istream7arith)
    return reply

def eval7arith(src, /):
    reply = parse7arith__pseudo_fname_('<eval7arith>', iter(src))
    if not reply.ok:raise SyntaxError(reply.ext_info8end, reply.errmsg)
        #ext_info8begin???
    oresult = reply.oresult
    assert type(oresult) in (int, Fraction, float, complex)
    if type(oresult) in (int, Fraction):
        (N, D) = oresult.as_integer_ratio()
        if D == 1:
            oresult = N
    return oresult

__all__
from seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression import eval7arith, parse7arith__pseudo_fname_
from seed.recognize.recognizer_LLoo__ver2_.example__arithmetic_expression import *
