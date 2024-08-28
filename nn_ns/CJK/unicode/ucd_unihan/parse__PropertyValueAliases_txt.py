#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyAliases_txt.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py

PropertyValueAliases_txt
view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt
  property_name_alias2property_std_name
    pa2pnm
  property_name_alias2property_value_name_alias2property_value_std_name
    pa2va2vnm
  property_std_name2property_value_std_name2property_value_name_aliases
    pnm2vnm2vas
  extra info...
    missing:default_pseudo_value...
    property_std_name___Z___code_pt_rng__default_pseudo_value__pairs




nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt:__doc__ -ht




[[
view /sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt

# PropertyValueAliases-14.0.0.txt
# Date: 2021-05-10, 21:08:53 GMT
# © 2021 Unicode®, Inc.
... ...
# FORMAT
#
# Each line describes a property value name.
# This consists of three or more fields, separated by semicolons.
#
# First Field: The first field describes the property for which that
# property value name is used.
#
# Second Field: The second field is the short name for the property value.
# It is typically an abbreviation, but in a number of cases it is simply
# a duplicate of the "long name" in the third field.
#
# Third Field: The third field is the long name for the property value, 
# typically the formal name used in documentation about the property value.
#
# In the case of Canonical_Combining_Class (ccc), there are 4 fields: 
# The second field is numeric, the third is the short name, and the fourth is the long name.
#
# The above are the preferred aliases. Other aliases may be listed in additional fields.
#
# Loose matching should be applied to all property names and property values, with
# the exception of String Property values. With loose matching of property names and
# values, the case distinctions, whitespace, hyphens, and '_' are ignored.
# For Numeric Property values, numeric equivalence is applied: thus "01.00"
# is equivalent to "1".
#
# NOTE: Property value names are NOT unique across properties. For example:
#
#   AL means Arabic Letter for the Bidi_Class property, and
#   AL means Above_Left for the Canonical_Combining_Class property, and
#   AL means Alphabetic for the Line_Break property.
#
# In addition, some property names may be the same as some property value names.
# For example:
#
#   sc means the Script property, and
#   Sc means the General_Category property value Currency_Symbol (Sc)
#
# The combination of property value and property name is, however, unique.
#
# For more information, see UAX #44, Unicode Character Database, and
# UTS #18, Unicode Regular Expressions.
# ================================================


# ASCII_Hex_Digit (AHex)

AHex; N                               ; No                               ; F                                ; False
AHex; Y                               ; Yes                              ; T                                ; True

# Age (age)

age; 1.1                              ; V1_1
... ...
... ...
# Canonical_Combining_Class (ccc)

ccc;   0; NR                         ; Not_Reordered
... ...
... ...
ccc; 133; CCC133                     ; CCC133 # RESERVED
... ...
... ...
# Case_Folding (cf)

# @missing: 0000..10FFFF; Case_Folding; <code point>

# Case_Ignorable (CI)

CI ; N                                ; No                               ; F                                ; False
... ...
... ...
gc ; C                                ; Other                            # Cc | Cf | Cn | Co | Cs
... ...
... ...
gc ; L                                ; Letter                           # Ll | Lm | Lo | Lt | Lu
gc ; LC                               ; Cased_Letter                     # Ll | Lt | Lu
... ...
... ...
# @missing: 0000..10FFFF; General_Category; Unassigned
... ...
... ...
# cjkPrimaryNumeric (cjkPrimaryNumeric)

# @missing: 0000..10FFFF; cjkPrimaryNumeric; NaN

# cjkRSUnicode (cjkRSUnicode)

# @missing: 0000..10FFFF; cjkRSUnicode; <none>

# EOF

]]




















py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt   @stable_repr__F__i1__d999.parse__PropertyValueAliases_txt____ipath  :/sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt  | more
py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt   @stable_repr__F__i1__d999.parse__PropertyValueAliases_txt____ipath  :/sdcard/0my_files/unzip/unicode14_0/UCD/PropertyValueAliases.txt  +to_dump_to_file
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py.out.ver14_0_0.txt


py_adhoc_call   nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt   @stable_repr__F__i1__d999.load___parsed_result__of__PropertyValueAliases_txt__of_ver_  :14_0_0




















>>> from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt import load___parsed_result__of__PropertyValueAliases_txt__of_ver_

