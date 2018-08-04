
'''
An metaclass for large class hierarchies


MRO problem:
    if there are many interfaces, mro errors will occur eventually.

    example:
        see problem(type) below
        error: class D7(C6,C5, metaclass=type):pass # 7>6>5


a possible solution:
    define a global total ordering between base classes
    use a metaclass to reorder and insert base classes

    example:
        see C6__solution below
        original:    class C6(B4,B3):pass # 6>4>3
        reorder mro: class C6__solution(B4,B3,A2,A1):pass # 6>4>3>2>1
        problem(MRO_Meta)



but that solution will cause new problem:
    C6.f == A1.f
    C6__solution.f == A2.f

    use a new metaclass to forbid that:
        (1) if there is ambiguity except (3), then
            (1.1) let the class be abstract
            (1.2) forbid C6.f
            # how? maybe insert an abstract descriptor into C6
        (2) forbid super([...]).f in subclass to avoid ambiguity, except (3)
            use A1.f instead
            # how? maybe insert a "super" function into class namespace
        (3) some methods are allow to work with super()
            such method should have stable api and default implement.
            for any acceptable mro, the result should not depends on mro.
            forbid super(cls[, ...]).f, since the mro may change
            "super().f" can occur in body of subclass.f only
            #let super_method() = super(__class__, self).f
            #??let super_method_unbinded() = super(__class__, type(self)).f
            #let super_classmethod() = curry(super(__class__, self_cls).f, self_cls)
            super_this_func() # binded with self or cls

auto subtyping
    AcyclicGraph + Connected ==>> UTree
    close world type system(like Haskell)
        {...
        ,(AcyclicGraph, Connected): [UTree_Mixin1, UTree_Mixin2]
        ...
        }
        inherit both UTree_Mixin1 and UTree_Mixin2
        we have to choose methods from UTree_Mixin1 or UTree_Mixin2
            e.g. by compare "speed" per method
    @classmethod
    def min_cycle_numbers(cls):
        return cls.__min_cycle_numbers
    @classmethod
    def maybe_max_cycle_numbers(cls):
    def __init_subclass__(cls):
        cls.__min_cycle_numbers = max1(0, (cls.min_cycle_numbers() for cls in get_mro(cls)[1:] if cls in MinCycleNumbers))



'''

class Error__type(TypeError):pass
def problem(*Metas):
    class Meta(*Metas):pass
    class O(metaclass=Meta):pass
    ###########
    class A1(O):
        def f(self):pass
    class A2(O):
        def f(self):pass
    ###########
    class B3(A2):pass # 3>2
    class B4(A1):pass # 4>1
    ###########
    class C5(A2,A1):pass # 5>2>1
    class C6(B4,B3):pass # 6>4>3 # C6.mro() = 6 4 1 3 2
    ###########
    try:
        class D7(C6,C5):pass # 7>6>5
        # ERROR: problem(type)
    except TypeError:
        class C6__solution(B4,B3,A2,A1):pass # 6>4>3>2>1
        class D7(C6__solution,C5):pass # 7>6>5
        assert C6.f == A1.f
        assert C6__solution.f == A2.f
        raise Error__type

    assert C6.f == A1.f
    assert C6__solution.f == A2.f


try:
    problem(type)
    #TypeError: Cannot create a consistent method resolution
    #       order (MRO) for bases A1, A2
except Error__type:pass
else: raise

from .MRO_Meta import MRO_Meta, class_order_key
problem(MRO_Meta) # fine


