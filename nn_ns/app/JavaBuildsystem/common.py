
__all__ = '''
    DependsFileExt
    JavaFileExt
    ClassFileExt

    is_ext
    '''.split()


DependsFileExt = '.depends'
JavaFileExt = '.java'
ClassFileExt = '.class'

def is_ext(ext):
    # ".tar.gz"
    # ".rar.001"
    return ext and ext[0] == '.' != ext[-1]

