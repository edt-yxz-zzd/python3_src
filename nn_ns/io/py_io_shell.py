
r"""

py shell
  iter chain cmd

read -e utf8 fin | ... | write x -e utf8

#"""


from abc import ABC, abstractmethod #, override, not_implemented, ABCMeta


class IStreamElementType(ABC):
    def is_stream_element(self, x):
        r = self._is_stream_element_(x)
        if type(r) is not bool: raise TypeError
        return r
        return bool(r)
    def le_stream_element_type(self, other):
        if other is self:
            return True
        if not isinstance(other, IStreamElementType):
            raise TypeError

        if 1:
            r = self <= other
        else:
            r = type(self).__le__(self, other)
            if r is NotImplemented:
                r = type(other).__ge__(other, self)
                if r is NotImplemented:
                    raise NotImplementedError(f'non-comparable: {type(self)} <= {type(other)}')
                pass
            pass
        pass
        if type(r) is not bool: raise TypeError
        return r
        return bool(r)
    @abstractmethod
    def _is_stream_element_(self, x):
        raise NotImplementedError or TypeError
    @abstractmethod
    def __le__(self, other):
        return NotImplemented
        raise NotImplementedError or TypeError or NotImplemented
    @abstractmethod
    def __ge__(self, other):
        return NotImplemented
        raise NotImplementedError or TypeError or NotImplemented


class IStreamFilterMaker(ABC):
    def get_may_input_element_type(self)->'None|IStreamElementType':
        m = self._get_may_input_element_type_()
        if not (m is None or isinstance(m, IStreamElementType)): raise TypeError
        return m
    def get_may_output_element_type(self)->'None|IStreamElementType':
        m = self._get_may_output_element_type_()
        if not (m is None or isinstance(m, IStreamElementType)): raise TypeError
        return m
    def mk(self, may_input_worker:'None|IStreamFilterWorker')->'IStreamFilterWorker':
        may_input_element_type = self.get_may_input_element_type()
        if (may_input_element_type is None) != (may_input_worker is None): raise TypeError
        if may_input_worker is not None:
            input_worker = may_input_worker
            required_input_element_type = may_input_element_type
            assert required_input_element_type is not None
            actual_may_input_element_type = input_worker.get_maker().get_may_output_element_type()
            if actual_may_input_element_type is None: raise TypeError
            actual_input_element_type = actual_may_input_element_type
            if not actual_input_element_type.le_stream_element_type(required_input_element_type): raise TypeError
        worker = self._mk_(may_input_worker)
        if not isinstance(worker, IStreamFilterWorker): raise TypeError
        if worker.get_maker() is not self: raise ValueError
        return worker

    @abstractmethod
    def _get_may_input_element_type_(self)->'None|IStreamElementType':
        raise NotImplementedError or None
    @abstractmethod
    def _get_may_output_element_type_(self)->'None|IStreamElementType':
        raise NotImplementedError or None
    @abstractmethod
    def _mk_(self, may_input_worker:'None|IStreamFilterWorker')->'IStreamFilterWorker':
        raise NotImplementedError
class IStreamFilterWorker(ABC):
    def get_maker(self)->'IStreamFilterMaker':
        r = self._get_maker_()
        if not isinstance(r, IStreamFilterMaker): raise TypeError
        return r
    def unsafe_get_stdin(self):
        assert self.get_maker().get_may_input_element_type() is not None
        return self._get_stdin_()
    def unsafe_iter(self):
        assert self.get_maker().get_may_output_element_type() is not None
        decl_output_element_type = self.get_maker().get_may_output_element_type()
        f = decl_output_element_type.is_stream_element
        for x in self._iter_():
            assert f(x)
            yield x
    def unsafe_run(self):
        assert self.get_maker().get_may_output_element_type() is None
        return self._run_()

    @abstractmethod
    def _get_maker_(self)->'IStreamFilterMaker':
        raise NotImplementedError
    @abstractmethod
    def _get_stdin_(self):
        '@maker.get_may_input_element_type() is not None'
        raise NotImplementedError
    @abstractmethod
    def _iter_(self):
        '@maker.get_may_output_element_type() is not None'
        raise NotImplementedError
    @abstractmethod
    def _run_(self):
        '@maker.get_may_output_element_type() is None'
        raise NotImplementedError




r"""

class XXX_as_StreamElementType(IStreamElementType):
    def _is_stream_element_(self, x):
        assert isinstance(x, self.py_types)
        assert not self.free
    def __le__(self, other):
        return NotImplemented
    def __ge__(self, other):
        return NotImplemented
#"""

class Object_as_StreamElementType(IStreamElementType):
    py_types = (object,)
    free = True
    def _is_stream_element_(self, x):
        assert isinstance(x, self.py_types)
        assert not self.free
        return NotImplemented
    def __le__(self, other):
        if type(self) is type(other):
            return True
        elif (isinstance(other, Object_as_StreamElementType)
            and other.free
            and all(issubclass(t, other.py_types) for t in self.py_types)
            ):
            return True

        return NotImplemented
    def __ge__(self, other):
        return NotImplemented

class String_as_StreamElementType(Object_as_StreamElementType):
    py_types = (str,)



