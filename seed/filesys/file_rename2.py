
r'''
seed.filesys.file_rename2
from seed.filesys.file_rename2 import rename_file

seed.filesys.file_rename2.rename_file vs seed.filesys.file_rename.rename_file
    ver2:
        * using keyword-parameter
        * allow args be not Path
        * allow to_fname==from_fname


#'''

__all__ = ['rename_file']

from pathlib import Path

def rename_file(*, from_fname, to_fname):
    if type(from_fname) is not Path:
        from_fname = Path(from_fname)
    if type(to_fname) is not Path:
        to_fname = Path(to_fname)

    if not from_fname.exists():
        raise FileNotFoundError(from_fname)
    elif to_fname.exists():
        if to_fname.samefile(from_fname):
            #do nothing
            pass
        else:
            raise FileExistsError(to_fname)
    else:
        from_fname.rename(to_fname)
    return


