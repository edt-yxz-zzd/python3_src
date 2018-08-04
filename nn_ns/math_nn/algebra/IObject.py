

ABCMeta
ISet


class IObject(metaclass=ABCMeta):
    def _get_Sets(self):
    def _get_object(self):

    def get_Sets(self):
        Sets = self._get_Sets()
        assert type(Sets) is tuple
        assert all(isinstance(s, ISet) for s in Sets)
        return Sets
    def get_object(self):
        obj = self._get_object()
        if __debug__: Sets = self.get_Sets()
        assert all(s.is_element(obj) for s in Sets)
        return obj


class PyTypeAsSet(ISet):
    def __init__(self, py_type):
        assert isinstance(py_type, type), TypeError
        self.py_type = py_type
    def is_element(self, obj):
        return type(obj) is self.py_type
PyIntSet = PyTypeAsSet(int)
class IIntObject(IObject):
    def _get_Sets(self):
        return (PyIntSet,)

class IPrimeIntObject(IIntObject):pass

