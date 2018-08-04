


r'''

>>> from .string_regex_pattern import parse_string_regex_pattern
>>> from .ISimpleNFA import ISimpleNFA
>>> ops = ISimpleNFA.NFA_ops

>>> pattern = 'a\+'
>>> regex = parse_string_regex_pattern(pattern)
>>> nfa = regex.toSimpleNFA()
>>> ops.search_leftmost_substring(nfa, 'bbaaahhaaa', True, False)
(2, 5)




>>> pattern2nfa = lambda pattern: parse_string_regex_pattern(pattern).toSimpleNFA()
>>> search_nfa = lambda nfa, s: ops.search_leftmost_substring(nfa, s, True, False)
>>> search = lambda pattern, s: search_nfa(pattern2nfa(pattern), s)


>>> pattern = 'a\|b'
>>> search(pattern, 'bbaaahhaaa')
(0, 1)
>>> pattern = '\(a\|b\)\+'
>>> search(pattern, 'bbaaahhaaa')
(0, 5)


>>> pattern = 'ab'
>>> search(pattern, 'bbaaahhaaa') is None
True
>>> pattern = 'ba'
>>> search(pattern, 'bbaaahhaaa')
(1, 3)

>>> pattern = '\.'
>>> search(pattern, 'bbaaahhaaa')
(0, 1)
>>> pattern = '\.\?'
>>> search(pattern, 'bbaaahhaaa')
(0, 1)
>>> pattern = '\.\*'
>>> search(pattern, 'bbaaahhaaa')
(0, 10)
>>> pattern = '\.\{2,5\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 5)
>>> pattern = '\.\{2,20\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 10)
>>> pattern = '\.\{2\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 2)
>>> pattern = '\.\{2,\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 10)
>>> pattern = '\.\{,8\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 8)
>>> pattern = '\.\{,\}'
>>> search(pattern, 'bbaaahhaaa')
(0, 10)


>>> pattern = '02n'
>>> search(pattern, '102n')
(1, 4)
>>> pattern = '\<0\>\<2\>\<n\>'
>>> search(pattern, '\1\0\2\n')
(1, 4)
>>> pattern = '\[a-f\]'
>>> search(pattern, '12ghab3')
(4, 5)
>>> pattern = '\[a-f\]\+'
>>> search(pattern, '12ghab3')
(4, 5)
>>> pattern = '\[a\-f\]\+'
>>> search(pattern, '12ghab3')
(4, 6)

>>> pattern = '\[\^a\-f\]\+'
>>> search(pattern, '12ghab3')
(0, 4)
>>> pattern = '\[\^21a\-f1\]\+'
>>> search(pattern, '12ghab3')
(2, 4)


'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()



