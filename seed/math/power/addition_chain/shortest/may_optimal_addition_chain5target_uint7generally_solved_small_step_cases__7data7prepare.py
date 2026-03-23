#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare.py
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare__py_adhoc_call.py

seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare   @f
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import print_err, at
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.pkg_tools.load_resource import read_under_pkg_

    from operator import call
    #.from functools import cached_property
    from seed.for_libs.for_functools.cached_property import cached_property
    from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data import 阳爻模板巛丨允负序号扌

#view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py
#view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py
#view ../../python3_src/seed/recognize/text_recognizer/TextRecognizer__util.py
    #_ver2解读冫阳爻模板扌
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.recognize.text_recognizer.ITextRecognizer import parse_text_, env4ops4oresult_seq__ftSeq, env4ops4oresult_seq__list
        #def parse_text_(txt_rgnr, env, txt, begin, end, /):
        #   'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> ParseResult/(OResult|Errmsg)'
        #   Errmsg(errmsg,end,severe){ok:=False}{ko:=True}
        #   OResult(oresult,end){ok:=True}{ko:=False}
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.recognize.text_recognizer.ITextRecognizer import (
#after:_BaseTextRecognizer__ops4mkr
#   other_mkrs:goto
ITextRecognizer
,mk_tagged_txt_rgnr_fallback_
,mk_ignorable_txt_rgnr_serial_
,mk_txt_rgnr__regex_#kw:as_regex
,mk_txt_rgnr__text_#kw:as_regex
,mk_txt_rgnr__oresult_
,mk_txt_rgnr__errmsg_
#_BaseTextRecognizer__ops4mkr::
#   .on_ok_
#   .on_ko_
#   .on_errmsg6ko_
#   .named_
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


#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#################################
def _加载冫文本冃阳爻模板数据扌():
    _文本冃阳爻模板数据 = read_under_pkg_(__package__, 'may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.bit_ptn_dat.txt', xencoding='ascii')
    return _文本冃阳爻模板数据
def _加载冫文本冃加链模板数据扌():
    _文本冃加链模板数据 = read_under_pkg_(__package__, 'may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.chain_ptn_dat.txt', xencoding='ascii')
    return _文本冃加链模板数据

##################################
##################################
##################################

def _版本比较冫趃解读冫阳爻模板灬扌(ver1, ver2, /):
    t1 = tuple(_趃解读冫阳爻模板灬扌(..., ver=ver1))
    t2 = tuple(_趃解读冫阳爻模板灬扌(..., ver=ver2))
    if not t1 == t2:
        if not len(t1) == len(t2): raise Exception(ver1, ver2, (len(t1), len(t2)))
        for a1, a2 in zip(t1, t2):
            if not a1 == a2: raise Exception(ver1, ver2, (a1, a2))
            #Exception: (1, 2, ((-1, 1, 2, True, 2, (((0, 1),), ((1, 1),)), ()), (-1, 1, 2, True, 2, (((0, 1),), ((0, 1),)), ())))
            #   => imay_jvar_coeff_pair5smay_var_coeff_pair_():.get()-->var2jvar.setdefault()
            #
            #Exception: (1, 2, ((92, 3, 6, True, 3, (((0, 1),), ((1, 1),), ((1, 1), (-1, -2)), ((2, 1),), ((2, 1), (-1, -1)), ((0, -1), (1, 1), (2, 1), (-1, 1))), (((0, -1), (1, 1), (2, 1)),)), (92, 3, 6, True, 3, (((0, 1),), ((1, 1),), ((1, 1), (-1, -2)), ((2, 1),), ((2, 1), (-1, -1)), ((0, -1), (1, 1), (2, 1), (-1, 1))), (((0, -1), (1, 1), (2, 1), (-1, 0)),))))
            #   => post4ieqn_():++rhs.filter『if coeff』
            #
        raise 000
def _版本号讠解读冫阳爻模板扌(ver, /):
    match ver:
        case 1:
            解读冫阳爻模板扌 = _ver1解读冫阳爻模板扌
        case 2:
            解读冫阳爻模板扌 = _ver2解读冫阳爻模板扌
        case _:
            raise Exception('unknown version:', ver)
    return 解读冫阳爻模板扌
#_趃解读冫阳爻模板灬扌(_文本冃阳爻模板数据)
def _趃解读冫阳爻模板灬扌(彧文本, /, *, ver=1):
    'emay str -> Iter 阳爻模板/(允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式)'
    解读冫阳爻模板扌 = _版本号讠解读冫阳爻模板扌(ver)
    文本 = _加载冫文本冃阳爻模板数据扌() if 彧文本 is ... else 彧文本
    prefix = '#Representable Numbers with '
    suffix = ' Small Step Chains'
    for s in 文本.split('\n'):
        s = s.strip()
        if s and (s[0].isdigit() or s[0] == '-'):
            yield 解读冫阳爻模板扌(总小步数, s)
        elif s.startswith(prefix) and s.endswith(suffix):
            总小步数 = int(s.removeprefix(prefix).removesuffix(suffix))
def _parse7full_(parse_text_, s, /):
    parse_result = parse_text_(s, 0, len(s))
    #match parse_result:
    if not parse_result.ok:
        raise Exception(parse_result, s[parse_result.end:])
    if not parse_result.end == len(s):
        raise Exception(parse_result, len(s)-parse_result.end, s[parse_result.end:])
    return parse_result.oresult

def _ver2解读冫阳爻模板扌(num_small_steps, s, /, *, 欤带变量名讠变量号=False):
    parse_text4record7miss_num_small_steps_ = _gmk_parse_text4record7miss_num_small_steps_()
    record7miss_num_small_steps = _parse7full_(parse_text4record7miss_num_small_steps_, s)
    (nidx, bitsum, whether_star_chain, tmay_num_vars, ls4smay_var_coeff_pairs8bits, ls4smay_var_coeff_pairs8ineqns) = record7miss_num_small_steps
    var2jvar = {}
    (ls5expr_, lss5exprs_) = _mk_ls5exprs_(var2jvar)
    ls8bits = lss5exprs_(ls4smay_var_coeff_pairs8bits)
    ls8ineqns = lss5exprs_(ls4smay_var_coeff_pairs8ineqns)
    num_vars = len(var2jvar)
    if tmay_num_vars and not tmay_num_vars == (num_vars,):raise Exception(tmay_num_vars, num_vars)
    record = (nidx, num_small_steps, bitsum, whether_star_chain, num_vars, ls8bits, ls8ineqns)
    hash(record)
    return record if not 欤带变量名讠变量号 else (record, var2jvar)
def _mk_ls5exprs_(var2jvar, /):
    #def _mk_imay_jvar_coeff_pairs5smay_var_coeff_pairs_(var2jvar, /):
    def imay_jvar_coeff_pair5smay_var_coeff_pair_(smay_var_coeff_pair, /):
        (smay_var, coeff) = smay_var_coeff_pair
        match smay_var:
            case '':
                imay_jvar = -1
            case var:
                #bug:jvar = var2jvar.get(var, len(var2jvar))
                jvar = var2jvar.setdefault(var, len(var2jvar))
                imay_jvar = jvar
        return (imay_jvar, coeff)
    def imay_jvar_coeff_pairs5smay_var_coeff_pairs_(smay_var_coeff_pairs, /):
        return tuple(map(imay_jvar_coeff_pair5smay_var_coeff_pair_, smay_var_coeff_pairs))
    #return imay_jvar_coeff_pairs5smay_var_coeff_pairs_
    def ls5expr_(expr, /):
        ls8expr = imay_jvar_coeff_pairs5smay_var_coeff_pairs_(expr)
        return ls8expr
    def lss5exprs_(exprs, /):
        lss8exprs = tuple(map(ls5expr_, exprs))
        return lss8exprs
    return (ls5expr_, lss5exprs_)
def _gmk_parse_text4record7miss_num_small_steps_():
    try:
        return _parse_text4record7miss_num_small_steps_
    except NameError:
        pass
    _prepare_1_2()
    return _gmk_parse_text4record7miss_num_small_steps_()
def _gmk_txt_rgnrs_1_2():
    try:
        return (_1_txt_rgnrs, _2_txt_rgnrs)
    except NameError:
        pass
    _prepare_1_2()
    return _gmk_txt_rgnrs_1_2()
if 0:
    _parse_text4record7miss_num_small_steps_ = ...
    _1_txt_rgnrs = ...
    _2_txt_rgnrs = ...
def _prepare_1_2():
    global _parse_text4record7miss_num_small_steps_, _1_txt_rgnrs, _2_txt_rgnrs
    from seed.recognize.text_recognizer.TextRecognizer__util import txt_rgnrs as _1_txt_rgnrs
    #txt_rgnr__decimal_int
    #txt_rgnr__decimal_uint
    #txt_rgnr__digits1
    #txt_rgnr__hexadecimal_int
    #txt_rgnr__hexadecimal_uint
    #txt_rgnr__hexdigits1
    #txt_rgnr__sign
    #txt_rgnr__signspaces0
    #txt_rgnr__spaces0
    #txt_rgnr__spaces1
    def post4ieqn_(t, /):
        match t:
            case (lhs, '>=', rhs):
                smay_var_coeff_pairs = (*lhs, *((smay_var, -coeff) for (smay_var, coeff) in rhs if coeff))
                return smay_var_coeff_pairs
            case _:
                raise Exception(t)
    def post4signed(sgn__sm_u, /):
        (sgn, (smay_var, coeff)) = sgn__sm_u
        return (smay_var, sgn*coeff)


    ########################
    @call
    class _2_txt_rgnrs:
        def __getattr__(sf, nm, /):
            return getattr(_1_txt_rgnrs, nm)

        # 25 5* 3  @(p)+@(q)+@(-p+2q-2)+@(r)+@(-p+q+r-1)
        # 42 6* 2  @(p)+@(p-7)+@(q)+@(q-3)+@(q-4)+@(q-5) ,q>=6
        txt_rgnr__var = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'[A-Za-z]', 0).named_('var'))
        txt_rgnr__sign1 = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'[-+]', 0).on_ok_(lambda s:-1 if s=='-' else +1).named_('sign1'))
        txt_rgnr__smay_var_unsigned_coeff = cached_property(lambda sf, /: sf.txt_rgnr__var.on_ok_(lambda nm:(nm, 1)).else_(sf.txt_rgnr__decimal_uint.then_(sf.txt_rgnr__var.optional_().on_ok_(lambda tm:tm[0] if tm else '')).on_ok_(lambda t:t[::-1])).named_('smay_var_unsigned_coeff'))
        txt_rgnr__smay_var_signed_coeff = cached_property(lambda sf, /: sf.txt_rgnr__sign1.then_(sf.txt_rgnr__smay_var_unsigned_coeff).on_ok_(post4signed).named_('smay_var_signed_coeff'))
        txt_rgnr__smay_var_optional_signed_coeff = cached_property(lambda sf, /: sf.txt_rgnr__smay_var_signed_coeff.else_(sf.txt_rgnr__smay_var_unsigned_coeff).named_('smay_var_optional_signed_coeff'))

        txt_rgnr__bit_ptn_expr = cached_property(lambda sf, /: (+sf.txt_rgnr__smay_var_optional_signed_coeff).then_(~sf.txt_rgnr__smay_var_signed_coeff.many0_(), cased=True).named_('bit_ptn_expr'))
        txt_rgnr__ieqn = cached_property(lambda sf, /: sf.txt_rgnr__bit_ptn_expr.then_(mk_txt_rgnr__text_('>='), sf.txt_rgnr__bit_ptn_expr).on_ok_(post4ieqn_).named_('ieqn'))

        txt_rgnr__bit_ptn_exprs1 = cached_property(lambda sf, /: (+sf.txt_rgnr__bit_ptn_expr.enclosed_by_('@(', ')').named_('enclosed_bit_ptn')).sep_by_(-mk_txt_rgnr__text_('+'), cased=True).named_('bit_ptn_exprs1'))
        txt_rgnr__ieqns0 = cached_property(lambda sf, /: sf.txt_rgnr__ieqn.enclosed_by_(r' *, *', r'', as_regex=True).many0_().named_('ieqns0'))

        txt_rgnr__tmay_num_vars__spaces1 = cached_property(lambda sf, /: sf.txt_rgnr__decimal_uint.enclosed_by_('', sf.txt_rgnr__spaces1).optional_().named_('tmay_num_vars'))

        txt_rgnr__record7miss_num_small_steps = cached_property(lambda sf, /: (+sf.txt_rgnr__decimal_int).then_(-sf.txt_rgnr__spaces1, +sf.txt_rgnr__decimal_uint, +mk_txt_rgnr__text_('*').optional_().on_ok_(bool), -sf.txt_rgnr__spaces1, +sf.txt_rgnr__tmay_num_vars__spaces1, +sf.txt_rgnr__bit_ptn_exprs1, -sf.txt_rgnr__spaces0, +sf.txt_rgnr__ieqns0, cased=True).named_('record7miss_num_small_steps'))
    _2_txt_rgnrs
    ########################
    def _parse_text4record7miss_num_small_steps_(txt, begin, end, /):
        txt_rgnr = _2_txt_rgnrs.txt_rgnr__record7miss_num_small_steps
        env = env4ops4oresult_seq__list
        return parse_text_(txt_rgnr, env, txt, begin, end)
    ########################
    return

