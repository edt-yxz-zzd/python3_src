#__all__#goto
r'''
see:
    view  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__Unihan_Variants_txt__of_ver13_0.py


parsed_result
    :: {kind: [((hz, hex), [((hz, hex), [src])])]}
    parsed_result = kind2hz_hex_ts_pairs
compact_result
    compact_result = (kind2exceptional_hz_hex_ts_pairs, idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr)
simplified_result
    :: {kind: {hz: sorted_hz_str}}



py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt


from nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt import load_parsed_result_from_compact_result_file__path, load_parsed_result_from_compact_result_file__text, parsed_result2readonly, parsed_result5readonly, parsed_result2simplified, main, reformat__Unihan_Variants_txt__lines, parse__Unihan_Variants_txt, reformat__Unihan_Variants_txt__parsed_result, uncompact__parsed_result__Unihan_Variants_txt, compact__parsed_result__Unihan_Variants_txt___human, kind2inv_kind___from___coupled_kind_pairs_, compact__parsed_result__Unihan_Variants_txt


[[unicode-13.0 版 Unihan_Variants.txt 的 重排版 实例 如下:
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt -o $my_tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.txt
view  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py
view /storage/emulated/0/0my_files/tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.txt
也没节省多少空间！因此 尝试 compact__parsed_result__Unihan_Variants_txt
    du -h /storage/emulated/0/0my_files/tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.txt
    404K
    du -h /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt
    604K
    du -h '/sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/zipped_UCD/UCD.zip'
        7.2 M
    du -h '/sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/zipped_UCD/Unihan.zip'
        6.7 M

猜测:
    # kZVariant 异体字(同字 不同 形)
    # kSpoofingVariant 形近字(不同字，形相近)(似乎 只列出 常见混淆的形近字，无『未/末』，有『妹/妺』)
    # kSemanticVariant 同义字(不同字 但 同义)
    # kSpecializedSemanticVariant ？专用字？(某些 特定场合下 的 专用字？你您妳)
    # kSimplifiedVariant 简体字
    # kTraditionalVariant 繁体字

#{
#k0=kSemanticVariant
#k1=kSimplifiedVariant
#k2=kSpecializedSemanticVariant
#k3=kSpoofingVariant
#k4=kTraditionalVariant
#k5=kZVariant
#}
...
#k0=kSemanticVariant
#{
...
k0:一-4E00->弌-5F0C<s7,s10,s12 壹-58F9<s7,s10,s12
k0:七-4E03->柒-67D2<s7,s10,s12
k0:万-4E07->卍-534D<s1 萬-842C<s7,s10,s12
k0:三-4E09->叁-53C1<s7,s10,s12
k0:与-4E0E->與-8207<s10,s12
k0:丐-4E10->匃-5303<s10
... # 同义字？？
#}
...
#k2=kSpecializedSemanticVariant
#{
...
k2:一-4E00->壹-58F9
k2:七-4E03->柒-67D2<s1
k2:三-4E09->叁-53C1<s1
...
k2:二-4E8C->貳-8CB3
...
k2:你-4F60->妳-59B3 您-60A8 祢-7962 袮-88AE
... #某些 义项/用途/使用场景 等同？？专用字？
#}
...
#k3=kSpoofingVariant
#{
...
k3:䚶-46B6->訞-8A1E
k3:䱅-4C45->鮇-9B87
...
k3:妹-59B9->妺-59BA
k3:妺-59BA->妹-59B9
k3:幐-5E50->㬺-3B3A
k3:抹-62B9->抺-62BA
k3:抺-62BA->抹-62B9
...#但无『天夭』，无『未末』，所以是 不常见的 形近字(非-变体)？？
#}
...
#k5=kZVariant
#{
...
k5:䱍-4C4D->䱎-4C4E
k5:䱎-4C4E->䱍-4C4D
k5:併-4F75->倂-5002
k5:倂-5002->併-4F75
k5:値-5024->值-503C
k5:值-503C->値-5024
k5:吳-5433->吴-5434 呉-5449
k5:吴-5434->吳-5433 呉-5449
k5:呉-5449->吳-5433 吴-5434
k5:塡-5861->填-586B
k5:填-586B->塡-5861
... #应该是 异体字。
#}

]]


[[紧凑表达


py -m nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt --compact   -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt -o $my_tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.compact.txt
view /storage/emulated/0/0my_files/tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.compact.txt
du -h /storage/emulated/0/0my_files/tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.compact.txt
    104K    #pprint
    92K     #stable_repr(compact_result, depth=0, maybe_max_depth=1)
    92K     #stable_repr(compact_result, depth=0, maybe_max_depth=2)
!cp /storage/emulated/0/0my_files/tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.compact.txt      ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py.out.ver13_0.compact.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py.out.ver13_0.compact.txt
view  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__Unihan_Variants_txt__of_ver13_0.py
from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0


发现 非对称！！
k0:㒚-349A->穩-7A69<s1,s10
k0:穩-7A69->㒚-349A<s10
    没有 s1!!!
k2:伷-4F37->胄-80C4<s12
k2:咮-54AE->胄-80C4<s12
k2:胄-80C4->伷-4F37<s12
    # 没有 胄-80C4->咮-54AE

发现 非顺序排列:
k0:㒋-348B->廝-5EDD<s10 厮-53AE<s10
    # 5EDD > 53AE
k2:折-6298->翼-7FFC<s1 拃-62C3<s1
    # 7FFC > 62C3


]]

e  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py
view /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt
    # Unihan_Variants.txt
    # Date: 2020-02-18 18:27:33 GMT [JHJ]
    # Unicode version: 13.0.0

U+NNNN \t kXxxVariant \t U+NNNN U+NNNN<zzz,zzz
-->>
#{
#s{j}=zzz
#}
#{
#k{i}=kXxxVariant
#}
#k{i}=kXxxVariant
#{
k{i}:hz-NNNN->hz-NNNN hz-NNNN<s{j},s{j}
#}

xxx i:hz-NNNN->[hz-NNNN[],hz-NNNN[zzz,zzz]]
#'''

r'''[[[
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt

    parse__Unihan_Variants_txt
    kind2hz_hex_ts_pairs_to_sources
    kind2hz2hz2srcs_to_sources
    kind2hz_hex_ts_pairs__from__kind2hz2hz2srcs
    kind2hz_hex_ts_pairs__to__kind2hz2hz2srcs
    hz2hex
    hz2hz_hex
    hz_hex_ts_pairs__from__hz2hz2srcs
    hz_hex_ts_pairs__to__hz2hz2srcs
    str_join__list_nonemty
    str_split__list_nonemty
    str_join__entry_nonemty
    str_split__entry_nonemty
    str_join__both_list_and_entry_may_be_emty
    str_split__both_list_and_entry_may_be_emty
    fmap4dict_value
    filter4dict_value
    dict_add__is
    dict_add__eq
    kind2inv_kind___from___coupled_kind_pairs_
    compact__parsed_result__Unihan_Variants_txt___human
    compact__parsed_result__Unihan_Variants_txt
    findout_exceptionals_or_check_inv_pair___kind
    check_inv_pair___kind
    single_direction_only_check_inv_pair___kind
    single_direction_only_check_inv_pair___hz2hz2srcs
    uncompact__parsed_result__Unihan_Variants_txt
    hzhz2isrcs__from__hzhzstr_ussstr_pair
    hzhz2isrcs__to__hzhzstr_ussstr_pair
    reformat__Unihan_Variants_txt__lines
    reformat__Unihan_Variants_txt__parsed_result
    load_parsed_result_from_compact_result_file__path
    load_parsed_result_from_compact_result_file__text
    hz_hex_ts_pairs5immutable
    hz_hex_ts_pairs2immutable
    parsed_result5readonly
    parsed_result2readonly
    hz_hex_ts_pairs2simplified
    parsed_result2simplified
    main
#]]]'''

