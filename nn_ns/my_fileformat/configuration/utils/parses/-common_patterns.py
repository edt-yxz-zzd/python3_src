name = r'(?:\w+)'
names1 = fr'(?:{name}(?:\s+{name})*)'
names0 = fr'(?:{names1}?)'

def make_op_name_patterns(op):
    assert op in r'[+] [+-]'.split()
    bar = r'\s*[|]\s*'
    xname = fr'(?:{op}{name})'
    unit_xnames1 = fr'(?:(?:{name}\s+)*{xname}(?:\s+{name})*|{name})'
    xnames1 = fr'(?:(?:{name}\s+)*{xname}(?:\s+{name})*|{name})'
    xnames1 = fr'(?:{xname}(?:{bar}{xname})*)'
    xnames1s1 = fr'(?:{xnames1}(?:{bar}{xnames1})*)'

_line = fr'(?P<name>\w+) = (?P<xnamess>{_xnames1s1})'


