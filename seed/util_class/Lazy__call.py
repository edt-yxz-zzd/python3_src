
r'''
seed.util_class.Lazy__call
    required from seed.types.Tester+seed.types.TriBoolOps
from seed.util_class.Lazy__call import Lazy

see also:
    seed.util_class.Lazy
        copy from RecognizeSystem
    seed.util_class.Lazy__call
        required from seed.types.Tester+seed.types.TriBoolOps::LazyTriBoolOps

#'''


__all__ = '''
    Lazy
        Lazy__call
    Lazy__value
    Lazy__Exception
    Lazy__mk_Exception

    LazyError
    '''.split()





class Lazy__value:
    def __init__(sf, value, /):
        sf.__x = value
    def __call__(sf):
        return sf.__x
class Lazy__Exception:
    def __init__(sf, exc, /):
        sf.__x = exc
    def __call__(sf):
        raise sf.__x
class Lazy__call:
    'like promise/future for async/concurrent eval'
    def __init__(sf, f, /, *args, **kwargs):
        if not callable(f): raise TypeError
        sf.__f = f
        sf.__3_result = () # ()|(1, result)|(-1, Exception)
        sf.__args = args
        sf.__kwargs = kwargs
    def __call__(sf):
        if sf.__3_result:
            (case, data) = sf.__3_result
            if case == +1:
                result = data
                return result
            elif case == -1:
                exc = data
                raise exc
            else:
                raise logic-err
        else:
            try:
                result = sf.__f(*sf.__args, **sf.__kwargs)
            except Exception as exc:
                sf.__3_result = (-1, exc)
                raise
            else:
                sf.__3_result = (+1, result)
                return result
        raise logic-err
Lazy = Lazy__call
class LazyError(BaseException):pass
class Lazy__mk_Exception(Lazy__call):
    def __call__(sf):
        try:
            exc = Lazy__call.__call__(sf)
        except Exception as e:
            raise LazyError(e)
        else:
            raise exc
Lazy #= Lazy__call
Lazy__call
Lazy__value
Lazy__Exception
Lazy__mk_Exception
LazyError


