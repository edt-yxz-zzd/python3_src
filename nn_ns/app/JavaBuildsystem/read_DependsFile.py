
r'''
DependsFile using encoding=utf8

# concrete syntax
DependsFile = Line (<newline> Line)*
Line = Spaces_or_Comment | IndentedContent Spaces_or_Comment
Spaces = regex"\s*"
Comment = regex"\s*#.*"
Spaces_or_Comment = regex"\s*(#.*)?"
IndentedContent = HasMain | ToplevelsHead | ModulesHead | ResourcesHead | Indent Class | Indent Module | Indent Path
Content = HasMain | ToplevelsHead | ModulesHead | ResourcesHead | Class | Module | Path
ToplevelsHead = "toplevels:"
ModulesHead = "modules:"
ResourcesHead = "resources:"
HasMain = regex"[-+]main"
Indent = regex" {4}"
Class = regex"\w+"
Module = regex"\w+(\.\w+)*"
Path = RelativePath | AbsolutePath
AbsolutePath = "/" RelativePath
RelativePath = regex"\w+(/\w+)*(\.\w+)?"

# abstract syntax over IndentedContent*
DependsFile = HasMain Toplevels Modules Resources
Toplevels = ToplevelsHead Class*
Modules = ModulesHead Module*
Resources = ResourcesHead Path*
'''

__all__ = '''
    read_DependsFile
    '''.split()

import re
from io import StringIO


def re_compile_ASCII(pattern):
    return re.compile(pattern, flags=re.ASCII)

Spaces_or_Comment = r"\s*(?:#.*)?"
HasMain = r"[-+]main"
Indent = " "*4
ToplevelsHead = "toplevels:"
ModulesHead = "modules:"
Class = r"\w+"
Module = r"\w+(?:\.\w+)*"
ResourcesHead = "resources:"
RelativePath = r"\w+(?:/\w+)*(?:\.\w+)?"
AbsolutePath = fr"/{RelativePath}"
Path = fr"/?{RelativePath}"
ClassAndModuleAndPath = fr"\w+(?:\.\w+)?"
Line = (
    fr"(?:"
    fr"(?P<HasMain>{HasMain})"                      #x
    fr"|(?P<ToplevelsHead>{ToplevelsHead})"         #T
    fr"|(?P<ModulesHead>{ModulesHead})"             #M
    fr"|(?P<ResourcesHead>{ResourcesHead})"         #R
    # ClassAndModuleAndPath must be
    #   before Class and Module and Path
    fr"|{Indent}(?P<ClassAndModuleAndPath>{ClassAndModuleAndPath})"
                                                    #A
    fr"|{Indent}(?P<Class>{Class})"                 #c  # useless
    fr"|{Indent}(?P<Module>{Module})"               #m
    fr"|{Indent}(?P<Path>{Path})"                   #r
    # "" must be last
    fr"|){Spaces_or_Comment}"
    # DependsFile = r"xT[Ac]*M[Am]*R[Ar]*" # over super chars
    )
regexLine = re_compile_ASCII(Line)
DependsFile = r"xT[Ac]*(M[Am]*)(R[Ar]*)" # over super chars
DependsFilePrefex = r"(?:x(?:T[Ac]*(?:M[Am]*(?:R[Ar]*)?)?)?)?" # over super chars
regexDependsFile = re_compile_ASCII(DependsFile)
regexDependsFilePrefex = re_compile_ASCII(DependsFilePrefex)
case2superchar = \
    {'HasMain': 'x'
    ,'ToplevelsHead': 'T'
    ,'ModulesHead': 'M'
    ,'ResourcesHead': 'R'
    ,'ClassAndModuleAndPath': 'A'
    ,'Class': 'c'
    ,'Module': 'm'
    ,'Path': 'r'
    }


def read_DependsFile(file_or_path):
    # -> (Bool, [String], [String], [String]) | raise Exception
    # -> depends_info | raise
    # depends_info = (has_main, toplevels, modules, resources)
    #
    if (hasattr(file_or_path, 'readline')):
        fin = file_or_path
        return read_DependsFile__file(fin)
    path = file_or_path
    with open(path, encoding='utf8') as fin:
        return read_DependsFile__file(fin)


def read_DependsFile__file(file):
    contents = [] # [Content]
    debug_infos = [] # [(lineno, old_line)]
    superchars = []
    for lineno, line in enumerate(file):
        old_line = line
        line = line.rstrip()
        m = regexLine.fullmatch(line)
        if not m:
            raise Exception(f"line#{lineno}: {old_line!r}")

        d = m.groupdict()
        items = [(key, val) for key, val in d.items() if val is not None]
        if not items:
            # only Spaces_or_Comment
            continue

        [(case, content)] = items # only one group
        assert case != 'Spaces_or_Comment'

        contents.append(content)
        debug_infos.append((lineno, old_line))
        superchars.append(case2superchar[case])
    superchars = ''.join(superchars)

    m = regexDependsFile.fullmatch(superchars)
    if not m:
        m = regexDependsFilePrefex.match(superchars)
        assert m
        if not m: raise logic-error
        L = m.end()
        if L == len(debug_infos):
            raise Exception(f'format error: incomplete file')

        lineno, old_line = debug_infos[L]
        raise Exception(f'format error: lineno#{lineno}: {old_line!r}')

    idx_x = 0
    idx_T = 1
    idx_M = m.start(1)
    idx_R = m.start(2)
    assert superchars[idx_x] == 'x'
    assert superchars[idx_M] == 'M'
    assert superchars[idx_T] == 'T'
    assert superchars[idx_R] == 'R'

    assert contents[idx_x][0] in ('+', '-')
    has_main = contents[idx_x][0] == '+'

    toplevels   = contents[idx_T+1: idx_M]
    modules     = contents[idx_M+1: idx_R]
    resources   = contents[idx_R+1:]
    return has_main, toplevels, modules, resources



def _read_from_str(s):
    return read_DependsFile(StringIO(s))
def _test():
    f1 = '''
#afaf

-main
#afa

toplevels:

modules: # afasfs
resources:  '''
    f2 = '''
+main
toplevels:
    xxx
    yyy
    zzz
modules:
    xxx.yyy.AFSFAS
    afaf.afsfa
    afs
resources:
    /afasf
    /afsfa.sf
    /afsfa/sf.afa
    /afaf/afsfa/sf.afa
    afasf
        #fafa;fk
 #afafas
    afsfa.sf
    afsfa/sf.afa
    afaf/afsfa/sf.afa
    '''

    def show(fin, has_main):
        _has_main, toplevels, modules, resources = _read_from_str(fin)
        assert _has_main == has_main
        print(toplevels)
        print('\n')
        print(modules)
        print('\n')
        print(resources)

    show(f1, False)
    print('\n'*4)
    show(f2, True)


if '__main__' == __name__:
    _test()