def _ver1解读冫阳爻模板扌(num_small_steps, s, /, *, 欤带变量名讠变量号=False):
    'str -> 阳爻模板/(允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式)'
    #s_, _, smay7bound = s.partition(',')
    [s_, *ls4s7bound] = s.split(',')
    (s7nidx, s7bitsum_whether_star, s7num_vars, s7bit_pattern_expr) = s_.split()
    nidx = int(s7nidx)
    bitsum = int(s7bitsum_whether_star.removesuffix('*'))
    whether_star_chain = s7bitsum_whether_star.endswith('*')
    num_vars = int(s7num_vars)
    var2jvar = {}
    ls8bits = [_解读冫表达式冃阳爻位扌(var2jvar, s7bit_expr) for s7bit_expr in s7bit_pattern_expr.replace('+@', '+:@').split('+:')]
    ls8ineqns = [_解读冫不等式冃非负整数扌(var2jvar, s7uint_expr) for s7uint_expr in ls4s7bound]
    ls8bits = tuple(ls8bits)
    ls8ineqns = tuple(ls8ineqns)
    record = (nidx, num_small_steps, bitsum, whether_star_chain, num_vars, ls8bits, ls8ineqns)
    hash(record)
    return record if not 欤带变量名讠变量号 else (record, var2jvar)
