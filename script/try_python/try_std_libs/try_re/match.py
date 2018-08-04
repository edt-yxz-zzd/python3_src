
import re

'''
>>> pattern = re.compile("o")
>>> pattern.match("dog")      # No match as "o" is not at the start of "dog".
>>> pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
<_sre.SRE_Match object at ...>

'''

m = re.match(r'a', 'abbbbb')
assert m.group(0) == 'a'

m = re.match(r'a', 'abbbbb', 0) # bug : 0 is flag not begin !!!!


def match(pattern, string, begin=None, end=None):
    if True:
        if begin is None:
            begin = 0
        if end is None:
            end = len(string)

        if begin > end:
            begin = end

    rex = re.compile(pattern)
    return rex.match(string, begin, end)

m = match(r'a', 'abbbbb', 0)
assert m.start() == 0
m = match(r'o', 'dog', 1)
assert m.start() == 1
m = match(r'a', 'bbabbbbb', 2)
assert m.start() == 2
