

__all__ = '''
    Token
    to_splited_source
    '''.split()



class Token:
    def __init__(self, terminal, source, begin, end):
        self.terminal = terminal
        self.source = source
        self.begin = begin
        self.end = end
        self.value = None
        self.__substring = None
    @property
    def substring(self):
        if self.__substring is None:
            self.__substring = self.source[self.begin:self.end]
        return self.__substring

    def __repr__(self):
        name = type(self).__name__
        return f'{name}({self.terminal!r}, <source>, {self.begin}, {self.end}, <substring={self.substring!r}>)'

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


