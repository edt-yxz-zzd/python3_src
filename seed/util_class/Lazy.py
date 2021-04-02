
r'''
seed.util_class.Lazy
    copy from RecognizeSystem

see also:
    seed.util_class.Lazy
        copy from RecognizeSystem
    seed.util_class.Lazy__call
        required from seed.types.Tester+seed.types.TriBoolOps

#'''


__all__ = ['Lazy']
class Lazy:
    # one and only one [v|f|e] exist at same time
    __slots__ = ('__e', '__v', '__f')
    def __init__(self, f):
        assert callable(f)
        self.__f = f # only (_, _, f)
    def __call__(self):
        return self.v
    @property
    def v(self):
        try:
            return self.__v
            # (_, v, _)
        except AttributeError:
            # (?, _, ?)
            pass

        # (?, _, ?)
        try:
            f = self.__f
            # (_, _, f)
        except AttributeError:
            # (e, _, _)
            raise self.__e
        # (_, _, f)
        del self.__f
        # (_, _, _) # none

        try:
            v = f()
        except BaseException as e:
            self.__e = e
            # (e, _, _)
            raise
        except:
            raise logic-error
        self.__v = v
        # (_, v, _)
        return self.__v


class Lazy:
    def __init__(self, f):
        assert callable(f)
        # (case, evf)
        # {-1: e, 0:v, 1:f}
        self.__evf = (1, f)
    def __call__(self):
        return self.v
    @property
    def v(self):
        try:
            case, evf = self.__evf
        except AttributeError:
            raise RecursionError('lazy = Lazy(f) where f depends on lazy')
        if not case:
            # v
            v = evf
            return v
        elif case == 1:
            # f
            f = evf
            del self.__evf # forbid f dependent on self
            try:
                v = f()
            except BaseException as e:
                self.__evf = (-1, e)
                raise
            except:
                raise logic-error
            self.__evf = (0, v)
            return v
        else:
            # e
            e = evf
            raise e
    @property
    def state(self):
        # (case, evf)
        # {-1: e, 0:v, 1:f}
        return self.__evf

def called_in_return_():
    return
def called_in_raise_():
    return
def raise_(e):
    called_in_raise_()
    raise e
def return_(v):
    called_in_return_()
    return v
will_raise = lambda e: lambda: raise_(e)
will_return = lambda v: lambda: return_(v)

def catch(Error, f):
    try:
        f()
    except Error:
        return True
    return False
def test():
    global called_in_return_
    global called_in_raise_
    ls = [0]
    def set():
        ls[0] = 1
    def clr():
        ls[0] = 0
    def is_set():
        return ls[0] == 1

    del called_in_raise_
    called_in_return_ = set
    clr()
    assert not is_set()
    lazy = Lazy(will_return(-1))
    assert not is_set()
    assert lazy.v == -1
    lazy.v
    assert is_set()
    assert lazy.v == -1
    assert is_set()
    clr()
    assert not is_set()
    assert lazy.v == -1
    lazy.v
    assert not is_set()

    del called_in_return_
    called_in_raise_ = set
    clr()
    assert not is_set()
    lazy = Lazy(will_raise(ValueError))
    assert not is_set()
    b = catch(ValueError, lazy)
    assert b
    assert is_set()
    assert catch(ValueError, lazy)
    assert is_set()
    clr()
    assert not is_set()
    b = catch(ValueError, lazy)
    assert b
    assert catch(ValueError, lazy)
    assert not is_set()
    assert catch(ValueError, lazy)
    assert not is_set()

test()


