
__all__ = '''
    IUserBufferedIOBase
    UserBufferedIOBase
    IUserBufferedIOBase__aspect
    '''.split()

from io import BufferedIOBase, IOBase
from abc import abstractmethod, ABC

from .IUserIOBase import IUserIOBase, UserIOBase, IUserIOBase__aspect

class IUserBufferedIOBase(IUserIOBase):
    # BufferedIOBase has not public constructor
    #   so, BufferedIOBase is not a base of IUserBufferedIOBase
    def detach(self):
        return self.get_underlying_io().detach()
    def read(self, size=-1):
        return self.get_underlying_io().read(size)
    def read1(self, size=-1):
        return self.get_underlying_io().read1(size)
    def write(self, bs):
        return self.get_underlying_io().write(bs)

    def readinto(self, bs):
        return self.get_underlying_io().readinto(bs)
    def readinto1(self, bs):
        return self.get_underlying_io().readinto1(bs)
BufferedIOBase.register(IUserBufferedIOBase)


class UserBufferedIOBase(UserIOBase, IUserBufferedIOBase):
    pass


class IUserBufferedIOBase__aspect(IUserBufferedIOBase, IUserIOBase__aspect):
    def read(self, size=-1):
        self.before_io()
        try:
            return self.get_underlying_io().read(size)
        finally:
            self.after_io()
    def read1(self, size=-1):
        self.before_io()
        try:
            return self.get_underlying_io().read1(size)
        finally:
            self.after_io()
    def write(self, bs):
        self.before_io()
        try:
            return self.get_underlying_io().write(bs)
        finally:
            self.after_io()

    def readinto(self, bs):
        self.before_io()
        try:
            return self.get_underlying_io().readinto(bs)
        finally:
            self.after_io()
    def readinto1(self, bs):
        self.before_io()
        try:
            return self.get_underlying_io().readinto1(bs)
        finally:
            self.after_io()


if __name__ == '__main__':
    XXX = IUserBufferedIOBase
    from seed.helper.print_methods import print_methods, wrapped_print_methods
    wrapped_print_methods(XXX)


    from io import BytesIO
    UserBufferedIOBase(BytesIO())





