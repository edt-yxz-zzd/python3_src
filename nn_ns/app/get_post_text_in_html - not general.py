
'''

<td class="t_f" id="postmessage_6976307">
<br>
　　冷小燕听到陌生人一番奇谈怪论，心中莫名得狐疑，这个陌生人不会是从哪<br>
<br>
个精神病院跑出来的吧？可是，裘瑛这个名字确实很熟悉，但是又很陌生，这属<br>
... ...
... ...
情搞掂了，不需要再担心了。他忙说道：“谢谢市长关怀啊！”</td>
'''

import html
from html.parser import HTMLParser
import bs4
from bs4 import BeautifulSoup
import re
import io
import glob





def read_txt(fname, encoding='utf8'):
    #rint(fname, encoding)
    with open(fname, encoding=encoding) as fin:
        return fin.read()
space_rex = re.compile(r'([\s\u3000])')
space_rex = re.compile(r'(\s)')

def get_post_text_in_html(html):
    return get_post_text_in_htmls([html])
def get_post_text_in_htmls(htmls):
    # assume each paragraph beginswith spaces (not EOL)
    posts = []
    for html in htmls:
        posts.extend(step1_get_posts(html))
    paragraphs = step2_strip_and_join(posts)
    paragraphs = step3_remove_spacelines(paragraphs)
    return '\n'.join(paragraphs)
def step1_get_posts(html):
    # @return: [[txt]]
    dom = BeautifulSoup(html, 'lxml')
    return [post.strings for post in dom.find_all('td', class_ = 't_f')]
def step2_strip_and_join(posts):
    # assume each paragraph beginswith spaces (not EOL)
    ls = [[]]
    strip_EOLs = lambda txt: txt.strip('\n\r')
    for txts in posts:
        for txt in txts:
            # if txt[0].isspace():
            txt = strip_EOLs(txt)
            # if space_rex.match(txt):
            if txt[:1].isspace():
                # a new paragraph
                ls.append([])
            ls[-1].append(txt)
    paragraphs = [''.join(txts) for txts in ls]
    return paragraphs
def step3_remove_spacelines(paragraphs):
    return [line for line in paragraphs if line and not line.isspace()]

def read_files(fnames, encoding='utf8'):
    return (read_txt(fname, encoding=encoding) for fname in fnames)
def main(args=None):
    import argparse, sys
    #
    parser = argparse.ArgumentParser(description='get_post_text_in_htmls',
        epilog='example: this.exe thread-1044993-?-*.html thread-1044993-??-*.html  -o xx.txt --output_mode w -ie gb18030')
    parser.add_argument('html_file_names', type=str, nargs='+',
                        help='files to extract text; in glob format')
    parser.add_argument('-o', '--output_file_name', type=str,
                        help='output file name')
    parser.add_argument('-oe', '--output_encoding', type=str,
                        help='output file\'s encoding',
                        default = 'utf8')
    parser.add_argument('-ie', '--input_encoding', type=str,
                        help='all input html files\' encoding',
                        default = 'utf8')
    parser.add_argument('--output_mode', type=str, choices=['x', 'w', 'a'],
                        help='x - fail if existed; w - overwrite; a - append',
                        default = 'x')

    args = parser.parse_args(args)
    html_file_names = args.html_file_names
    output_file_name = args.output_file_name
    input_encoding = args.input_encoding
    output_encoding = args.output_encoding
    output_mode = args.output_mode
    fnames = []
    for fname in html_file_names:
        fnames.extend(glob.glob(fname))

    # html_file = 'thread-1044993-*-*.html'
    # gb18030
    html_fnames = fnames
    htmls = read_files(html_fnames, encoding=input_encoding)
    txt = get_post_text_in_htmls(htmls)
    fout = None # sys.stdout
    if output_file_name is not None:
        fout = open(output_file_name, output_mode, encoding=output_encoding)
    try:
        print(txt, file=fout)
    except:
        if output_file_name is not None:
            fout.close()
        raise
    parser.exit(0)
if __name__ == '__main__':
    #main('thread-1044993-?-*.html thread-1044993-??-*.html  -o xx.txt --output_mode w -ie gb18030'.split())
    main()



