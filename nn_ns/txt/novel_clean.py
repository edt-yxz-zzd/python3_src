
r'''
#######################################
usage:
    optional:
      #########
      > file2all_char_set -e gb18030 -i the_novel.txt -o 0.txt -u
      > nongbk -i the_novel.txt -o 0.txt -e gb18030 -r
        # covert gb18030 to gbk by replacing non_gbk char by \UXXXXxxxx
        # now below encoding can use gbk instead of gb18030
      #########

  > novel_clean -i 0.txt -e gb18030 find -oms mspam.txt -oss spamset.txt
    # make "are_spams.txt" whose file foramt is same as of "spamset.txt"
    # file foramt:
    #   #score=...:
    #   {'...'
    #   ,'...'
    #   }
    #   #score=...:
    #   {'...'
    #   ,'...'
    #   }
    #
    # first round: content comes from "spamset.txt"
  > novel_clean -i 0.txt -e gb18030 clean -iss are_spams.txt -o 1.txt


  > remove are_spams.txt

    # make "are_spams.txt" whose file foramt is same as of "spamset.txt"
    # other rounds: content comes from "spamset.txt" and "mspam.txt"
    #   "are_spams.txt": update - inrease only
    #   turn-on: "-f"
    #
    #infinite loop:
    #   input file is always "1.txt"
    #   output file is always "2.txt"
  > novel_clean -i 1.txt -e gb18030 -f find -oms mspam.txt -oss spamset.txt
  > novel_clean -i 1.txt -e gb18030 -f clean -iss are_spams.txt -o 2.txt


#######################################
algo:
1) detect which line in novel contains spam
    e.g.
    * well-formatted
        <tag>...</tag>
        [www.....]
    * inline
        WwW. xxx .Com
    * maybe
        [
        &#23435
2) classify lines/spams by score
3) output to file in line format:
    -os     # output_spam_infos
        f'#score={score}:'
        f'{lineno}:{spam!r}'
    -oss    # output_spam_set
        f'#score={score}:'
        f'{{{head_spam!r}'
        f',{spam!r}'
        '}'
    -oms    # output_maybe_spams
        f'#score={score}:'
        f'{lineno}#{line!r}'

4) usr delete nonspam line in the output file "-oss"
    or make a new "are_spams.txt" file of same format
5) using the result file to clean the novel
'''
epilog_str = __doc__

__all__ = '''
    main
    '''.split()

import re
from collections import defaultdict
from ast import literal_eval
from seed.io.may_open import may_open_stdin, may_open_stdout
from seed.text.make_strings_pattern import make_strings_pattern
import sys


class FullWidthRegexPatternInsideBracket:
    digits = r"０-９"
    lowers = r"ａ-ｚ"
    uppers = r"Ａ-Ｚ"
    puncts = r"‘’“”々～‖∶＂＇｀｜〃〔〕〈〉《》「」『』．〖〗【】（）［］｛｝。，、；：？！…—·ˉˇ¨"


html_tag_spam_pattern = r"<[^</>][^<>]{,50}>[^<>]{,100}</[^<>]{,20}>|<!--(?:(?!-->).){,100}-->"
html_tag_pattern = r"<[^</>][^<>]*>[^<>]*</[^<>]*>|<!--.*?-->"
bracket_spam_pattern = r"[\[［][^\[\]［］]{,100}[］\]]"
bracket_pattern = r"[\[［][^\[\]［］]*[］\]]"
spam_line_pattern = r"[wWｗＷ]{3}|[tTｔＴ][xXｘＸ][tTｔＴ]|[cCｃＣ][oOｏＯ][mMｍＭ]|[.．][cCｃＣ][cCｃＣ]|&amp;|&gt;|&lt;|amp;|gt;|lt;|&amp|&gt|&lt|&#"
maybe_spam_line_pattern = rf"[\[\](){{}}（）［］〖〗【】｛｝.#&<>]|{spam_line_pattern!s}" # if contains

parenthesis_pattern = r"[(（][^(（）)]*[）)]|【[^【】]*】|〖[^〖〗]*〗"


html_tag_and_bracket_and_parenthesis_maybespam_pattern = f"({html_tag_pattern}|{bracket_pattern}|{parenthesis_pattern})"
html_tag_and_bracket_spam_pattern = f"({html_tag_spam_pattern}|{bracket_spam_pattern})"
html_tag_and_bracket_and_parenthesis_maybespam_rex = re.compile(html_tag_and_bracket_and_parenthesis_maybespam_pattern)
html_tag_and_bracket_spam_rex = re.compile(html_tag_and_bracket_spam_pattern)
    # split: require capture"()"
maybe_spam_line_rex = re.compile(maybe_spam_line_pattern)
    # search: whether contains
spam_line_rex = re.compile(spam_line_pattern)

