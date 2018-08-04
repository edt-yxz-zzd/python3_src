

'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.fileformat.zip.move_last_zip_to

e.g.
    concat_files xxx.jpg yyy.rar

'''

__all__ = '''
    concat_files
    write_files
    '''.split()

from shutil import copyfileobj
from seed.filesys.check_paths_exist import check_paths_exist

def concat_files(out_fname, in_fnames, mode='a'):
    '''

mode = x | a | w

example:
    # test copyfileobj
    >>> from io import BytesIO as mk
    >>> fout = mk()
    >>> fout.write(b'0')
    1

    >>> fin1 = mk(b'1')
    >>> fin2 = mk(b'2')
    >>> copyfileobj(fin1, fout)
    >>> copyfileobj(fin2, fout)
    >>> fout.getvalue()
    b'012'


'''
    in_fnames = tuple(in_fnames)
    check_paths_exist(in_fnames)

    if len(mode) != 1 and mode not in 'xaw': raise ValueError

    mode += 'b'
    with open(out_fname, mode) as fout:
        write_files(fout, in_fnames)

def write_files(fout, in_fnames):
    in_fnames = tuple(in_fnames)
    check_paths_exist(in_fnames)

    for fname in in_fnames:
        with open(fname, 'rb') as fin:
            copyfileobj(fin, fout)


def _test():
    from tempfile import TemporaryFile, NamedTemporaryFile
    import os
    import sys

    def removes(locals, *fnames):
        locals = dict(locals)
        err_fnames = []
        for fname in fnames:
            if fname in locals:
                try:
                    os.remove(fname)
                except Exception as e:
                    print(fname, file=sys.stderr)
                    err_fnames.append((fname, e))
                    #raise
                except:
                    print(fname, file=sys.stderr)
                    raise

        if err_fnames:
            raise Exception(err_fnames)

    fname0, fname1, fname2 = [None]*3
    def read(fname):
        with open(fname, 'rb') as fin:
            return fin.read()

    try:
        with NamedTemporaryFile(delete=False) as file0:
            fname0 = file0.name
            file0.write(b'0')
        with NamedTemporaryFile(delete=False) as file1:
            fname1 = file1.name
            file1.write(b'1')
        with NamedTemporaryFile(delete=False) as file2:
            fname2 = file2.name
            file2.write(b'2')

        concat_files(fname0, [fname1, fname2], mode='a')
        assert read(fname0) == b'012'

        concat_files(fname0, [fname1, fname2])
        assert read(fname0) == b'01212'

        concat_files(fname0, [fname1, fname2], mode='w')
        assert read(fname0) == b'12'

        try:
            concat_files(fname0, [fname1, fname2], mode='x')
        except FileExistsError:
            pass
        except:
            assert False
        else:
            assert False
    finally:
        try:
            removes(locals(), fname0, fname1, fname2)
        except:
            print('\n'.join([fname0, fname1, fname2]), file=sys.stderr)
            raise



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    _test()

