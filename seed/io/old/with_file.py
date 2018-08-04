

'''
with-version of as_file/curry_file

close or not close?
    e.g. stdin and open(...)
'''

from seed.io.Args import Args
from abc import abstractmethod, ABCMeta
import sys

special_fname2file_obj_gettor = \
    { b'<stdin>':lambda:sys.stdin
    , b'<stdout>':lambda:sys.stdout
    , b'<stderr>':lambda:sys.stderr}

def open_file_ex(file, *args, **kwargs):
    fobj, to_close = None, False
    if type(file) is bytes:
        fobj = special_fname2file_obj_gettor.get(file)
    if fobj is not None:
        return fobj, to_close
    elif is_file_obj(file):
        fobj = file
    else:
        fobj = open(file, *args, **kwargs)
        to_close = True
    return fobj, to_close

def _t():
    import io
    f = io.StringIO()
    open(f) # not support file obj
    # and more important
    with open(stdin) as fin:
        ... # error since will close fin!
#_t()

class IClsArgs(metaclass=ABCMeta):
    # .cls2args :: bool
    @abstractmethod
    def _get_cls_args_(self, cls):
        # return self.cls2args[cls]
        raise NotImplementedError
    @abstractmethod
    def _set_cls_args_(self, cls, args):
        # self.cls2args[cls] = args
        raise NotImplementedError

class IWithObj(IClsArgs, metaclass=ABCMeta):
    @abstractmethod
    def _open_ex_(self):
        # return obj, to_close
        raise NotImplementedError
    def _close_(self, obj):
        # close
        obj.close()
    def __enter__(self):
        obj, to_close = self._open_ex_()
        self._set_cls_args_(__class__, (obj, to_close))
        return obj
    def __exit__(self, exc_type, exc_value, traceback):
        self.on_exit()
        self.close_on_exit()
        if exc_type is None:
            self.normal_exit()
            return
        else:
            handled = self.except2handled(exc_type, exc_value, traceback)
            assert type(handled) == bool
            return handled
    def normal_exit(self): pass
    def on_exit(self): pass
    def close_on_exit(self):
        obj, to_close = self._get_cls_args_(__class__)
        if to_close:
            self._close_(obj)

    def except2handled(self, exc_type, exc_value, traceback):
        # return handled :: bool
        return False


class ClsArgs(IClsArgs):
    # .cls2args :: bool
    def __init__(self, cls2args={}):
        self.cls2args = cls2args
    def _get_cls_args_(self, cls):
        return self.cls2args[cls]
    def _set_cls_args_(self, cls, args):
        self.cls2args[cls] = args


class WithOpen(IWithObj, ClsArgs):
    def __init__(self, *args, **kwargs):
        # open()'s args kwargs
        ClsArgs.__init__(self)
        self._set_cls_args_(__class__, Args(*args, **kwargs))
    def _open_ex_(self):
        args = self._get_cls_args_(__class__)
        return args.call(open_file_ex)


def to_with_file(file, *args, **kwargs):
    # if file is file obj, then not to be closed
    return WithOpen(file, *args, **kwargs)
def read_all(file, *args, **kwargs):
    fin = to_with_file(file, *args, **kwargs)
    with fin as fin:
        return fin.read()