def _解读冫表达式冃阳爻位扌(var2jvar, s7bit_expr, /):
    s = s7bit_expr.removeprefix('@(').removesuffix(')')
    if not len(s)+3 == len(s7bit_expr):raise Exception(s7bit_expr)
    return _解读冫表达式扌(var2jvar, s)
def _解读冫表达式扌(var2jvar, s, /):
    def __():
        begin = 0
        end = len(s)
        while not begin == end:
            (coeff, _begin) = _解读冫系数扌(s, begin, end)
            (imay_jvar, _2_begin) = _解读冫毝变量号牜单字母扌(var2jvar, s, _begin, end)
            if imay_jvar == -1:
                if begin == _begin: raise Exception(s[begin:end])
            else:
                jvar = imay_jvar
            #if 0b00001:print_err(s, begin, _begin, _2_begin, imay_jvar, coeff)
            yield (imay_jvar, coeff)
            begin = _2_begin
    ls8expr = tuple(__())
    return ls8expr
def _解读冫正负号扌(s, begin, end, /):
    sign = +1
    for i in range(begin, end):
        match s[i]:
            case '+':
                continue
            case '-':
                sign = -sign
            case _:
                _begin = i
                break
    else:
        _begin = end
    return (sign, _begin)
def _解读冫十进制数字牜无符号扌(s, begin, end, /):
    for i in range(begin, end):
        if not s[i].isdigit():
            _begin = i
            break
    else:
        _begin = end
    t = s[begin:_begin]
    u = int(t) if t else 1
    return (u, _begin)
