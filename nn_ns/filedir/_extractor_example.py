
'''
glob_cmd | line_filter_cmd | sort_lines_cmd | extract_data_cmd nn_ns.filedir._extractor_example.main --encoding=utf8
'''

from bs4 import BeautifulSoup

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
#main = extractor = extract_txt__fpath
def main(fout, path, encoding):
    # since "--encoding = a b c" will be {encoding:[a, b, c]}
    encoding_ls = encoding
    if not encoding_ls:
        encoding = 'utf8'
    else:
        [encoding] = encoding_ls
    return extract_txt__fpath(fout, path, encoding)







