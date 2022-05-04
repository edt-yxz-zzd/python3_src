r'''
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/_main4dump_load___parsed_result__of__xxx_txt.py

nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt

from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

used by:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__Blocks_txt.py
    copy from:
        view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__CJKRadicals_txt.py


#'''

__all__ = '''
    mainT
    load_readonly_dataobj_from_compact_result_file__ver
    '''.split()


from seed.tiny import check_callable, echo

def load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, /, *, may_path_bypass_version_str, result_readonly=True):
    'version_str -> readonly__dataobj'
    readonly__dataobj = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=result_readonly, may_path_bypass_version_str=may_path_bypass_version_str)
    return readonly__dataobj


def mainT(*, description, epilog, parse__xxx_txt__lines, cfg4load_compact_result_file4xxx_txt, parsed_result2dataobj, args4repr, kwargs4repr, args4dump, kwargs4dump):
  if 1:
    _cfg = cfg4load_compact_result_file4xxx_txt
    if parsed_result2dataobj is None:
        parsed_result2dataobj = echo
    check_callable(parsed_result2dataobj)

  def main(args=None, /):
    r'''
    st = compact_result
    dataobj =?= parsed_result
        !![dataobj derived from parsed_result]
        !![dataobj contains parsed_result]
            #eg. dataobj = (parsed_result, compact_result)
        [dataobj <==> parsed_result]

        [dataobj==parsed_result]:
            parsed_result2compact = cfg4load_compact_result_file4xxx_txt.state5dataobj___save
            parsed_result5compact = cfg4load_compact_result_file4xxx_txt.state2dataobj___create
    #'''
    if 0b00:
        import sys
        sys.stdout = 'wwwwwww'
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description=description
        , epilog=epilog
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
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('--donot_output_result4load', action='store_true'
                        , default = False
                        , help='donot use output file')


    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'


    ######################
    ######################
    ######################
    ######################
    if args.load:
        version_str = args.load
        _cfg.drop_cache_at(version_str)
        dataobj = load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=None, result_readonly=False)

    else:
        may_ifname = args.input
        with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
            lines = [*fin]

        parsed_result = parse__xxx_txt__lines(lines)
        dataobj = parsed_result2dataobj(parsed_result)
    dataobj

    if not args.donot_output_result4load:
        may_ofname = args.output
        with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
            print(dataobj, file=fout)

    if args.dump and (not args.load):
        version_str = args.dump
        dataobj
        _cfg.dump_data_file__ver(version_str, dataobj, force=False, args4repr=args4repr, kwargs4repr=kwargs4repr, args4dump=args4dump, kwargs4dump=kwargs4dump, is_readonly_dataobj=False, may_path_bypass_version_str=None)
            #force=False not args.force to protect data
            #   rm manually
        _cfg.drop_cache_at(version_str)
        _dataobj = load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=None, result_readonly=False)
        if not _dataobj == dataobj: raise logic-err
        return

    return
  #end-def main
  return main
#end-def mainT

from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver
