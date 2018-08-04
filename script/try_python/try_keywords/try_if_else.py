
# a if b else c if d else e ::= a if b else (c if d else e)

a = -1 if 1 else 2 if 0 else 4
b = -1 if 1 else (2 if 0 else 4)
c = (-1 if 1 else 2) if 0 else 4
assert b == -1
assert c == 4
assert a == b