>>> (meta_info, core_data, handy_data, miscellaneous_data) = load___parsed_result__of__PropertyValueAliases_txt__of_ver_('14_0_0')

>>> meta_info['unicode_version']
'14_0_0'

>>> (pa2pnm, pnm2vnm2vas, pnm2rng_ppv_pairs) = core_data
>>> (pa2fst_vas, pa2va2vnm) = handy_data
>>> (pnm2fst_va2comment, pnm2fst_va2children, ccc_fst_va2numeric) = miscellaneous_data

>>> pa2pnm['gc']
'General_Category'
>>> pnm2vnm2vas['General_Category']['Cased_Letter']
['LC']
>>> pnm2rng_ppv_pairs['General_Category']
[((0, 1114111), 'Unassigned')]
>>> pnm2rng_ppv_pairs['Case_Folding']
[((0, 1114111), '<code point>')]

>>> pnm2rng_ppv_pairs['cjkRSUnicode']
[((0, 1114111), '<none>')]

>>> pnm2fst_va2comment
{'Canonical_Combining_Class': {'CCC133': 'RESERVED'}, 'General_Category': {'C': 'Cc | Cf | Cn | Co | Cs', 'L': 'Ll | Lm | Lo | Lt | Lu', 'LC': 'Ll | Lt | Lu', 'M': 'Mc | Me | Mn', 'N': 'Nd | Nl | No', 'P': 'Pc | Pd | Pe | Pf | Pi | Po | Ps', 'S': 'Sc | Sk | Sm | So', 'Z': 'Zl | Zp | Zs'}}

>>> pnm2fst_va2children == {'General_Category': {'C': ['Cc', 'Cf', 'Cn', 'Co', 'Cs'], 'L': ['Ll', 'Lm', 'Lo', 'Lt', 'Lu'], 'LC': ['Ll', 'Lt', 'Lu'], 'M': ['Mc', 'Me', 'Mn'], 'N': ['Nd', 'Nl', 'No'], 'P': ['Pc', 'Pd', 'Pe', 'Pf', 'Pi', 'Po', 'Ps'], 'S': ['Sc', 'Sk', 'Sm', 'So'], 'Z': ['Zl', 'Zp', 'Zs']}}
True
>>> ccc_fst_va2numeric['AL']
'228'


#]]]'''
__all__ = r'''

parse__PropertyValueAliases_txt
    parse__PropertyValueAliases_txt____ipath


load___parsed_result__of__PropertyValueAliases_txt__of_ver_
    mk_path5ver_



'''.split()#'''
__all__



from nn_ns.CJK.unicode.ucd_unihan._load import _load__literal_eval
from seed.tiny_.dict__add_fmap_filter import dict_add__new
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
from pathlib import Path
import re

_re4title = re.compile(r'# (?P<property_std_name>\w+) [(](?P<property_name_alias>\w+)[)]')
#_re4missing = re.compile(r'# @missing: (?P<fst_cp>[0-9A-F]+)..(?P<lst_cp>[0-9A-F]+); (?P<property_std_name>\w+); (?P<property_default_pseudo_value>\S+)')
_re4missing = re.compile(r'# @missing: (?P<fst_cp>[0-9A-F]+)..(?P<lst_cp>[0-9A-F]+); (?P<property_std_name>\w+); (?P<property_default_pseudo_value><[^\n<>]*>|\w+)')
            # Unassigned #long_name#property_value_std_name
            # <none>
            # <code point>
            # ...
            #
_re4empty_lines = re.compile(r'\n\n+')
_re4field_sep = re.compile(r'\s*;\s*')

#view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py.out.ver14_0_0.txt
_fmt4ofile = 'parse__PropertyValueAliases_txt.py.out.ver{}.txt'

_pager = '\n# ================================================\n'

#def parse__PropertyValueAliases_txt____ipath(ipath, /, *, encoding='ascii'):
    #fail:『encoding='ascii'』:©®:『# © 2021 Unicode®, Inc.』
    #
def parse__PropertyValueAliases_txt____ipath(ipath, /, *, encoding='utf8', to_dump_to_file=False):
    txt = Path(ipath).read_text(encoding)
    r = parse__PropertyValueAliases_txt(txt)
    if to_dump_to_file:
        from seed.helper.stable_repr import stable_repr
        opath = mk_path5ver_(ver:=r[0]['unicode_version'])
        with open(opath, 'xt', encoding=encoding) as ofile:
            #stable_repr__F__i1__d999
            s = stable_repr(r, indent=' '*1, depth=0, has_head_eol_when_indent=False)
            ofile.write(s)
    return r

