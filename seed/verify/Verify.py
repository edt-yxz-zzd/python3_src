
__all__ = '''
    Verify
    '''.split()

from abc import ABC, abstractmethod
class Verify(ABC):
    # err_msg_or_f = err_msg | mk_err_msg
    # err_msg is not callable
    # mk_err_msg :: () -> err_msg

    #@abstractmethod
    def _iter_verify_type_(self, tp):
        # -> Iter (bool, err_msg_or_f)
        return iter('')
    #@abstractmethod
    def _iter_verify_object_(self, obj):
        # -> Iter (bool, err_msg_or_f)
        return iter('')



    def __new__(cls, __obj, __mkError=None, **kwargs):
        self = super().__new__(cls)
        self.obj = __obj
        self.maybe_mkError = __mkError
        self.__init__(**kwargs)
        return self.verify()


    def return_or_raise(self, err_msg_or_f):
        if self.maybe_mkError is None:
            return False
        else:
            mkError = self.maybe_mkError
            if callable(err_msg_or_f):
                mk_err_msg = err_msg_or_f
                err_msg = mk_err_msg()
            else:
                err_msg = err_msg_or_f
            raise mkError(err_msg)


    def verify_type(self, tp):
        # -> bool|raise ...
        # -> bool if self.__mkError is None
        # -> True | raise if self.__mkError is not None
        return self.__verify(self._iter_verify_type_(tp))

    def verify(self):
        # -> bool|raise ...
        # -> bool if self.__mkError is None
        # -> True | raise if self.__mkError is not None
        return self.__verify(self.iter_verify())
    def __verify(self, it):
        for b, err_msg_or_f in it:
            assert type(b) is bool
            if not b:
                return self.return_or_raise(err_msg_or_f)
        return True
    def iter_verify(self):
        yield from self._iter_verify_type_(type(self.obj))
        yield from self._iter_verify_object_(self.obj)


'''
def is_UInt(i, Error=None):
    return type(i) is int and i > 0
def is_tuple(obj):
    return type(obj) is tuple

def is_pair(obj):
    return type(obj) is tuple and len(obj) == 2
'''