def _解读冫十进制数字牜带符号扌(s, begin, end, /):
    (sign, begin) = _解读冫正负号扌(s, begin, end)
    (u, begin) = _解读冫十进制数字牜无符号扌(s, begin, end)
    i = sign*u
    return (i, begin)
def _解读冫系数扌(s, begin, end, /):
    (i, begin) = _解读冫十进制数字牜带符号扌(s, begin, end)
    return (i, begin)
#def _解读冫彣变量名牜单字母扌(var2jvar, s, begin, end, /):
def _解读冫毝变量号牜单字母扌(var2jvar, s, begin, end, /):
    if begin < end and (nm:=s[begin]).isalpha():
        jvar = var2jvar.setdefault(nm, len(var2jvar))
        imay_jvar = jvar
        _begin = 1+begin
    else:
        imay_jvar = -1
        _begin = begin
    return (imay_jvar, _begin)
def _解读冫不等式冃非负整数扌(var2jvar, s7uint_expr, /):
    lhs, rhs = s7uint_expr.split('>=')
    ls8expr = _解读冫表达式扌(var2jvar, lhs)
    rhs = int(rhs)
    if not rhs == 0:
        ls8expr = (*ls8expr, (-1, -rhs))
    return ls8expr
#################################



#def 阳爻模板巛丨允负序号扌(阳爻模板丨允负序号, /):










