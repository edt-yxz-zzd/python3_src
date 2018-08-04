
__all__ = ['is_numeric_char']

from unicodedata import numeric

def is_numeric_char(char):
    Nothing = []
    n = numeric(char, Nothing)
    return n is not Nothing


def main():
    from sys import stdout
    from io import StringIO
    b_stdout = stdout.buffer
    old_print = print
    encoding = 'utf8'
    def new_print(*args):
        sout = StringIO()
        old_print(*args, file=sout)
        string = sout.getvalue()
        bs = string.encode(encoding=encoding)
        b_stdout.write(bs)

    from .iter_all_char_ords import iter_all_chars
    it = iter_all_chars()
    for char in it:
        if is_numeric_char(char):
            new_print('U+{:0>6X}'.format(ord(char)), '#', char)

def main():
    from seed.io.stdout_print import stdout_print
    from .iter_all_char_ords import iter_all_chars
    it = iter_all_chars()
    for char in it:
        if is_numeric_char(char):
            stdout_print('U+{:0>6X}'.format(ord(char))
                        , '#', char
                        , '#', repr(numeric(char))
                        , encoding='utf8')

if __name__ == '__main__':
    '''
    chcp 936 # gbk
    chcp 65001 # Windows only: Windows UTF-8 (CP_UTF8)
    chcp 54936 # gb18030
    from sys import stdout
    print(repr(stdout.encoding))
    if stdout.encoding == 'gbk':
        print('gbk -> gb18030')
        stdout.encoding = 'gb18030'
    elif stdout.encoding == 'cp936':
        print('cp936 -> cp54936')
        stdout.encoding = 'cp54936'
    '''
    main()

