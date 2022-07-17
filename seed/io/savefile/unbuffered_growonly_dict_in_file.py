r'''
e ../../python3_src/seed/io/savefile/unbuffered_growonly_dict_in_file.py
    #deprecated:e ../../python3_src/seed/io/savefile/UnbufferedGrowonlyDictInFile.py
!mv ../../python3_src/seed/io/savefile/UnbufferedGrowonlyDictInFile.py ../../python3_src/seed/io/savefile/unbuffered_growonly_dict_in_file.py

vs:
    seed.io.savefile.unbuffered_growonly_dict_in_file.UnbufferedGrowonlyDictInFile
        no delete-/overwrite- operation
        growing-only
        write when add new item
            to avoid loss data when power-down

    seed.io.savefile.SaveFile.SaveFileDict
        write when close:
            to avoid too many useless contents/history
            since there are delete-/overwrite- operation
from seed.io.savefile.unbuffered_growonly_dict_in_file import tabular_cached_calc, UnbufferedGrowonlyDictInFile, UnbufferedDictInFile
from seed.io.savefile.SaveFile import SaveFileDict


SaveFileDict(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)

UnbufferedDictInFile(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)

UnbufferedGrowonlyDictInFile(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs, may_key2default=may_key2default, setitem_by_key2default_only=True)

#'''

__all__ = '''
    UnbufferedGrowonlyDictInFile
    UnbufferedDictInFile

    tabular_cached_calc
    '''.split()

from collections.abc import MutableMapping#, Sequence, MutableSet
#from seed.io.savefile.SaveFile import SaveFileDict
from seed.io.savefile.SaveFile import SaveFileMethods__UpdatableDict, SaveFileContainerABC, SaveFile__UpdatableDict
from seed.tiny import check_type_is #check_bool
from seed.abc.abc__ver0 import override#, abstractmethod, ABC# final

#from seed.types.GrowingDict import GrowingDict
#view ../../python3_src/seed/types/GrowingDict.py

def _flush(ofile, /):
    ofile.flush()
class UnbufferedDictInFile(
    SaveFileMethods__UpdatableDict
    , SaveFileContainerABC
    , MutableMapping
    ):
    @override
    def _init_(self):
        pass
    @override
    def _close_(self):
        pass


    def __getitem__(self, k):
        return self._data[k]
    def __setitem__(self, k, v):
        case = SaveFile__UpdatableDict.caseNEWorOVERWRITE
            #caseOVERWRITE
            #caseNEW
        case = caseOVERWRITE if k in self._data else caseNEW
        #may_old_v = self._data.get(k)
        self._data[k] = v
        #try:
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        aSaveFile.write_item(ofile, case, k, v)
        _flush(ofile)

    def __delitem__(self, k):
        del self._data[k]
        case = SaveFile__UpdatableDict.caseDELETE
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        aSaveFile.write_item(ofile, case, k, None)
        _flush(ofile)
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __contains__(self, k):
        return k in self._data


class UnbufferedGrowonlyDictInFile(
    SaveFileMethods__UpdatableDict
    , SaveFileContainerABC
    , MutableMapping
    ):
    @override
    def __init__(self, path_or_iofile, *
        , allow_create_file
        , allow_write_file
        , allow_write_header
        , encoding
        , kwargs
        ######new args:
        , may_key2default
        , setitem_by_key2default_only
        ):
        if not (may_key2default is None or callable(may_key2default)): raise TypeError
        #check_bool(setitem_by_key2default_only)
        check_type_is(bool, setitem_by_key2default_only)
        self._may_key2default = may_key2default
        self._setitem_by_key2default_only = setitem_by_key2default_only
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

    @override
    def _init_(self):
        #self._data = GrowingDict(self._data)
        pass
    @override
    def _close_(self):
        pass


    if 0:
        def __miss__(self, k):
            raise KeyError(k)
    def __getitem__(self, k):
        if k not in self:
        #try:
            #return self._data[k]
        #except KeyError:
            #v = type(self).__miss__(self, k)
            m = self._may_key2default
            if m is None:
                raise
            key2default = m
            v = key2default(k)
            self._set_new_item(k, v)
            return self[k]
        return self._data[k]

    def __setitem__(self, k, v):
        if self._setitem_by_key2default_only:
            raise KeyError('growing-only: forbid set-new-item-bypass-key2default') #KeyError#TypeError
        self._set_new_item(k, v)
    def _set_new_item(self, k, v):
        if k in self._data:
            raise KeyError('growing-only: forbid overwrite') #KeyError#TypeError
        self._data[k] = v
        if 0:
            # __main__ 在作怪
            if k == 4:
                print(self._data)
                nm = 'xxxxxxx'
                if nm in globals():
                    raise Exception(k)
                globals()[nm] = 1
        case = SaveFile__UpdatableDict.caseNEW
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        aSaveFile.write_item(ofile, case, k, v)
        _flush(ofile)

    def __delitem__(self, k):
        raise KeyError('growing-only: forbid delete') #KeyError#TypeError
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __contains__(self, k):
        return k in self._data



def tabular_cached_calc(path_or_iofile, calc, kwargs_as_description4ofile, /, *, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, setitem_by_key2default_only=True):
    #if not callable(calc): raise TypeError
    return UnbufferedGrowonlyDictInFile(path_or_iofile, encoding=encoding, allow_create_file=allow_create_file, allow_write_file=allow_write_file, allow_write_header=allow_write_header, kwargs=kwargs_as_description4ofile, may_key2default=calc, setitem_by_key2default_only=setitem_by_key2default_only)


