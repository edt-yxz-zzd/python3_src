def parse_triples_in_str(triples_in_str):
    '''
>>> parse_triples_in_str(' 1 2 3 \n \n\n a b c\nabc bc c\n\n')
[('1', '2', '3'), ('a', 'b', 'c'), ('abc', 'bc', 'c')]
'''

    triples = []
    for line in triples_in_str.split('\n'):
        may_triple = line.split()
        L = len(may_triple)
        if L == 3:
            triples.append(tuple(may_triple))
        elif L == 0:
            pass
        else:
            raise Exception(f'not a triple line: {line!r}')
    return triples

