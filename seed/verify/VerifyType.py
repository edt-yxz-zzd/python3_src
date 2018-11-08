
__all__ = '''
    VerifyType
    VerifyType__static
    '''.split()

from .Verify import Verify
from inspect import isabstract
from abc import abstractmethod

class VerifyType(Verify):
    def __init__(self, types):
        # types :: type | tuple<types>
        self.types = types
    def _iter_verify_type_(self, tp):
        yield issubclass(tp, self.types), lambda:'{} is not {}'.format(tp, self.types)
        yield from super()._iter_verify_type_(tp)
class VerifyType__static(VerifyType):
    # require cls.types
    @abstractmethod
    def types():
        'require cls.types; cls.types = ...'
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if isabstract(cls): return
        if not hasattr(cls, 'types'): raise AttributeError

    def __init__(self):
        super().__init__(type(self).types)


