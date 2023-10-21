
def split_tuples(length, tuples):
    def mk_iter():
        return range(length)
    lsls = tuple([] for _ in mk_iter())
    for t in tuples:
        for i in mk_iter():
            lsls[i].append(t[i])
    return lsls

def unzip_pairs(pairs, /):
    (fsts, snds) = split_tuples(2, pairs)
    return (fsts, snds)

from seed.seq_tools.split_tuples import split_tuples, unzip_pairs

