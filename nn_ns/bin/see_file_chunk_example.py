
import get_file_chunks
import os

def t():
    path = r'C:\game\WHITE_ALBUM2_-introductory_chapter-\WHITE ALBUM2 -introductory chapter-/'
    fn = r'char.pak'
    ls = os.listdir(path)
    fs = [ fn for fn in ls if fn[-4:].lower() == '.pak' and os.path.isfile(os.path.join( path, fn))]
    hs = [(get_file_chunks.get_file_chunks(path+fn), fn) for fn in fs]
    hs.sort()
    for h in hs:
        print(h)
        
