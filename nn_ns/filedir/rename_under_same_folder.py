

__all__ = ['rename_under_same_folder']


from .reorder_src_dst_pairs import reorder_src_dst_pairs
from .rename import rename as global_rename
from os.path import join, exists
from itertools import chain


class TmpPath:
    def __init__(self, folder, basename_prefix, tmp_number, basename_suffix):
        self.folder = folder
        self.basename_prefix = basename_prefix
        self.basename_suffix = basename_suffix

        self.tmp_number = None
        self.tmp_basename = None
        self.tmp_path = None
        self.set_tmp_number(tmp_number)
    def set_tmp_number(self, tmp_number):
        if type(tmp_number) is not int: raise TypeError
        if tmp_number < 0: raise TypeError
        self.tmp_number = tmp_number
        self.tmp_basename = str(tmp_number).join(
                    [self.basename_prefix, self.basename_suffix])
        self.tmp_path = join(self.folder, self.tmp_basename)
    def next(self):
        self.set_tmp_number(self.tmp_number+1)
        return self.tmp_path
    def exists(self):
        return exists(self.tmp_path)
    def many0_next_until_not_exists(self):
        while self.exists():
            self.next()
        return self.tmp_path
    def many1_next_until_not_exists(self):
        self.next()
        return self.many0_next_until_not_exists()

def rename_under_same_folder(folder, src_dst_basename_pairs
        , *, pseudo_rename=None):
    basename_lsls = reorder_src_dst_pairs(src_dst_basename_pairs)
    _rename_under_same_folder(folder, basename_lsls
        , pseudo_rename=pseudo_rename)
def _rename_under_same_folder(folder, basename_lsls, tmp_prefix = '__tmp_'
        , *, pseudo_rename=None):
    '''rename under same folder

pseudo_rename :: src -> dst -> None
basename_lsls:
    see: output of reorder_src_dst_pairs
    for ls in basename_lsls:
        ls :: [basename]
        len(ls) >= 2
        ls[i] will rename to ls[i+1]
        ls[:-1] are all srcs
        if ls[0] == ls[-1] then a rename cycle
        else ls[-1] is not a src
    ls1 is ls2 or set(ls1) & set(ls2) == {}

'''
    rename = global_rename if pseudo_rename is None else pseudo_rename

    for ls in basename_lsls:
        if len(ls) < 2: raise ValueError
        L_ = len(set(ls))
        L = len(ls)
        if not (L == L_ or (L == L_+1 and ls[0] == ls[-1])): raise ValueError

    # check src exists
    for ls in basename_lsls:
        for src in ls[:-1]:
            path = join(folder, src)
            if not exists(path):
                raise FileNotFoundError(f'src not found: {path!r}')
    '''
    # NOTE: dst may be nonexist_basename!!
    #       now use tmp_prefix instead of nonexist_basename
    # check nonexist_basename not exists
    path = join(folder, nonexist_basename)
    if exists(path):
        raise FileExistsError(f'nonexist_basename exists: {path!r}')
    '''
    # check dst not exists
    for ls in basename_lsls:
        if ls[0] == ls[-1]: continue
        dst = ls[-1]
        path = join(folder, dst)
        if exists(path):
            raise FileExistsError(f'dst exists: {path!r}')


    ####
    basenames = set(chain.from_iterable(basename_lsls))
    tmp = TmpPath(folder, tmp_prefix, 0, '')
    tmp.many0_next_until_not_exists()
    while tmp.tmp_basename in basenames:
        tmp.many1_next_until_not_exists()

    # NOTE: dst may be a tmp_path
    for ls in basename_lsls:
        ls = list(ls)
        is_cycle = ls[0] == ls[-1]
        if is_cycle:
            if len(ls) == 2: continue
            #ls[-1] = nonexist_basename
            tmp.many0_next_until_not_exists()
            nonexist_basename = tmp.tmp_basename
            ls[-1] = nonexist_basename
            ls.insert(0, nonexist_basename)

        paths = [join(folder, basename) for basename in ls]
        dst = paths.pop()
        assert not exists(dst)
        while paths:
            src = paths.pop()
            assert exists(src) or (pseudo_rename is not None and is_cycle and not paths)
            rename(src, dst)
            dst = src
            assert not exists(dst) or (pseudo_rename is not None)

    return


def _test():
    f = _rename_under_same_folder

    import tempfile
    from seed.tiny import expectError


    def new_file(path, content):
        with open(path, 'xb') as fout:
            fout.write(content)
    def expectFile(path, content):
        with open(path, 'rb') as fin:
            bs = fin.read()
        return bs == content

    with tempfile.TemporaryDirectory() as tmp_folder:
        print(tmp_folder)
        basename1 = '1'
        basename2 = '2'
        basename3 = '3'
        path1 = join(tmp_folder, basename1)
        path2 = join(tmp_folder, basename2)
        path3 = join(tmp_folder, basename3)
        assert not exists(path1)
        assert not exists(path2)
        assert not exists(path3)

        new_file(path1, b'1')
        assert expectFile(path1, b'1')
        assert exists(path1)
        assert not exists(path2)

        f(tmp_folder, [[basename1, basename1]])
        assert exists(path1)
        assert not exists(path2)

        f(tmp_folder, [[basename1, basename2]])
        assert not exists(path1)
        assert exists(path2)

        expectError(OSError, lambda:f(tmp_folder, [[basename1, basename2]]))
        assert not exists(path1)
        assert exists(path2)

        new_file(path1, b'2')
        assert exists(path1)
        assert exists(path2)
        assert expectFile(path1, b'2')
        assert expectFile(path2, b'1')

        f(tmp_folder, [[basename1, basename2, basename1]])
        assert expectFile(path1, b'1')
        assert expectFile(path2, b'2')


        assert not exists(path3)
        f(tmp_folder, [[basename1, basename2, basename3]])
        assert not exists(path1)
        assert expectFile(path2, b'1')
        assert expectFile(path3, b'2')


if __name__ == '__main__':
    _test()

