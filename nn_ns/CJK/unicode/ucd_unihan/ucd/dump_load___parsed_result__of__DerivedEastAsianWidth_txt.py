#__all__:goto
r'''
NOTE:
    char_pt2east_asian_width.get(pt, 'N')
        !! buggy@N
    now:fixed:++kw:to_patch_missing

===
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__DerivedEastAsianWidth_txt.py
view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedEastAsianWidth.txt
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py
======================
to load parsed_result of UCD::DerivedEastAsianWidth.txt


======================
.readonly__char_pt2east_asian_width
    :: TouchRangeBasedIntMapping<str>
    =char_pt2east_asian_width
.readonly__east_asian_width2char_pt_rngs
    :: MapView<str, NonTouchRanges>


======================
.dataobj
    :: (char_pt2east_asian_width, east_asian_width2char_pt_rngs)
    :: (parsed_result, extra_derived_result)
    mutable
.state
    :: txt
    = compact_result
    immutable

======================
.parsed_result
    :: char_pt2east_asian_width
    = readonly__parsed_result
    immutable
.extra_derived_result
    :: east_asian_width2char_pt_rngs
    mutable
.compact_result
    :: str / txt{linefmt=f'{ea}@0x{i:X}+{sz}'}
    immutable


======================
.char_pt2east_asian_width
    :: TouchRangeBasedIntMapping<str>
        immutable
    :: (tmp) StackStyleSimpleIntMapping<str>
        mutable
.char_pt_rng2east_asian_width
    ###conceptual:
    :: {(int, int): str}
.east_asian_width2char_pt_rngs
    :: {str, NonTouchRanges}
        mutable
    :: (tmp) {str: StackStyleSimpleIntSet}
    ###conceptual:
    :: {str: [(int, int)]}
    :: {str: [(HexReprInt, HexReprInt)]}
======================





nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__DerivedEastAsianWidth_txt.py

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt



######################
#ver13_0
######################
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/extracted/DerivedEastAsianWidth.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/extracted/DerivedEastAsianWidth.txt --dump ver13_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt --load ver13_0

cp -iv ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__Blocks_txt__of_ver13_0.py ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedEastAsianWidth_txt__of_ver13_0.py
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedEastAsianWidth_txt__of_ver13_0.py
    %s/Blocks/DerivedEastAsianWidth/g
    %s/code_block_name/east_asian_width/g



######################
#ver14_0
######################
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt -i /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedEastAsianWidth.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt -i /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedEastAsianWidth.txt --dump ver14_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt --load ver14_0

cp -iv ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedEastAsianWidth_txt__of_ver13_0.py ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedEastAsianWidth_txt__of_ver14_0.py
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__DerivedEastAsianWidth_txt__of_ver14_0.py
    %s/ver13/ver14/g

######################
#ver13_0 vs ver14_0
######################
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver13_0.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver14_0.txt
[[
new:+to_patch_missing=True
71 lines:
diff ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver13_0.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver14_0.txt
===
409,410c409,413
< N@0x18D09+8951
< N@0x1B11F+49
---
> N@0x18D09+8935
> N@0x1AFF4+1
> N@0x1AFFC+1
> N@0x1AFFF+1
> N@0x1B123+45
446c449,450
< N@0x1F6D8+19
---
> N@0x1F6D8+5
> N@0x1F6E0+11
449c453,454
< N@0x1F7EC+288
---
> N@0x1F7EC+4
> N@0x1F7F1+283
452,453d456
< N@0x1F979+1
< N@0x1F9CC+1
456c459
< N@0x1FA7B+5
---
> N@0x1FA7D+3
458,461c461,466
< N@0x1FAA9+7
< N@0x1FAB7+9
< N@0x1FAC3+13
< N@0x1FAD7+1321
---
> N@0x1FAAD+3
> N@0x1FABB+5
> N@0x1FAC6+10
> N@0x1FADA+6
> N@0x1FAE8+8
> N@0x1FAF7+1289
536c541,544
< W@0x1B000+287
---
> W@0x1AFF0+4
> W@0x1AFF5+7
> W@0x1AFFD+2
> W@0x1B000+291
570a579
> W@0x1F6DD+3
573a583
> W@0x1F7F0+1
576,578c586
< W@0x1F947+50
< W@0x1F97A+82
< W@0x1F9CD+51
---
> W@0x1F947+185
580c588
< W@0x1FA78+3
---
> W@0x1FA78+5
582,585c590,595
< W@0x1FA90+25
< W@0x1FAB0+7
< W@0x1FAC0+3
< W@0x1FAD0+7
---
> W@0x1FA90+29
> W@0x1FAB0+11
> W@0x1FAC0+6
> W@0x1FAD0+10
> W@0x1FAE0+8
> W@0x1FAF0+7
===
]]
[[
old:-to_patch_missing=False
176 lines:
diff ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver13_0.txt ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver14_0.txt
===
259,260c259
< N@0x600+29
< N@0x61E+240
---
> N@0x600+270
269,271c268,270
< N@0x8A0+21
< N@0x8B6+18
< N@0x8D3+177
---
> N@0x870+31
> N@0x890+2
> N@0x898+236
349c348
< N@0xC3D+8
---
> N@0xC3C+9
353a353
> N@0xC5D+1
365c365
< N@0xCDE+1
---
> N@0xCDD+2
433,435c433,434
< N@0x1700+13
< N@0x170E+7
< N@0x1720+23
---
> N@0x1700+22
> N@0x171F+24
443,444c442
< N@0x1800+15
< N@0x1810+10
---
> N@0x1800+26
463,465c461,463
< N@0x1AB0+17
< N@0x1B00+76
< N@0x1B50+45
---
> N@0x1AB0+31
> N@0x1B00+77
> N@0x1B50+47
473,474c471
< N@0x1D00+250
< N@0x1DFB+283
---
> N@0x1D00+534
509c506
< N@0x20AD+19
---
> N@0x20AD+20
623,625c620
< N@0x2B97+152
< N@0x2C30+47
< N@0x2C60+148
---
> N@0x2B97+349
640c635
< N@0x2DE0+115
---
> N@0x2DE0+126
645,647c640,644
< N@0xA700+192
< N@0xA7C2+9
< N@0xA7F5+56
---
> N@0xA700+203
> N@0xA7D0+2
> N@0xA7D3+1
> N@0xA7D5+5
> N@0xA7F2+59
679,681c676,677
< N@0xFB46+124
< N@0xFBD3+365
< N@0xFD50+64
---
> N@0xFB46+125
> N@0xFBD3+445
683c679,680
< N@0xFDF0+14
---
> N@0xFDCF+1
> N@0xFDF0+16
717c714,721
< N@0x1056F+1
---
> N@0x1056F+12
> N@0x1057C+15
> N@0x1058C+7
> N@0x10594+2
> N@0x10597+11
> N@0x105A3+15
> N@0x105B3+7
> N@0x105BB+2
720a725,727
> N@0x10780+6
> N@0x10787+42
> N@0x107B2+9
763a771
> N@0x10F70+26
767,768c775,776
< N@0x11052+30
< N@0x1107F+67
---
> N@0x11052+36
> N@0x1107F+68
810c818
< N@0x11680+57
---
> N@0x11680+58
814c822
< N@0x11730+16
---
> N@0x11730+23
830c838
< N@0x11AC0+57
---
> N@0x11AB0+73
857a866
> N@0x12F90+99
864c873,874
< N@0x16A6E+2
---
> N@0x16A6E+81
> N@0x16AC0+10
880a891,893
> N@0x1CF00+46
> N@0x1CF30+23
> N@0x1CF50+116
883c896
< N@0x1D129+192
---
> N@0x1D129+194
910a924
> N@0x1DF00+31
919a934
> N@0x1E290+31
921a937,940
> N@0x1E7E0+7
> N@0x1E7E8+4
> N@0x1E7ED+2
> N@0x1E7F0+15
1085c1104,1107
< W@0x1B000+287
---
> W@0x1AFF0+4
> W@0x1AFF5+7
> W@0x1AFFD+2
> W@0x1B000+291
1119a1142
> W@0x1F6DD+3
1122a1146
> W@0x1F7F0+1
1125,1127c1149
< W@0x1F947+50
< W@0x1F97A+82
< W@0x1F9CD+51
---
> W@0x1F947+185
1129c1151
< W@0x1FA78+3
---
> W@0x1FA78+5
1131,1134c1153,1158
< W@0x1FA90+25
< W@0x1FAB0+7
< W@0x1FAC0+3
< W@0x1FAD0+7
---
> W@0x1FA90+29
> W@0x1FAB0+11
> W@0x1FAC0+6
> W@0x1FAD0+10
> W@0x1FAE0+8
> W@0x1FAF0+7
===
]]








from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt import findout_available_version_strs, load_readonly_char_pt2east_asian_width_from_compact_result_file__ver, load_readonly_east_asian_width2char_pt_rngs_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import parse__DerivedEastAsianWidth_txt, helper4parse__UCD_DerivedEastAsianWidth_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt import _cfg




======================
======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/extracted/DerivedEastAsianWidth.txt
# DerivedEastAsianWidth-13.0.0.txt


view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver13_0.txt


#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_char_pt2east_asian_width_from_compact_result_file__ver
    load_readonly_east_asian_width2char_pt_rngs_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj


    '''.split()
    #_cfg




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import parse__DerivedEastAsianWidth_txt, helper4parse__UCD_DerivedEastAsianWidth_txt as _helper4parse

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
from seed.abc.abc__ver0 import override
from seed.helper.stable_repr import stable_repr__expand_top_layer
from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

