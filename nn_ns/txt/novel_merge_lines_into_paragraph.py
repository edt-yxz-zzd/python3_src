
'''
which line not to be merge?
    e.g. title
which line are transparent?
    e.g. empty line or spaces line
(not) to merge which line with next line?
    e.g. not end by punct and length > 50
(not) to merge which line with prev line?
    e.g. not begin with space+


'''

__all__ = '''
    main
    '''.split()


import re
from enum import Enum, unique
from seed.io.may_open import may_open_stdin, may_open_stdout



@unique
class LineCase(Enum):
    Transparent = 'Transparent'
    NotMerge = 'NotMerge'
    MergeToNext = 'MergeToNext'
    MayMergeToPrev = 'MayMergeToPrev'

@unique
class PatternCase(Enum):
    '''
XxxT: regex pattern for match
XxxF: regex pattern for not match
'''
    # fullmatch
    WholeT = 'WholeT'
    WholeF = 'WholeF'
    # search
    SubstringT = 'SubstringT'
    SubstringF = 'SubstringF'
    # match
    PrefixT = 'PrefixT'
    PrefixF = 'PrefixF'
    # reversed regex pattern
    ReversedSuffixT = 'ReversedSuffixT'
    ReversedSuffixF = 'ReversedSuffixF'



def novel_merge_lines_into_paragraph__pattern(
    not_merge_pattern
    , transparent_pattern # e.g. "(?m)^\s*$"
    , case_pattern_pairs_for_merge_to_next
    , lines
    ):
    # not_merge_pattern :: regex pattern for not match
    # transparent_pattern :: regex pattern
    # case_pattern_pairs :: Iter (PatternCase, Pattern)
    # lines :: Iter str
    # -> Iter (LineCase, line)
    compile = re.compile
    pairs_next = ((case, compile(pattern))
                    for case, pattern in case_pattern_pairs_for_merge_to_next)
    return novel_merge_lines_into_paragraph__regex(
                compile(not_merge_pattern)
                , compile(transparent_pattern)
                , pairs_next
                , lines
                )

def reverse_line(line):
    return ''.join(reversed(line))
def do_line_match(line, case_regex_pairs):
    may_rline = None
    def get_rline():
        nonlocal may_rline
        if may_rline is None:
            may_rline = reverse_line(line)
        return may_rline

    for case, regex in case_regex_pairs:
        if case == PatternCase.WholeF:
            if regex.fullmatch(line): return False
        elif case == PatternCase.WholeT:
            if not regex.fullmatch(line): return False
        elif case == PatternCase.SubstringF:
            if regex.search(line): return False
        elif case == PatternCase.SubstringT:
            if not regex.search(line): return False
        elif case == PatternCase.PrefixF:
            if regex.match(line): return False
        elif case == PatternCase.PrefixT:
            if not regex.match(line): return False
        elif case == PatternCase.ReversedSuffixF:
            if regex.match(get_rline()): return False
        elif case == PatternCase.ReversedSuffixT:
            if not regex.match(get_rline()): return False
        else:
            raise unknown-case
    return True

def novel_merge_lines_into_paragraph__regex(
    not_merge_regex
    , transparent_regex # e.g. "(?m)^\s*$"
    , case_regex_pairs_for_merge_to_next
    , lines
    ):
    fullmatch = re.fullmatch
    search = re.search
    match = re.match

    case_regex_pairs_for_merge_to_next = tuple(case_regex_pairs_for_merge_to_next)
    for line in lines:
        if line[-1:] == '\n':
            line = line[:-1]
        assert not line or line[-1] != '\n'

        if transparent_regex.fullmatch(line):
            yield LineCase.Transparent, line
            continue
        elif not_merge_regex.fullmatch(line):
            yield LineCase.NotMerge, line
            continue
        merge_to_next = not do_line_match(
                                line, case_regex_pairs_for_merge_to_next)
        if merge_to_next:
            yield LineCase.MergeToNext, line
            continue
        yield LineCase.MayMergeToPrev, line

def merge_case_line_pairs(case_line_pairs):
    # Iter (LineCase, line) -> Iter line
    lines = []
    def join():
        if lines:
            r = ''.join(line.strip() for line in lines)
            lines.clear()
            return r
        return None

    for case, line in case_line_pairs:
        if case == LineCase.Transparent:
            continue
        elif case == LineCase.NotMerge:
            if lines: yield join()
            lines.append(line)
            yield join()
            continue
        elif case == LineCase.MergeToNext:
            lines.append(line)
            continue
        elif case == LineCase.MayMergeToPrev:
            lines.append(line)
            yield join()
            continue
        else:
            raise unknown-case
    if lines: yield join()
    assert not lines
    return

class GlobalArgsExample:
    not_merge_pattern = r'\s*[【第].*'
    transparent_pattern = r'\s*'
    case_pattern_pairs = \
        [(PatternCase.ReversedSuffixF, r'(?:[,;「『〖【《、，；“‘]|\w).{,50}')
        #[(PatternCase.ReversedSuffixF, r'(?:[,;「『〖【《、，；“‘]|\w).{30,50}')
        ]


def main(argv = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='merge lines into paragraph for novel text')
    parser.add_argument('-i', '--input', type=str
                        , default=None
                        , help='input file name')
    parser.add_argument('-o', '--output', type=str
                        , default=None
                        , help='output file name')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='encoding of input/output file')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        case_line_pairs = novel_merge_lines_into_paragraph__pattern(
                            GlobalArgsExample.not_merge_pattern
                            , GlobalArgsExample.transparent_pattern
                            , GlobalArgsExample.case_pattern_pairs
                            , iter(fin)
                            )
        case_line_pairs = list(case_line_pairs)

    #print(case_line_pairs)
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        for line in merge_case_line_pairs(case_line_pairs):
            print(line, file=fout)

if __name__ == "__main__":
    main()



