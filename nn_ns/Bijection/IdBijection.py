
__all__ = '''
    id_bijection
    id_of
    is_IdBijection
    '''.split()

from .Bijection import Bijection
from .TypeVerifier import TypeVerifier
from .AnyHashableTV import Any

class IdBijection(Bijection):
    def __init__(self, io_type = Any):
        assert isinstance(io_type, TypeVerifier)
        self.io_type = io_type

    def is_idBJ(self):
        return True
    def get_InputType(self):
        return self.io_type
    def get_OutputType(self):
        return self.io_type
    def untypechecked_forward(self, input):
        return input
    def untypechecked_backward(self, output):
        return output

    def get_construct_info(self):
        return self.make_args_kwargs(self.io_type)

    def __repr__(self):
        return '{!r}.idBJ'.format(self.io_type)

id_bijection = IdBijection()
def id_of(io_type):
    return IdBijection(io_type)
def is_IdBijection(bj):
    return type(bj) == IdBijection

