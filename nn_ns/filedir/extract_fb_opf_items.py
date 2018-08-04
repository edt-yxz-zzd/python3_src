

'''

instead of "glob_cmd | line_filter_cmd | sort_lines_cmd"
    , we can extract sorted fnames directly from "fb.opf".


    extract_fb_opf_items_cmd -i ./fb.opf | extract_data_cmd -oe gbk -o ./3(3-3).txt nn_ns.filedir._extractor_example.main --encoding=utf8
'''


__all__ = '''
    extract_fb_opf_items
    '''.split()



'''
example:
*.epub/
    OPS/
        fb.opf/
            # manifest.item & media-type="application/xhtml+xml"
            #   ==>> href=???
            ...
            <manifest>
            <!-- Content Documents -->
            <item id="main-css" href="css/main.css" media-type="text/css"/>
            <item id="coverpage"  href="coverpage.html"  media-type="application/xhtml+xml"/>
            <item id="chapter1"  href="chapter1.html"  media-type="application/xhtml+xml"/>
            ...
            ...
            <item id="chapter9"  href="chapter9.html"  media-type="application/xhtml+xml"/>

            <item id="ncx"  href="fb.ncx" media-type="application/x-dtbncx+xml"/>
            <item id="css" href="css/main.css" media-type="text/css"/>
            </manifest>

            ...
'''


from bs4 import BeautifulSoup

def extract_fb_opf_items(fout, fin):
    html_doc = fin
    soup = BeautifulSoup(html_doc, 'html.parser')
    def oprint(s):
        print(s, file=fout)

    # manifest.item & media-type="application/xhtml+xml"
    #   ==>> href=???
    attrs = {'media-type': "application/xhtml+xml"}
    for e in soup.manifest.find_all('item', attrs=attrs):
        #bug: oprint(e.href)
        oprint(e['href'])












##########################

def main(argv=None):
    import argparse, sys
    from seed.io.may_open import may_open_stdout, may_open_stdin
    class Globals:
        output_file_encoding = 'utf8'
        input_file_encoding = 'utf8'



    ###################
    parser = argparse.ArgumentParser(description='extract epub/OPS/fb.opf'
        , epilog='''
    extract epub/OPS/fb.opf::manifest.item.href
        where item["media-type"]=="application/xhtml+xml"
''')
    add_argument = parser.add_argument


    add_argument('-i', '--input_file', type=str
        , default=None
        , help='the input file')
    add_argument('-ie', '--input_encoding', type=str
        , default = Globals.input_file_encoding
        , help='the encoding of input file')
    add_argument('-o', '--output_file', type=str
        , default=None
        , help='the output file')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args = parser.parse_args(argv)
    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout\
        , may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        extract_fb_opf_items(fout, fin)

    #parser.exit(0)
    return 0


if __name__ == '__main__':
    main()


