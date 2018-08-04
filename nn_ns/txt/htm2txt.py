'''
#glob_cmd | line_filter_cmd | sort_lines_cmd | extract_data_cmd nn_ns.filedir._extractor_example.main --encoding=utf8
glob_cmd | line_filter_cmd | sort_lines_cmd | extract_data_cmd nn_ns.txt.htm2txt.main --encoding=utf8


glob_cmd ./*.html | line_filter_cmd 3-(\d+)\.html --group_names 1 --INT_GROUP | sort_lines_cmd --line_type=KEY_LINE | extract_data_cmd -oe gbk -o ./3(1+2).txt nn_ns.txt.htm2txt.main --encoding=utf8
'''
__all__ = '''
    htm2txt
    '''.split()

from bs4 import BeautifulSoup

def htm2txt(fout, fin):
    html_doc = fin
    soup = BeautifulSoup(html_doc, 'html.parser')
    def oprint(s):
        print(s, file=fout)
    def node2str(e):
        return '\n'.join(e.stripped_strings)
        return ' '.join(e.stripped_strings)
        return e.string

    oprint('\n'*3)
    may_title = soup.title.string
    title = '' if may_title is None else may_title
    oprint('>'*6 + title)
    oprint('='*16)
    #for e in soup.find_all('h1 h2 h3 h4 h5 h6'.split()): oprint(node2str(e))
    oprint(node2str(soup.head))
    oprint('-'*16)
    #for e in soup.find_all('p div'.split()): oprint(node2str(e))
    oprint(node2str(soup.body))
    oprint('\n'*3)

extract_txt = htm2txt
def extract_txt__fpath(fout, html_fpath, encoding):
    with open(html_fpath, encoding=encoding) as html_doc:
        extract_txt(fout, html_doc)
    return
#main = extractor = extract_txt__fpath
def main(fout, path, encoding):
    # since "--encoding = a b c" will be {encoding:[a, b, c]}
    encoding_ls = encoding
    if not encoding_ls:
        encoding = 'utf8'
    else:
        [encoding] = encoding_ls
    return extract_txt__fpath(fout, path, encoding)