def find_spam(line):
    # String -> (spam_line_score:UInt, [(Score, SpamSubstring)])
    # UInt for spam_line_score:
    #   0 - not spam line
    #   >0 - maybe spame line
    # Score:
    #   score of spam > 0
    #   score of maybe spam < 0
    # result may be:
    #   (spam_line_score=[0|1|2], [])
    #   (spam_line_score=[1|2], [...])

    maybe_spam_line = maybe_spam_line_rex.search(line) is not None
    if not maybe_spam_line:
        spam_line_score = 0
        return (0, [])

    spam_line_score = 1 + (spam_line_rex.search(line) is not None)

    ls = html_tag_and_bracket_and_parenthesis_maybespam_rex.split(line)
    assert ls
    L = len(ls)
    assert L & 1 # odd

    if L == 1:
        return (spam_line_score, [])

    maybe_spams = ls[1::2]
    assert maybe_spams
    lineno_spam_pairs = [] # [(score, maybe_spam)]
    for maybe_spam in maybe_spams:
        assert maybe_spam
        head = maybe_spam[0]
        if html_tag_and_bracket_spam_rex.fullmatch(maybe_spam):
            spam = maybe_spam
            if head == '<':
                score = 6
            elif head in '[':
                score = 5
            elif head in '［':
                score = 1
            else:
                raise logic-error-unknown-case
            lineno_spam_pairs.append((score, spam))
        else:
            if head == '<':
                score = -1
            elif head in '[':
                score = -2
            elif head in '(':
                score = -3
            elif head in '（':
                score = -4
            elif head in '［':
                score = -5
            elif head in '〖【':
                score = -6
            else:
                raise logic-error-unknown-case
            lineno_spam_pairs.append((score, maybe_spam))
    return spam_line_score, lineno_spam_pairs


def classify_spams(lineno_line_pairs):
    # Iter (Int, String) -> (score2lineno_line_pairs:Map UInt [(Int, String)], Map Score [(Int, SpamSubstring)])
    score2lineno_line_pairs = defaultdict(list)
    score2lineno_spam_pairs = defaultdict(list)
    for lineno, line in lineno_line_pairs:
        spam_line_score, score_spam_pairs = find_spam(line)
        if not spam_line_score: continue

        if not score_spam_pairs or spam_line_score > 1:
            #print(f'{lineno}#{line!r}', file=fout)
            score2lineno_line_pairs[spam_line_score].append((lineno, line))
            continue

        for score, spam in score_spam_pairs:
            #print(f'{lineno}:{spam!r}', file=fout)
            score2lineno_spam_pairs[score].append((lineno, spam))

    score2lineno_spam_pairs = dict(score2lineno_spam_pairs)
    score2lineno_line_pairs = dict(score2lineno_line_pairs)
    return score2lineno_line_pairs, score2lineno_spam_pairs


def output_maybe_spams(fout_maybe_spam, score2lineno_line_pairs):
    it = iter(sorted(score2lineno_line_pairs.items(), reverse=True))
    for score, lineno_maybe_spam_line_pairs in it:
        print(f'#score={score}:', file=fout_maybe_spam)
        for lineno, line in lineno_maybe_spam_line_pairs:
            print(f'{lineno}#{line!r}', file=fout_maybe_spam)

def output_spam_infos(fout_spam_info, score2lineno_spam_pairs):
    it = iter(sorted(score2lineno_spam_pairs.items(), reverse=True))
    for score, lineno_spam_pairs in it:
        if not lineno_spam_pairs: continue

        print(f'#score={score}:', file=fout_spam_info)
        for lineno, spam in lineno_spam_pairs:
            print(f'{lineno}:{spam!r}', file=fout_spam_info)

def output_spam_set(fout_spam_set, score2lineno_spam_pairs):
    it = iter(sorted(score2lineno_spam_pairs.items(), reverse=True))
    for score, lineno_spam_pairs in it:
        if not lineno_spam_pairs: continue

        print(f'#score={score}:', file=fout_spam_set)
        spam_set = {spam for lineno, spam in lineno_spam_pairs}
        spam_list = sorted(sorted(spam_set), key=len)
        it = iter(spam_list)
        for head_spam in it:
            break
        else:
            raise logic-error
        print(f'{{{head_spam!r}', file=fout_spam_set)
        for spam in it:
            print(f',{spam!r}', file=fout_spam_set)
        print('}', file=fout_spam_set)




