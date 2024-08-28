#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__DerivedGeneralCategory_txt.py
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__DerivedEastAsianWidth_txt.py


.+1,$s/east_asian_width/general_category/g
.+1,$s/DerivedEastAsianWidth/DerivedGeneralCategory/g

view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedGeneralCategory.txt
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py
======================
to load parsed_result of UCD::DerivedGeneralCategory.txt


======================
.readonly__char_pt2general_category
    :: TouchRangeBasedIntMapping<str>
    =char_pt2general_category
.readonly__general_category2char_pt_rngs
    :: MapView<str, NonTouchRanges>


======================
.dataobj
    :: (char_pt2general_category, general_category2char_pt_rngs)
    :: (parsed_result, extra_derived_result)
    mutable
.state
    :: txt
    = compact_result
    immutable

======================
.parsed_result
    :: char_pt2general_category
    = readonly__parsed_result
    immutable
.extra_derived_result
    :: general_category2char_pt_rngs
    mutable
.compact_result
    :: str / txt{linefmt=f'{ea}@0x{i:X}+{sz}'}
    immutable


======================
.char_pt2general_category
    :: TouchRangeBasedIntMapping<str>
        immutable
    :: (tmp) StackStyleSimpleIntMapping<str>
        mutable
.char_pt_rng2general_category
    ###conceptual:
    :: {(int, int): str}
.general_category2char_pt_rngs
    :: {str, NonTouchRanges}
        mutable
    :: (tmp) {str: StackStyleSimpleIntSet}
    ###conceptual:
    :: {str: [(int, int)]}
    :: {str: [(HexReprInt, HexReprInt)]}
======================



nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt -x



######################
#ver13_0
######################
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/extracted/DerivedGeneralCategory.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/extracted/DerivedGeneralCategory.txt --dump ver13_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt --load ver13_0

cp -iv ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__Blocks_txt__of_ver13_0.py ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedGeneralCategory_txt__of_ver13_0.py
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedGeneralCategory_txt__of_ver13_0.py
    %s/Blocks/DerivedGeneralCategory/g
    %s/code_block_name/general_category/g



######################
#ver14_0
######################
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt -i /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedGeneralCategory.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt -i /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedGeneralCategory.txt --dump ver14_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt --load ver14_0

cp -iv ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedGeneralCategory_txt__of_ver13_0.py ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedGeneralCategory_txt__of_ver14_0.py
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedGeneralCategory_txt__of_ver14_0.py
    %s/ver13/ver14/g

