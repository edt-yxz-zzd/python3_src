r'''
to load parsed_result of kCompatibilityVariant@Unihan_IRGSources.txt


======================
.readonly__cjk_compatibility_variant2unified
    :: MapView {variant_hz:unified_hz}

======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: cjk_compatibility_variant2unified
    mutable
.extra_derived_result
    :: None
    immutable
.compact_result
    :: variant_unified_packedpair_rawlines
    immutable

======================
.cjk_compatibility_variant2unified
    :: {variant_hz:unified_hz}
    mutable
.variant_unified_packedpair_rawlines
    :: '\n'.join(f'{variant_hz}{unified_hz}'...)
    immutable
======================






======================
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt.py
copy from:
      view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt.py
.+1,$s/kIICore/kCompatibilityVariant/g





======================
nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt

py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt --donot_output_result5load
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt --dump ver13_0 --donot_output_result5load
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt --load ver13_0 --donot_output_result5load





from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt import findout_available_version_strs, load_readonly_cjk_compatibility_variant2unified_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt import parse__kCompatibilityVariant8Unihan_IRGSources_txt, helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt import _cfg




======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kCompatibilityVariant8Unihan_IRGSources_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt
# Unihan_IRGSources.txt
# Date: 2020-02-18 18:27:33 GMT [JHJ]
# Unicode version: 13.0.0

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kCompatibilityVariant8Unihan_IRGSources_txt.py.out.ver13_0.txt
    1002对
!du -h ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kCompatibilityVariant8Unihan_IRGSources_txt.py.out.ver13_0.txt
    8K



#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_cjk_compatibility_variant2unified_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj


    '''.split()




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt import parse__kCompatibilityVariant8Unihan_IRGSources_txt, helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt as _helper4parse

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
from seed.abc.abc__ver0 import override
from seed.helper.stable_repr import stable_repr__expand_top_layer
from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

___end_mark_of_excluded_global_names__1___ = ...


#[[[

_cfg = Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(_helper4parse
    ,dataobj_immutable = False
    ,state_immutable = True
    ,__file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__kCompatibilityVariant8Unihan_IRGSources_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    ,state_rawtxt=True
        #state is compact_result is rawtxt
    )

#]]]







def load_readonly_cjk_compatibility_variant2unified_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__cjk_compatibility_variant2unified'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__cjk_compatibility_variant2unified = readonly__parsed_result

    return readonly__cjk_compatibility_variant2unified








main = _mainT(
    description
    ='parse,dump,load kCompatibilityVariant@Unihan_IRGSources.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    =parse__kCompatibilityVariant8Unihan_IRGSources_txt
    ,cfg4load_compact_result_file4xxx_txt
    =_cfg
    ,parsed_result2dataobj
    =_helper4parse.parsed_result2dataobj
    ,args4repr
    =[]
    ,kwargs4repr
    ={}
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
    readonly__cjk_compatibility_variant2unified4ver13_0 = load_readonly_cjk_compatibility_variant2unified_from_compact_result_file__ver('ver13_0')

if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    if 0b01:print(version_strs)
    if 0b00:assert 'ver13_0' in version_strs


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kCompatibilityVariant8Unihan_IRGSources_txt import findout_available_version_strs, load_readonly_cjk_compatibility_variant2unified_from_compact_result_file__ver
