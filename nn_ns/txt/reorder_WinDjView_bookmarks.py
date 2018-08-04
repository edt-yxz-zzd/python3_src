
'''
WinDjView_bookmarks


list, not tree
new bookmark always appended as last
newline must be 0A, not 0D0A
    // convert 0D0A -> 0A
    sub xxx.bookmarks -f "" // i.e. py -m nn_ns.txt.txt_replace xxx.bookmarks -f ""



fields:
    title, page, offset-y

<?xml version="1.0" encoding="UTF-8"?>
<content>
<bookmarks>
<bookmark title="封面" type="2" page="0" offset-x="0" offset-y="2335" margin="0" />
<bookmark title="概览" type="2" page="23" offset-x="0" offset-y="2165" margin="0" />
</bookmarks>
</content>
'''

from seed.text.encodings import to_std_encoding

import io
import xml.etree.ElementTree as ET
from collections.abc import Sequence

bookmarks_src = '''\
<?xml version="1.0" encoding="UTF-8"?>
<content>
<bookmarks>
<bookmark title="封面" type="2" page="0" offset-x="0" offset-y="2335" margin="0" />
<bookmark title="概览" type="2" page="23" offset-x="0" offset-y="2165" margin="0" />
</bookmarks>
</content>
'''

def xml_root_str2bytes(xml_root_str, encoding='utf8'):
    decl = '<?xml version="1.0" encoding="{}"?>\n'.format(to_std_encoding(encoding))
    return (decl + xml_root_str).encode(encoding)

bookmarks_file = io.StringIO(bookmarks_src)
sorted_titles = ['概览', '封面']
def reorder_WinDjView_bookmarks(bookmarks_file, sorted_titles):
    'return xml_root_str'
    #assert isinstance(sorted_titles, Sequence)

    tree = ET.parse(bookmarks_file)
    content = tree.getroot() 
    assert content.tag.lower() == "content"
    bookmarks, = content
    assert bookmarks.tag.lower() == "bookmarks"
    assert all(bookmark.tag.lower() == "bookmark" for bookmark in bookmarks)
    assert (set(bookmark.attrib['title'] for bookmark in bookmarks)
               == set(sorted_titles))

    title2index = dict((t,i) for i,t in enumerate(sorted_titles))
    bookmark_ls = list(bookmarks)
    bookmark_ls = sorted(bookmark_ls,
                         key=lambda bookmark: title2index[bookmark.attrib['title']])
    for i, bookmark in enumerate(bookmark_ls):
        bookmarks[i] = bookmark
        # print(repr(bookmark.tail)) == '\n'

    #assert bookmark.tail == '\n'
    #assert bookmarks.text == bookmarks.tail == '\n'
    #assert content.text == '\n'
    #assert content.tail == None
    s = ET.tostring(content, encoding='unicode')
    return s

r = reorder_WinDjView_bookmarks(bookmarks_file, sorted_titles)




    

def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='reorder WinDjView bookmarks')
    parser.add_argument('titles', type=str, help='ordered titles file (one title per line)')
    parser.add_argument('source', type=str, help='source bookmarks file')

    parser.add_argument('destination', type=str,
                        nargs='?', default=None,
                        help='destination bookmarks file(default to <source>)')
    
    parser.add_argument('-te', '--title_encoding', type=str,
                        default='utf8',
                        help='encoding of titles file')
    parser.add_argument('-oe', '--output_encoding', type=str,
                        default='utf8',
                        help='encoding of destination bookmarks file')
    

    args = parser.parse_args(args)


    src = args.source
    dst = args.destination
    if dst == None:
        dst = src
    sorted_titles = []
    with open(args.titles, encoding=args.title_encoding) as titles:
        for line in titles:
            if line[-1] == '\n':
                line = line[:-1]
            sorted_titles.append(line)

    xml_root_str = reorder_WinDjView_bookmarks(src, sorted_titles)
    
    out = xml_root_str2bytes(xml_root_str, args.output_encoding)
    with open(dst, 'wb') as fout:
        fout.write(out)
    return

    


if __name__ == "__main__":
    main()

'''
py -m nn_ns.txt.reorder_WinDjView_bookmarks titles.py "哥德尔 艾舍尔 巴赫：集异璧之大成more.pre.bookmarks.PY" out.py
'''












