r'''
.readonly_simplified_result
    :: {kind: {hz: sorted_hz_str}}
.readonly_parsed_result
    :: {kind: [((hz, hex), [((hz, hex), [src])])]}



renamed:
    e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__Unihan_Variants_txt.py
[[

nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt import findout_available_version_strs, load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver, load_readonly_parsed_result_from_compact_result_file__ver, load_readonly_simplified_result_from_compact_result_file__ver


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt import cache_view__version_str2readonly_parsed_result_and_simplified_result

from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt import _cfg, Config4load_compact_result_file4Unihan_Variants_txt

]]




######################
######################
.readonly_simplified_result4ver13_0
    :: {kind: {hz: sorted_hz_str}}
.readonly_parsed_result4ver13_0
    :: {kind: [((hz, hex), [((hz, hex), [src])])]}
    #eg:
    # U+348B  kSemanticVariant    U+5EDD<kMatthews U+53AE<kMatthews
    # ==>> {..., kSemanticVariant: [..., ((㒋, 348B), [((廝, 5EDD), [kMatthews]), ((厮, 53AE), [kMatthews])]), ...], ...}


[[old
nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0

from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0

from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import findout_available_version_strs, load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver, load_readonly_parsed_result_from_compact_result_file__ver, load_readonly_simplified_result_from_compact_result_file__ver


from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import cache_view__version_str2readonly_parsed_result_and_simplified_result


e  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__Unihan_Variants_txt__of_ver13_0.py
]]







view  ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py.out.ver13_0.compact.txt
view /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt
    # Unihan_Variants.txt
    # Date: 2020-02-18 18:27:33 GMT [JHJ]
    # Unicode version: 13.0.0

#'''

__all__ = '''
    findout_available_version_strs

    load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver
        load_readonly_parsed_result_from_compact_result_file__ver
        load_readonly_simplified_result_from_compact_result_file__ver

    cache_view__version_str2readonly_parsed_result_and_simplified_result

    _cfg
        Config4load_compact_result_file4Unihan_Variants_txt
    '''.split()
    #readonly_parsed_result4ver13_0
    #readonly_simplified_result4ver13_0















___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt import parsed_result2simplified, parsed_result2readonly, parsed_result5readonly, load_parsed_result_from_compact_result_file__path, uncompact__parsed_result__Unihan_Variants_txt, compact__parsed_result__Unihan_Variants_txt___human
from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
from seed.abc.abc__ver0 import override

___end_mark_of_excluded_global_names__1___ = ...

#[[[
class Config4load_compact_result_file4Unihan_Variants_txt(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = (parsed_result, simplified_result)
    st = compact_result
    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = False
    sf.coupled_kind_pairs4compact__parsed_result
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding):
        dataobj_immutable = False
        state_immutable = False
        #sf.coupled_kind_pairs4compact__parsed_result = [*coupled_kind_pairs4compact__parsed_result]
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)

    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        #see: seed.func_tools.fmapT
        'compact_result -> (parsed_result, simplified_result)'
        #raise NotImplementedError('see: nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt ')
        compact_result = st
        (kind2hz_hex_ts_pairs, kind2inv_kind) = uncompact__parsed_result__Unihan_Variants_txt(*compact_result)
        parsed_result = kind2hz_hex_ts_pairs
        simplified_result = parsed_result2simplified(parsed_result, result_readonly=False)
        dataobj = (parsed_result, simplified_result)
        return dataobj



    @override
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        (parsed_result, simplified_result) = dataobj
        readonly_simplified_result = parsed_result2simplified(parsed_result, result_readonly=True)
        readonly_parsed_result = parsed_result2readonly(parsed_result)
        readonly_dataobj = (readonly_parsed_result, readonly_simplified_result)
        return readonly_dataobj



    @override
    def dataobj5readonly___literal_rebuild(sf, readonly_dataobj, /):
        #.dataobj2readonly___recur_view
        'readonly_dataobj -> dataobj'
        (readonly_parsed_result, readonly_simplified_result) = readonly_dataobj
        parsed_result = parsed_result5readonly(readonly_parsed_result)
        simplified_result = parsed_result2simplified(parsed_result, result_readonly=False)
        dataobj = (parsed_result, simplified_result)
        return dataobj


    @override
    def check_extra_input4dump(sf, /, *, coupled_kind_pairs4compact__parsed_result):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass


    @override
    def state5dataobj___save(sf, dataobj, /, *, coupled_kind_pairs4compact__parsed_result):
        '(parsed_result, simplified_result) -> compact_result'
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        #raise NotImplementedError('see: nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt ')
        (parsed_result, simplified_result) = dataobj
        #coupled_kind_pairs = sf.coupled_kind_pairs4compact__parsed_result
        coupled_kind_pairs = coupled_kind_pairs4compact__parsed_result

        compact_result = compact__parsed_result__Unihan_Variants_txt___human(parsed_result, coupled_kind_pairs=coupled_kind_pairs)
            #def compact__parsed_result__Unihan_Variants_txt___human(kind2hz_hex_ts_pairs, /, *, coupled_kind_pairs):
        st = compact_result
        return st