##################################
##################################
##################################
################################
#### [lss == idx2span == idx2uss :: [[uint]]]
#format:
#   "0"
#       => lss[0] := [1]
#   "idx4span(idx4span4big_addend, idx4span4little_addend)"
#       => lss[idx4span] := [lss[idx4span4big_addend][-1]+lss[idx4span4little_addend][-1]]
#   "idx4span(idx4span4big_addend, idx4span4little_addend:ez)"
#       => lss[idx4span] := [lss[idx4span4big_addend][-1]+lss[idx4span4little_addend][ez-1]]
#   ####above:3 fmts:solo_span
#   ####below:1 fmts:long_span
#   "idx4span(idx4span4big_addend, *:max_ez)"
#       => lss[idx4span] := [lss[idx4span4big_addend][-1] << ez for ez in range(1,1+max_ez)]
################################
#

if 0:
    _parse_text4def_new_vars_ = ...
    _parse_text4addtwo_ex_ = ...
    _3_txt_rgnrs = ...
def _prepare_1_2_3():
    global _3_txt_rgnrs, _parse_text4def_new_vars_, _parse_text4addtwo_ex_
    (_1_txt_rgnrs, _2_txt_rgnrs) = _gmk_txt_rgnrs_1_2()
    ########################
    def post4idx4span_ex7little_addend_(may_idx4span4little_addend__tmay_expr8ez__pair, /):
        '-> midx_mexpr_pair/(may_idx4span4little_addend, may_expr8ez)'
        # (may_idx4span4little_addend, tmay_expr8ez) = may_idx4span4little_addend__tmay_expr8ez__pair
        match may_idx4span4little_addend__tmay_expr8ez__pair:
            case (None, (expr8max_ez,)):
                '*:max_ez'
                midx_mexpr_pair = (None, expr8max_ez)
            case (idx4span4little_addend, (expr8ez,)):
                'j:ez'
                midx_mexpr_pair = (idx4span4little_addend, expr8ez)
            case (idx4span4little_addend, ()):
                'j'
                midx_mexpr_pair = (idx4span4little_addend, None)
            case bad:
                raise Exception(bad)
            #case
        midx_mexpr_pair
        return midx_mexpr_pair
    ########################
    @call
    class _3_txt_rgnrs:
        def __getattr__(sf, nm, /):
            return getattr(_2_txt_rgnrs, nm)

        # 25 5* 3  @(p)+@(q)+@(-p+2q-2)+@(r)+@(-p+q+r-1)
        # 42 6* 2  @(p)+@(p-7)+@(q)+@(q-3)+@(q-4)+@(q-5) ,q>=6
        #注意:缺失:num_vars
        #8 5* @(p)+@(p-7)+@(q)+@(q-1)+@(q-3) ,q>=4
        #  A=p-6,  C=q-4
        #  0                 1
        #  1( 0, *:A)        @(A)
        #  2( 1, 1:A-1)      @(A)+@(A-1)
        #  3( 2, 1:C)        @(A)+@(A-1)+@(C)
        #   ... ...
        #
        #90 6* @(p)+@(q)+@(p-5)+@(q-3)+@(q-4)+@(q-5)
        #   A=q-4,  E=p-q-2
        #   0                 1
        #   1( 0, *:A)        @(A)
        #   2( 1, 1:A-1)      @(A)+@(A-1)
        #   3( 2, *:3)        @(A+3)+@(A+2)
        #   4( 3, 2  )        @(A+3)+@(A+2)+@(A)+@(A-1)
        #   5( 4, 3:2)        @(A+4)+@(A+1)+@(A)+@(A-1)
        #   ... ...
        #
        #   『0』 => lss[0] := [1]
        #   『址引纟阶段(址引纟阶段纟大加数, 址引纟阶段纟小加数)』 => lss[址引纟阶段] := [lss[址引纟阶段纟大加数][-1]+lss[址引纟阶段纟小加数][-1]]
        #   『址引纟阶段(址引纟阶段纟大加数, 址引纟阶段纟小加数:幂次)』 => lss[址引纟阶段] := [lss[址引纟阶段纟大加数][-1]+lss[址引纟阶段纟小加数][幂次-1]]
        #   『址引纟阶段(址引纟阶段纟大加数, *:最大幂次)』 => lss[址引纟阶段] := [lss[址引纟阶段纟大加数][-1] << ez for ez in range(1,1+最大幂次)]
        #
        #txt_rgnr__bit_ptn_expr
        #txt_rgnr__bit_ptn_exprs1
        txt_rgnr__def_new_var = cached_property(lambda sf, /: (+sf.txt_rgnr__var).then_(-mk_txt_rgnr__text_('='), +sf.txt_rgnr__bit_ptn_expr, cased=True).named_('def_new_var'))
        txt_rgnr__def_new_vars = cached_property(lambda sf, /: (+sf.txt_rgnr__def_new_var).sep_by_(-mk_txt_rgnr__regex_(' *, *', 0), cased=True).named_('def_new_vars'))

        txt_rgnr__zero = cached_property(lambda sf, /: mk_txt_rgnr__text_(r'0').named_('zero'))
        txt_rgnr__idx4span = cached_property(lambda sf, /: sf.txt_rgnr__decimal_uint.named_('idx4span'))
        txt_rgnr__idx4span_ex7little_addend = cached_property(lambda sf, /: (sf.txt_rgnr__idx4span.else_(mk_txt_rgnr__text_(r'*').on_ok_(None, -1))).then_(sf.txt_rgnr__bit_ptn_expr.enclosed_by_(r':', '').optional_()).on_ok_(post4idx4span_ex7little_addend_).named_('idx4span_ex7little_addend'))
        txt_rgnr__addtwo = cached_property(lambda sf, /: (+sf.txt_rgnr__idx4span).then_(-sf.txt_rgnr__spaces0, -mk_txt_rgnr__text_(r'('), -sf.txt_rgnr__spaces0, +sf.txt_rgnr__idx4span, -sf.txt_rgnr__spaces0, -mk_txt_rgnr__text_(r','), -sf.txt_rgnr__spaces0, +sf.txt_rgnr__idx4span_ex7little_addend, -sf.txt_rgnr__spaces0, -mk_txt_rgnr__text_(r')'), cased=True).named_('addtwo'))
        txt_rgnr__addtwo_ex = cached_property(lambda sf, /: (+sf.txt_rgnr__addtwo).then_(-sf.txt_rgnr__spaces1, +sf.txt_rgnr__bit_ptn_exprs1, cased=True).named_('addtwo_ex'))
        ###################
        #三行型:
        #txt_rgnr__record7miss_num_small_steps
        txt_rgnr__def_new_vars
        txt_rgnr__addtwo_ex
        ###################
    _3_txt_rgnrs
    _3_txt_rgnrs.txt_rgnr__record7miss_num_small_steps
    _3_txt_rgnrs.txt_rgnr__def_new_vars
    _3_txt_rgnrs.txt_rgnr__addtwo_ex
    ########################
    def _parse_text4def_new_vars_(txt, begin, end, /):
        txt_rgnr = _3_txt_rgnrs.txt_rgnr__def_new_vars
        env = env4ops4oresult_seq__list
        return parse_text_(txt_rgnr, env, txt, begin, end)
    def _parse_text4addtwo_ex_(txt, begin, end, /):
        txt_rgnr = _3_txt_rgnrs.txt_rgnr__addtwo_ex
        env = env4ops4oresult_seq__list
        return parse_text_(txt_rgnr, env, txt, begin, end)
    ########################
    return
