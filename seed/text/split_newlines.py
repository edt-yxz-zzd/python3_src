

__all__ = ['split_newlines']


def split_newlines(line):
    r'''line -> (content, newlines)

newlines may be ''
len(newlines) == 0|1|2|...??

example:
    >>> split_newlines('')
    ('', '')
    >>> split_newlines('a')
    ('a', '')
    >>> split_newlines('a\r\n')
    ('a', '\r\n')
    >>> split_newlines('\r\n')
    ('', '\r\n')
'''
    L = len(line)

    i = -1
    for i, ch in enumerate(reversed(line)):
        if ch not in '\r\n': break
    else:
        i += 1
        assert i == L

    assert L == i or line[L-1-i] not in '\r\n'
    assert 0 == i or line[L-i] in '\r\n'
    return line[:L-i], line[L-i:]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