_cfg = Config4load_compact_result_file4Unihan_Variants_txt(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='reformat__Unihan_Variants_txt.py.out.{}.compact.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    #,coupled_kind_pairs4compact__parsed_result = [('kSimplifiedVariant', 'kTraditionalVariant')] #hardwired????
    )
#]]]

def load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str):
    'version_str -> (readonly_parsed_result, readonly_simplified_result)'
    (parsed_result, simplified_result) = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
    return (parsed_result, simplified_result)

def load_readonly_parsed_result_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly_parsed_result'
    (parsed_result, simplified_result) = load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    return parsed_result
def load_readonly_simplified_result_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly_simplified_result'
    (parsed_result, simplified_result) = load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    return simplified_result




cache_view__version_str2readonly_parsed_result_and_simplified_result = _cfg.get_view_of_cache__version_str2readonly_dataobj()

findout_available_version_strs = _cfg.findout_available_version_strs




if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    print(version_strs)
    assert 'ver13_0' in version_strs
    readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_compact_result_file__ver('ver13_0')
    readonly_simplified_result4ver13_0 = load_readonly_simplified_result_from_compact_result_file__ver('ver13_0')


if 0:
    #test dump
    _cfg.dump_data_file__ver('ver13_0', (readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0), force=False, args4repr=[], kwargs4repr=dict(maybe_max_depth4repr=2), args4dump=[], kwargs4dump=dict(coupled_kind_pairs4compact__parsed_result=[('kSimplifiedVariant', 'kTraditionalVariant')]), is_readonly_dataobj=True, may_path_bypass_version_str=_cfg.pkg_path / '0000.tmp.ver13_0.txt')
    #diff '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py.out.ver13_0.compact.txt'     '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/0000.tmp.ver13_0.txt'













r"""[[[[[old-version
__all__ = '''
    readonly_parsed_result4ver13_0
    readonly_simplified_result4ver13_0

    load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver
        load_readonly_parsed_result_from_compact_result_file__ver
        load_readonly_simplified_result_from_compact_result_file__ver

    cache_view__version_str2readonly_parsed_result_and_simplified_result
    '''.split()


from nn_ns.CJK.unicode.ucd_unihan.unihan.reformat__Unihan_Variants_txt import load_parsed_result_from_compact_result_file__path, parsed_result2simplified
from seed.tiny import MapView

from pathlib import Path
import re

class Globals:
    encoding = 'utf8'
    pkg_path = Path(__file__).parent
    if 0:
        ver2basename = dict(
            ver13_0='reformat__Unihan_Variants_txt.py.out.ver13_0.compact.txt'
            )
    else:
        basename_fmt = 'reformat__Unihan_Variants_txt.py.out.{}.compact.txt'
        version_str__rex = re.compile(r'^ver[0-9]+_[0-9]+$')
def verify_version_str(version_str, /):
    m = Globals.version_str__rex.fullmatch(version_str)
    return m is not None
def version_str2compact_result_file_path(version_str, /):
    if 0:
        basename = Globals.ver2basename[version_str]
    else:
        if not verify_version_str(version_str): raise ValueError
        basename = Globals.basename_fmt.format(version_str)
    path = Globals.pkg_path / basename
    return path


def _load_parsed_result_from_compact_result_file__ver(version_str, /, *, result_readonly):
    path = version_str2compact_result_file_path(version_str)
    parsed_result = load_parsed_result_from_compact_result_file__path(path, encoding=Globals.encoding, result_readonly=result_readonly)
    kind2hz_hex_ts_pairs = parsed_result
        # {kind: [((hz, hex), [((hz, hex), [src])])]}
    return parsed_result


#def parsed_result2simplified(parsed_result, /, *, result_readonly): -> simplified_result

_cache = {}
def load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str, /):
    'version_str -> (readonly_parsed_result, readonly_simplified_result)'
    def recur(version_str, /):
        if version_str in _cache:
            return _cache[version_str]

        parsed_result = _load_parsed_result_from_compact_result_file__ver(version_str, result_readonly=True)
        simplified_result = parsed_result2simplified(parsed_result, result_readonly=True)
        _cache[version_str] = parsed_result, simplified_result
        return recur(version_str)
        return (parsed_result, simplified_result)
    return recur(version_str)

cache_view__version_str2readonly_parsed_result_and_simplified_result = MapView(_cache)


def load_readonly_parsed_result_from_compact_result_file__ver(version_str, /):
    'version_str -> readonly_parsed_result'
    (parsed_result, simplified_result) = load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str)
    return parsed_result
def load_readonly_simplified_result_from_compact_result_file__ver(version_str, /):
    'version_str -> readonly_simplified_result'
    (parsed_result, simplified_result) = load_readonly_parsed_result_and_simplified_result_from_compact_result_file__ver(version_str)
    return simplified_result

readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_compact_result_file__ver('ver13_0')
readonly_simplified_result4ver13_0 = load_readonly_simplified_result_from_compact_result_file__ver('ver13_0')

#]]]]]"""