def _gmk_txt_rgnrs_3():
    try:
        return _3_txt_rgnrs
    except NameError:
        pass
    _prepare_1_2_3()
    return _gmk_txt_rgnrs_3()
def _gmk_parse_text4def_new_vars_():
    try:
        return _parse_text4def_new_vars_
    except NameError:
        pass
    _prepare_1_2_3()
    return _gmk_parse_text4def_new_vars_()
def _gmk_parse_text4addtwo_ex_():
    try:
        return _parse_text4addtwo_ex_
    except NameError:
        pass
    _prepare_1_2_3()
    return _gmk_parse_text4addtwo_ex_()
#
#_趃解读冫加链模板灬扌(_文本冃加链模板数据)
def _趃解读冫加链模板灬扌(彧文本, /):
    'emay str -> Iter (允负序号, jnvar2old_ls8expr, k2j_ls8ez_pairs)'
    #'emay str -> 临时:Iter (阳爻模板, jnvar2old_ls8expr, k2j_ls8ez_pairs)'
    _ver2解读冫阳爻模板扌
        # !! ver2:tmay_num_vars
    parse_text4def_new_vars_ = _gmk_parse_text4def_new_vars_()
    parse_text4addtwo_ex_ = _gmk_parse_text4addtwo_ex_()
    文本 = _加载冫文本冃加链模板数据扌() if 彧文本 is ... else 彧文本
    prefix = '#Shortest Addition Chains with '
    suffix = ' Small Steps'
    lines = 文本.split('\n')
    it = map(str.strip, lines)
    def iprint_err(s, /):
        print_err(s)
        return s
    #if 0b00001:it = map(iprint_err, it)
    for s in it:
        #s = s.strip()
        if not s:
            #yield from _flush()
            continue
        elif s.startswith('#'):
            if s.startswith(prefix):
                if not s.endswith(suffix):raise Exception(s)
                总小步数 = int(s.removeprefix(prefix).removesuffix(suffix))
            continue
        elif (s[0].isdigit() or s[0] == '-'):
            (阳爻模板, 变量名讠变量号) = _ver2解读冫阳爻模板扌(总小步数, s, 欤带变量名讠变量号=True)
            允负序号 = 阳爻模板[0]
            if not 阳爻模板 == (__:=阳爻模板巛丨允负序号扌(允负序号)):raise Exception(阳爻模板, __)
            s7new_vars_ex = next(it, None)
            [s7new_vars, *_] = s7new_vars_ex.split('==>')
            s7new_vars = s7new_vars.strip()
            (nvar2jnvar, jnvar2old_ls8expr) = _解读冫新增变量赋值语句序列扌(变量名讠变量号, s7new_vars)
                #nvar2jnvar/new_var2new_jvar
            for _0_1 in it:
                break
            match _0_1.split():
                case ('0', '1'):
                    pass
                case _:
                    raise Exception('format error:', _0_1)
            k2j_ls8ez_pairs = [()]
            for s7addtwo_ex in it:
                if not s7addtwo_ex:
                    break
                s7addtwo_ex
                (idx4span, j_ls8ez_pairs) = _解读冫关键节点扌(k2j_ls8ez_pairs, nvar2jnvar, s7addtwo_ex)
                assert len(k2j_ls8ez_pairs) == idx4span # == k
                k2j_ls8ez_pairs.append(j_ls8ez_pairs)
            k2j_ls8ez_pairs = tuple(k2j_ls8ez_pairs)
            #yield from _flush()
            #yield (阳爻模板, jnvar2old_ls8expr, k2j_ls8ez_pairs)
            yield (允负序号, jnvar2old_ls8expr, k2j_ls8ez_pairs)
            continue
