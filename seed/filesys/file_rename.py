

__all__ = '''
    rename_files

    replace_file
    rename_file
    swap_file

    rename_files__left_shift1
    swap_files__left_cyclic1
    '''.split()
    #is_empty_file
    #write_force



from seed.filesys.to_abspath import where, to_abspath
from seed.iters.duplicate_elements import find_maybe_duplicate_element1


import os # replace remove
from os import path
from tempfile import NamedTemporaryFile as _nTempFile


_prefix = 'tmp_'
_suffix = '.tmp'


def replace_file(src, dst):
    os.replace(src, dst)
    return
def rename_file(src, dst):
    if path.exists(dst):
        raise FileExistsError(dst)
    replace_file(src, dst)
    return


'''
def is_empty_file(fname):
    with open(fname, 'rb') as fin:
        b = fin.read1(1)
        return len(b) == 0
'''

def swap_file(src, dst):
    src = path.abspath(src)
    dst = path.abspath(dst)
    if src == dst:
        return

    outdir = where(dst)
    with _nTempFile(mode='wb', delete=False, \
                    suffix=_suffix, prefix=_prefix, dir=outdir) as fout:
        tmp_dst = fout.name
    os.replace(dst, tmp_dst)
    rename_file(src, dst)
    rename_file(tmp_dst, src)
    return

def normalize_fnames(fnames):
    return tuple(map(to_abspath, fnames))

def rename_files__left_shift1(fnames):
    'rename fnames[i] as fnames[i-1] for i > 0'
    fnames = normalize_fnames(fnames)
    if not all(map(path.exists, fnames[1:])):
        raise ValueError('not all(map(path.exists, fnames[1:]))')
    L = len(fnames)
    if L > 0:
        if path.exists(fnames[0]):
            raise ValueError('path.exists(fnames[0]) : {!r}'
                             .format(fnames[0]))
    if L < 2:
        return
    if len(frozenset(fnames)) != L:
        raise ValueError('duplicate path : {!r}'
                         .format(find_maybe_duplicate_element1(fnames)[0]))
    for i in range(1, L):
        # fnames[i-1] not exists
        rename_file(fnames[i], fnames[i-1])
    return

def swap_files__left_cyclic1(fnames):
    'rename fnames[i] as fnames[i-1] include i == 0'
    fnames = normalize_fnames(fnames)
    if not all(map(path.exists, fnames)):
        raise ValueError('not all(map(path.exists, fnames))')
    L = len(fnames)
    if L < 2:
        return
    if len(frozenset(fnames)) != L:
        raise ValueError('duplicate path : {!r}'
                         .format(find_maybe_duplicate_element1(fnames)[0]))

    dst = fnames[-1]
    outdir = where(dst)
    with _nTempFile(mode='wb', delete=False, \
                    suffix=_suffix, prefix=_prefix, dir=outdir) as fout:
        tmp = fout.name
    os.replace(dst, tmp) # del tmp

    for i in range(L-1):
        # fnames[i-1] not exists
        rename_file(fnames[i], fnames[i-1])

    # tmp is fnames[L-1]
    rename_file(tmp, fnames[L-2])
    return


def rename_files(srcs, dsts):
    srcs = normalize_fnames(srcs)
    dsts = normalize_fnames(dsts)
    if len(srcs) != len(dsts):
        raise ValueError('len(srcs) != len(dsts)')
    if not all(map(path.exists, srcs)):
        raise ValueError('not all(map(path.exists, srcs))')

    L = len(srcs)
    src_set = frozenset(srcs)
    dst_set = frozenset(dsts)
    if len(dsts) != len(srcs):
        raise ValueError('len(dsts) != len(srcs)')
    if len(src_set) != len(srcs):
        raise ValueError('len(srcs) != len(src_set)')
    if len(dst_set) != len(dsts):
        raise ValueError('len(dsts) != len(dst_set)')

    existing_dsts = frozenset(filter(path.exists, dsts))
    if not existing_dsts <= src_set:
        raise ValueError('not set(filter(path.exists, dsts)) <= set(srcs) : {}'
                         .format(existing_dsts - src_set))

    src2src_idx = dict(map(reversed, enumerate(srcs)))
    dst_idx2real_idx = {i: src2src_idx.get(dsts[i-L], i) for i in range(L, 2*L)}
    src_idx2real_dst_idx = [dst_idx2real_idx[i+L] for i in range(L)]

##    path2idx = dict(map(reversed, enumerate(L, dsts)))
##    path2idx.update(src2idx)

##    paths = srcs + dsts
    nondst_srcs = src_set - existing_dsts
    assert len(existing_dsts) + len(nondst_srcs) == len(src_set)


    rename_lsls = []
    for i in map(lambda fname: src2src_idx[fname], nondst_srcs):
        ls = [i]
        while i < L:
            i = src_idx2real_dst_idx[i]
            ls.append(i)
        rename_lsls.append(ls)


    rename_idcs = tuple(chain_iters(rename_lsls))
    rename_idx_set = frozenset(idcs)
    assert len(rename_idcs) == len(rename_idx_set)

    swap_idx_set = frozenset(range(L)) - rename_idx_set
    swap_lsls = []
    for i in swap_idx_set:
        ls = [i]
        j = i
        while True:
            j = src_idx2real_dst_idx[j]
            if j == i: break
            ls.append(j)
        swap_lsls.append(ls)
    swap_idcs = tuple(chain_iters(swap_lsls))
    assert len(swap_idx_set) == len(swap_idcs)
    assert swap_idx_set == frozenset(swap_idcs)
    assert len(swap_idx_set) + len(rename_idx_set) == L
    assert swap_idx_set | rename_idx_set == frozenset(range(L))


    for rename_fs, rev_fs_ls in [(rename_files__left_shift1, rename_lsls),
                                 (swap_files__left_cyclic1, swap_lsls)]:
        for rev_fs in rev_fs_ls:
            rename_fs(reversed(rev_fs))

    return



'''
def write_force(fname, data, *, encoding=None):
    if encoding:
        data = data.encode(encoding)

    outdir = where(fname)
    with _nTempFile(mode='wb', delete=False, \
                    suffix=_suffix, prefix=_prefix, dir=outdir) as fout:
        tmp = fout.name
        fout.write(data)
    replace_file(tmp, fname)
    return
'''

