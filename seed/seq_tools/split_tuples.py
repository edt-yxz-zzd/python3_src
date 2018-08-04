
def split_tuples(length, tuples):
    def mk_iter():
        return range(length)
    lsls = tuple([] for _ in mk_iter())
    for t in tuples:
        for i in mk_iter():
            lsls[i].append(t[i])
    return lsls


