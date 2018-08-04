

r'''
\xhh -> normal char or not
i.e. if chr(0xhh) == '(', r'\xhh' ==>> '(' or r'\('???
ans: rex(r'\xhh') ==>> rex(r'\(') instead of rex('(')
'''

import re
print(hex(ord('(')))
p = r'\x{:0>2x}'.format(ord('('))
rex = re.compile(p)
print(rex.pattern)
m = rex.match('(')
assert m.group(0) == '('