######################
#ver13_0 vs ver14_0
######################
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py.out.ver13_0.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py.out.ver14_0.txt
[[
424 lines:
diff ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py.out.ver13_0.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py.out.ver14_0.txt
===
7a8
> Cf@0x890+2
35d35
< Cn@0x61D+1
44,46c44,46
< Cn@0x86B+53
< Cn@0x8B5+1
< Cn@0x8C8+11
---
> Cn@0x86B+5
> Cn@0x88F+1
> Cn@0x892+6
124c124
< Cn@0xC3A+3
---
> Cn@0xC3A+2
129c129,130
< Cn@0xC5B+5
---
> Cn@0xC5B+2
> Cn@0xC5E+2
140c141
< Cn@0xCD7+7
---
> Cn@0xCD7+6
208,209c209
< Cn@0x170D+1
< Cn@0x1715+11
---
> Cn@0x1716+9
218d217
< Cn@0x180F+1
238,240c237,239
< Cn@0x1AC1+63
< Cn@0x1B4C+4
< Cn@0x1B7D+3
---
> Cn@0x1ACF+49
> Cn@0x1B4D+3
> Cn@0x1B7F+1
248d246
< Cn@0x1DFA+1
269c267
< Cn@0x20C0+16
---
> Cn@0x20C1+15
276,277d273
< Cn@0x2C2F+1
< Cn@0x2C5F+1
293c289
< Cn@0x2E53+45
---
> Cn@0x2E5E+34
305d300
< Cn@0x9FFD+3
310,311c305,308
< Cn@0xA7C0+2
< Cn@0xA7CB+42
---
> Cn@0xA7CB+5
> Cn@0xA7D2+1
> Cn@0xA7D4+1
> Cn@0xA7DA+24
347,348c344
< Cn@0xFBC2+17
< Cn@0xFD40+16
---
> Cn@0xFBC3+16
350,351c346,347
< Cn@0xFDC8+40
< Cn@0xFDFE+2
---
> Cn@0xFDC8+7
> Cn@0xFDD0+32
395c391,398
< Cn@0x10570+144
---
> Cn@0x1057B+1
> Cn@0x1058B+1
> Cn@0x10593+1
> Cn@0x10596+1
> Cn@0x105A2+1
> Cn@0x105B2+1
> Cn@0x105BA+1
> Cn@0x105BD+67
398c401,404
< Cn@0x10768+152
---
> Cn@0x10768+24
> Cn@0x10786+1
> Cn@0x107B1+1
> Cn@0x107BB+69
441c447,448
< Cn@0x10F5A+86
---
> Cn@0x10F5A+22
> Cn@0x10F8A+38
445,446c452,453
< Cn@0x11070+15
< Cn@0x110C2+11
---
> Cn@0x11076+9
> Cn@0x110C3+10
488c495
< Cn@0x116B9+7
---
> Cn@0x116BA+6
492c499
< Cn@0x11740+192
---
> Cn@0x11747+185
507c514
< Cn@0x11AA3+29
---
> Cn@0x11AA3+13
535c542,543
< Cn@0x12544+2748
---
> Cn@0x12544+2636
> Cn@0x12FF3+13
542c550,551
< Cn@0x16A70+96
---
> Cn@0x16ABF+1
> Cn@0x16ACA+6
558,559c567,571
< Cn@0x18D09+8951
< Cn@0x1B11F+49
---
> Cn@0x18D09+8935
> Cn@0x1AFF4+1
> Cn@0x1AFFC+1
> Cn@0x1AFFF+1
> Cn@0x1B123+45
567c579,582
< Cn@0x1BCA4+4956
---
> Cn@0x1BCA4+4700
> Cn@0x1CF2E+2
> Cn@0x1CF47+9
> Cn@0x1CFC4+60
570c585
< Cn@0x1D1E9+23
---
> Cn@0x1D1EB+21
597c612,613
< Cn@0x1DAB0+1360
---
> Cn@0x1DAB0+1104
> Cn@0x1DF1F+225
606c622,623
< Cn@0x1E150+368
---
> Cn@0x1E150+320
> Cn@0x1E2AF+17
608c625,629
< Cn@0x1E300+1280
---
> Cn@0x1E300+1248
> Cn@0x1E7E7+1
> Cn@0x1E7EC+1
> Cn@0x1E7EF+1
> Cn@0x1E7FF+1
662c683
< Cn@0x1F6D8+8
---
> Cn@0x1F6D8+5
667c688,689
< Cn@0x1F7EC+20
---
> Cn@0x1F7EC+4
> Cn@0x1F7F1+15
674,675d695
< Cn@0x1F979+1
< Cn@0x1F9CC+1
679c699
< Cn@0x1FA7B+5
---
> Cn@0x1FA7D+3
681,684c701,706
< Cn@0x1FAA9+7
< Cn@0x1FAB7+9
< Cn@0x1FAC3+13
< Cn@0x1FAD7+41
---
> Cn@0x1FAAD+3
> Cn@0x1FABB+5
> Cn@0x1FAC6+10
> Cn@0x1FADA+6
> Cn@0x1FAE8+8
> Cn@0x1FAF7+9
688,689c710,711
< Cn@0x2A6DE+34
< Cn@0x2B735+11
---
> Cn@0x2A6E0+32
> Cn@0x2B739+7
1135c1157
< Ll@0x2C30+47
---
> Ll@0x2C30+48
1303a1326
> Ll@0xA7C1+1
1306a1330,1334
> Ll@0xA7D1+1
> Ll@0xA7D3+1
> Ll@0xA7D5+1
> Ll@0xA7D7+1
> Ll@0xA7D9+1
1316a1345,1348
> Ll@0x10597+11
> Ll@0x105A3+15
> Ll@0x105B3+7
> Ll@0x105BB+2
1347a1380,1381
> Ll@0x1DF00+10
> Ll@0x1DF0B+20
1363a1398
> Lm@0x8C9+1
1393a1429
> Lm@0xA7F2+3
1403a1440,1442
> Lm@0x10780+6
> Lm@0x10787+42
> Lm@0x107B2+9
1407a1447,1449
> Lm@0x1AFF0+4
> Lm@0x1AFF5+7
> Lm@0x1AFFD+2
1433,1434c1475,1477
< Lo@0x8A0+21
< Lo@0x8B6+18
---
> Lo@0x870+24
> Lo@0x889+6
> Lo@0x8A0+41
1498a1542
> Lo@0xC5D+1
1507c1551
< Lo@0xCDE+1
---
> Lo@0xCDD+2
1571,1573c1615,1616
< Lo@0x1700+13
< Lo@0x170E+4
< Lo@0x1720+18
---
> Lo@0x1700+18
> Lo@0x171F+19
1593c1636
< Lo@0x1B45+7
---
> Lo@0x1B45+8
1626,1627c1669
< Lo@0x4E00+20989
< Lo@0xA000+21
---
> Lo@0x4E00+21013
1754a1797
> Lo@0x10F70+18
1757a1801,1802
> Lo@0x11071+2
> Lo@0x11075+1
1798a1844
> Lo@0x11740+7
1817c1863
< Lo@0x11AC0+57
---
> Lo@0x11AB0+73
1833a1880
> Lo@0x12F90+97
1837a1885
> Lo@0x16A70+79
1847c1895
< Lo@0x1B000+287
---
> Lo@0x1B000+291
1854a1903
> Lo@0x1DF0A+1
1856a1906
> Lo@0x1E290+30
1857a1908,1911
> Lo@0x1E7E0+7
> Lo@0x1E7E8+4
> Lo@0x1E7ED+2
> Lo@0x1E7F0+15
1892,1893c1946,1947
< Lo@0x20000+42718
< Lo@0x2A700+4149
---
> Lo@0x20000+42720
> Lo@0x2A700+4153
2340c2394
< Lu@0x2C00+47
---
> Lu@0x2C00+48
2504a2559
> Lu@0xA7C0+1
2507a2563,2565
> Lu@0xA7D0+1
> Lu@0xA7D6+1
> Lu@0xA7D8+1
2511a2570,2573
> Lu@0x10570+11
> Lu@0x1057C+15
> Lu@0x1058C+7
> Lu@0x10594+2
2603a2666,2667
> Mc@0x1715+1
> Mc@0x1734+1
2751c2815,2816
< Mn@0x8D3+15
---
> Mn@0x898+8
> Mn@0x8CA+24
2791a2857
> Mn@0xC3C+1
2841c2907
< Mn@0x1732+3
---
> Mn@0x1732+2
2849a2916
> Mn@0x180F+1
2866c2933
< Mn@0x1ABF+2
---
> Mn@0x1ABF+16
2889,2890c2956
< Mn@0x1DC0+58
< Mn@0x1DFB+5
---
> Mn@0x1DC0+64
2948a3015
> Mn@0x10F82+4
2950a3018,3019
> Mn@0x11070+1
> Mn@0x11073+2
2953a3023
> Mn@0x110C2+1
3032a3103,3104
> Mn@0x1CF00+46
> Mn@0x1CF30+23
3049a3122
> Mn@0x1E2AE+1
3108a3182
> Nd@0x16AC0+10
3213a3288
> Pd@0x2E5D+1
3264a3340,3343
> Pe@0x2E56+1
> Pe@0x2E58+1
> Pe@0x2E5A+1
> Pe@0x2E5C+1
3338c3417
< Po@0x61E+2
---
> Po@0x61D+3
3374a3454
> Po@0x1B7D+2
3403c3483
< Po@0x2E52+1
---
> Po@0x2E52+3
3456a3537
> Po@0x10F86+4
3474a3556
> Po@0x116B9+1
3486a3569
> Po@0x12FF1+2
3541a3625,3628
> Ps@0x2E55+1
> Ps@0x2E57+1
> Ps@0x2E59+1
> Ps@0x2E5B+1
3582c3669
< Sc@0x20A0+32
---
> Sc@0x20A0+33
3604a3692
> Sk@0x888+1
3617c3705
< Sk@0xFBB2+16
---
> Sk@0xFBB2+17
3793c3881,3883
< So@0xFDFD+1
---
> So@0xFD40+16
> So@0xFDCF+1
> So@0xFDFD+3
3811a3902
> So@0x1CF50+116
3818c3909
< So@0x1D1AE+59
---
> So@0x1D1AE+61
3844c3935
< So@0x1F6E0+13
---
> So@0x1F6DD+16
3848a3940
> So@0x1F7F0+1
3855,3857c3947
< So@0x1F900+121
< So@0x1F97A+82
< So@0x1F9CD+135
---
> So@0x1F900+340
3860c3950
< So@0x1FA78+3
---
> So@0x1FA78+5
3862,3865c3952,3957
< So@0x1FA90+25
< So@0x1FAB0+7
< So@0x1FAC0+3
< So@0x1FAD0+7
---
> So@0x1FA90+29
> So@0x1FAB0+11
> So@0x1FAC0+6
> So@0x1FAD0+10
> So@0x1FAE0+8
> So@0x1FAF0+7
===
]]





