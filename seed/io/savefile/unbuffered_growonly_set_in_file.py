#__all__:goto
r'''
e ../../python3_src/seed/io/savefile/unbuffered_growonly_set_in_file.py

vs:
    seed.io.savefile.unbuffered_growonly_set_in_file.UnbufferedGrowonlySetInFile
        no delete-/overwrite- operation
        growing-only
        write when add new item
            to avoid loss data when power-down

    seed.io.savefile.SaveFile.SaveFileSet
        write when close:
            to avoid too many useless contents/history
            since there are delete-/overwrite- operation

from seed.io.savefile.unbuffered_growonly_set_in_file import mk_cached_set, UnbufferedGrowonlySetInFile, UnbufferedSetInFile
from seed.io.savefile.SaveFile import SaveFileSet

SaveFileSet(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)

UnbufferedSetInFile(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs, growing=False)

UnbufferedGrowonlySetInFile(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)


seed.io.savefile.unbuffered_growonly_set_in_file
py -m nn_ns.app.debug_cmd   seed.io.savefile.unbuffered_growonly_set_in_file -x
py -m nn_ns.app.doctest_cmd seed.io.savefile.unbuffered_growonly_set_in_file:__doc__ -ht #  -ff -v -df

#'''

__all__ = '''
    UnbufferedGrowonlySetInFile
    UnbufferedSetInFile

    mk_cached_set
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import MutableSet
#from seed.io.savefile.SaveFile import SaveFileSet
from seed.io.savefile.SaveFile import SaveFileMethods__UpdatableSet, SaveFileContainerABC, SaveFile__UpdatableSet
from seed.abc.abc__ver0 import override

#from seed.types.GrowingSet import GrowingSet
#view ../../python3_src/seed/types/GrowingSet.py

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is

___end_mark_of_excluded_global_names__0___ = ...


def _flush(ofile, /):
    ofile.flush()
class UnbufferedSetInFile(
    SaveFileMethods__UpdatableSet
    , SaveFileContainerABC
    , MutableSet
    ):
    @override
    def _init_(self):
        pass
    @override
    def _close_(self):
        pass

    def __contains__(self, x):
        return x in self._data
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def add(self, x):
        if x not in self:
            #case = SaveFile__UpdatableSet.caseADD
            case = SaveFile__UpdatableSet.caseNEW
            self._alter(case, x)
        return self._data.add(x)
    def discard(self, x):
        if self._growonly:
            raise TypeError('growing only set')

        if x in self:
            case = SaveFile__UpdatableSet.caseDELETE
            self._alter(case, x)
        return self._data.discard(x)

    def _alter(self, case, x):
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        aSaveFile.write_element(ofile, case, x)
        _flush(ofile)

    @override
    def __init__(self, path_or_iofile, *
        , allow_create_file
        , allow_write_file
        , allow_write_header
        , encoding
        , kwargs
        ######new args:
        , growonly
        ):
        check_type_is(bool, growonly)
        self._growonly = growonly
        super().__init__(path_or_iofile
        , allow_create_file
        = allow_create_file
        , allow_write_file
        = allow_write_file
        , allow_write_header
        = allow_write_header
        , encoding
        = encoding
        , kwargs
        = kwargs
        )




class UnbufferedGrowonlySetInFile(
    UnbufferedSetInFile
    ):
    @override
    def __init__(self, path_or_iofile, *
        , allow_create_file
        , allow_write_file
        , allow_write_header
        , encoding
        , kwargs
        ######no new args:
        ):
        super().__init__(path_or_iofile
        , allow_create_file
        = allow_create_file
        , allow_write_file
        = allow_write_file
        , allow_write_header
        = allow_write_header
        , encoding
        = encoding
        , kwargs
        = kwargs
        , growonly=True
        )
    def discard(self, x):
        raise TypeError('growing only set')



def mk_cached_set(path_or_iofile, kwargs_as_description4ofile, /, *, growonly=True, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True):
    return UnbufferedSetInFile(path_or_iofile, growonly=growonly, encoding=encoding, allow_create_file=allow_create_file, allow_write_file=allow_write_file, allow_write_header=allow_write_header, kwargs=kwargs_as_description4ofile)


from seed.io.savefile.unbuffered_growonly_set_in_file import mk_cached_set, UnbufferedGrowonlySetInFile, UnbufferedSetInFile
#from seed.io.savefile.SaveFile import SaveFileSet
from seed.io.savefile.unbuffered_growonly_set_in_file import *