__all__ = '''
load_parsed_result_from_compact_result_file__path
    load_parsed_result_from_compact_result_file__text
    parsed_result2readonly
    parsed_result5readonly
    parsed_result2simplified
main
    reformat__Unihan_Variants_txt__lines
        parse__Unihan_Variants_txt
        reformat__Unihan_Variants_txt__parsed_result

    uncompact__parsed_result__Unihan_Variants_txt
    compact__parsed_result__Unihan_Variants_txt___human
        kind2inv_kind___from___coupled_kind_pairs_
        compact__parsed_result__Unihan_Variants_txt
    '''.split()
'''










parsed_result2readonly
parsed_result5readonly
    hz_hex_ts_pairs2immutable
    hz_hex_ts_pairs5immutable

parsed_result2simplified
    hz_hex_ts_pairs2simplified

compact__parsed_result__Unihan_Variants_txt
uncompact__parsed_result__Unihan_Variants_txt
    kind2hz_hex_ts_pairs__from__kind2hz2hz2srcs
    kind2hz_hex_ts_pairs__to__kind2hz2hz2srcs
        hz_hex_ts_pairs__from__hz2hz2srcs
        hz_hex_ts_pairs__to__hz2hz2srcs

    hzhz2isrcs__to__hzhzstr_ussstr_pair
    hzhz2isrcs__from__hzhzstr_ussstr_pair


    hz2hex
    hz2hz_hex

    kind2hz_hex_ts_pairs_to_sources
    kind2hz2hz2srcs_to_sources




    findout_exceptionals_or_check_inv_pair___kind
        check_inv_pair___kind
        single_direction_only_check_inv_pair___kind
        single_direction_only_check_inv_pair___hz2hz2srcs

    '''.split()
#__all__:end


___begin_mark_of_excluded_global_names__0___ = ...

from ast import literal_eval

from seed.tiny import mk_fprint
from seed.tiny import expectError, MapView#, check_uint
from seed.io.FieldedLineHandler import FieldedLineHandler, IFieldedLineHandler

from seed.text.base64 import uint__to__radix64_digits_, uint__from__radix64_digits_, uint__to__radix64_digits__b64__str_, uint__from__radix64_digits__b64__str_
    #view ../../python3_src/seed/text/base64.py


from seed.tiny import str_join__list_nonemty, str_split__list_nonemty, str_join__entry_nonemty, str_split__entry_nonemty, str_join__both_list_and_entry_may_be_emty, str_split__both_list_and_entry_may_be_emty
from seed.tiny import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq
___end_mark_of_excluded_global_names__0___ = ...






_fielded_line_handler__Unihan_Variants_txt = FieldedLineHandler(remove_empty_lines=True, line_strip=True, field_strip=True, line_comment_prefix='#', line_tail_comment_prefix='#', field_sep='\t')

def _pt2char_hex(pt, /):
    if not pt.startswith('U+'):raise ValueError
    hex = pt[2:]
    ch = chr(int(hex, 16))
    return (ch, hex)

def parse__Unihan_Variants_txt(lines, /):
    r'''Iter line -> kind2hz_hex_ts_pairs

    kind2hz_hex_ts_pairs
        :: Map str [(hz_hex, [(hz_hex, [src])])]
    where
        hz_hex :: (char, xdigits)
        xdigits :: str
        src :: str
    #'''
    fieldss = _fielded_line_handler__Unihan_Variants_txt.lines2fieldss(lines)
    kind2hz_hex_ts_pairs = {}
    for pt, kind, ls in fieldss:
        _0_hz_hex = _pt2char_hex(pt)
        ls = ls.split()
        ts = []
        for pt_srcs in ls:
            pt, _, srcs = pt_srcs.partition('<')
            hz_hex = _pt2char_hex(pt)
            #srcs = srcs.split(',') if srcs else []
            srcs = str_split__entry_nonemty(',', srcs)
            ts.append((hz_hex, srcs))
        ###
        pairs = kind2hz_hex_ts_pairs.setdefault(kind, [])
        pairs.append((_0_hz_hex, ts))
    return kind2hz_hex_ts_pairs
def kind2hz_hex_ts_pairs_to_sources(kind2hz_hex_ts_pairs, /):
    sources = set()
    for kind, hz_hex_ts_pairs in kind2hz_hex_ts_pairs.items():
        for _0_hz_hex, ts in hz_hex_ts_pairs:
            for hz_hex, srcs in ts:
                sources.update(srcs)
    return sources
def kind2hz2hz2srcs_to_sources(kind2hz2hz2srcs, /):
    sources = set()
    for kind, hz2hz2srcs in kind2hz2hz2srcs.items():
        for hz0, hz2srcs in hz2hz2srcs.items():
            for hz1, srcs in hz2srcs.items():
                sources.update(srcs)
    return sources


def kind2hz_hex_ts_pairs__from__kind2hz2hz2srcs(kind2hz2hz2srcs, /):
    #kind2hz_hex_ts_pairs__to__kind2hz2hz2srcs
    f = hz_hex_ts_pairs__from__hz2hz2srcs
    kind2hz_hex_ts_pairs = fmap4dict_value(f, kind2hz2hz2srcs)
    return kind2hz_hex_ts_pairs
def kind2hz_hex_ts_pairs__to__kind2hz2hz2srcs(kind2hz_hex_ts_pairs, /):
    #kind2hz_hex_ts_pairs__from__kind2hz2hz2srcs
    f = hz_hex_ts_pairs__to__hz2hz2srcs
    kind2hz2hz2srcs = fmap4dict_value(f, kind2hz_hex_ts_pairs)
    return kind2hz2hz2srcs


assert f'{0:0>4X}' == '0000'
def hz2hex(hz, /):
    s = f'{ord(hz):0>4X}'
    assert chr(int(s, 16)) == hz
    return s #5也行！！
    if len(s)%2 == 1:
        s = f'0{s}'
    assert chr(int(s, 16)) == hz
    assert len(s)%2 == 0
    return s
def hz2hz_hex(hz, /):
    return hz, hz2hex(hz)

