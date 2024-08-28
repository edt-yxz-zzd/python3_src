#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyAliases_txt.py
PropertyAliases_txt
view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
  property_kind2property_name_alias2property_std_name
    pk2pa2pnm
  property_std_name2property_kind
    pnm2pk
  property_std_name2property_name_aliases
    pnm2pas



nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt:__doc__ -ht
py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt   @pprint__pformat.parse__PropertyAliases_txt____ipath  :/sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt   @stable_repr__F__i1__d999.parse__PropertyAliases_txt____ipath  :/sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt

py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt   @stable_repr__F__i1__d999.parse__PropertyAliases_txt____ipath  :/sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt  +to_dump_to_file
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyAliases_txt.py.out.ver14_0_0.txt
du -h ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyAliases_txt.py.out.ver14_0_0.txt
    24K

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parsed_result__of__PropertyAliases_txt__of_ver14_0_0.py




view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyAliases.txt
# PropertyAliases-14.0.0.txt
# Date: 2021-03-08, 19:35:48 GMT
# © 2021 Unicode®, Inc.
... ...
cjkRSUnicode             ; kRSUnicode                  ; Unicode_Radical_Stroke; URS
... ...
# ================================================
# Binary Properties
# ================================================
... ...
WSpace                   ; White_Space                 ; space
XIDC                     ; XID_Continue
... ...
# ================================================
# Total:    129

# EOF

#]]]'''
__all__ = r'''
parse__PropertyAliases_txt____ipath
parse__PropertyAliases_txt

mk_path5ver_
load___parsed_result__of__PropertyAliases_txt__of_ver_
'''.split()#'''
__all__


from nn_ns.CJK.unicode.ucd_unihan._load import _load__literal_eval
from seed.tiny_.dict__add_fmap_filter import dict_add__new
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
from pathlib import Path


#view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyAliases_txt.py.out.ver14_0_0.txt
_fmt4ofile = 'parse__PropertyAliases_txt.py.out.ver{}.txt'

_pager = '\n# ================================================\n'

#def parse__PropertyAliases_txt____ipath(ipath, /, *, encoding='ascii'):
    #fail:『encoding='ascii'』:©®:『# © 2021 Unicode®, Inc.』
    #
def parse__PropertyAliases_txt____ipath(ipath, /, *, encoding='utf8', to_dump_to_file=False):
    txt = Path(ipath).read_text(encoding)
    r = parse__PropertyAliases_txt(txt)
    if to_dump_to_file:
        from seed.helper.stable_repr import stable_repr
        opath = mk_path5ver_(ver:=r[0]['unicode_version'])
        with open(opath, 'xt', encoding=encoding) as ofile:
            #stable_repr__F__i1__d999
            s = stable_repr(r, indent=' '*1, depth=0, has_head_eol_when_indent=False)
            ofile.write(s)
    return r
    with open(ipath, 'rt', encoding=encoding) as ifile:
        txt = ifile.read()
    return parse__PropertyAliases_txt(txt)

def parse__PropertyAliases_txt(txt, /):
    '-> (meta_info, (ls4fst_pa, pa2pnm, pnm2pk), (pk2pa2pnm, pnm2pas))    /    (meta_info, (list4first_property_name_alias, property_name_alias2property_std_name, property_std_name2property_kind), (property_kind2property_name_alias2property_std_name, property_std_name2property_name_aliases))'
            #__doc__==>>『data_semantics』
    assert not '\r' in txt
    assert _pager in txt

    ls = txt.split(_pager)
    ls = [*map(str.strip, ls)]
    assert not ls[1]
    [header, sp, *data_ls, footer] = ls
    assert not sp
    assert all(data_ls)
    assert all(s[0] == '#' for s in data_ls[0::2])
    assert not any('#' in s for s in data_ls[1::2])

    [_none, s4total, s4eof] = ''.join(footer.split()).split('#')
    assert not _none
    assert s4total.startswith('Total:')
    assert s4eof == 'EOF'
    num_properties = num_pnms = total = int(s4total.removeprefix('Total:'))
    _, ver, date, _ = cut_text_by_marker_seq(header, '# PropertyAliases-', '.txt\n# Date: ', '\n# © ')
        # 『# PropertyAliases-14.0.0.txt』
    ver = ver.replace('.', '_')
    meta_info = dict(unicode_version=ver, date=date, num_properties=num_properties, data_semantics=_data_semantics)


    list4first_property_name_alias = ls4fst_pa = []
    property_name_alias2property_std_name = pa2pnm = {}
    property_std_name2property_kind = pnm2pk = {}
    #extra:
    property_std_name2property_name_aliases = pnm2pas = {}
    property_kind2property_name_alias2property_std_name = pk2pa2pnm = {}

    L = len(data_ls)
    for i in range(L)[::2]:
        pk = data_ls[i].removeprefix('# ').strip()
        assert pk.endswith(' Properties')

        _pa2pnm = {}
        dict_add__new(pk2pa2pnm, pk, _pa2pnm)

        lines = data_ls[i+1].split('\n')
        fieldss = [[field.strip() for field in s.split(';')] for s in lines]
        for pa0, pnm, *other_pas in fieldss:
            ls4fst_pa.append(pa0)
            dict_add__new(pnm2pk, pnm, pk)
            pas = [pa0, *other_pas]
            dict_add__new(pnm2pas, pnm, pas)
            for pa in pas:
                dict_add__new(pa2pnm, pa, pnm)
                dict_add__new(_pa2pnm, pa, pnm)

    assert num_pnms == len(pnm2pk)
    assert num_pnms == len(pnm2pas)
    assert num_pnms == len(ls4fst_pa)
    return (
    meta_info
    ,(list4first_property_name_alias
    ,property_name_alias2property_std_name
    ,property_std_name2property_kind
    )
    ,(property_kind2property_name_alias2property_std_name
    ,property_std_name2property_name_aliases
    )
    )
_data_semantics = parse__PropertyAliases_txt____ipath.__doc__ = parse__PropertyAliases_txt.__doc__




def mk_path5ver_(ver, /):
    assert '_' in ver
    assert not '.' in ver
    path = Path(__file__).parent / _fmt4ofile.format(ver)
    return path

def load___parsed_result__of__PropertyAliases_txt__of_ver_(ver, /):
    ipath = mk_path5ver_(ver)
    return _load__literal_eval(ipath, 'ascii')







__all__
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt import parse__PropertyAliases_txt, parse__PropertyAliases_txt____ipath
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt import mk_path5ver_
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt import load___parsed_result__of__PropertyAliases_txt__of_ver_
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyAliases_txt import *