def parse__PropertyValueAliases_txt(txt, /):
    r'''-> (meta_info, core_data, handy_data, miscellaneous_data)
#core_data
    / (pa2pnm, pnm2vnm2vas, pnm2rng_ppv_pairs)
    / (property_name_alias2property_std_name, property_std_name2property_value_std_name2property_value_name_aliases, property_std_name___Z___code_pt_rng__default_pseudo_value__pairs)
#handy_data
    / (pa2fst_vas, pa2va2vnm)
    / (property_name_alias2property_value_name_first_aliases, property_name_alias2property_value_name_alias2property_value_std_name)
#miscellaneous_data
    / (pnm2fst_va2comment, pnm2fst_va2children, ccc_fst_va2numeric) / (property_std_name2property_value_name_first_alias2comment, property_std_name2property_value_name_first_alias2children, ccc_property_value_name_first_alias2numeric)
'''#'''
            #__doc__==>>『data_semantics』
    assert not '\r' in txt
    assert _pager in txt

    ls = txt.split(_pager)
    ls = [*map(str.strip, ls)]
    assert len(ls) == 2
    [header, body] = ls
    body = _re4empty_lines.sub('\n', body)
    assert body.endswith('\n# EOF')
    body = body.removesuffix('\n# EOF')
    ss = _re4title.split(body)
    assert not ss[0]
    assert (len(ss)-1)%3 == 0
    num_properties = (len(ss)-1)//3

    _, ver, date, _ = cut_text_by_marker_seq(header, '# PropertyValueAliases-', '.txt\n# Date: ', '\n# © ')
        # 『# PropertyValueAliases-14.0.0.txt』
    ver = ver.replace('.', '_')
    meta_info = dict(unicode_version=ver, date=date, num_properties=num_properties, data_semantics=_data_semantics)


    property_name_alias2property_std_name = pa2pnm = {}
    property_name_alias2property_value_name_first_aliases = pa2fst_vas = {}
    property_name_alias2property_value_name_alias2property_value_std_name = pa2va2vnm = {}
    property_std_name2property_value_std_name2property_value_name_aliases = pnm2vnm2vas = {}
    property_std_name___Z___code_pt_rng__default_pseudo_value__pairs = pnm2rng_ppv_pairs = {}
    property_std_name2property_value_name_first_alias2comment = pnm2fst_va2comment = {}
    property_std_name2property_value_name_first_alias2children = pnm2fst_va2children = {}
    ccc_property_value_name_first_alias2numeric = ccc_fst_va2numeric = {}



    assert (len(ss)-1)%3 == 0
    for j in range(1, len(ss), 3):
        (property_std_name, property_name_alias, body4p) = ss[j:j+3]

        pa = property_name_alias
        pnm = property_std_name
        dict_add__new(pa2pnm,pa, pnm)

        it = _parse_per_property_(property_std_name, property_name_alias, body4p)
            # :: Iter [rng_ppv..., None, row_data...]
        rng_ppv_pairs = []
        for m in it:
            if m is None:break
            rng_ppv_pairs.append(m)
        rng_ppv_pairs
        row_datas = it

        dict_add__new(pa2fst_vas, pa, fst_vas:=[])
        dict_add__new(pnm2rng_ppv_pairs, pnm, rng_ppv_pairs)
        dict_add__new(pa2va2vnm, pa, va2vnm:={})
        dict_add__new(pnm2vnm2vas, pnm, vnm2vas:={})
        row_datas, va2vnm, vnm2vas
        for ((property_value_name_alias, property_value_std_name, property_value_name_alias_others), (may_numeric4ccc, smay_comment, may_children)) in row_datas:
            vnm = property_value_std_name
            fst_va = property_value_name_alias
            fst_vas.append(fst_va)
            vas = [fst_va, *property_value_name_alias_others]
            for va in vas:
                dict_add__new(va2vnm, va, vnm)
            dict_add__new(vnm2vas, vnm, vas)
            ######################
            ######################
            if smay_comment:
                comment = smay_comment
                fst_va2comment = pnm2fst_va2comment.setdefault(pnm, {})
                dict_add__new(fst_va2comment, fst_va, comment)
            ######################
            if not may_children is None:
                children = may_children
                fst_va2children = pnm2fst_va2children.setdefault(pnm, {})
                dict_add__new(fst_va2children, fst_va, children)
            ######################
            if not may_numeric4ccc is None:
                numeric4ccc = may_numeric4ccc
                dict_add__new(ccc_fst_va2numeric, fst_va, numeric4ccc)
            ######################
            ######################

    return (
    (meta_info
    ,#core_data
    (property_name_alias2property_std_name
    ,property_std_name2property_value_std_name2property_value_name_aliases
    ,property_std_name___Z___code_pt_rng__default_pseudo_value__pairs
    )
    ,#handy_data
    (property_name_alias2property_value_name_first_aliases
    ,property_name_alias2property_value_name_alias2property_value_std_name
    )
    ,#miscellaneous_data
    (property_std_name2property_value_name_first_alias2comment
    ,property_std_name2property_value_name_first_alias2children
    ,ccc_property_value_name_first_alias2numeric
    )
    ))