def hz_hex_ts_pairs__from__hz2hz2srcs(hz2hz2srcs, /):
    #hz_hex_ts_pairs__to__hz2hz2srcs
    hz_hex_ts_pairs = []
    for hz0, hz2srcs in hz2hz2srcs.items():
        _0_hz_hex = hz2hz_hex(hz0)
        ts = []
        for hz1, srcs in hz2srcs.items():
            hz_hex = hz2hz_hex(hz1)
            ts.append((hz_hex, [*srcs]))
        ts.sort()
        hz_hex_ts_pairs.append((_0_hz_hex, ts))
    hz_hex_ts_pairs.sort()
    return hz_hex_ts_pairs
    r'''
发现 非顺序排列:
k0:㒋-348B->廝-5EDD<s10 厮-53AE<s10
k2:折-6298->翼-7FFC<s1 拃-62C3<s1


kSemanticVariant
['kSemanticVariant', 13, (('㒋', '348B'), [(('廝', '5EDD'), ['kMatthews']), (('厮', '53AE'), ['kMatthews'])]), (('㒋', '348B'), [(('厮', '53AE'), ['kMatthews']), (('廝', '5EDD'), ['kMatthews'])])]
kSpecializedSemanticVariant
['kSpecializedSemanticVariant', 181, (('折', '6298'), [(('翼', '7FFC'), ['kFenn']), (('拃', '62C3'), ['kFenn'])]), (('折', '6298'), [(('拃', '62C3'), ['kFenn']), (('翼', '7FFC'), ['kFenn'])])]

    #'''
def hz_hex_ts_pairs__to__hz2hz2srcs(hz_hex_ts_pairs, /):
    #hz_hex_ts_pairs__from__hz2hz2srcs
    hz2hz2srcs = {}
    for _0_hz_hex, ts in hz_hex_ts_pairs:
        hz0, _ = _0_hz_hex
        assert not hz0 in hz2hz2srcs
        hz2srcs = hz2hz2srcs[hz0] = {}
        for hz_hex, srcs in ts:
            hz, _ = hz_hex
            assert not hz in hz2srcs
            #hz2srcs[hz] = {*srcs}
            hz2srcs[hz] = [*srcs]
    return hz2hz2srcs


def _mk_bijection_pair(s, /):
    i2e = sorted(set(s))
    e2i = {e:i for i, e in enumerate(i2e)}
    if not len(i2e) == len(e2i): raise ValueError
    return i2e, e2i

r'''
from itertools import chain
assert ','.join([]) == '' == ','.join([''])
assert ''.split(',') == ['']
assert expectError(ValueError, lambda:''.split(''))
    # ''.split('')
    #   ==>> ValueError: empty separator

def str_join__list_nonemty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if not ls: raise TypeError
    s = sep.join(ls)
    if not ls == str_split__list_nonemty(sep, s): raise logic-err
    return s
def str_split__list_nonemty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep)
    if not ls: raise logic-err
    return ls

def str_join__entry_nonemty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if not all(ls): raise TypeError
    s = sep.join(ls)
    if not ls == str_split__entry_nonemty(sep, s): raise logic-err
    return s
def str_split__entry_nonemty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep) if s else []
    if not all(ls): raise TypeError
    return ls

def str_join__both_list_and_entry_may_be_emty(sep, iterable, /):
    if not sep: raise TypeError
    ls = [*iterable] if type(iterable) is not list else iterable
    if 0:
        def f(sep, it, /):
            for x in it:
                yield sep
                yield x
        s = ''.join(f(sep, ls))
    else:
        s = sep.join(chain([''], ls))
    if not ls == str_split__both_list_and_entry_may_be_emty(sep, s): raise logic-err
    return s
def str_split__both_list_and_entry_may_be_emty(sep, s, /):
    if not sep: raise TypeError
    ls = s.split(sep)
    if not ls: raise logic-err
    if ls[0]: raise TypeError#==>> (s and not s.startswith(sep))
    del ls[0]
    return ls


def fmap4dict_value(f, d, /):
    return {k:f(v) for k, v in d.items()}
def filter4dict_value(f, d, /):
    return {k:v for k, v in d.items() if f(v)}
def dict_add__is(d, k, v, /):
    _v = d.setdefault(k, v)
    if 0b00:
        if not (_v is v):
            print(v)
            print(_v)
            raise ValueError
    else:
        if not (_v is v): raise ValueError
    return
def dict_add__eq(d, k, v, /):
    _v = d.setdefault(k, v)
    if not (_v is v or _v == v): raise ValueError
    return

#'''

def kind2inv_kind___from___coupled_kind_pairs_(all_kinds, coupled_kind_pairs, /):
    kind2inv_kind = {}
    for kind, inv_kind in coupled_kind_pairs:
        dict_add__eq(kind2inv_kind, kind, inv_kind)
        dict_add__eq(kind2inv_kind, inv_kind, kind)
    for kind in set(all_kinds) - set(kind2inv_kind):
        dict_add__eq(kind2inv_kind, kind, kind)
    return kind2inv_kind
def compact__parsed_result__Unihan_Variants_txt___human(kind2hz_hex_ts_pairs, /, *, coupled_kind_pairs):
    kind2inv_kind = kind2inv_kind___from___coupled_kind_pairs_(kind2hz_hex_ts_pairs.keys(), coupled_kind_pairs)
    return compact__parsed_result__Unihan_Variants_txt(kind2hz_hex_ts_pairs, kind2inv_kind=kind2inv_kind)
def compact__parsed_result__Unihan_Variants_txt(kind2hz_hex_ts_pairs, /, *, kind2inv_kind):
    #uncompact__parsed_result__Unihan_Variants_txt
    kind2hz2hz2srcs = kind2hz_hex_ts_pairs__to__kind2hz2hz2srcs(kind2hz_hex_ts_pairs)
    (idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr) = _1_compact__parsed_result__Unihan_Variants_txt(kind2hz2hz2srcs, kind2inv_kind=kind2inv_kind)

    if 1:
        #求出 非顺序排列 补丁
        kind2exceptional_hz_hex_ts_pairs = {kind:
            [(_0_hz_hex, ts)
                for _0_hz_hex, ts in hz_hex_ts_pairs if ts != sorted(ts)
                #for hz_hex, srcs in ts:
            ] for kind, hz_hex_ts_pairs in kind2hz_hex_ts_pairs.items()
        }
        kind2exceptional_hz_hex_ts_pairs = filter4dict_value(bool, kind2exceptional_hz_hex_ts_pairs)
    compact_result = (kind2exceptional_hz_hex_ts_pairs, idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr)
    return compact_result


def findout_exceptionals_or_check_inv_pair___kind(kind2hz2hz2srcs, kind, inv_kind, /, **kw):
    #old-name:check_inv_pair___kind
    single_direction_only_check_inv_pair___kind(kind2hz2hz2srcs, kind, inv_kind, **kw)
    if not inv_kind == kind:
        single_direction_only_check_inv_pair___kind(kind2hz2hz2srcs, inv_kind, kind, **kw)
check_inv_pair___kind = findout_exceptionals_or_check_inv_pair___kind

def single_direction_only_check_inv_pair___kind(kind2hz2hz2srcs, kind, inv_kind, /, **kw):
    hz2hz2srcs = kind2hz2hz2srcs[kind]
    inv__hz2hz2srcs = kind2hz2hz2srcs[inv_kind]
    single_direction_only_check_inv_pair___hz2hz2srcs(hz2hz2srcs, inv__hz2hz2srcs, **kw)
