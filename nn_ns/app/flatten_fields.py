#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/flatten_fields.py
e ../../python3_src/nn_ns/app/transpose_fields.py

py -m nn_ns.app.flatten_fields
py -m nn_ns.app.debug_cmd   nn_ns.app.flatten_fields -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.flatten_fields:__doc__ -ht # -ff -df
#######

[[
come_from:
    view others/数学/prime/Carmichael_numbers.txt

eg:
561=3x11x17, 15841=7x31x73, 101101=7x11x13x101, 
1105=5x13x17, 29341=13x37x61, 115921=13x37x241, 
1729=7x13x19, 41041=7x11x13x41, 126217=7x13x19x73, 
... ...

==>>:
561=3x11x17
1105=5x13x17
1729=7x13x19
...
15841=7x31x73
29341=13x37x61
...
101101=7x11x13x101
...

]]
[[
view others/app/termux/help/cmd_intro.man1.20251130-group.txt
cut
  echo $'a,b,c\n0,1,2\nx_x,y-y\n999,\n###' | cut -s -d, -f1
  echo $'a,b,c\n0,1,2\nx_x,y-y\n999,\n###' | cut -s -d, -f2
一栏一栏地提取...
太麻烦

]]



'#'; __doc__ = r'#'
>>>


[[
concat_column6file
echo $'a, b\n000,999' | concat_column6file --regex8sep ', *'
    a
    000
    b
    999
]]

[[
echo $'a, b\n000,999'
    a, b
    000,999

echo $'a, b\n000,999' | py -m nn_ns.app.flatten_fields --regex8sep ', *'
    a
    000
    b
    999

echo $'a, b\n000,999' | py -m nn_ns.app.flatten_fields --regex8sep ', *' --replacemant4sep=';'
    a
    000
    ;b
    ;999

echo $'a, b\n000,' | py -m nn_ns.app.flatten_fields --regex8sep ', *'
    a
    000
    b
    <BLANK>

echo $'a, b\n000' | py -m nn_ns.app.flatten_fields --regex8sep ', *'
    ^NotImplementedError: to_transpose but not aligned

echo $'a, b\n000' | py -m nn_ns.app.flatten_fields --regex8sep ', *' --default_field '666xxx999'
    a
    000
    b
    666xxx999

echo $'a, b\n000' | py -m nn_ns.app.flatten_fields --regex8sep ', *' --regex8ignore_line '000\n?'
    a
    b





cat <<END
a, b
000,999
END

==>>:
    a, b
    000,999




py -m nn_ns.app.flatten_fields --regex8sep ', *' --default_field '666xxx999' <<END
a, b
000
END

==>>:
    a
    000
    b
    666xxx999

]]


py_adhoc_call   nn_ns.app.flatten_fields   @f
from nn_ns.app.flatten_fields import *
]]]'''#'''
__all__ = r'''
flatten_fields6file_
main
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.for_libs.for_re import mk_regex5or_pattern_
    from seed.for_libs.for_re___split import split as asif_re__split_, iter_split as iter_asif_re__split_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#def split_line_(regex8sep, /):
#def flatten_fields6path_(*, ipath, opath, regex8ignore_line, regex8sep, replacemant4sep='', to_transpose=True, force=False):
def flatten_fields6file_(*, ifile, ofile, regex8sep, may_regex8ignore_line=None, replacemant4sep='', may_default4nonexisted_field=None, nonexisted_field_ok=True, to_transpose=True):
    #########################
    regex8sep = mk_regex5or_pattern_(regex8sep)
    if not None is may_regex8ignore_line:
        regex8ignore_line = may_regex8ignore_line
        regex8ignore_line = mk_regex5or_pattern_(regex8ignore_line)
        skip_ = regex8ignore_line.fullmatch
    else:
        def skip_(line, /):
            return False
    skip_
    regex8sep



    #########################
    skip_
    regex8sep
    fieldss = []
    for line in ifile:
        if skip_(line):continue
        s = line.removesuffix('\n')
        fields = asif_re__split_(regex8sep, s)
        fieldss.append(fields)
    fieldss

    #########################
    fieldss
    nonexisted_field_ok

    max_num_fields_per_line = max(map(len, fieldss), default=0)
    min_num_fields_per_line = min(map(len, fieldss), default=0)
    if not nonexisted_field_ok and min_num_fields_per_line < max_num_fields_per_line:raise Exception(min_num_fields_per_line, max_num_fields_per_line)

    #########################
    fieldss
    replacemant4sep

    if replacemant4sep:
        for fields in fieldss:
            for j in range(1, len(fields)):
                fields[j] = replacemant4sep +fields[j]
    fieldss


    #########################
    fieldss
    may_default4nonexisted_field
    min_num_fields_per_line
    max_num_fields_per_line


    whether_aligned = min_num_fields_per_line == max_num_fields_per_line

    if not None is may_default4nonexisted_field and not whether_aligned:
        whether_aligned = True
        default4nonexisted_field = may_default4nonexisted_field
        for fields in fieldss:
            sz = max_num_fields_per_line - len(fields)
            if sz:
                fields += [default4nonexisted_field]*sz
        whether_aligned = True
        assert max_num_fields_per_line == min(map(len, fieldss), default=0)
        assert max_num_fields_per_line == max(map(len, fieldss), default=0)
    fieldss
    whether_aligned
    if whether_aligned:
        num_fields_per_line = max_num_fields_per_line

    #########################
    fieldss
    whether_aligned
    if to_transpose:
        if not whether_aligned:raise NotImplementedError('to_transpose but not aligned')
        num_fields_per_line
        mx = [[] for _ in range(num_fields_per_line)]
        for fields in fieldss:
            for row, field in zip(mx, fields):
                row.append(field)
        mx
    else:
        mx = fieldss
    mx



    #########################
    mx

    for row in mx:
        for z in row:
            print(z, file=ofile)

    #########################
    return


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='concat column by column'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )


    parser.add_argument('--regex8sep', type=str, required=True
                        , help='regex to search delimiter for fields')
    parser.add_argument('--regex8ignore_line', type=str, default=None
                        , help='regex used to identify lines that should be skipped')
    parser.add_argument('--replacemant4sep', type=str, default=''
                        , help='initial text for non-first field')
    parser.add_argument('--default_field', type=str, default=None
                        , help='default text for missing field')
    parser.add_argument('--disallow_missing_field', action='store_true'
                        , default = False
                        , help='halt if field missing')
    parser.add_argument('--no_transpose', action='store_true'
                        , default = False
                        , help='concat row by row')




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
    may_ofname = args.output
    with (may_open_stdin(may_ifname, 'rt', encoding=iencoding) as ifile, may_open_stdout(may_ofname
        , omode, encoding=oencoding) as ofile):
        flatten_fields6file_(ifile=ifile, ofile=ofile, may_regex8ignore_line=args.regex8ignore_line, regex8sep=args.regex8sep, replacemant4sep=args.replacemant4sep, may_default4nonexisted_field=args.default_field, nonexisted_field_ok=not args.disallow_missing_field, to_transpose=not args.no_transpose)



if __name__ == '__main__':
    main()


__all__
from nn_ns.app.flatten_fields import *
