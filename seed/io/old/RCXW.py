
'''
OO-version of read_or_calc_xwrite


Ixxxx is a class that need not __init__, and almost abstract class
'''




from abc import abstractmethod, ABCMeta
from seed.io.Args import Args, act, isArgs
import pickle, json

class Read_Or_CalcXWrite(metaclass=ABCMeta):
    '''
example:
    def read_or_calc_xwrite (excepts)
                            (calc_func, c...)
                            (write_func, w...)
                            (read_func, r...):
        try:
            return read(r...)
        except excepts:
            v = calc_func(c...)
            write_func(v, w...)
            return v

    '''

    # abstractmethod:
    #   _catched_RCXW_read_ExceptionTypes_
    #   _read_
    #   _calc_
    #   _write_

    def _check_RCXW_Exceptions_(self, e)->None:
        # if this exception should raise, then raise in this func
        return
    @abstractmethod
    def _catched_RCXW_read_ExceptionTypes_(self):
        # return Exception-subtype | tuple of Exception-subtypes
        raise NotImplementedError
    @abstractmethod
    def _read_(self):
        # return value or raise one of the _RCXW_Exceptions_
        raise NotImplementedError
    @abstractmethod
    def _calc_(self):
        # return value
        raise NotImplementedError
    @abstractmethod
    def _write_(self, value)->None:
        raise NotImplementedError
    def __call__(self):
        # return value
        try:
            return self._read_()
        except self._catched_RCXW_read_ExceptionTypes_() as e:
            self._check_RCXW_Exceptions_(e)
        v = self._calc_()
        self._write_(v)
        return v

IRCXW = Read_Or_CalcXWrite











class IReadArgs(metaclass=ABCMeta):
    # have .read_args
    @abstractmethod
    def get_read_args(self):
        raise NotImplementedError
    pass
class ReadArgs(IReadArgs):
    # e.g. pickle.load errors
    def __init__(self, args:Args):
        assert isArgs(args)
        self.read_args = args
    def get_read_args(self):
        return self.read_args
class IWriteArgs(metaclass=ABCMeta):
    # have .write_args
    @abstractmethod
    def get_write_args(self):
        raise NotImplementedError
    pass
class WriteArgs(IWriteArgs):
    # e.g. pickle.dump protocol
    def __init__(self, args:Args):
        assert isArgs(args)
        self.write_args = args
    def get_write_args(self):
        return self.write_args

class ICalcArgs(metaclass=ABCMeta):
    # have .calc_args
    @abstractmethod
    def get_calc_args(self):
        raise NotImplementedError
    pass
class CalcArgs(ICalcArgs):
    def __init__(self, args:Args):
        assert isArgs(args)
        self.calc_args = args
    def get_calc_args(self):
        return self.calc_args

class IRCXW_G_Calc(IRCXW, ICalcArgs):
    # generic _calc_
    def _calc_(self):
        return act(self.calc_args)





class IFileRW(metaclass=ABCMeta):
    @abstractmethod
    def open_read_file(self):
        raise NotImplementedError
    @abstractmethod
    def open_write_file(self):
        raise NotImplementedError




class IRCXW_File(IRCXW, IFileRW):
    @abstractmethod
    def _read_file_(self, file_obj):
        raise NotImplementedError
    @abstractmethod
    def _write_file_(self, file_obj, value):
        raise NotImplementedError


    def _read_(self):
        with self.open_read_file() as fin:
            return self._read_file_(fin)
    def _write_(self, v):
        with self.open_write_file() as fout:
            return self._write_file_(fout, v)


    def _catched_RCXW_read_ExceptionTypes_(self):
        return FileNotFoundError



class IRW_Args_RCXW_File(IReadArgs, IWriteArgs, IRCXW_File):pass
class IRCXW_Pickle(IRW_Args_RCXW_File):
    def _read_file_(self, file_obj):
        return self.read_args.call_self_after(pickle.load, file_obj)
    def _write_file_(self, file_obj, value):
        return self.write_args.call_self_after(pickle.dump, value, file_obj)



#IRCXW_Pickle()
#   missing: _calc_, open_read_file, open_write_file
#   missing: get_calc_args, get_read_args, get_write_args






def make_txtbin_mode(open_in_binary):
    return 'b' if open_in_binary else 't'
def make_read_mode():
    return 'r'
def make_write_mode(force_write):
    return 'w' if force_write else 'x'

def make_readwrite_mode(open_in_binary, force_write):
    tb_mode = make_txtbin_mode(open_in_binary)
    read_mode = make_read_mode()
    write_mode = make_write_mode(force_write)
    read_mode += tb_mode
    write_mode += tb_mode
    return read_mode, write_mode