def single_direction_only_check_inv_pair___hz2hz2srcs(hz2hz2srcs, inv__hz2hz2srcs, /, *, show_not_raise, exceptional_hzhz2srcs_may_inv):
    def f():
        err_msg = f'not inv_pair: {hex(ord(hz0))}:{hex(ord(hz1))}: {srcs}, {may_srcs__inv}'
        if 0b00 and show_not_raise:
            print(err_msg)
        elif exceptional_hzhz2srcs_may_inv is not None:
            hzhz = hz0 + hz1
            dict_add__is(exceptional_hzhz2srcs_may_inv, hzhz, (srcs, may_srcs__inv))
        else:
            raise ValueError(err_msg)
        r'''
        ValueError: not inv_pair: 0x349a:0x7a69: ['kFenn', 'kMatthews'], ['kMatthews']
        ====
        发现 非对称！！
        k0:㒚-349A->穩-7A69<s1,s10
        k0:穩-7A69->㒚-349A<s10
            没有 s1!!!

        k2:伷-4F37->胄-80C4<s12
        k2:咮-54AE->胄-80C4<s12
        k2:胄-80C4->伷-4F37<s12
            # 没有 胄-80C4->咮-54AE
        ====
$ py -m nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt --compact   -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt -o $my_tmp/out4py/cjk.reformat__Unihan_Variants_txt.ver13_0.compact.txt > $my_tmp/_.txt
    #设置 show_not_raise = True

view /storage/emulated/0/0my_files/tmp/_.txt
其中 只有 两类 非对称:
    check_inv_pair___kind<'kSpecializedSemanticVariant', 'kSpecializedSemanticVariant'>
        34 例
    check_inv_pair___kind<'kSemanticVariant', 'kSemanticVariant'>
        64 例
[[
check_inv_pair___kind<'kSimplifiedVariant', 'kTraditionalVariant'>
check_inv_pair___kind<'kTraditionalVariant', 'kSimplifiedVariant'>
check_inv_pair___kind<'kZVariant', 'kZVariant'>
check_inv_pair___kind<'kSpoofingVariant', 'kSpoofingVariant'>
check_inv_pair___kind<'kSpecializedSemanticVariant', 'kSpecializedSemanticVariant'>
not inv_pair: 0x53df:0x58b0: ['kMeyerWempe'], None
not inv_pair: 0x54ae:0x80c4: ['kMeyerWempe'], None
not inv_pair: 0x55fb:0x8655: ['kMeyerWempe'], None
not inv_pair: 0x5f91:0x52c1: ['kMeyerWempe'], None
not inv_pair: 0x613f:0x9858: ['kHanYu:T'], None
not inv_pair: 0x6389:0x68f9: ['kMeyerWempe'], None
not inv_pair: 0x63dc:0x63a9: ['kMeyerWempe'], None
not inv_pair: 0x646d:0x62d3: ['kMeyerWempe'], None
not inv_pair: 0x6555:0x52c5: ['kMeyerWempe'], None
not inv_pair: 0x6696:0x5a20: ['kFenn'], None
not inv_pair: 0x684c:0x68f9: ['kFenn'], None
not inv_pair: 0x6ac2:0x6389: ['kMeyerWempe'], None
not inv_pair: 0x6b79:0x239b5: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x6b79:0x239b6: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x70df:0x83f8: [], None
not inv_pair: 0x7586:0x5c07: ['kFenn'], None
not inv_pair: 0x7947:0x53ea: [], None
not inv_pair: 0x7a95:0x963f: ['kMeyerWempe'], None
not inv_pair: 0x7b87:0x500b: ['kMeyerWempe'], None
not inv_pair: 0x7f48:0x58b0: ['kMeyerWempe'], None
not inv_pair: 0x89dd:0x7274: [], None
not inv_pair: 0x8afc:0x7156: ['kMeyerWempe'], None
not inv_pair: 0x8e5f:0x901f: ['kMeyerWempe'], None
not inv_pair: 0x8ff9:0x901f: ['kMeyerWempe'], None
not inv_pair: 0x9183:0x814c: [], None
not inv_pair: 0x9688:0x504e: ['kMeyerWempe'], None
not inv_pair: 0x96e8:0x99ad: ['kFenn'], None
not inv_pair: 0x9856:0x56df: ['kFenn'], None
not inv_pair: 0x9912:0x9927: ['kMeyerWempe'], None
not inv_pair: 0x9927:0x5582: ['kMeyerWempe'], None
not inv_pair: 0x217be:0x5af0: ['kFenn'], None
not inv_pair: 0x239b5:0x6b79: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x239b6:0x6b79: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x2456d:0x5c07: ['kFenn'], None
check_inv_pair___kind<'kSemanticVariant', 'kSemanticVariant'>
not inv_pair: 0x349a:0x7a69: ['kFenn', 'kMatthews'], ['kMatthews']
not inv_pair: 0x3551:0x53a8: ['kLau'], None
not inv_pair: 0x3a17:0x6377: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x3aaf:0x8209: [], ['kFenn']
not inv_pair: 0x3ace:0x5e51: ['kHanYu:T'], None
not inv_pair: 0x3d11:0x6eaf: ['kMatthews'], None
not inv_pair: 0x4430:0x9948: ['kMatthews'], None
not inv_pair: 0x50bb:0x510d: ['kFenn'], []
not inv_pair: 0x510d:0x50bb: [], ['kFenn']
not inv_pair: 0x5231:0x5275: ['kHanYu:TZ', 'kMeyerWempe'], ['kHanYu:T', 'kMeyerWempe']
not inv_pair: 0x5275:0x5231: ['kHanYu:T', 'kMeyerWempe'], ['kHanYu:TZ', 'kMeyerWempe']
not inv_pair: 0x534c:0x2098c: ['kHanYu'], ['kHanYu:T']
not inv_pair: 0x5bda:0x5b9d: ['kMatthews'], None
not inv_pair: 0x5bda:0x5bf3: ['kMatthews'], None
not inv_pair: 0x5c49:0x5c5c: ['kLau', 'kMatthews'], None
not inv_pair: 0x5ef1:0x96dd: ['kMeyerWempe'], None
not inv_pair: 0x5f0b:0x2237a: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x6377:0x3a17: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x64cb:0x6529: ['kFennIndex:T', 'kLau:T', 'kMatthews', 'kMeyerWempe'], ['kFennIndex:T', 'kLau:T', 'kMeyerWempe']
not inv_pair: 0x64cb:0x2bf6e: ['kFennIndex:T', 'kLau:T'], ['kFennIndex:T', 'kLau:T', 'kMeyerWempe']
not inv_pair: 0x6529:0x64cb: ['kFennIndex:T', 'kLau:T', 'kMeyerWempe'], ['kFennIndex:T', 'kLau:T', 'kMatthews', 'kMeyerWempe']
not inv_pair: 0x6529:0x2bf6e: ['kFennIndex:T', 'kLau:T'], ['kFennIndex:T', 'kLau:T', 'kMatthews', 'kMeyerWempe']
not inv_pair: 0x6661:0x231c0: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x6caa:0x51b1: ['kMeyerWempe'], None
not inv_pair: 0x6cc4:0x6e2b: ['kFenn'], []
not inv_pair: 0x6e2b:0x6cc4: [], ['kFenn']
not inv_pair: 0x723f:0x2456a: ['kHanYu:T'], ['kHanYu:TZ']
not inv_pair: 0x74a2:0x7409: ['kMeyerWempe'], None
not inv_pair: 0x758d:0x86cb: ['kMeyerWempe'], None
not inv_pair: 0x75d2:0x7662: ['kMatthews'], ['kFenn', 'kMatthews']
not inv_pair: 0x7662:0x75d2: ['kFenn', 'kMatthews'], ['kMatthews']
not inv_pair: 0x7a69:0x349a: ['kMatthews'], ['kFenn', 'kMatthews']
not inv_pair: 0x7d25:0x7d2e: [], ['kFenn']
not inv_pair: 0x7d2e:0x7d25: ['kFenn'], []
not inv_pair: 0x7d71:0x7d82: ['kHanYu:T'], ['kHanYu']
not inv_pair: 0x7d82:0x7d71: ['kHanYu'], ['kHanYu:T']
not inv_pair: 0x7dca:0x260b3: ['kHanYu'], ['kHanYu:TZ']
not inv_pair: 0x8209:0x3aaf: ['kFenn'], []
not inv_pair: 0x8534:0x9ebb: [], ['kFenn']
not inv_pair: 0x93e5:0x92b9: ['kMatthews'], None
not inv_pair: 0x93e5:0x93fd: ['kMatthews'], None
not inv_pair: 0x9ebb:0x8534: ['kFenn'], []
not inv_pair: 0x9f8d:0x9f92: ['kHanYu:T'], ['kHanYu']
not inv_pair: 0x9f92:0x9f8d: ['kHanYu'], ['kHanYu:T']
not inv_pair: 0x9fcc:0x6dbc: [], None
not inv_pair: 0x2098c:0x534c: ['kHanYu:T'], ['kHanYu']
not inv_pair: 0x2228d:0x53a8: ['kLau'], None
not inv_pair: 0x2237a:0x5f0b: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x22c3e:0x6460: ['kLau'], None
not inv_pair: 0x22c3e:0x7e3d: ['kLau'], None
not inv_pair: 0x231c0:0x6661: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x2456a:0x723f: ['kHanYu:TZ'], ['kHanYu:T']
not inv_pair: 0x25500:0x6e39: ['kMeterWempe'], None
not inv_pair: 0x25500:0x8a07: ['kMeyerWempe'], None
not inv_pair: 0x25edf:0x7cef: ['kLau'], None
not inv_pair: 0x260b3:0x7dca: ['kHanYu:TZ'], ['kHanYu']
not inv_pair: 0x2690e:0x81ef: ['kMeyerWempe'], None
not inv_pair: 0x26c44:0x83c7: ['kLau'], None
not inv_pair: 0x26cb7:0x849e: ['kLau'], None
not inv_pair: 0x2aa9d:0x96dd: ['kMatthews'], None
not inv_pair: 0x2bf6e:0x64cb: ['kFennIndex:T', 'kLau:T', 'kMeyerWempe'], ['kFennIndex:T', 'kLau:T']
not inv_pair: 0x2bf6e:0x6529: ['kFennIndex:T', 'kLau:T', 'kMatthews', 'kMeyerWempe'], ['kFennIndex:T', 'kLau:T']
not inv_pair: 0x2d016:0x91d0: ['kFennIndex:T'], None
not inv_pair: 0x2f817:0x5197: ['kMeyerWempe'], None
]]

        #'''
    for hz0, hz2srcs in hz2hz2srcs.items():
        for hz1, srcs in hz2srcs.items():
            try:
                #if not inv__hz2hz2srcs[hz1][hz0] == srcs: f()
                srcs__inv = inv__hz2hz2srcs[hz1][hz0]
            except KeyError:#f()
                may_srcs__inv = None
            else:
                may_srcs__inv = srcs__inv
            if not may_srcs__inv == srcs: f()
    return
