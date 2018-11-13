

__all__ = '''
    Token
    to_splited_source
    '''.split()

from ..debug_tools.position2lineno_columnno import position2lineno_columnno_ex

class Token:
    def __init__(self, terminal, source, begin, end):
        self.terminal = terminal
        self.source = source
        self.begin = begin
        self.end = end
        self.value = None
        self.__substring = None
        self.__lineno_columnno_ex = None
    @property
    def substring(self):
        if self.__substring is None:
            self.__substring = self.source[self.begin:self.end]
        return self.__substring
    def get_lineno_columnno(self):
        if self.__lineno_columnno_ex is None:
            self.__lineno_columnno_ex = \
                position2lineno_columnno_ex(self.source, self.begin)
        lineno, columnno, line_position = self.__lineno_columnno_ex
        return lineno, columnno

    def __repr__(self):
        name = type(self).__name__
        lineno, columnno = self.get_lineno_columnno()
        return f'{name}({self.terminal!r}, <source>, begin={self.begin}, end={self.end}, <lineno={lineno}>, <columnno={columnno}>, <substring={self.substring!r}>)'

def to_splited_source(self):
    init = self.source[:self.begin]
    sub = self.substring
    tail = self.source[self.end:]
    sep = '='*60
    sep = f'\n{sep}\n'
    s = f'{sep}{init}{sep}{sub}{sep}{tail}{sep}'
    return s
    print('='*60)
    print(init)
    print('='*60)
    print(sub)
    print('='*60)
    print(tail)
    print('='*60)


