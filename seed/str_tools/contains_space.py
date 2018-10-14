

__all__ = '''
    contains_space
    find_first_space
    find_last_space
    '''.split()

import re
space_regex = re.compile(r'\s')

def find_first_space(s:str)->bool:
    '''-> None|UIntIdx

>>> find_first_space('')
>>> find_first_space('a')
>>> find_first_space(' ')
0
>>> find_first_space('  a')
0
>>> find_first_space('a  ')
1

'''
    m = space_regex.search(s)
    if not m: return None
    return m.start()

def find_last_space(s:str)->bool:
    '''-> None|UIntIdx

>>> find_last_space('')
>>> find_last_space('a')
>>> find_last_space(' ')
0
>>> find_last_space('  a')
1
>>> find_last_space('a  ')
2

'''
    for i, ch in zip(reversed(range(len(s))), reversed(s)):
        if ch.isspace():
            return i
    return None

def contains_space(s:str)->bool:
    '''

>>> ' '.isspace()
True
>>> ''.split()
[]
>>> ' '.strip()
''
>>> '　' == '\u3000'
True
>>> '\u3000'.isspace()
True
>>> '\u3000'.split()
[]
>>> '\u3000'.strip()
''
>>> ' a b '.strip()
'a b'

>>> contains_space('\u3000')
True
>>> contains_space(' ')
True
>>> contains_space(' a')
True
>>> contains_space('a ')
True
>>> contains_space(' a ')
True
>>> contains_space('a b')
True
>>> contains_space('')
False
>>> contains_space('a')
False
'''
    return bool(space_regex.search(s))
    # bug: return s and ...
    #   may return ''
    return bool(s) and (len(s.strip()) != len(s) or len(s.split()) != 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL

