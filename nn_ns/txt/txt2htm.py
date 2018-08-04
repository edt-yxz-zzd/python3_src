
from sand import raw_text2html_content, \
     read_txt, write_txt, zh_cn_encoding, is_main



html_tpl = r'''
<!DOCTYPE html>
<html>
<head>
    <meta charset={encoding!r}/>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href={style_css_fname!r} />
    <style type="text/css">
        <!-- body {{ background-color:{{bgcolor}}; }} -->
        <!-- p {{ color:{{fgcolor}}; }} -->
        {styles}
    </style>
</head>

<body>
<p>{content}</p>
</body>
</html>
'''


def text2html(txt, title, *, html_tpl=html_tpl,
              style_css_fname='style.css', styles = '',
              encoding = 'utf-8'):
    content = raw_text2html_content(txt)
    title = raw_text2html_content(title)
    return html_tpl.format(encoding=encoding,
                           title=title,
                           style_css_fname=style_css_fname,
                           styles=styles,
                           content=content)



def txt2htm(txt_fname, htm_fname, *, title, iencoding, oencoding = 'utf-8', **kwargs):
    txt = read_txt(txt_fname, iencoding)
    htm = text2html(txt, title, encoding=oencoding, **kwargs)
    write_txt(htm_fname, htm, oencoding)
    return

def main(args=None):
    import argparse, sys, os.path

    parser = argparse.ArgumentParser(description='convert text to html')
    parser.add_argument('source', type=str, \
                        help='text file name')
    parser.add_argument('destination', type=str, \
                        help='html file name')
    
    parser.add_argument('-t', '--title', type=str, \
                        default = None,
                        help='title of html file')
    
    parser.add_argument('-e', '--encoding', type=str, \
                        default = 'utf-8',
                        help='encoding of both text/html file')
    
    parser.add_argument('-ie', '--iencoding', type=str, \
                        default = None,
                        help='encoding of the input text file')
    
    parser.add_argument('-oe', '--oencoding', type=str, \
                        default = None,
                        help='encoding of the output html file')
    
    parser.add_argument('-css', '--style_css_fname', type=str, \
                        default = 'style.css',
                        help='css fname')
    
    parser.add_argument('-s', '--styles', type=str, \
                        default = '',
                        help='inline css')



    
##    parser.add_argument('-a', '--kwargs', type=str, \
##                        default = {},
##                        help='keyword arguments')




    args = parser.parse_args(args)
    if args.title == None:
        args.title = os.path.basename(args.destination)

    if args.iencoding == None:
        args.iencoding = args.encoding

    if args.oencoding == None:
        args.oencoding = args.encoding

    kwargs = {'style_css_fname':args.style_css_fname, 'styles':args.styles}
    txt2htm(args.source, args.destination,
            title=args.title,
            iencoding=args.iencoding, oencoding = args.oencoding,
            **kwargs)
    
    
def test_text2html():
    txt = 'nhead\n第一卷 偶得仙缘始觉寒\nvolhead\n第一章 精怪\nchaptertxt'
    title = '仙道求索[虫豸]'
    oencoding = 'gbk'
    kwargs = {}
    return text2html(txt, title, encoding=oencoding, **kwargs)

def t1():
    print(test_text2html())
    pass


def test_txt2htm():
    txt_fname = r'E:/download/novel/仙道求索[虫豸].txt'
    htm_fname = r'E:/temp_output/仙道求索[虫豸].htm'
    title = '仙道求索[虫豸]'
    iencoding = 'gbk'
    oencoding = 'gbk'

    
    txt2htm(txt_fname, htm_fname,
            title=title, 
            iencoding=iencoding, oencoding=oencoding)
    return

if is_main(__name__):
    main()



