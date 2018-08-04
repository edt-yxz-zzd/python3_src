


r'''
see: "E:\my_data\my_record_txt\NOTE\other\subclass multi inheritance.txt"


MRO_Meta
    reorder bases and insert bases
    As = [cls in MRO_Meta for cls in bases]
    Bs = [cls not in MRO_Meta for cls in bases]
    As = reorder and insert bases(As)
    bases = As + [Sep] + Bs # reorder


'''

__all__ = '''
        SetCls_MetaBase
    SetCls_Meta
    SetCls_Object

        ClassOrder_MetaBase
    ClassOrder_Meta
    ClassOrder_Object
    class_order_compare
    class_order_key

        MRO_MetaBase
    MRO_Meta
    MRO_Object
    sorted_bases_by_class_order_and_insert_bases
    '''.split()

import weakref


def get_mro(cls):
    # assert cls in type
    # return cls.mro() # is error if cls <: type
    return cls.__mro__
    return type(cls).mro(cls)

class SetCls_MetaBase(type):
    # class Meta(SetCls_MetaBase):pass
    # class C(metaclass=SetCls_MetaBase/Meta):pass ==>> obj in C; C <= B
    '''
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        if meta_cls is __class__ and SetCls_Meta is not None:
            raise Exception('use SetCls_Meta instead of SetCls_MetaBase')
        self = super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        return self
    '''
    def __contains__(cls, obj):
        return isinstance(obj, cls)
    def __le__(cls, super_cls):
        return issubclass(cls, super_cls)
    def __lt__(cls, super_cls):
        return cls is not super_cls and issubclass(cls, super_cls)
    def __ge__(cls, subcls):
        return issubclass(subcls, cls)
    def __gt__(cls, subcls):
        return cls is not subcls and issubclass(subcls, cls)
#SetCls_Meta = None
class SetCls_Meta(SetCls_MetaBase, metaclass=SetCls_MetaBase):
    '(SetCls_MetaBase) to be Meta; (metaclass=SetCls_MetaBase) for "obj in SetCls_Meta"'
    pass
#del SetCls_MetaBase
class SetCls_Object(metaclass=SetCls_Meta):pass








class SeperatorForNonClassOrder_MetaBase_cls:
    '''

assume A1,A2 in ClassOrder_MetaBase, B1,B2 not in ClassOrder_MetaBase
class C(A1,A2, SeperatorForNonClassOrder_MetaBase_cls, B1,B2):pass
cls in MRO_MetaBase
    get_mro(cls) = [A..., Sep, B...]
    or get_mro(cls) = [A..., ClassOrder_MetaBase, Sep, B...]
    '''
    pass

__wrap_non_ClassOrder_MetaBase_cls__dict = weakref.WeakValueDictionary()
def wrap_non_ClassOrder_MetaBase_cls(cls):
    # ClassOrder_MetaBase not in ClassOrder_MetaBase
    d = __wrap_non_ClassOrder_MetaBase_cls__dict
    wrapper = d.get(cls)
    if wrapper is not None: return wrapper

    if cls in ClassOrder_MetaBase: return cls # raise TypeError
    Sep = SeperatorForNonClassOrder_MetaBase_cls
    if cls is Sep: raise logic-error
        # Sep should not be wrapped
    if cls is ClassOrder_MetaBase: raise logic-error
        # ClassOrder_MetaBase should not be wrapped
    '''
    class wrapper(Sep, cls, metaclass=ClassOrder_Meta):pass # not MetaBase
    '''
    # not ClassOrder_MetaBase
    bases = (Sep, cls)
    wrapper = ClassOrder_Meta('wrap_non_ClassOrder_MetaBase_cls.<locals>.' + cls.__qualname__, bases, {})
    d[cls] = wrapper
    return wrapper








def class_order_compare(self, other):
    # self and other are classes
    # so, self.class_order_compare may get the self class's method
    # bug: return self.class_order_compare(other)
    # now rename to __class_order_compare__
    return type(self).__class_order_compare__(self, other)
def class_order_key(self):
    return type(self).__class_order_key__(self)
