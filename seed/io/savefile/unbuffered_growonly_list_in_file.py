r'''
e ../../python3_src/seed/io/savefile/unbuffered_growonly_list_in_file.py

vs:
    seed.io.savefile.unbuffered_growonly_list_in_file.UnbufferedGrowonlyListInFile
        no delete-/overwrite- operation
        growing-only
        flush-write when add new item
            to avoid loss data when power-down

    seed.io.savefile.SaveFile.SaveFileSeq__ObjectPerLine
        write when close:
            to avoid too many useless contents/history
            since there are delete-/overwrite- operation
from seed.io.savefile.unbuffered_growonly_list_in_file import tabular_cached_calc, UnbufferedGrowonlyListInFile
from seed.io.savefile.SaveFile import SaveFileSeq__ObjectPerLine


SaveFileSeq__ObjectPerLine(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)


UnbufferedGrowonlyListInFile(path_or_iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs, may_idx2default=may_idx2default, setitem_by_idx2default_only=True)

#'''

__all__ = '''
    UnbufferedGrowonlyListInFile

    tabular_cached_calc
    '''.split()

from collections.abc import Sequence#, MutableSequence, MutableMapping, MutableSet
#from seed.io.savefile.SaveFile import SaveFileSeq__ObjectPerLine
from seed.io.savefile.SaveFile import SaveFileMethods__ObjectPerLine, SaveFileSeqABC#, SaveFileContainerABC
from seed.tiny import check_type_is #check_bool
from seed.abc.abc__ver0 import override#, abstractmethod, ABC# final
from itertools import chain


def _flush(ofile, /):
    ofile.flush()

class UnbufferedGrowonlyListInFile(
    SaveFileMethods__ObjectPerLine
    ,SaveFileSeqABC
    #, SaveFileContainerABC
    , Sequence
    ):
    @override
    def __init__(self, path_or_iofile, *
        , allow_create_file
        , allow_write_file
        , allow_write_header
        , encoding
        , kwargs
        ######new args:
        , may_idx2default
        , setitem_by_idx2default_only
        ):
        if not (may_idx2default is None or callable(may_idx2default)): raise TypeError
        #check_bool(setitem_by_idx2default_only)
        check_type_is(bool, setitem_by_idx2default_only)
        self._may_idx2default = may_idx2default
        self._setitem_by_idx2default_only = setitem_by_idx2default_only
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
        pass
    @override
    def _close_(self):
        pass


    @override
    def append(self, v):
        self._set_new_item__tmay(len(self), (v,))

    if 0:
        def __miss__(self, j):
            raise IndexError(j)
    def __getitem__(self, j):
        if not (type(j) is int and j > 0):
            return self._data[j]
        ####
        try:
            return self._data[j]
        except IndexError:
            if not (type(j) is int and j > len(self)): raise logic-err
            #v = type(self).__miss__(self, j)
            m = self._may_idx2default
            if m is None:
                raise
            idx2default = m
            #v = idx2default(j)
            self._set_new_item__tmay(j, ())
            return self[j]
        #return self._data[j]
        raise logic-err

    def __setitem__(self, j, v):
        if self._setitem_by_idx2default_only:
            raise IndexError('growing-only: forbid set-new-item-bypass-idx2default') #IndexError#TypeError
        self._set_new_item__tmay(j, (v,))
    def __extend__vs(self, vs):
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        for v in vs:
            aSaveFile.write_body(ofile, [v])
            _flush(ofile)
            self._data.append(v)
    def _set_new_item__tmay(self, j, tmay_v):
        check_type_is(int, j)
        if not j >= len(self):
            raise IndexError('growing-only: forbid overwrite') #IndexError#TypeError
        L = len(self)
        L_ = j+1 if not tmay_v else j

        if not (tmay_v and L == j):
            m = self._may_idx2default
            if m is None:
                raise IndexError(f'missing self[{L}:{j+1}]')
            idx2default = m
            #v = idx2default(j)
            ex = map(idx2default, range(L, L_))
        else:
            ex = ()
        if 0:
            ex = [*ex, *tmay_v]
            assert len(self) + len(ex) == j+1

            aSaveFile = self._get_SaveFile()
            ofile = self._iofile
            aSaveFile.write_body(ofile, ex)
            _flush(ofile)
            self._data.extend(ex)
            assert len(self) == j+1
        else:
            ex = chain(ex, tmay_v)
            self.__extend__vs(ex)

    def __delitem__(self, j):
        raise IndexError('growing-only: forbid delete') #IndexError#TypeError
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __contains__(self, v):
        return v in self._data



def tabular_cached_calc(path_or_iofile, calc, kwargs_as_description4ofile, /, *, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, setitem_by_idx2default_only=True):
    #if not callable(calc): raise TypeError
    return UnbufferedGrowonlyListInFile(path_or_iofile, encoding=encoding, allow_create_file=allow_create_file, allow_write_file=allow_write_file, allow_write_header=allow_write_header, kwargs=kwargs_as_description4ofile, may_idx2default=calc, setitem_by_idx2default_only=setitem_by_idx2default_only)


