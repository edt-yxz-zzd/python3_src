r'''
to load parsed_result of UCD::CJKRadicals.txt


.readonly__radical_char2unified_ideograph
    :: MapView {radical:unified}
.readonly__simplified_radical2traditional_radical
    :: MapView {simplified_radical:traditional_radical}


.parsed_result
    :: [((pint, str), char, hz)]
    :: [((cjk_radical_number, smay4ST), cjk_radical_character, cjk_unified_ideograph)]
    = readonly__parsed_result
    = idxZ_radical_unified_triples
.compact_result
    :: str
    <- (";".join0s(",".join1s([f"{radical}{unified}"])))
    = radical_char_unified_ideograph_pairss__str

.radical_char2unified_ideograph
    :: {radical:unified}

.simplified_radical2traditional_radical
    :: {simplified_radical:traditional_radical}




nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__CJKRadicals_txt.py

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt --dump ver13_0

py -m nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt --load ver13_0



from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt import findout_available_version_strs, load_readonly_parsed_result_from_compact_result_file__ver, load_readonly_compact_result_from_compact_result_file__ver, load_readonly_radical_char2unified_ideograph_from_compact_result_file__ver, load_readonly_simplified_radical2traditional_radical_from_compact_result_file__ver


from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt import _cfg, Config4load_compact_result_file4UCD_CJKRadicals_txt




======================
======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__CJKRadicals_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt
# CJKRadicals-13.0.0.txt
# Date: 2019-09-09, 19:38:00 GMT [RC, KW, LI]

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__CJKRadicals_txt.py.out.ver13_0.txt


#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_parsed_result_from_compact_result_file__ver
    load_readonly_compact_result_from_compact_result_file__ver
    load_readonly_radical_char2unified_ideograph_from_compact_result_file__ver
    load_readonly_simplified_radical2traditional_radical_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj

    _cfg
        Config4load_compact_result_file4UCD_CJKRadicals_txt

    '''.split()
    #readonly_parsed_result4ver13_0




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__CJKRadicals_txt import parse__CJKRadicals_txt, parsed_result2compact, parsed_result5compact, compact_result2dicts

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
from seed.abc.abc__ver0 import override

___end_mark_of_excluded_global_names__1___ = ...

#[[[
def _compact_result2dataobj(compact_result, /):
    parsed_result = parsed_result5compact(compact_result)
    dicts = (radical_char2unified_ideograph, simplified_radical2traditional_radical) = compact_result2dicts(compact_result)
    dataobj = (parsed_result, compact_result, dicts)
    return dataobj
def _compact_result5dataobj(dataobj, /):
    (parsed_result, compact_result, dicts) = dataobj
    return compact_result


class Config4load_compact_result_file4UCD_CJKRadicals_txt(IConfig4load_versioned_repr_txt_file):
    r'''
    dataobj = (parsed_result, compact_result, dicts/(radical_char2unified_ideograph, simplified_radical2traditional_radical))
    st = compact_result
    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = True
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding):
        dataobj_immutable = False
        state_immutable = True
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)

    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        #see: seed.func_tools.fmapT
        compact_result = st
        dataobj = _compact_result2dataobj(compact_result)
        return dataobj







    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        #see: seed.func_tools.fmapT
        compact_result = _compact_result5dataobj(dataobj)
        st = compact_result
        return st
    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass


_cfg = Config4load_compact_result_file4UCD_CJKRadicals_txt(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__CJKRadicals_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )
#]]]





def _load_readonly_dataobj_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str, result_readonly=True):
    'version_str -> readonly__dataobj/(readonly__parsed_result, readonly__compact_result, readonly__dicts)'
    readonly__dataobj = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=result_readonly, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__compact_result, readonly__dicts) = readonly__dataobj
    return readonly__dataobj

def load_readonly_parsed_result_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__parsed_result'
    (readonly__parsed_result, readonly__compact_result, readonly__dicts) = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    return readonly__parsed_result

def load_readonly_compact_result_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__compact_result'
    (readonly__parsed_result, readonly__compact_result, readonly__dicts) = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    return readonly__compact_result





def load_readonly_radical_char2unified_ideograph_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__radical_char2unified_ideograph'
    (readonly__parsed_result, readonly__compact_result, readonly__dicts) = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__radical_char2unified_ideograph, readonly__simplified_radical2traditional_radical) = readonly__dicts
    return readonly__radical_char2unified_ideograph


def load_readonly_simplified_radical2traditional_radical_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__simplified_radical2traditional_radical'
    (readonly__parsed_result, readonly__compact_result, readonly__dicts) = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__radical_char2unified_ideograph, readonly__simplified_radical2traditional_radical) = readonly__dicts
    return readonly__simplified_radical2traditional_radical






def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='parse,dump,load UCD::CJKRadicals.txt#ETL tool (extract, transform, load)'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--load', type=str, default = ''
                        , help='load and show file@given-version_str; disable --input & --dump')
    parser.add_argument('--dump', type=str, default = ''
                        , help='parse and dump to file@given-version_str')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
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


    ######################
    ######################
    ######################
    ######################
    if args.load:
        version_str = args.load
        _cfg.drop_cache_at(version_str)
        dataobj = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=None, result_readonly=False)

    else:
        may_ifname = args.input
        with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
            lines = [*fin]

        parsed_result = parse__CJKRadicals_txt(lines)
        compact_result = parsed_result2compact(parsed_result)
        dataobj = _compact_result2dataobj(compact_result)
    dataobj

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print(dataobj, file=fout)

    if args.dump and (not args.load):
        version_str = args.dump
        dataobj
        _cfg.dump_data_file__ver(version_str, dataobj, force=False, args4repr=[], kwargs4repr=dict(maybe_max_depth4repr=None), args4dump=[], kwargs4dump={}, is_readonly_dataobj=True, may_path_bypass_version_str=None)
        _cfg.drop_cache_at(version_str)
        _dataobj = _load_readonly_dataobj_from_compact_result_file__ver(version_str, may_path_bypass_version_str=None, result_readonly=False)
        if not _dataobj == dataobj: raise logic-err
        return

    return
if __name__ == "__main__":
    main()



findout_available_version_strs = _cfg.findout_available_version_strs

cache_view__version_str2readonly_dataobj = _cfg.get_view_of_cache__version_str2readonly_dataobj()




if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    if 0b00:print(version_strs)
    assert 'ver13_0' in version_strs

    readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_compact_result_file__ver('ver13_0')

    if 0b00:print((readonly_parsed_result4ver13_0))