def _解读冫新增变量赋值语句序列扌(var2jvar, s7new_vars, /):
    parse_text4def_new_vars_ = _gmk_parse_text4def_new_vars_()
    stmts7def_new_var = _parse7full_(parse_text4def_new_vars_, s7new_vars)
    #if 0b00001:print_err(stmts7def_new_var)
    nvar2jnvar = {}
    for nvar, old_expr8rhs in stmts7def_new_var:
        nvar2jnvar.setdefault(nvar, len(nvar2jnvar))
    assert len(nvar2jnvar) == len(stmts7def_new_var)


    (ls5expr_, lss5exprs_) = _mk_ls5exprs_(var2jvar)
    jnvar2old_ls8expr = []
    for nvar, old_expr8rhs in stmts7def_new_var:
        jnvar = len(jnvar2old_ls8expr)
        assert jnvar == nvar2jnvar[nvar]
        old_ls8rhs = ls5expr_(old_expr8rhs)
        jnvar2old_ls8expr.append(old_ls8rhs)
    jnvar2old_ls8expr = tuple(jnvar2old_ls8expr)
    return (nvar2jnvar, jnvar2old_ls8expr)
def _解读冫关键节点扌(k2j_ls8ez_pairs, nvar2jnvar, s7addtwo_ex, /):
    (ls5expr_, lss5exprs_) = _mk_ls5exprs_(nvar2jnvar)
    ls8ez_zero = ()

    parse_text4addtwo_ex_ = _gmk_parse_text4addtwo_ex_()
    addtwo_ex = _parse7full_(parse_text4addtwo_ex_, s7addtwo_ex)
    #if 0b00001:print_err(addtwo_ex)
    (addtwo, bit_ptn_exprs1) = addtwo_ex
    (idx4span, idx4span4big_addend, idx4span_ex7little_addend) = addtwo
    (may_idx4span4little_addend, may_expr8ez) = midx_mexpr_pair = idx4span_ex7little_addend
    match midx_mexpr_pair:
        case (None, expr8max_ez):
            '*:max_ez'
            ls8max_ez = ls5expr_(expr8max_ez)
            j_ls8ez_pairs = ((idx4span4big_addend, ls8max_ez),)
        case (idx4span4little_addend, None):
            'j'
            j_ls8ez_pairs = ((idx4span4big_addend, ls8ez_zero), (idx4span4little_addend, ls8ez_zero))
        case (idx4span4little_addend, expr8ez):
            'j:ez'
            ls8ez = ls5expr_(expr8ez)
            ((_idx4span4big_addend, _ls8max_ez),) = k2j_ls8ez_pairs[idx4span4little_addend]
            #assert 1 <= ez < max_ez, (ez, max_ez)
            j_ls8ez_pairs = ((idx4span4big_addend, ls8ez_zero), (_idx4span4big_addend, ls8ez))
    j_ls8ez_pairs
    return (idx4span, j_ls8ez_pairs)

##################################
##################################
##################################




__all__
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare import *
