

'''
glob_cmd -> src_fnames
src_fname -> re.sub -> matchobj2str -> dst_fname
src_dst_fname_pairs -> duplicate? reorder to nonoverlap
rename...
'''

__all__ = ['reorder_src_dst_pairs']


from collections import defaultdict

def reorder_src_dst_pairs(src_dst_pairs):
    '''reorder_src_dst_pairs :: [(src, dst)] -> [[path]]

output: [paths]
    where
        len(paths) >= 2
        paths[i] --[rename to]-> paths[i+1]
        paths[:-1] are all srcs
        if paths[0] == paths[-1] then is a rename cycle
        else: paths[-1] is not a src
        if paths1 is not paths2 then set(paths1) & set(paths2) == {}

example:
    >>> from seed.tiny import expectError
    >>> assert expectError(ValueError, lambda:reorder_src_dst_pairs([(1, ''), (2, '')]))
    >>> assert expectError(ValueError, lambda:reorder_src_dst_pairs([('', 1), ('', 2)]))

    # cycle
    >>> reorder_src_dst_pairs([(1,1)])
    [[1, 1]]
    >>> r = reorder_src_dst_pairs([(1,2), (2,1)])
    >>> assert r == [[1, 2, 1]] or r == [[2, 1, 2]]
    >>> r = reorder_src_dst_pairs([(1,1), (2,2)])
    >>> assert r == [[1, 1], [2, 2]] or r == [[2, 2], [1, 1]]

    # open list
    >>> reorder_src_dst_pairs([(1,2)])
    [[1, 2]]
    >>> reorder_src_dst_pairs([(1,2), (2,3)])
    [[1, 2, 3]]
    >>> r = reorder_src_dst_pairs([(1,2), (3,4)])
    >>> assert r == [[1, 2], [3, 4]] or r == [[3, 4], [1, 2]]

'''

    # unique src and dst
    src2dsts = defaultdict(set)
    dst2srcs = defaultdict(set)
    for src, dst in src_dst_pairs:
        src2dsts[src].add(dst)
        dst2srcs[dst].add(src)
    one_src2many_dsts = {src: dsts for src, dsts in src2dsts.items() if len(dsts) > 1}
    one_dst2many_srcs = {dst: srcs for dst, srcs in dst2srcs.items() if len(srcs) > 1}
    if one_src2many_dsts:
        raise ValueError(f'one_src2many_dsts: {one_src2many_dsts}')
    if one_dst2many_srcs:
        raise ValueError(f'one_dst2many_srcs: {one_dst2many_srcs}')

    def get_the_one(s):
        [x] = s
        return x
    def a2bs_to_a2b(a2bs):
        return {a:get_the_one(bs) for a, bs in a2bs.items()}
    src2dst = a2bs_to_a2b(src2dsts)
    dst2src = a2bs_to_a2b(dst2srcs)


    # reorder
    # 1) cycle; 2) link list
    # ls[i] rename to ls[i+1]
    # if cycle then ls[0] == ls[-1]
    # len(ls) >= 2
    # maybe: ls = [a, a]

    def del_src(src):
        dst = src2dst[src]
        del src2dst[src]
        del dst2src[dst]

    lsls = []
    while True:
        for src in src2dst: break
        else:               break
        ls = [src]

        # backward
        xdst = src
        while xdst in dst2src:
            xsrc = dst2src[xdst]
            ls.append(xsrc)
            if xsrc == src:
                # cycle
                break
            xdst = xsrc
        ls.reverse()

        if len(ls) == 1 or ls[0] != ls[-1]:
            # forward
            while src in src2dst:
                dst = src2dst[src]
                ls.append(dst)
                src = dst
        assert len(ls) >= 2

        # clear
        lsls.append(ls)
        if ls[0] == ls[-1]:
            # cycle
            srcs_to_be_remove = iter(ls[:-1])
        else:
            # bug: srcs_to_be_remove = iter(ls)
            srcs_to_be_remove = iter(ls[:-1])
        for src in srcs_to_be_remove:
            del_src(src)

    assert not src2dst
    assert not dst2src
    return lsls


if __name__ == "__main__":
    import doctest
    doctest.testmod()