def _1_compact__parsed_result__Unihan_Variants_txt(kind2hz2hz2srcs, /, *, kind2inv_kind):
    r'''#紧致表达，方式:拆出 同类型 数据 合并
    -> (idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr)
        #kind2inv_kind is required to derived dropped_coupled_kind


    统一为 互反关系 kind2inv_kind:
        等价关系 :: Set kind
        相反关系对 :: Set (kind, kind){sorted}
            相反关系对 :: Set (Set kind){len=2}
    ====
    kind <- {kZVariant, ...}
    ====
    猜:unicode_13__Unihan::Unihan_Variants.txt 中，所有 kind 刚好 分成 这两类:
        相反关系对 = {(kSimplifiedVariant, kTraditionalVariant)}
            #只有一对
    #'''
    #_1_uncompact__parsed_result__Unihan_Variants_txt
    if 1:
        #互反
        #允许 kind==inv_kind
        if not kind2inv_kind.keys() == kind2hz2hz2srcs.keys(): raise ValueError
        if not {*kind2inv_kind.values()} == kind2hz2hz2srcs.keys(): raise ValueError
        if not all(kind2inv_kind[inv_kind] == kind for kind, inv_kind in kind2inv_kind.items()): raise ValueError

    if 0:
        r'''
        #对立
        assert len(等价关系) + 2*len(相反关系对) == len(kind2hz2hz2srcs)
        assert all(L == 2 for L in map(len, 相反关系对))
        assert set().union(等价关系, *相反关系对) == kind2hz2hz2srcs.keys()
        #'''

    if 1:
        # 检验 互反关系对  +求出 非对称 补丁
        if 1:
            show_not_raise = False
            if 0b00: show_not_raise = True
            kw = dict(show_not_raise=show_not_raise)

        kind2exceptional_hzhz2srcs_may_inv = {kind:{} for kind in kind2inv_kind}
            #{kind: {hzhz: (srcs, may_srcs__inv)}}
        for kind, inv_kind in kind2inv_kind.items():
            if 0b00 and show_not_raise:
                print(f'check_inv_pair___kind<{kind!r}, {inv_kind!r}>')
            exceptional_hzhz2srcs_may_inv = kind2exceptional_hzhz2srcs_may_inv[kind]
            findout_exceptionals_or_check_inv_pair___kind(kind2hz2hz2srcs, kind, inv_kind, **kw, exceptional_hzhz2srcs_may_inv=exceptional_hzhz2srcs_may_inv)

    kind2exceptional_hzhz2srcs_may_inv

    if 1:
        #分为两类 进行处理
        #自反的reflexive_kind2hzhz2isrcs
        #成对的coupled_kind2hzhz2isrcs
        reflexive_kind2hzhz2isrcs = {}
        coupled_kind2hzhz2isrcs = {}
        for kind, inv_kind in kind2inv_kind.items():
            if kind == inv_kind:
                reflexive_kind2hzhz2isrcs[kind] = {}
            elif kind < inv_kind:
                coupled_kind2hzhz2isrcs[kind] = {}
            else:
                pass

        sources = kind2hz2hz2srcs_to_sources(kind2hz2hz2srcs)
        idx2src, src2idx = _mk_bijection_pair(sources)

        def f(exceptional_hzhz_set, src2idx, hzhz2isrcs, hz0, hz1, srcs, /):
            hzhz = hz0+hz1
            if hzhz in exceptional_hzhz_set: return
                ## 这里 要求 双向记录 hz0hz1, hz1hz0
            #isrcs = sorted(src2idx[src] for src in srcs)
            isrcs = [src2idx[src] for src in srcs]
            dict_add__is(hzhz2isrcs, hzhz, isrcs)
            return
        ######################
        for reflexive_kind, hzhz2isrcs in reflexive_kind2hzhz2isrcs.items():
            hz2hz2srcs = kind2hz2hz2srcs[reflexive_kind]
            exceptional_hzhz_set = kind2exceptional_hzhz2srcs_may_inv[reflexive_kind].keys()

            for hz0, hz2srcs in hz2hz2srcs.items():
                for hz1, srcs in hz2srcs.items():
                    if hz0 <= hz1: #自减近半
                        f(exceptional_hzhz_set, src2idx, hzhz2isrcs, hz0, hz1, srcs)

        ######################
        for coupled_kind, hzhz2isrcs in coupled_kind2hzhz2isrcs.items():
            hz2hz2srcs = kind2hz2hz2srcs[coupled_kind]
            exceptional_hzhz_set = kind2exceptional_hzhz2srcs_may_inv[coupled_kind].keys()

            assert coupled_kind < kind2inv_kind[coupled_kind] #省略镜像
            for hz0, hz2srcs in hz2hz2srcs.items():
                for hz1, srcs in hz2srcs.items():
                    f(exceptional_hzhz_set, src2idx, hzhz2isrcs, hz0, hz1, srcs)
        ######################
    kind2exceptional_hzhz2srcs_may_inv = filter4dict_value(bool, kind2exceptional_hzhz2srcs_may_inv)
    ####################################
    ####################################
    #所有数据: idx2src, reflexive_kind2hzhz2isrcs, coupled_kind2hzhz2isrcs, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv
    ####################################
    ####################################
    #紧凑表达 数据
    if 0:
        # idx2src, kind2inv_kind 无需 紧凑表达
        #   重灾区 是 hzhz2isrcs
        srcs__str = ','.join(idx2src)
        assert srcs__str.split(',') == idx2src

    #hzhzstr_ussstr = hzhz2isrcs__to__hzhzstr_ussstr_pair(hzhz2isrcs)
    f = hzhz2isrcs__to__hzhzstr_ussstr_pair
    reflexive_kind2hzhzstr_ussstr = fmap4dict_value(f, reflexive_kind2hzhz2isrcs)
        #reflexive_kind__to__hzhz_str__isrcs_str__pair
    coupled_kind2hzhzstr_ussstr = fmap4dict_value(f, coupled_kind2hzhz2isrcs)
    return (idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr)
        #kind2inv_kind is required to derived dropped_coupled_kind

