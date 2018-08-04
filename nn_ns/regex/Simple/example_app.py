
r'''
    does_accept
    does_accept_ex
    search_prefix
    search_prefix_ex
    search_leftmost_substring
    search_leftmost_substring_ex
    search_leftmost_substring_ex_ex



# search_leftmost_substring (S+A+|B+S+A+X+) in "BBBSSSAAAXXX"
#   greedy leftmost_end_first   result
#   True        False           (0, 12)
#   False       False           (0, 10)
#   True        True            (3, 7)
#   False       True            (5, 7)

>>> from .app import search_leftmost_substring
>>> pattern = r"S\+A\+\|B\+S\+A\+X\+"
>>> string = "BBBSSSAAAXXX"
>>> search_leftmost_substring(pattern, iter(string))
(0, 12)
>>> search_leftmost_substring(pattern, string, True, False)
(0, 12)
>>> search_leftmost_substring(pattern, string, False, False)
(0, 10)
>>> search_leftmost_substring(pattern, string, True, True)
(3, 7)
>>> search_leftmost_substring(pattern, string, False, True)
(5, 7)
>>> search_leftmost_substring(pattern, '') is None
True
>>> search_leftmost_substring(pattern, 'Z') is None
True



>>> from .app import search_leftmost_substring_ex
>>> low_begin = '0'
>>> char_low_pairs = [*zip(string, map(str, range(1, 1+len(string))))]
>>> len(char_low_pairs) == len(string)
True
>>> search_leftmost_substring_ex(pattern, low_begin, char_low_pairs)
(((0, '0'), (12, '12')), (12, '12'))
>>> search_leftmost_substring_ex(pattern, low_begin, char_low_pairs, True, False)
(((0, '0'), (12, '12')), (12, '12'))
>>> search_leftmost_substring_ex(pattern, low_begin, char_low_pairs, False, False)
(((0, '0'), (10, '10')), (10, '10'))
>>> search_leftmost_substring_ex(pattern, low_begin, char_low_pairs, True, True)
(((3, '3'), (7, '7')), (7, '7'))
>>> search_leftmost_substring_ex(pattern, low_begin, char_low_pairs, False, True)
(((5, '5'), (7, '7')), (7, '7'))
>>> search_leftmost_substring_ex(pattern, low_begin, [])
(None, (0, '0'))
>>> search_leftmost_substring_ex(pattern, low_begin, [('Z', '1')])
(None, (1, '1'))




>>> from .app import search_leftmost_substring_ex_ex
>>> search_leftmost_substring_ex_ex(pattern, low_begin, char_low_pairs)
('LeftMostBegin_SuccessUntilEnd', ((0, '0'), (12, '12')), (12, '12'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, char_low_pairs, True, False)
('LeftMostBegin_SuccessUntilEnd', ((0, '0'), (12, '12')), (12, '12'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, char_low_pairs, False, False)
('LeftMostBegin_NonGreedyEnd', ((0, '0'), (10, '10')), (10, '10'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, char_low_pairs, True, True)
('LeftMostEnd_GreedyBegin', ((3, '3'), (7, '7')), (7, '7'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, char_low_pairs, False, True)
('LeftMostEnd_NonGreedyBegin', ((5, '5'), (7, '7')), (7, '7'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, [])
('FailUntilEnd', None, (0, '0'))
>>> search_leftmost_substring_ex_ex(pattern, low_begin, [('Z', '1')])
('FailUntilEnd', None, (1, '1'))


#####################################
>>> from .app import does_accept, does_accept_ex
>>> pattern = r"S\+A\+\|B\+S\+A\+X\+"
>>> string = "BBBSSSAAAXXX"
>>> does_accept(iter(pattern), iter(string))
True
>>> does_accept(iter(pattern), '0'+string)
False
>>> does_accept(iter(pattern), string+'0')
False

>>> does_accept_ex(pattern, low_begin, char_low_pairs)
('SuccessUntilEnd', True, (12, '12'))
>>> does_accept_ex(pattern, low_begin, [('Z', '1'), ...])
('FailOnGlobalDead', False, (1, '1'))




#####################################
>>> from .app import search_prefix, search_prefix_ex
>>> pattern = r"\(S\+A\+\)\+"
>>> string = "SSAASASAAASA"
>>> low_begin = '0'
>>> char_low_pairs = [*zip(string, map(str, range(1, 1+len(string))))]
>>> assert len(char_low_pairs) == len(string)

>>> search_prefix(iter(pattern), iter(string))
12
>>> search_prefix(pattern, string, True)
12
>>> search_prefix(pattern, string, False)
3
>>> search_prefix(pattern, 'Z'+string) is None
True
>>> search_prefix(pattern, string+'Z')
12


>>> search_prefix_ex(iter(pattern), low_begin, iter(char_low_pairs))
('SuccessUntilEnd', (12, '12'), (12, '12'))
>>> search_prefix_ex(iter(pattern), low_begin, char_low_pairs, True)
('SuccessUntilEnd', (12, '12'), (12, '12'))
>>> search_prefix_ex(iter(pattern), low_begin, char_low_pairs, False)
('SuccessOnNonGreedy', (3, '3'), (3, '3'))

>>> search_prefix_ex(iter(pattern), low_begin, [])
('FailUntilEnd', None, (0, '0'))
>>> search_prefix_ex(iter(pattern), low_begin, [('Z', '1')])
('FailOnGlobalDead', None, (1, '1'))




############ test char class
>>> pattern = r'\<digit\>\+'
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(4, 7)
>>> pattern = r'\<space\>\+'
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(2, 4)
>>> pattern = r'\[\<space\>\<digit\>\]\+'
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(2, 7)
>>> pattern = r'\[\^\<space\>\<digit\>\]\+'
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(0, 2)
>>> pattern = r'\[\w\s\]\+'
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(0, 12)


############ test reverse
>>> pattern = r'\(\d\+\l\+\)\+' # \l for lower alpha
>>> search_leftmost_substring(pattern, 'ab  234agg34')
(4, 10)
>>> search_leftmost_substring(pattern, reversed('ab  234agg34'), reverse=True)
(2, 8)


############ others
>>> pattern = r'\\' # \\
>>> search_leftmost_substring(pattern, '01234\\')
(5, 6)
>>> pattern = r'\.\*\n' # \n \.
>>> search_leftmost_substring(pattern, 'ab  234agg34') is None
True
>>> search_leftmost_substring(pattern, '01234\n')
(0, 6)
>>> pattern = r'\.\*\<n \>' # \< n \>
>>> search_leftmost_substring(pattern, '01234\n')
(0, 6)

>>> chr(0x64) == 'd'
True
>>> ord('d') == 100 == 0x64 == 0o144 == 0b1100100
True
>>> pattern = r'\< \< 100 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< 0x64 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< x64 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< U+64 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< 0o144 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< o144 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< 0b1100100 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
>>> pattern = r'\< \< b1100100 \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)

>>> pattern = r'\< \< U+6\<x34\> \>igit \>\+' # space and nest
>>> search_leftmost_substring(pattern, '01234\n')
(0, 5)
'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()