___end_mark_of_excluded_global_names__1___ = ...


#[[[
_cfg = Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(_helper4parse
    ,dataobj_immutable = False
    ,state_immutable = True#False
        ,state_rawtxt = True
    ,__file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__DerivedEastAsianWidth_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )

#]]]







def load_readonly_char_pt2east_asian_width_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__char_pt2east_asian_width'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__char_pt2east_asian_width = readonly__parsed_result

    return readonly__char_pt2east_asian_width



def load_readonly_east_asian_width2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__east_asian_width2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__east_asian_width2char_pt_rngs = readonly__extra_derived_result

    return readonly__east_asian_width2char_pt_rngs




main = _mainT(
    description
    ='parse,dump,load UCD::DerivedEastAsianWidth.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    #=parse__DerivedEastAsianWidth_txt
    =lambda lines, /:parse__DerivedEastAsianWidth_txt(lines, to_patch_missing=True)
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

    readonly__char_pt2east_asian_width4ver13_0 = load_readonly_char_pt2east_asian_width_from_compact_result_file__ver('ver13_0')
    readonly__east_asian_width2char_pt_rngs4ver13_0 = load_readonly_east_asian_width2char_pt_rngs_from_compact_result_file__ver('ver13_0')

    if 0b00:print((readonly__char_pt2east_asian_width4ver13_0))
    if 0b00:print((readonly__east_asian_width2char_pt_rngs4ver13_0))

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__DerivedEastAsianWidth_txt import findout_available_version_strs, load_readonly_char_pt2east_asian_width_from_compact_result_file__ver, load_readonly_east_asian_width2char_pt_rngs_from_compact_result_file__ver

