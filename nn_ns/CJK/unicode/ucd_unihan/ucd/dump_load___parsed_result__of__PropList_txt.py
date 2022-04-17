
r'''
to load parsed_result of UCD::PropList.txt
    真值属性
    出现 即 turnon

.parsed_result
    :: {property_name:[(begin,end)]}
.readonly__parsed_result
    :: MapView {property_name:NonTouchRanges}'


renamed:
    e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__PropList_txt.py
[[
nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt import findout_available_version_strs, load_readonly_parsed_result_from_parsed_result_file__ver

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt import cache_view__version_str2readonly_parsed_result

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__PropList_txt import _cfg, Config4load_parsed_result_file4UCD_PropList_txt


e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__PropList_txt.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__Unihan_Variants_txt.py
]]



[[old
######################
######################
nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__PropList_txt__of_ver13_0

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__PropList_txt__of_ver13_0

from nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__PropList_txt__of_ver13_0 import readonly_parsed_result4ver13_0, load_readonly_parsed_result_from_parsed_result_file__ver, cache_view__version_str2readonly_parsed_result


e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__PropList_txt__of_ver13_0.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__Unihan_Variants_txt__of_ver13_0.py
]]





view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py
    #decimal_vs_hex
    view /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.txt
    view /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt

view /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt
# PropList-13.0.0.txt
# Date: 2019-11-27, 03:13:28 GMT


#'''


__all__ = '''
    findout_available_version_strs
    load_readonly_parsed_result_from_parsed_result_file__ver

    cache_view__version_str2readonly_parsed_result

    _cfg
        Config4load_parsed_result_file4UCD_PropList_txt
    '''.split()
    #readonly_parsed_result4ver13_0

r'''
def parse__PropList_txt(lines, /, *, result_readonly):
def parsed_result2readonly(parsed_result, /):
def parsed_result5readonly(readonly__parsed_result, /):
def parsed_result2literal_text(parsed_result, /, *, decimal_vs_hex):
def parsed_result5literal_text(repr_result, /):

#'''



___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt import parse__PropList_txt, parsed_result2readonly, parsed_result5readonly, parsed_result2literal_text, parsed_result5literal_text

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
from seed.abc.abc__ver0 import override

___end_mark_of_excluded_global_names__1___ = ...

#[[[
class Config4load_parsed_result_file4UCD_PropList_txt(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = st = parsed_result
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
        dataobj = parsed_result = st
        return dataobj



    @override
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        parsed_result = dataobj
        readonly_parsed_result = parsed_result2readonly(parsed_result)
        readonly_dataobj = readonly_parsed_result
        return readonly_dataobj



    @override
    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        readonly_parsed_result = readonly_dataobj
        parsed_result = parsed_result5readonly(readonly_parsed_result)
        dataobj = parsed_result
        return dataobj


    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass


    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        st = parsed_result = dataobj
        return st

    def check_extra_input4repr(sf, /, *, decimal_vs_hex4repr):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass
    def text5state___repr(sf, st, /, *, decimal_vs_hex4repr):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr
        parsed_result = st
        txt = parsed_result2literal_text(parsed_result, decimal_vs_hex=decimal_vs_hex4repr)
        return txt

_cfg = Config4load_parsed_result_file4UCD_PropList_txt(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__PropList_txt.py.out.{}.hex.txt'
        #decimal_vs_hex4repr=True
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )
#]]]





def load_readonly_parsed_result_from_parsed_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly_parsed_result'
    parsed_result = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
    return parsed_result

if 0:
    #init&test

    #init
    readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_parsed_result_file__ver('ver13_0', may_path_bypass_version_str='/storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt')
        #not '/storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt'
    _cfg.dump_data_file__ver('ver13_0', readonly_parsed_result4ver13_0, force=False, args4repr=[], kwargs4repr=dict(decimal_vs_hex4repr=True), args4dump=[], kwargs4dump={}, is_readonly_dataobj=True, may_path_bypass_version_str=None)
    _cfg.drop_cache_at('ver13_0')

    #test dump
    #diff '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py.out.ver13_0.hex.txt'     '/storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt'


findout_available_version_strs = _cfg.findout_available_version_strs

cache_view__version_str2readonly_parsed_result = _cfg.get_view_of_cache__version_str2readonly_dataobj()




if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    print(version_strs)
    assert 'ver13_0' in version_strs

    readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_parsed_result_file__ver('ver13_0')

    print(sorted(readonly_parsed_result4ver13_0))


