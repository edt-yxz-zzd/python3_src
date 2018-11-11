
__all__ = '''
    position2lineno_columnno
    position2lineno_columnno_ex
    show_splited_text_at
    '''.split()


def show_splited_text_at(__string, __position):
    lineno, columnno, line_position = position2lineno_columnno_ex(
                                            __string, __position)
    print(__string[:line_position])
    print('='*60)
    print(f'lineno={lineno}, columnno={columnno}, position={__position}')
    print('='*60)
    print(__string[line_position:])
    return

def position2lineno_columnno(__string, __position, *, starting_from_0=False):
    lineno, columnno, line_position = position2lineno_columnno_ex(
        __string, __position, starting_from_0=starting_from_0)
    return lineno, columnno

def position2lineno_columnno_ex(__string, __position, *, starting_from_0=False):
    '''
input:
    __string        :: str
    __position      :: int
    starting_from_0 :: bool
        lineno starting_from_0?
        columnno starting_from_0?
output:
    lineno      :: int
    columnno    :: int
    line_position :: int
'''
    if not 0 <= __position < len(__string): raise ValueError
    offset = not starting_from_0
    i = __string.rfind('\n', 0, __position)
    line_position = i+1

    if i == -1:
        lineno__starting_from_0 = 0
        columnno__starting_from_0 = __position
    else:
        assert i < __position
        columnno__starting_from_0 = __position-i-1
        assert columnno__starting_from_0 >= 0

        lineno__starting_from_0 = __string.count('\n', 0, i)+1
        assert lineno__starting_from_0 >= 1

    lineno = offset + lineno__starting_from_0
    columnno = offset + columnno__starting_from_0
    return lineno, columnno, line_position