def main_func(fout_spam_info, fout_spam_set, fout_maybe_spam, lineno_line_pairs):
    # was not called actually; here to given the big-picture only
    score2lineno_line_pairs, score2lineno_spam_pairs = \
                classify_spams(lineno_line_pairs)
    output_spam_infos(fout_spam_info, score2lineno_spam_pairs)
    output_spam_set(fout_spam_set, score2lineno_spam_pairs)
    output_maybe_spams(fout_maybe_spam, score2lineno_line_pairs)


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='clean novel text.'
        , epilog=epilog_str
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-e', '--encoding', type=str
                            , default='utf8'
                            , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                            , default = False
                            , help='open mode for output file')
    parser.add_argument('-i', '--input', type=str
                            , help='path to the input novel text file')


    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')

    parser_find = subparsers.add_parser('find', help='find spams')
    parser_clean = subparsers.add_parser('clean', help='clean spams')

    mk_parser_find(parser_find)
    mk_parser_clean(parser_clean)

    args = parser.parse_args(argv)

    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    if args.subcommand == 'find':
        main_find(args, omode, encoding)
    elif args.subcommand == 'clean':
        main_clean(args, omode, encoding)
    else:
        raise Exception('should choose one subcommand: "find"/"clean"')
        raise logic-error




def mk_parser_find(parser_find):
    parser_find.add_argument('-os', '--output_spam_infos', type=str
                            , help='(optional) path to output file to write spam info')
    parser_find.add_argument('-oss', '--output_spam_set', type=str
                            , help='path to output file to write spams')
    parser_find.add_argument('-oms', '--output_maybe_spams', type=str
                            , help='path to output file to write maybe_spam info')


def main_find(args, omode, encoding):
    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        # see: main_func
        lineno_line_pairs = enumerate(fin)
        score2lineno_line_pairs, score2lineno_spam_pairs = \
                    classify_spams(lineno_line_pairs)

    may_ofname = args.output_spam_infos
    if may_ofname is not None:
        # since output_spam_set export enough info
        with open(may_ofname, omode, encoding=encoding) as fout_spam_info:
            # see: main_func
            output_spam_infos(fout_spam_info, score2lineno_spam_pairs)

    may_ofname = args.output_spam_set
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout_spam_set:
        # see: main_func
        output_spam_set(fout_spam_set, score2lineno_spam_pairs)

    may_ofname = args.output_maybe_spams
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout_maybe_spam:
        # see: main_func
        output_maybe_spams(fout_maybe_spam, score2lineno_line_pairs)



def mk_parser_clean(parser_clean):
    #parser_clean.add_argument('-is', '--input_spam_infos', type=str
    #                       , required=True
    #                       , help='path to input file to read spam info')
    parser_clean.add_argument('-iss', '--input_spam_set', type=str
                            , required=True
                            , help='path to input file to read spams')
    #parser_clean.add_argument('-ims', '--input_maybe_spams', type=str
    #                       , help='path to input file to read maybe_spam info')
    parser_clean.add_argument('-o', '--output', type=str
                            , help='path to output file to write cleaned novel')

def main_clean(args, omode, encoding):
    '''
    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        lines = list(fin)

    ifname = args.input_spam_infos
    bad_foramt = Exception(f'bad format: input_spam_infos:"{ifname!r}"')
    with open(ifname, 'rt', encoding=encoding) as fin:
        for line in fin:
            line = line.strip()
            if not line or line[0] == '#': continue

            #f'#score={score}:'
            #f'{lineno}:{spam!r}'
            str_lineno, sep, repr_spam = line.partition(':')
            if not sep: raise bad_foramt

            lineno = int(str_lineno)
            spam = literal_eval(repr_spam)
            if type(spam) is not str: raise bad_foramt

            # update: remove spam
            lines[lineno] = ''.join(lines[lineno].split(spam))

    txt = ''.join(lines)
    '''

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()

    ifname = args.input_spam_set
    bad_foramt = Exception(f'bad format: input_spam_set:"{ifname!r}"')
    with open(ifname, 'rt', encoding=encoding) as fin:
        repr_spam_sets = fin.read()
    repr_spam_sets = re.split(f'(?m)^#score=.*?:$', repr_spam_sets)
    assert repr_spam_sets
    try:
        if repr_spam_sets[0].strip(): raise bad_foramt
    except:
        print(repr(repr_spam_sets[0]), file=sys.stderr)
        raise
    all_spam_set = set()
    for repr_spam_set in repr_spam_sets[1:]:
        spam_set = literal_eval(repr_spam_set)
        if type(spam_set) is not set: raise bad_foramt
        all_spam_set |= spam_set
    if not all_spam_set:
        print("no spam at all", file=sys.stderr)
        return

    for spam in all_spam_set:
        if type(spam) is not str: raise bad_foramt
        #txt = ''.join(txt.split(spam))
    #bug:
    #   patterns = map(re.escape, all_spam_set)
    #   pattern = '|'.join(patterns)
    # should sort pattern from longest to shortest
    pattern = make_strings_pattern(all_spam_set)
    assert pattern
    txt = ''.join(re.split(pattern, txt))


    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        #for line in lines: fout.write(line)
        fout.write(txt)
    return


if __name__ == '__main__':
    main()