class FileRW(IFileRW):
    def __init__(self, file:'open(file,...)', args:Args
                , *, open_in_binary:bool, force_write:bool):
        # open() args kwargs except mode
        assert isArgs(args)
        read_write_mode = make_readwrite_mode(open_in_binary, force_write)
        #self.open_args = file, read_write_mode, args
        read_mode, write_mode = read_write_mode
        read_args = args.new_self_after(file, read_mode)
        write_args = args.new_self_after(file, write_mode)
        self.open_args = read_args, write_args

    def open_read_file(self):
        read_args, _ = self.open_args
        return read_args.call(open)
        file, (read_mode, _), args = self.open_args
        return args.call_self_after(open, file, read_mode)
        file, (read_mode, _), args, kws = self.open_args
        return open(file, read_mode, *args, **kws)

    def open_write_file(self):
        _, write_args = self.open_args
        return write_args.call(open)
        file, (_, write_mode), args, kws = self.open_args
        return open(file, write_mode, *args, **kws)


# IRCXW_Pickle + FileRW
# class RCXW_Pickle_FileRW(IRCXW_Pickle, FileRW): pass
# RCXW_Pickle_FileRW()
#   missing: _calc_
#   missing: get_calc_args, get_read_args, get_write_args

# IRCXW_G_Calc + IRCXW_Pickle + FileRW
#class RCXW_GCalc_Pickle_FileRW(IRCXW_G_Calc, IRCXW_Pickle, FileRW): pass
#RCXW_GCalc_Pickle_FileRW()
#   missing: get_calc_args, get_read_args, get_write_args

class RWC_Args(ReadArgs, WriteArgs, CalcArgs):
    def __init__(self, read_args, write_args, calc_args):
        ReadArgs.__init__(self, read_args)
        WriteArgs.__init__(self, write_args)
        CalcArgs.__init__(self, calc_args)

class RWCO_Args(RWC_Args, FileRW):
    def __init__(self, read_args:Args, write_args:Args, calc_args:Args
                , file:'open(file,...)', open_args:Args
                , *, open_in_binary:bool, force_write:bool):
        assert isArgs(open_args)
        FileRW.__init__(self, file, open_args
                        , open_in_binary=open_in_binary
                        , force_write=force_write)
        RWC_Args.__init__(self, read_args, write_args, calc_args)


class RCXW_Pickle_GCalc_RWCO_Args(IRCXW_Pickle, IRCXW_G_Calc, RWCO_Args): pass
#RCXW_Pickle_GCalc_RWCO_Args()

_empty_args = Args()
def make_rcxw__pickle(calc_func, fname, *, force_write=False):
    return RCXW_Pickle_GCalc_RWCO_Args(
        _empty_args, _empty_args, Args(calc_func)
        , fname, _empty_args, open_in_binary=True, force_write=force_write)






class IRCXW_Json(IRW_Args_RCXW_File):
    def _read_file_(self, file_obj):
        return self.read_args.call_self_after(json.load, file_obj)
    def _write_file_(self, file_obj, value):
        return self.write_args.call_self_after(json.dump, value, file_obj)
class RCXW_Json_GCalc_RWCO_Args(IRCXW_Json, IRCXW_G_Calc, RWCO_Args): pass
def make_rcxw__json(calc_func, fname, *, force_write=False
                    , read_args=_empty_args, write_args=_empty_args
                    , open_args=_empty_args):
    return RCXW_Json_GCalc_RWCO_Args(
        read_args, write_args, Args(calc_func)
        , fname, open_args, open_in_binary=False, force_write=force_write)






class IRCXW_Text(IRW_Args_RCXW_File):
    def _read_file_(self, file_obj):
        return file_obj.read()
        return self.read_args.call_self_after(file_obj.read)
    def _write_file_(self, file_obj, value):
        file_obj.write(value)
        return
        return self.write_args.call_self_after(file_obj.write, value)
class RCXW_Text_GCalc_RWCO_Args(IRCXW_Text, IRCXW_G_Calc, RWCO_Args): pass
def make_rcxw__text(calc_func, fname, *, force_write=False
                    , encoding='utf8', open_args=_empty_args):
    open_args = open_args.new_ex(None, None, encoding=encoding)
    return RCXW_Text_GCalc_RWCO_Args(
        _empty_args, _empty_args, Args(calc_func)
        , fname, open_args, open_in_binary=False, force_write=force_write)











'''
#
class OpenArgs(FileRW):
    def __init__(self, file:'open(file,...)', args:Args
                , *, open_in_binary:bool, force_write:bool):
        super().__init__(file, args
                        , open_in_binary=open_in_binary
                        , force_write=force_write)







class RCXW_File_Args(IRCXW_File, RWCO_Args):
    pass
#class RCXW_Pickle_GCalc(RCXW_File_Args, )
'''



