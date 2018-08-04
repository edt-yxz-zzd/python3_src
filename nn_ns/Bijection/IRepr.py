

__all__ = 'IRepr'.split()

from abc import ABCMeta, abstractmethod
from .import_repr_helper import repr_helper, repr_helper__str


class IRepr(metaclass=ABCMeta):
    @abstractmethod
    def get_construct_info(self):
        # return:
        #   1) the_name:str
        #       self == eval(the_name)
        #   2) input:(args, kwargs)
        #       self == type(self)(*args, **kwargs)
        #   3) (constructor_name:str, input:(args, kwargs))
        #       self = eval(constructor_name)(*args, **kwargs)
        pass

    def make_name_args_kwargs(self, name, *args, **kwargs):
        return name, (args, kwargs)
    def make_args_kwargs(self, *args, **kwargs):
        return (args, kwargs)
    def __repr__(self):
        r = self.get_construct_info()
        if type(r) is str:
            #   1) the_name:str
            the_name = r
            return the_name

        assert type(r) is tuple
        fst, snd = r
        if type(fst) is tuple:
            #   2) input:(args, kwargs)
            args, kwargs = r
            assert type(args) is tuple
            return repr_helper(self, *args, **kwargs)

        assert type(fst) is str
        #   3) (constructor_name:str, input:(args, kwargs))
        constructor_name, (args, kwargs) = r
        assert type(args) is tuple
        return repr_helper__str(constructor_name, *args, **kwargs)


