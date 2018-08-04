
titles_with_page_file_format = r'''
# comment = regex"#.*#|#" #
# title_page = regex"(?P<title>.*) (?P<content_page>[+-]?\d+)" ; note the middle space #
# empty_line = regex"" #
# command = regex"@.*@" #

# content_page = 3 # see below "上篇：集异璧GEB" #
# bookmark.page index = 38 # begin from 0 #
# offset = bookmark.page - content_page = 38 - 3 = 35 #
# @offset=[+-]?\d+([+-]\d+)?@ # appear anywhere anytimes ; add to baseoffset #


@offset=24-20@
作者为中文版所写的前言 1
译校者的话 15
概览 20
插图目示 30

@offset=34-1@
目录 1
@offset=37-1@
鸣谢 1

上篇：集异璧GEB 3
'''

'''
<?xml version="1.0" encoding="UTF-8"?>
<content>
<bookmarks>
<bookmark title="封面" type="2" page="0" offset-x="0" offset-y="2335" margin="0" />
<bookmark title="概览" type="2" page="23" offset-x="0" offset-y="2165" margin="0" />
</bookmarks>
</content>
'''


import xml.etree.ElementTree as ET
import re
from seed.excepts.all import ParseError
from .reorder_WinDjView_bookmarks import xml_root_str2bytes


re_offset = re.compile(r'^@offset=([+-]?\d+(?:[+-]\d+)?)@$')
re_title_page = re.compile(r'^(?P<title>.*?) (?P<content_page>[+-]?\d+)$')
assert re_title_page.match('a b 3')


__default_bookmark_attrs = {
    'type': 2,
    'offset-x': 0,
    'offset-y': 0,
    'margin': 0
    }
def dict_value_map(d, f):
    return dict((k, f(v)) for k, v in d.items())
__default_bookmark_attrs = dict_value_map(__default_bookmark_attrs, str)


#assert bookmark.tail == '\n'
#assert bookmarks.text == bookmarks.tail == '\n'
#assert content.text == '\n'
#assert content.tail == None
def new_WinDjView_bookmark_entry(title, page):
    bookmark = ET.Element('bookmark', __default_bookmark_attrs,
                          title=title, page=str(page))
    bookmark.tail = '\n'
    return bookmark
def new_WinDjView_bookmarks_root():
    content = ET.Element('content')
    bookmarks = ET.Element('bookmarks')
    content.append(bookmarks)
    bookmarks.text = '\n'
    bookmarks.tail = '\n'
    content.text = '\n'
    return content
def title_page_pairs2WinDjView_bookmarks_root(title_page_pairs):
    content = new_WinDjView_bookmarks_root()
    bookmarks, = content
    bookmarks.extend(new_WinDjView_bookmark_entry(title, page)
                      for title, page in title_page_pairs)
    return content


# see : reorder_WinDjView_bookmarks.xml_root_str2bytes
def generate_WinDjView_bookmarks_root_str(titles_with_page_file, base_offset):
    content = generate_WinDjView_bookmarks_root(titles_with_page_file, base_offset)
    #return '\n'.join(ET.tostringlist(content, encoding='unicode'))
    return ET.tostring(content, encoding='unicode')
def generate_WinDjView_bookmarks_root(titles_with_page_file, base_offset):
    ls = []
    offset = base_offset
    def error():
        return ParseError(line_no, line)
    for line_no, line in enumerate(titles_with_page_file):
        if line[-1] == '\n':
            line = line[:-1]
        if not line: continue
        if line[-1] not in '#@':
            m = re_title_page.match(line)
            if not m:
                raise error()
            ls.append((m.group('title'), int(m.group('content_page')) + offset))
        elif line[-1] != line[0]:
            raise error()
        elif line[-1] == '#':
            # comment
            pass
        elif line[-1] == '@':
            m = re_offset.match(line)
            if not m:
                raise error()
            new_offset = eval(m.group(1))
            offset = base_offset + new_offset
    return title_page_pairs2WinDjView_bookmarks_root(ls)



def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='reorder WinDjView bookmarks')
    parser.add_argument('titles', type=str, help='titles_with_page file (one title per line)')

    parser.add_argument('destination', type=str,
                        help='destination bookmarks file(default to <source>)')
    
    parser.add_argument('-te', '--title_encoding', type=str,
                        default='utf8',
                        help='encoding of titles_with_page file')
    parser.add_argument('-oe', '--output_encoding', type=str,
                        default='utf8',
                        help='encoding of destination bookmarks file')
    parser.add_argument('-b', '--base_offset', type=int,
                        default=0,
                        help='base_offset; bookmark.page = base_offset+offset+page where offset is the latest in titles_with_page file')
    

    args = parser.parse_args(args)

    dst = args.destination

    with open(args.titles, encoding=args.title_encoding) as titles:
        xml_root_str = generate_WinDjView_bookmarks_root_str(titles, args.base_offset)

    
    out = xml_root_str2bytes(xml_root_str, args.output_encoding)
    with open(dst, 'wb') as fout:
        fout.write(out)
    return

    


if __name__ == "__main__":
    main()

    
'''
py -m nn_ns.txt.generate_WinDjView_bookmarks titles_with_page.py out.py -b -2
'''



    