from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import findout_available_version_strs, load_readonly_char_pt2general_category_from_compact_result_file__ver, load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt import parse__DerivedGeneralCategory_txt, helper4parse__UCD_DerivedGeneralCategory_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import _cfg





#]]]'''
__all__ = r'''
    findout_available_version_strs

    load_readonly_char_pt2general_category_from_compact_result_file__ver
    load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj

'''.split()#'''
    #_cfg




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt import parse__DerivedGeneralCategory_txt, helper4parse__UCD_DerivedGeneralCategory_txt as _helper4parse

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
from seed.abc.abc__ver0 import override
from seed.helper.stable_repr import stable_repr__expand_top_layer
from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

___end_mark_of_excluded_global_names__1___ = ...
__all__


#[[[
_cfg = Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(_helper4parse
    ,dataobj_immutable = False
    ,state_immutable = True#False
        ,state_rawtxt = True
    ,__file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__DerivedGeneralCategory_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )

#]]]







def load_readonly_char_pt2general_category_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__char_pt2general_category'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__char_pt2general_category = readonly__parsed_result

    return readonly__char_pt2general_category



def load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__general_category2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__general_category2char_pt_rngs = readonly__extra_derived_result

    return readonly__general_category2char_pt_rngs




main = _mainT(
    description
    ='parse,dump,load UCD::DerivedGeneralCategory.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    =parse__DerivedGeneralCategory_txt
    ,cfg4load_compact_result_file4xxx_txt
    =_cfg
    ,parsed_result2dataobj
    =_helper4parse.parsed_result2dataobj
    ,args4repr
    =[]
    ,kwargs4repr
    ={}
    #=dict(maybe_max_depth4repr=1)
    #=dict(maybe_max_depth4repr=None)
    ,args4dump
    =[]
    ,kwargs4dump
    ={}
    )
if __name__ == "__main__":
    main()



findout_available_version_strs = _cfg.findout_available_version_strs

cache_view__version_str2readonly_dataobj = _cfg.get_view_of_cache__version_str2readonly_dataobj()




if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    if 0b01:print(version_strs)
    if 0b00:assert 'ver13_0' in version_strs

    readonly__char_pt2general_category4ver13_0 = load_readonly_char_pt2general_category_from_compact_result_file__ver('ver13_0')
    readonly__general_category2char_pt_rngs4ver13_0 = load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver('ver13_0')

    if 0b00:print((readonly__char_pt2general_category4ver13_0))
    if 0b00:print((readonly__general_category2char_pt_rngs4ver13_0))

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import findout_available_version_strs, load_readonly_char_pt2general_category_from_compact_result_file__ver, load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver



__all__
from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import findout_available_version_strs, load_readonly_char_pt2general_category_from_compact_result_file__ver, load_readonly_general_category2char_pt_rngs_from_compact_result_file__ver
from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedGeneralCategory_txt import *
