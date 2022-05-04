r'''
to load parsed_result of UCD::Blocks.txt


======================
.readonly__char_pt2code_block_name
    :: TouchRangeBasedIntMapping<str>
    =char_pt2code_block_name
.readonly__code_block_name2char_pt_rngs
    :: MapView<str, NonTouchRanges>


======================
.dataobj
    :: (char_pt2code_block_name, code_block_name2char_pt_rngs)
    :: (parsed_result, extra_derived_result)
    mutable
.state
    :: char_pt_rng2code_block_name
    = compact_result
    mutable

======================
.parsed_result
    :: char_pt2code_block_name
    = readonly__parsed_result
    immutable
.extra_derived_result
    :: code_block_name2char_pt_rngs
    mutable
.compact_result
    :: char_pt_rng2code_block_name
    mutable


======================
.char_pt2code_block_name
    :: TouchRangeBasedIntMapping<str>
        immutable
    :: (tmp) StackStyleSimpleIntMapping<str>
        mutable
.char_pt_rng2code_block_name
    # st 4 store
    :: (literal_store) {(HexReprInt, HexReprInt): str}
    ###conceptual:
    :: {(int, int): str}
.code_block_name2char_pt_rngs
    :: {str, NonTouchRanges}
        mutable
    :: (tmp) {str: StackStyleSimpleIntSet}
    ###conceptual:
    :: {str: [(int, int)]}
    :: {str: [(HexReprInt, HexReprInt)]}
======================





nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__Blocks_txt.py

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt --dump ver13_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt --load ver13_0



from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt import findout_available_version_strs, load_readonly_char_pt2code_block_name_from_compact_result_file__ver, load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt import parse__Blocks_txt, helper4parse__UCD_Blocks_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt import _cfg, Config4load_compact_result_file4UCD_Blocks_txt




======================
======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt
# Blocks-13.0.0.txt
# Date: 2019-07-10, 19:06:00 GMT [KW]

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py.out.ver13_0.txt


#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_char_pt2code_block_name_from_compact_result_file__ver
    load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj


    '''.split()
    #_cfg Config4load_compact_result_file4UCD_Blocks_txt




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt import parse__Blocks_txt, helper4parse__UCD_Blocks_txt as _helper4parse

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
from seed.abc.abc__ver0 import override
from seed.helper.stable_repr import stable_repr__expand_top_layer
from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

___end_mark_of_excluded_global_names__1___ = ...


#[[[
r"""
class Config4load_compact_result_file4UCD_Blocks_txt(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = (parsed_result, extra_derived_result)
    st = compact_result/char_pt_rng2code_block_name
    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = False
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding):
        dataobj_immutable = False
        state_immutable = False
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)

    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        #see: seed.func_tools.fmapT
        dataobj = _helper4parse.state2dataobj___create(st)
        return dataobj







    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        st = _helper4parse.state5dataobj___save(dataobj)
        return st
    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass

    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        return _helper4parse.dataobj2readonly(dataobj)
    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        #un verbose? un view?
        #neat naive clean rebuild simplified
        return _helper4parse.dataobj5readonly(readonly_dataobj)


    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr
        txt = stable_repr__expand_top_layer(st)
        return txt


_cfg = Config4load_compact_result_file4UCD_Blocks_txt(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__Blocks_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )
#"""
_cfg = Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(_helper4parse
    ,dataobj_immutable = False
    ,state_immutable = False
    ,__file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__Blocks_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )

#]]]







def load_readonly_char_pt2code_block_name_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__char_pt2code_block_name'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__char_pt2code_block_name = readonly__parsed_result

    return readonly__char_pt2code_block_name



def load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__code_block_name2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__code_block_name2char_pt_rngs = readonly__extra_derived_result

    return readonly__code_block_name2char_pt_rngs




main = _mainT(
    description
    ='parse,dump,load UCD::Blocks.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    =parse__Blocks_txt
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

    readonly__char_pt2code_block_name4ver13_0 = load_readonly_char_pt2code_block_name_from_compact_result_file__ver('ver13_0')
    readonly__code_block_name2char_pt_rngs4ver13_0 = load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver('ver13_0')

    if 0b00:print((readonly__char_pt2code_block_name4ver13_0))
    if 0b00:print((readonly__code_block_name2char_pt_rngs4ver13_0))

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt import findout_available_version_strs, load_readonly_char_pt2code_block_name_from_compact_result_file__ver, load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver

