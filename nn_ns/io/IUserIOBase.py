
__all__ = '''
    IUserIOBase
    UserIOBase
    IUserIOBase__aspect
    '''.split()

from io import BufferedIOBase, IOBase
from abc import abstractmethod, ABC

class IUserIOBase(ABC):
    # IOBase has not public constructor
    #   so, IOBase is not a base of IUserIOBase

    @abstractmethod
    def get_underlying_io(self):
        raise NotImplementedError

    @property
    def closed(self):
        return self.get_underlying_io().closed

    def close(self):
        return self.get_underlying_io().close()
    def fileno(self):
        return self.get_underlying_io().fileno()
    def flush(self):
        return self.get_underlying_io().flush()
    def isatty(self):
        return self.get_underlying_io().isatty()
    def readable(self):
        return self.get_underlying_io().readable()
    def readline(self, size=-1):
        return self.get_underlying_io().readline(size)
    def readlines(self, hint=-1):
        return self.get_underlying_io().readlines(hint)
    def seek(self, offset, whence=0):
        return self.get_underlying_io().seek(offset, whence)
    def seekable(self):
        return self.get_underlying_io().seekable()
    def tell(self):
        return self.get_underlying_io().tell()
    def truncate(self, size=None):
        return self.get_underlying_io().truncate()
    def writable(self):
        return self.get_underlying_io().writable()
    def writelines(self, lines):
        return self.get_underlying_io().writelines(lines)
    def __del__(self):
        io = self.get_underlying_io()
        cls = type(io)
        cls.__del__(io)

IOBase.register(IUserIOBase)


class UserIOBase(IUserIOBase):
    def __init__(self, io):
        self.__io = io
    def get_underlying_io(self):
        return self.__io





class IUserIOBase__aspect(IUserIOBase):
    @abstractmethod
    def before_io(self):
        raise NotImplementedError
    @abstractmethod
    def after_io(self):
        raise NotImplementedError

    '''
    def before_io(self):
        return
    def after_io(self):
        return
    '''

    def flush(self):
        self.before_io()
        try:
            return self.get_underlying_io().flush()
        finally:
            self.after_io()
    def readline(self, size=-1):
        self.before_io()
        try:
            return self.get_underlying_io().readline(size)
        finally:
            self.after_io()
    def readlines(self, hint=-1):
        self.before_io()
        try:
            return self.get_underlying_io().readlines(hint)
        finally:
            self.after_io()
    def seek(self, offset, whence=0):
        self.before_io()
        try:
            return self.get_underlying_io().seek(offset, whence)
        finally:
            self.after_io()

    def truncate(self, size=None):
        self.before_io()
        try:
            return self.get_underlying_io().truncate()
        finally:
            self.after_io()
    def writelines(self, lines):
        self.before_io()
        try:
            return self.get_underlying_io().writelines(lines)
        finally:
            self.after_io()



if __name__ == '__main__':
    XXX = IUserIOBase
    from seed.helper.print_methods import print_methods, wrapped_print_methods
    wrapped_print_methods(XXX)


    from io import BytesIO
    UserIOBase(BytesIO())