class ClassOrder_MetaBase(SetCls_Meta):
    # __slots__ = ['__class_order_idx']
    # cls in ClassOrder_MetaBase ==>> cls <= SeperatorForNonClassOrder_MetaBase_cls
    __global_order_idx = 0 # per_python_excute
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        mk_self = lambda: super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        self = mk_self()
        if self not in __class__: return self

        if not (self <= SeperatorForNonClassOrder_MetaBase_cls):
            raise TypeError('miss SeperatorForNonClassOrder_MetaBase_cls in bases')
        if __debug__:
            mro = get_mro(self)
            i = mro.index(SeperatorForNonClassOrder_MetaBase_cls)
            assert all(cls in __class__ for cls in mro[:i])
            assert all(cls not in __class__ for cls in mro[i+1:])

        self.__class_order_idx = __class__.__global_order_idx
        __class__.__global_order_idx += 1
        return self
    def __class_order_compare__(self, other):
        return self.__class_order_idx - other.__class_order_idx
    def __class_order_key__(self):
        # functools.cmp_to_key
        return self.__class_order_idx
class ClassOrder_Meta(SeperatorForNonClassOrder_MetaBase_cls
    , ClassOrder_MetaBase, metaclass=ClassOrder_MetaBase):pass
#del ClassOrder_MetaBase
class ClassOrder_Object(SeperatorForNonClassOrder_MetaBase_cls
    , SetCls_Object, metaclass=ClassOrder_Meta):pass


#def sorted_bases_by_class_order(bases):
def sorted_bases_by_class_order_and_insert_bases(bases):
    # return half_mro, bases
    # bases = list(bases)
    Sep = SeperatorForNonClassOrder_MetaBase_cls
    bases = [cls for cls in bases if cls is not Sep]
    # ClassOrder_MetaBase not in ClassOrder_MetaBase
    at_end = [cls for cls in bases if cls not in ClassOrder_MetaBase]
    bases = map(wrap_non_ClassOrder_MetaBase_cls, bases)

    first_half_mro_set = set()
    for cls in bases:
        mro = get_mro(cls)
        i = mro.index(Sep)
        first_half_mro_set.update(mro[:i])

    bases = sorted(first_half_mro_set, key=class_order_key, reverse=True)

    bases.append(Sep)
    bases += at_end
    bases = tuple(bases)
    return bases


class MRO_MetaBase(ClassOrder_Meta, SetCls_Meta):
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        bases = sorted_bases_by_class_order_and_insert_bases(bases)
        self = super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        return self
    '''
    # __slots__ = ['__ClassOrder_Meta_bases']
    #       __ClassOrder_Meta_bases:
    #           include self;
    #           == tuple(super_cls for supercls in get_mro(cls) if supercls in ClassOrder_Meta)
    def get_ClassOrder_Meta_bases(self):
        return self.__ClassOrder_Meta_bases
    '''
class MRO_Meta(MRO_MetaBase, metaclass=MRO_MetaBase):pass
class MRO_Object(ClassOrder_Object, metaclass=MRO_Meta):pass


def _test():
    class a:pass
    class b:pass
    # A -> B
    class A(a, MRO_Object):pass
    class B(b, MRO_Object):pass

    class x:pass
    class y:pass
    # Y -> X
    class Y(y, MRO_Object):pass
    class X(x, MRO_Object):pass

    class C(A,B, X,Y):pass
    class D(B,A, Y,X):pass
    class E(C,D):pass

    # force order for a,b,x,y
    # compare F with C
    class F(A,B, X,Y, a,b,x,y):pass

    # assert x < y # TypeError: '<' not supported between instances of 'type' and 'type'
    assert not (A <= y)
    assert A <= A
    assert A() in A
    assert A < MRO_Object
    assert A in MRO_Meta
    for cls in [C,D,E]: print(get_mro(cls))

    wy = wrap_non_ClassOrder_MetaBase_cls(y)
    wx = wrap_non_ClassOrder_MetaBase_cls(x)
    wb = wrap_non_ClassOrder_MetaBase_cls(b)
    wa = wrap_non_ClassOrder_MetaBase_cls(a)
    Sep = SeperatorForNonClassOrder_MetaBase_cls
    ls0 = [x,y, b, a, object]
    ls1 = [MRO_Object, ClassOrder_Object, SetCls_Object, Sep]
    ls2 = [X,wx,Y,wy,B,wb,A,wa]
    ls210 = ls2+ls1+ls0
    assert get_mro(C) == [C] + ls210
    assert get_mro(D) == [D] + ls210
    assert get_mro(E) == [E,D,C] + ls210
    assert get_mro(F) == [F] + ls2 + ls1 + [a,b,x,y, object]
    return

if __name__ == "__main__":
    _test()
    print('\n'.join(globals()))