def uncompact__parsed_result__Unihan_Variants_txt(kind2exceptional_hz_hex_ts_pairs, idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr, /):
    '-> (kind2hz_hex_ts_pairs, kind2inv_kind)'
    #compact__parsed_result__Unihan_Variants_txt
    kind2hz2hz2srcs, kind2inv_kind = _1_uncompact__parsed_result__Unihan_Variants_txt(idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr)
    kind2hz_hex_ts_pairs = kind2hz_hex_ts_pairs__from__kind2hz2hz2srcs(kind2hz2hz2srcs)
    #打补丁:例外数据/非顺序数据
    for kind, exceptional_hz_hex_ts_pairs in kind2exceptional_hz_hex_ts_pairs.items():
        hz_hex_ts_pairs = kind2hz_hex_ts_pairs[kind]
        assert hz_hex_ts_pairs == sorted(hz_hex_ts_pairs)
        assert exceptional_hz_hex_ts_pairs == sorted(exceptional_hz_hex_ts_pairs)

        it = enumerate(hz_hex_ts_pairs)
        if 0:
            #bug: each round will runover it
            idc = [i
            for _0_hz_hex__exc, ts__exc in exceptional_hz_hex_ts_pairs
            for i, (_0_hz_hex, ts) in it
            if _0_hz_hex == _0_hz_hex__exc
                #SHOULD break now
            ]
        else:
            idc = []
            for _0_hz_hex__exc, ts__exc in exceptional_hz_hex_ts_pairs:
                for i, (_0_hz_hex, ts) in it:
                    if _0_hz_hex == _0_hz_hex__exc:
                        idc.append(i)
                        break

        if not len(idc) == len(exceptional_hz_hex_ts_pairs): raise logic-err
        for i, (_0_hz_hex__exc, ts__exc) in zip(idc, exceptional_hz_hex_ts_pairs):
            (_0_hz_hex, ts) = hz_hex_ts_pairs[i]
            assert _0_hz_hex == _0_hz_hex__exc
            assert not ts == ts__exc
            assert ts == sorted(ts__exc)
            hz_hex_ts_pairs[i] = (_0_hz_hex__exc, ts__exc)
    return kind2hz_hex_ts_pairs, kind2inv_kind

def _1_uncompact__parsed_result__Unihan_Variants_txt(idx2src, kind2inv_kind, kind2exceptional_hzhz2srcs_may_inv, reflexive_kind2hzhzstr_ussstr, coupled_kind2hzhzstr_ussstr, /):
    '-> (kind2hz2hz2srcs, kind2inv_kind)'
    #_1_compact__parsed_result__Unihan_Variants_txt
    f = hzhz2isrcs__from__hzhzstr_ussstr_pair
    reflexive_kind2hzhz2isrcs = fmap4dict_value(f, reflexive_kind2hzhzstr_ussstr)
    coupled_kind2hzhz2isrcs = fmap4dict_value(f, coupled_kind2hzhzstr_ussstr)
    ###求出 另一半
    def isrcs2srcs(isrcs, /):
        srcs = [idx2src[isrc] for isrc in isrcs]
        return srcs
    def inject(from__hzhz2isrcs, to__hz2hz2srcs, /, *, reverse):
        f = reversed if reverse else iter
        for hzhz, isrcs in from__hzhz2isrcs.items():
            srcs = isrcs2srcs(isrcs)
            (hz0, hz1) = f(hzhz)
            hz2srcs = to__hz2hz2srcs.setdefault(hz0, {})
            dict_add__eq(hz2srcs, hz1, srcs)

    kind2hz2hz2srcs = {}
    for kind, hzhz2isrcs in reflexive_kind2hzhz2isrcs.items():
        if not kind2inv_kind[kind] == kind: raise ValueError
        to__hz2hz2srcs = {}
        dict_add__is(kind2hz2hz2srcs, kind, to__hz2hz2srcs)

        inject(hzhz2isrcs, to__hz2hz2srcs, reverse=False)
        inject(hzhz2isrcs, to__hz2hz2srcs, reverse=True)

    for kind, hzhz2isrcs in coupled_kind2hzhz2isrcs.items():
        inv_kind = kind2inv_kind[kind]
        if inv_kind == kind: raise ValueError
        to__hz2hz2srcs = {}
        to__hz2hz2srcs__inv = {}
        dict_add__is(kind2hz2hz2srcs, kind, to__hz2hz2srcs)
        dict_add__is(kind2hz2hz2srcs, inv_kind, to__hz2hz2srcs__inv)

        inject(hzhz2isrcs, to__hz2hz2srcs, reverse=False)
        inject(hzhz2isrcs, to__hz2hz2srcs__inv, reverse=True)

    #打补丁:例外数据/非对称数据
    for kind, exceptional_hzhz2srcs_may_inv in kind2exceptional_hzhz2srcs_may_inv.items():
        hz2hz2srcs = kind2hz2hz2srcs[kind]
        for (hz0, hz1), (srcs, may_srcs__inv) in exceptional_hzhz2srcs_may_inv.items():
            hz2srcs = hz2hz2srcs.setdefault(hz0, {})
            dict_add__is(hz2srcs, hz1, [*srcs])
    return kind2hz2hz2srcs, kind2inv_kind










