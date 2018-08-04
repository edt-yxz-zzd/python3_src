
__all__ = '''
    IUserRawIOBase
    UserRawIOBase
    IUserRawIOBase__aspect
    '''.split()

from io import RawIOBase, IOBase
from abc import abstractmethod, ABC

from .IUserIOBase import IUserIOBase, UserIOBase, IUserIOBase__aspect


class IUserRawIOBase(IUserIOBase):
    # RawIOBase has not public constructor
    #   so, RawIOBase is not a base of IUserRawIOBase
    def read(self, size=-1):
        return self.get_underlying_io().read(size)
    def readall(self):
        return self.get_underlying_io().readall()

    def readinto(self, bs):
        return self.get_underlying_io().readinto(bs)
    def write(self, bs):
        return self.get_underlying_io().write(bs)
RawIOBase.register(IUserRawIOBase)


class UserRawIOBase(UserIOBase, IUserRawIOBase):
    pass


class IUserRawIOBase__aspect(IUserRawIOBase, IUserIOBase__aspect):
    def read(self, size=-1):
        self.before_io()
        try:
            return self.get_underlying_io().read(size)
        finally:
            self.after_io()
    def readall(self):
        self.before_io()
        try:
            return self.get_underlying_io().readall()
        finally:
            self.after_io()

    def readinto(self, bs):
        self.before_io()
        try:
            return self.get_underlying_io().readinto(bs)
        finally:
            self.after_io()
    def write(self, bs):
        self.before_io()
        try:
            return self.get_underlying_io().write(bs)
        finally:
            self.after_io()



if __name__ == '__main__':
    XXX = IUserRawIOBase
    from seed.helper.print_methods import print_methods, wrapped_print_methods
    wrapped_print_methods(XXX)


    #from io import FileIO
    #UserRawIOBase(FileIO())
    from io import BytesIO
    # BytesIO is not RawIOBase, but ...
    UserRawIOBase(BytesIO()) # test not abstract class





