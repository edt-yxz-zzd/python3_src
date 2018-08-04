
__all__ = '''
    Newtype
    NewtypeWithMultiArgs
'''.split()

from seed.helper.repr_input import repr_helper


class Newtype:
    __slots__ = ('_Newtype__data',)
    def __init__(self, underly_obj):
        self.__data = (type(self), underly_obj)
    def unbox(self):
        return self.__data[1]

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() == other.unbox()
    def __ne__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() != other.unbox()
    def __lt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() < other.unbox()
    def __le__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() <= other.unbox()
    def __gt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() > other.unbox()
    def __ge__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.unbox() >= other.unbox()
    def __repr__(self):
        return repr_helper(self, self.unbox())
        return '{}({!r})'.format(type(self).__name__, self.unbox())
    def __hash__(self):
        return hash((type(self), self.__data))
    def __bool__(self):
        return bool(self.unbox())



class NewtypeWithMultiArgs(Newtype):
    def __init__(self, *args):
        super().__init__(args)
    def __repr__(self):
        return repr_helper(self, *self.unbox())
        args = self.unbox()
        cls_name = type(self).__name__
        if len(args) == 1:
            return '{}({})'.format(cls_name, args[0])
        return '{}{}'.format(cls_name, args)
