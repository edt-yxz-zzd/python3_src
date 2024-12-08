#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/txt/grep_between.py

nn_ns.txt.grep_between
py -m nn_ns.app.debug_cmd   nn_ns.txt.grep_between -x
py -m nn_ns.app.doctest_cmd nn_ns.txt.grep_between:__doc__ -ht

#py_adhoc_call   nn_ns.txt.grep_between   @grep_between__txt_ "'[^']*'"
py -m nn_ns.txt.grep_between -s -u -ptn "'[^']*'" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py

e ../../python3_src/bash_script/app/grep_between
grep_between -s -u -ptn "'[^']*'" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py


#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
#def strip_text_by_marker_pair(txt, begin_marker, end_marker, /):
from seed.types.StackStyleSet import StackStyleSet
___end_mark_of_excluded_global_names__0___ = ...

def grep_between__txt_(pattern8regex, txt, begin_marker, end_marker, /, *, to_uniq:bool, to_sort:bool):
    'str -> str -> str -> str -> [str]'
    s = strip_text_by_marker_pair(txt, begin_marker, end_marker)
    rex = re.compile(pattern8regex)
    words = (m.group(0) for m in rex.finditer(s))
    if to_uniq:
        words = StackStyleSet(words)
    if to_sort:
        words = sorted(words)
    return tuple(words)

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='show matched words in text between markers'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-r', '--repr', action='store_true'
                        , default = False
                        , help='repr output words')
    parser.add_argument('-s', '--sort', action='store_true'
                        , default = False
                        , help='sort output words')
    parser.add_argument('-u', '--uniq', action='store_true'
                        , default = False
                        , help='unique output words')
    parser.add_argument('-ptn', '--pattern8regex', type=str, required=True
                        , help='python regex pattern')
    parser.add_argument('-begin', '--begin_marker', type=str, required=True
                        , help='begin_marker to extract center txt')
    parser.add_argument('-end', '--end_marker', type=str, required=True
                        , help='end_marker to extract center txt')

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

    args = parser.parse_args(args)
    force = args.force
    omode = 'wt' if args.force else 'xt'
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_ifname = args.input
    with open4r(may_ifname, xencoding=iencoding) as fin:
        txt = fin.read()
    txt
    pattern8regex = args.pattern8regex
    begin_marker = args.begin_marker
    end_marker = args.end_marker
    words = grep_between__txt_(pattern8regex, txt, begin_marker, end_marker, to_uniq=args.uniq, to_sort=args.sort)

    to_str = repr if args.repr else str
    may_ofname = args.output
    with open4w(may_ofname, force=force, xencoding=oencoding) as fout:
        for word in map(to_str, words):
            print(word, file=fout)

if __name__ == "__main__":
    main()




__all__
from nn_ns.txt.grep_between import grep_between__txt_, main
from nn_ns.txt.grep_between import *