_kw4b64 = dict(b64_cfg_case='std', bigendian=True)
def hzhz2isrcs__from__hzhzstr_ussstr_pair(hzhzstr_ussstr, /):
    #hzhz2isrcs__to__hzhzstr_ussstr_pair
    hzhzstr, ussstr = hzhzstr_ussstr
    if 0:
        if not len(hzhzstr) == 2*(1+ussstr.count(';')): raise ValueError
    if not len(hzhzstr) == 2*(ussstr.count(';')): raise ValueError
        #now using str_join__both_list_and_entry_may_be_emty

    s2u_ = uint__from__radix64_digits__b64__str_
    _kw4b64
    if 0:isrcss = uss = [[s2u_(u__str, **_kw4b64) for u__str in us__str.split(',')] for us__str in ussstr.split(';')]
    isrcss = uss = [
        [s2u_(u__str, **_kw4b64)
            for u__str in str_split__entry_nonemty(',', us__str)
                #see below:str_join__entry_nonemty
        ] for us__str in str_split__both_list_and_entry_may_be_emty(';', ussstr)
            #see below:str_join__both_list_and_entry_may_be_emty
    ]
    if not len(hzhzstr) == 2*len(isrcss): raise logic-err
    hzhz_ls = [hzhzstr[i:i+2] for i in range(0, len(hzhzstr), 2)]
    if not len(hzhz_ls) == len(isrcss): raise logic-err
    hzhz2isrcs = dict(zip(hzhz_ls, isrcss))

    return hzhz2isrcs
def hzhz2isrcs__to__hzhzstr_ussstr_pair(hzhz2isrcs, /):
    #hzhz2isrcs__from__hzhzstr_ussstr_pair
    def isrcs2usstr(isrcs, /):
        #？使用base64？
        #改为:使用 16进制，但借用base16的字母表:『A-Za-z0-9+/』
        u2s_ = uint__to__radix64_digits__b64__str_
        if 0:
            if len(isrcs) < 2: raise NotImplementedError
            usstr = us__str = ','.join(u2s_(u, **_kw4b64) for u in isrcs)
                #bug:
                # s64 may be ''
                # len(isrcs) may be 0
                # hence both [''] and [] ==>> usstr == ''

        #usstr = us__str = str_join__both_list_and_entry_may_be_emty(',', (u2s_(u, **_kw4b64) for u in isrcs))
        def u2s__result_nonemty(u, /):
            return u2s_(u, **_kw4b64) if u else 'A'
        usstr = us__str = str_join__entry_nonemty(',', (u2s__result_nonemty(u) for u in isrcs))
        return us__str
    def isrcss2ussstr(isrcss, /):
        if 0:
            isrcss = [*isrcss]
            if len(isrcss) < 2: raise NotImplementedError
            ussstr = uss__str = ';'.join(map(isrcs2usstr, isrcss))
        ussstr = uss__str = str_join__both_list_and_entry_may_be_emty(';', map(isrcs2usstr, isrcss))
        return uss__str


    assert all(len(hzhz)==2 for hzhz in hzhz2isrcs)
    ps = sorted(hzhz2isrcs.items())
    hzhzstr = hzhz__str = ''.join(hzhz for hzhz, isrcs in ps)
    ussstr = uss__str = isrcss2ussstr(isrcs for hzhz, isrcs in ps)
    if 0:assert len(hzhzstr) == 2*(1+ussstr.count(';'))
    assert len(hzhzstr) == 2*(ussstr.count(';'))
        #now using str_join__both_list_and_entry_may_be_emty

    return hzhzstr, ussstr


def reformat__Unihan_Variants_txt__lines(lines, /, *, fout):
    kind2hz_hex_ts_pairs = parse__Unihan_Variants_txt(lines)
    reformat__Unihan_Variants_txt__parsed_result(kind2hz_hex_ts_pairs, fout=fout)
def reformat__Unihan_Variants_txt__parsed_result(kind2hz_hex_ts_pairs, /, *, fout):
    #def tail_of__reformat__Unihan_Variants_txt(kind2hz_hex_ts_pairs, /, *, fout):
    'reformat__parsed_result__Unihan_Variants_txt'
    print = mk_fprint(fout)
    idx2kind, kind2idx = _mk_bijection_pair(kind2hz_hex_ts_pairs)

    sources = kind2hz_hex_ts_pairs_to_sources(kind2hz_hex_ts_pairs)
    idx2src, src2idx = _mk_bijection_pair(sources)

    def show_assign(prefix, i, x, /):
        print(f'#{prefix!s}{i!s}={x!s}')
    def show_assigns(prefix, i2x, /):
        print('#{')
        for i, x in enumerate(i2x):
            show_assign(prefix, i, x)
        print('#}')
    def show_kind_body(prefix4kind, prefix4src, idx, kind, /):
        show_assign(prefix4kind, idx, kind)
        hz_hex_ts_pairs = kind2hz_hex_ts_pairs[kind]
        print('#{')
        for hz_hex, ts in hz_hex_ts_pairs:
            show_content_line(prefix4kind, prefix4src, idx, hz_hex, ts)
        print('#}')
    def hz_hex2str(hz_hex, /):
        hz, hex = hz_hex
        return f'{hz!s}-{hex!s}'
    def show_content_line(prefix4kind, prefix4src, idx, hz_hex, ts, /):

        print(f'{prefix4kind!s}{idx!s}:{hz_hex2str(hz_hex)!s}->', end='')
        may_sp = ''
        for hz_hex, srcs in ts:
            print(f'{may_sp!s}{hz_hex2str(hz_hex)!s}', end='')
            may_sp = ' '
            ####
            sep = '<'
            for src in srcs:
                i4src = src2idx[src]
                print(f'{sep!s}{prefix4src!s}{i4src!s}', end='')
                sep = ','
        print()
    def main():
        prefix4kind, prefix4src = 'ks'
        show_assigns(prefix4kind, idx2kind)
        show_assigns(prefix4src, idx2src)
        for idx, kind in enumerate(idx2kind):
            show_kind_body(prefix4kind, prefix4src, idx, kind)


    return main()
    r'''
    def _():
        kind2idx = {}
        for pt, kind, ls in fieldss:
            if 0:
                sz = len(kind2idx)
                i = kind2idx.setdefault(kind, sz)
                if i == sz:
                    print(f'#k{i}={kind!s}')

            print(f'k{i}:{hz!s}->')
    #'''


def load_parsed_result_from_compact_result_file__path(ifname, /, *, encoding, result_readonly):
    with open(ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()
    return load_parsed_result_from_compact_result_file__text(txt, result_readonly=result_readonly)
def load_parsed_result_from_compact_result_file__text(txt, /, *, result_readonly):
    compact_result = literal_eval(txt)
    uncompact_result = (_kind2hz_hex_ts_pairs, _kind2inv_kind) = uncompact__parsed_result__Unihan_Variants_txt(*compact_result)
    (kind2hz_hex_ts_pairs, kind2inv_kind) = uncompact_result
    parsed_result = kind2hz_hex_ts_pairs
    if not result_readonly:
        return parsed_result
    else:
        return parsed_result2readonly(parsed_result)
    raise logic-err
    return kind2hz_hex_ts_pairs
    return (kind2hz_hex_ts_pairs, kind2inv_kind)

def hz_hex_ts_pairs5immutable(hz_hex_ts_pairs, /):
    #hz_hex_ts_pairs2immutable
    'immutable -> [((hz, hex), [((hz, hex), [src])])]'
    tuple = list
    r = tuple((a, tuple((b, tuple(srcs)) for b, srcs in ls)) for a, ls in hz_hex_ts_pairs)
    return r
def hz_hex_ts_pairs2immutable(hz_hex_ts_pairs, /):
    #hz_hex_ts_pairs5immutable
    '[((hz, hex), [((hz, hex), [src])])] -> immutable'
    r = tuple((a, tuple((b, tuple(srcs)) for b, srcs in ls)) for a, ls in hz_hex_ts_pairs)
    hash(r) #immutable
    if not hz_hex_ts_pairs == hz_hex_ts_pairs5immutable(r): raise logic-err
    return r
def parsed_result5readonly(parsed_result, /):
    #parsed_result2readonly
    'readonly_parsed_result -> {kind: [((hz, hex), [((hz, hex), [src])])]}'
    kind2hz_hex_ts_pairs = parsed_result
    return fmap4dict_value(hz_hex_ts_pairs5immutable, kind2hz_hex_ts_pairs)
def parsed_result2readonly(parsed_result, /):
    #parsed_result5readonly
    '{kind: [((hz, hex), [((hz, hex), [src])])]} -> readonly_parsed_result'
    kind2hz_hex_ts_pairs = parsed_result
    MapView
    hz_hex_ts_pairs2immutable
    return MapView(fmap4dict_value(hz_hex_ts_pairs2immutable, kind2hz_hex_ts_pairs))


def hz_hex_ts_pairs2simplified(hz_hex_ts_pairs, /, *, result_readonly=False):
    '[((hz, hex), [((hz, hex), [src])])] -> {hz: sorted_hz_str}'
    # 不可逆映射
    hz2hzstr = {hz0: ''.join(sorted(hz1 for (hz1, _), srcs in ls)) for (hz0, _), ls in hz_hex_ts_pairs}
    if result_readonly:
        hz2hzstr = MapView(hz2hzstr)
    return hz2hzstr
def parsed_result2simplified(parsed_result, /, *, result_readonly):
    '{kind: [((hz, hex), [((hz, hex), [src])])]} -> {kind: {hz: sorted_hz_str}}'
    # used by parsed_result__of__Unihan_Variants_txt__of_ver13_0.py
    # 不可逆映射
    kind2hz_hex_ts_pairs = parsed_result
    kind2hz2hzstr = fmap4dict_value(hz_hex_ts_pairs2simplified, kind2hz_hex_ts_pairs)
    if result_readonly:
        kind2hz2hzstr = fmap4dict_value(MapView, kind2hz2hzstr)
        kind2hz2hzstr = MapView(kind2hz2hzstr)
    simplified_result = kind2hz2hzstr
    return simplified_result

def main(args=None, /):
    from pprint import pprint
    from seed.helper.stable_repr import stable_repr
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    if 0:
        help(pprint)
        #pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
        return

    parser = argparse.ArgumentParser(
        description='reformat unicode::UCD::Unihan::Unihan_Variants.txt'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--compact', action='store_true'
                        , default = False
                        , help='output compact-form')

    parser.add_argument('--coupled_kind_pairs4compact', type=str
                        , default='kSimplifiedVariant:kTraditionalVariant'
                        , help='coupled variant kind pairs in unicode::UCD::Unihan::Unihan_Variants.txt; format="xxx:yyy,zzz:www" default="kSimplifiedVariant:kTraditionalVariant"')

    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path for unicode::UCD::Unihan::Unihan_Variants.txt')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    kps__str = args.coupled_kind_pairs4compact
    coupled_kind_pairs = kps = []
    if kps__str:
        #bug:kp__strs = kps__str.split(',')
        kp__strs = str_split__entry_nonemty(',', kps__str)
        for kp__str in kp__strs:
            #bug:kind, inv_kind = kp__str.split(':')
            kind, inv_kind = str_split__entry_nonemty(':', kp__str)
            kps.append((kind, inv_kind))


    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        #lines = [*fin]
        lines = iter(fin)
        kind2hz_hex_ts_pairs = parsed_result = parse__Unihan_Variants_txt(lines)

    kind2inv_kind = kind2inv_kind___from___coupled_kind_pairs_(kind2hz_hex_ts_pairs.keys(), coupled_kind_pairs)
    compact_result = compact__parsed_result__Unihan_Variants_txt(kind2hz_hex_ts_pairs, kind2inv_kind=kind2inv_kind)
    if 0b00:
        uncompact_result = (_kind2hz_hex_ts_pairs, _kind2inv_kind) = uncompact__parsed_result__Unihan_Variants_txt(*compact_result)
        if not (kind2hz_hex_ts_pairs, kind2inv_kind) == uncompact_result:
            assert kind2inv_kind is _kind2inv_kind
            assert kind2hz_hex_ts_pairs.keys() == _kind2hz_hex_ts_pairs.keys()
            for kind, hz_hex_ts_pairs in kind2hz_hex_ts_pairs.items():
                _hz_hex_ts_pairs = _kind2hz_hex_ts_pairs[kind]
                assert len(hz_hex_ts_pairs) == len(_hz_hex_ts_pairs)
                if not hz_hex_ts_pairs == _hz_hex_ts_pairs:
                    print(kind)
                    for i, (lhs, rhs) in enumerate(zip(hz_hex_ts_pairs, _hz_hex_ts_pairs)):
                        if not lhs == rhs:
                            #见上面:『发现 非顺序排列』
                            print([kind, i, lhs, rhs])
                            break
            raise logic-err
    else:
        if not (kind2hz_hex_ts_pairs, kind2inv_kind) == uncompact__parsed_result__Unihan_Variants_txt(*compact_result): raise logic-err



    repr_result = stable_repr(compact_result, depth=0, maybe_max_depth=2)
    if not compact_result == literal_eval(repr_result): raise logic-err


    if not parsed_result == load_parsed_result_from_compact_result_file__text(repr_result, result_readonly=False): raise logic-err

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        if not args.compact:
            #reformat__Unihan_Variants_txt__lines(lines, fout=fout)
            reformat__Unihan_Variants_txt__parsed_result(kind2hz_hex_ts_pairs, fout=fout)
        else:
            compact__parsed_result__Unihan_Variants_txt
            #compact_result = compact__parsed_result__Unihan_Variants_txt___human(kind2hz_hex_ts_pairs, coupled_kind_pairs=kps)
            #pprint(compact_result, stream=fout, indent='', compact=True)
            stable_repr
            print(repr_result, file=fout)
if __name__ == "__main__":
    main()


