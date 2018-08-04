
r'''
extract text from "六朝清羽记（共31集）和第二部《六朝云龙吟》（1至36集）[1-67含图精校版].epub"
    <title>
    <h3>
    <p>
    <img>

ver1 extract to plain text
ver2 just extract the body, and plug it directly into
    novel_split_tree2html.Node.head
    success:
        # "2gbk....txt" - ver2, gbk encoding
        # "-H"          - raw text are indeed html
        > py extract_txt__ver2_html_body.py .\epub\OPS -o .\"2gbk《六朝清羽记》1-67含图精校版.txt" -oe gbk
        > novel2htm "2gbk《六朝清羽记》1-67含图精校版.txt" 六朝清羽记1_67.htm -e gbk -rs  "(?m)(?<=(?:\n{3}^================$))\n+^(.+)" -H


'''


from bs4 import BeautifulSoup
from glob import iglob
import os.path
import re, sys

class Globals:
    html_basename_glob_pattern = 'chapter*.html'
    html_basename_regex_pattern = r'chapter(?P<idx>\d+)\.html'
    input_file_encoding = 'utf8'
    output_file_encoding = 'utf8'


def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='extract text from html')
    add_argument = parser.add_argument

    add_argument('input_folder', type=str
        , help='the folder which contains htmls to extract')
    add_argument('-o', '--output_file', type=str
        , help='the output file')
    add_argument('-ie', '--input_encoding', type=str
        , default = Globals.input_file_encoding
        , help='the encoding of input html files')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args = parser.parse_args(argv)
    if args.output_file is None:
        if True:
            fout = sys.stdout
            extract_txt__folder(fout
                , args.input_folder, encoding=args.input_encoding)
    else:
        with open(args.output_file, 'x', encoding=args.output_encoding) as fout:
            extract_txt__folder(fout
                , args.input_folder, encoding=args.input_encoding)
    #parser.exit()
    return


def _try():
    fpath = r'E:\download\novel_new\novel_20170808\小说\ooxx\六朝清羽记（共31集）和第二部《六朝云龙吟》（1至36集）[1-67含图精校版]\epub\OPS\chapter357.html'
    fpath = r'E:\download\novel_new\novel_20170808\小说\ooxx\六朝清羽记（共31集）和第二部《六朝云龙吟》（1至36集）[1-67含图精校版]\epub\OPS\chapter410.html'
    pr = print
    encoding = 'utf8'
    with open(fpath, encoding=encoding) as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
        pr(soup.title.string)
        pr(soup.h3)
        for e in soup.find_all(['p', 'img']): # find 'p' or 'img'
            pr(e.name)
            if e.name == 'img': pr(e)
            else:
                pr(e.string)
                pr(list(e.stripped_strings))
                pr(' '.join(e.stripped_strings))
        e = soup.body
        e.name = 'xxx'
        pr(e)

#_try(); raise

def extract_txt(fout, fin):
    html_doc = fin
    soup = BeautifulSoup(html_doc, 'html.parser')
    def oprint(s):
        print(s, file=fout)

    oprint('\n'*3)
    oprint('='*16)
    oprint(soup.title.string)
    oprint(soup.h3)
    oprint('='*16)
    # for e in soup.find_all('p'): oprint(e.string)
    if True:
        body = soup.body
        body.name = 'div'
        oprint(body)
    oprint('\n'*3)


def extract_txt__fpath(fout, html_fpath, encoding):
    with open(html_fpath, encoding=encoding) as html_doc:
        extract_txt(fout, html_doc)
    return
def folder2sorted_html_fpaths(path):
    glob_basename = Globals.html_basename_glob_pattern
    regex_basename = re.compile(Globals.html_basename_regex_pattern)
    glob_pattern = os.path.join(path, glob_basename)

    def eprint(s):
        print(s, file=sys.stderr)
    get_basename = os.path.basename
    fullmatch = regex_basename.fullmatch
    idx2fpath = {}
    for fpath in iglob(glob_pattern):
        basename = get_basename(fpath)
        m = fullmatch(basename)
        if not m:
            eprint(f'??? {fpath!r}')
        idx = int(m['idx'])
        fpath2 = idx2fpath.setdefault(idx, fpath)
        if fpath2 is not fpath:
            cmp = '==' if fpath2 == fpath else '!='
            raise Exception('logic-error? why two fpath has same basename in same folder? \n\t{fpath2!r}\n\t{fpath!r}\n\t{cmp}')
    pairs = sorted(idx2fpath.items())
    if not pairs:
        return pairs
    begin = pairs[0][0]
    end = pairs[-1][0]+1
    if end-begin != len(pairs):
        if end-begin < len(pairs):
            raise logic-error
        eprint('some file indices are missing...')
    return [fpath for idx, fpath in pairs]




def extract_txt__folder(fout, path, encoding):
    sorted_fpaths = folder2sorted_html_fpaths(path)
    for fpath in sorted_fpaths:
        extract_txt__fpath(fout, fpath, encoding=encoding)
    return


if __name__ == '__main__':
    main()


