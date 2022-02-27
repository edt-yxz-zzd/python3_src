r'''
see: py::contextlib.AbstractContextManager/@contextlib.contextmanager'

intend: show API here only, donot use this module
#'''

raise see-contextlib.AbstractContextManager

from seed.abc.abc import abstractmethod, ABC
class IContextManager(ABC):
    'see: py::contextlib.AbstractContextManager/@contextlib.contextmanager'
    __slots__ = ()

    @abstractmethod
    def __enter__(self, /):
        r'''
        Enter the runtime context related to this object. The with statement will bind this method’s return value to the target(s) specified in the as clause of the statement, if any.
        #'''

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback, /):
        r'''
        Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.

        If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.

        Note that __exit__() methods should not reraise the passed-in exception; this is the caller’s responsibility.
        #'''
        return None#reraise


