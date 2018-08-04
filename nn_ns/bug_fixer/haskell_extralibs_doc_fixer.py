
r'''
GHCi version 7.4.2
HaskellPlatform-2012.4.0.0

// install Haskell in "D:/software/programming/Haskell Platform/2012.4.0.0"
// it seems the extralibs doc are all refer to hard coded Haskell doc
documentation
    <- file:///D:/software/programming/Haskell%20Platform/2012.4.0.0/lib/extralibs/doc/OpenGL-2.2.3.1/html/Graphics-Rendering-OpenGL-GL-BasicTypes.html
    click on "Word8"
    not found -> file:///C:/ghc/ghc-7.4.2/doc/html/libraries/base-4.5.1.0/Data-Word.html#t:Word8
    <a href="C:\ghc\ghc-7.4.2\lib/../doc/html/libraries/base-4.5.1.0/Data-Word.html#t:Word8">Word8</a>
    should be D:\software\programming\Haskell Platform\2012.4.0.0\doc\html\libraries\base-4.5.1.0\Data-Word.html#t:Word8
    
    
    <- file:///D:/software/programming/Haskell%20Platform/2012.4.0.0/lib/extralibs/doc/parsec-3.1.3/html/Text-Parsec-Prim.html
    click on "Text"
    not found -> file:///C:/Program%20Files%20(x86)/Haskell/doc/text-0.11.2.3/html/Data-Text-Lazy-Internal.html#t:Text
    <a href="C:\Program Files (x86)\Haskell\doc\text-0.11.2.3\html/Data-Text-Lazy-Internal.html#t:Text">Text</a>
    should be D:\software\programming\Haskell Platform\2012.4.0.0\lib\extralibs\doc\text-0.11.2.3\html/Data-Text-Lazy-Internal.html#t:Text

    rex'(?i)<a +href="C:[\\/][^"]+?[\\/]+doc(?=[\\/]+html[\\/]+)'
        replaced by '<a href="D:/software/programming/Haskell%20Platform/2012.4.0.0/doc'
    rex'(?i)<a +href="C:[\\/][^"]+?[\\/]+doc(?=[\\/]+(?!html[\\/]+))'
        replaced by '<a href="D:/software/programming/Haskell%20Platform/2012.4.0.0/lib/extralibs/doc'



'''

import os
import os.path
import re

haskell_home = r"D:/software/programming/Haskell Platform/2012.4.0.0"
#haskell_home = r''
extralibs_doc_relpath = r'lib/extralibs/doc'
extralibs_path_identify_substring = r'extralibs'
wrong_href_to_haskell_doc_rex = re.compile(
    r'(?i)(<a\b[^>]+\bhref=")(C:[\\/][^"]+?[\\/]+doc)(?=[\\/]+html[\\/]+)')
wrong_href_to_extralibs_doc_rex = re.compile(
    r'(?i)(<a\b[^>]+\bhref=")(C:[\\/][^"]+?[\\/]+doc)(?=[\\/]+(?!html[\\/]+))')
def fix_haskell_extralibs_doc_href(haskell_home,
                                   extralibs_doc_relpath=extralibs_doc_relpath,
                                   extralibs_path_identify_substring=extralibs_path_identify_substring):
    #haskell_home = os.path.abspath(haskell_home)
    extralibs_doc_path = os.path.join(haskell_home, extralibs_doc_relpath)
    haskell_doc_path = os.path.join(haskell_home, 'doc')
    dirpath = None # used in repl!! bugs: cannot use html_path instead!
    
    def repl_to_haskell_doc(m):
        haskell_doc_relpath = os.path.relpath(haskell_doc_path, dirpath)
        return m.group(1) + haskell_doc_relpath
        if extralibs_path_identify_substring in m.group(0):
            print("warning unchanged: ", m.group(0))
            return m.group(0)

    def repl_to_extralibs_doc(m):
        extralibs_doc_relpath = os.path.relpath(extralibs_doc_path, dirpath)
        return m.group(1) + extralibs_doc_relpath

    for dirpath, dirnames, filenames in os.walk(extralibs_doc_path):
        for fname in filenames:
            root, ext = os.path.splitext(fname)
            ext = ext.lower()
            if ext == '.html' or ext == '.htm':
                html_path = os.path.join(dirpath, fname)
                with open(html_path, encoding='utf-8') as fin:
                    htm = fin.read()

                new = wrong_href_to_haskell_doc_rex.sub(repl_to_haskell_doc, htm)
                new = wrong_href_to_extralibs_doc_rex.sub(repl_to_extralibs_doc, new)
                if new != htm:
                    with open(html_path, 'w', encoding='utf-8') as fout:
                        fout.write(new)
    return



def main(argv=None):
    import argparse, shutil, sys

    parser = argparse.ArgumentParser(description='fix haskell extralibs doc href.',
                                     epilog='Windows only') # since using C:/...
    parser.add_argument('haskell_home', type=str, nargs='?',
                       help='haskell home path, i.e. {!r}'.format(haskell_home))

    args = parser.parse_args(argv)
    if args.haskell_home is None:
        # guess haskell_home by finding ghc.exe
        ghc_path = shutil.which('ghc')
        if ghc_path is None:
            print('not found "ghc"', file=sys.stderr)
            parser.exit(1)
            raise logic-error
            
        bin_path = os.path.dirname(ghc_path)
        home, bin_ = os.path.split(bin_path)
        assert bin_.lower() == 'bin'
        args.haskell_home = home

##    print(args.haskell_home)
##    print(argv)
##    print(sys.argv)
##    return
    fix_haskell_extralibs_doc_href(args.haskell_home)
    parser.exit(0)
    raise logic-error

if __name__ == '__main__':
    #fix_haskell_extralibs_doc_href(haskell_home)
    main()








