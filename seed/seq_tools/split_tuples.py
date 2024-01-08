
def split_tuples(length, tuples):
    rg = range(length)
    lsls = tuple([] for _ in rg)
    for t in tuples:
        for i in rg:
            lsls[i].append(t[i])
    return lsls

def unzip_pairs(pairs, /):
    (fsts, snds) = split_tuples(2, pairs)
    return (fsts, snds)

from seed.seq_tools.split_tuples import split_tuples, unzip_pairs