def _parse_per_property_(property_std_name, property_name_alias, body4p):
    '-> Iter [rng_ppv..., None, row_data...] / # rng_ppv/((fst_cp,lst_cp), property_default_pseudo_value) # row_data/((property_value_name_alias, property_value_std_name, property_value_name_alias_others), (may_numeric4ccc, smay_comment, may_children))'
    ls = body4p.strip().split('\n')
    assert all(ls), (property_std_name, property_name_alias, body4p, ls)
    assert ls
    if ls[-1][0] == '#':
        s4missing = ls.pop()
        m = _re4missing.fullmatch(s4missing)
        if m is None:
            raise Exception(s4missing)
                # <code point>
        assert property_std_name == m['property_std_name']
        fst_cp = int(m['fst_cp'], 16)
        lst_cp = int(m['lst_cp'], 16)
        property_default_pseudo_value = m['property_default_pseudo_value']
            # Unassigned #long_name#property_value_std_name
            # <none>
            # <code point>
            # ...
            #
        rng_ppv_pairs = [((fst_cp,lst_cp), property_default_pseudo_value)]
    else:
        rng_ppv_pairs = []
    rng_ppv_pairs
    yield from rng_ppv_pairs
    yield None

    for s in ls:
        s4fields, _, smay_comment = s.partition('#')
        s4fields = s4fields.strip()
        smay_comment = smay_comment.strip()
        if smay_comment:
            assert '|' in smay_comment or property_name_alias == 'ccc'
            if property_name_alias == 'ccc':
                ...
                may_children = None
            else:
                assert property_name_alias == 'gc'
                children = [c.strip() for c in smay_comment.split('|')]
                may_children = children
            smay_comment, may_children
        else:
            may_children = None
        smay_comment, may_children

        fields = [field.strip() for field in s4fields.split(';')]
        assert len(fields) >= 3
        assert property_name_alias == fields[0]
        if not property_name_alias == 'ccc':
            [_, property_value_name_alias, property_value_std_name, *property_value_name_alias_others] = fields
            may_numeric4ccc = None
        else:
            assert len(fields) == 4
            [_, numeric4ccc, property_value_name_alias, property_value_std_name] = fields
            property_value_name_alias_others = []
            may_numeric4ccc = numeric4ccc
        (property_value_name_alias, property_value_std_name, property_value_name_alias_others, may_numeric4ccc)
        yield ((property_value_name_alias, property_value_std_name, property_value_name_alias_others), (may_numeric4ccc, smay_comment, may_children))




_data_semantics = parse__PropertyValueAliases_txt____ipath.__doc__ = parse__PropertyValueAliases_txt.__doc__
#end-def _parse_per_property_(property_std_name, property_name_alias, body4p):
#end-def parse__PropertyValueAliases_txt(txt, /):




def mk_path5ver_(ver, /):
    assert '_' in ver
    assert not '.' in ver
    path = Path(__file__).parent / _fmt4ofile.format(ver)
    return path

def load___parsed_result__of__PropertyValueAliases_txt__of_ver_(ver, /):
    ipath = mk_path5ver_(ver)
    return _load__literal_eval(ipath, 'ascii')






__all__
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt import parse__PropertyValueAliases_txt, parse__PropertyValueAliases_txt____ipath, load___parsed_result__of__PropertyValueAliases_txt__of_ver_
from nn_ns.CJK.unicode.ucd_unihan.parse__PropertyValueAliases_txt import *
