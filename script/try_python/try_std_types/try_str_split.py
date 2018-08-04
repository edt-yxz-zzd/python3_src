
for s in ['', '  ', '   faf  ']:
    print(repr(s), s.split())
assert '   faf  '.split() == ['faf']
assert '  '.split() == []
