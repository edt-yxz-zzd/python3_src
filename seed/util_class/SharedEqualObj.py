
r'''
merge equal objects
    two ways to implement
    1) after __eq__
    2) global WeakSet, at __new__
'''

__all__ = '''
    SharedEqualObj__WeakRef
    mk_subclass_SharedEqualObj__WeakRef
    SharedEqualObj__AfterEq
    HashableSharedEqualObj__AfterEq
    '''.split()

import weakref



class _Obj:
    # TypeError: cannot create weak reference to 'tuple' object
    def __init__(self, obj):
        self.__obj = obj
    @property
    def obj(self):
        return self.__obj
    def __ne__(self, other):
        return not (self == other)
    def __eq__(self, other):
        if self is other: return True
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.obj == other.obj

    def __hash__(self):
        return hash(self.obj)
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.obj)

class SharedEqualObj__WeakRef:
    '''\
subclass should override
    __shared_weak_key_dict__
'''
    # {ref(obj):(ref(obj), self)}
    # TypeError: cannot create weak reference to 'tuple' object
    # TypeError: cannot create weak reference to 'weakref' object
    # bug: {obj:(ref(obj), self)} # self ref to obj directly!
    # {self:ref(self)}
    # to fasten __eq__
    # {_Obj(hashable):ref(self)}
    __shared_weak_key_dict__ = weakref.WeakKeyDictionary()
    def __new__(cls, hashable):
        '''
        if hashable is None:
            raise TypeError('to use weakref, hashable should not be None')
        # TypeError: cannot create weak reference to 'tuple' object
        now using _Obj to wrap hashable
        '''
        self = super(__class__, cls).__new__(cls)
        self.__obj = obj = _Obj(hashable)
        self.__hash = hash(hashable)

        d = cls.__shared_weak_key_dict__
        ref = weakref.ref(self); #rint(ref)
        val = ref
        key = obj
        while True: # this loop is a pin-lock
            val_ = d.setdefault(key, val)
            if val_ is val:
                # setdefault -> set
                break
                return self

            # setdefault -> get
            _ref = val_
            # here _ref may be invalid now.
            _self = _ref()
            if _self is not None:
                val = ref = _ref
                key = obj = _self.__obj
                self = _self
                assert self.obj == hashable
                break
                return self
        return self

    # no __init__

    @property
    def obj(self):
        return self.__obj.obj
    def __ne__(self, other):
        return not (self == other)
    def __eq__(self, other):
        if self is other: return True
        if not isinstance(other, type(self)):
            return NotImplemented
        assert self.obj is not other.obj
        assert self.obj != other.obj
        return False
    def __hash__(self):
        return self.__hash
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.obj)
# end SharedEqualObj__WeakRef

hashable_type2subclass_SubClass_SharedEqualObj__WeakRef = {}
def mk_subclass_SharedEqualObj__WeakRef(hashable_type):
    class SubClass_SharedEqualObj__WeakRef(SharedEqualObj__WeakRef):
        __shared_weak_key_dict__ = weakref.WeakKeyDictionary()
        def __new__(cls, hashable):
            assert isinstance(hashable, hashable_type)
            return super(__class__, cls).__new__(cls, hashable)
    subclass = SubClass_SharedEqualObj__WeakRef
    subclass = hashable_type2subclass_SubClass_SharedEqualObj__WeakRef\
                    .setdefault(hashable_type, subclass)
    return subclass




###################################

class SharedEqualObj__AfterEq:
    def __init__(self, obj):
        self.__obj = obj
        self.__parent = self
    @property
    def obj(self):
        # not self.__obj
        # but self(.__parent){oo,oo}.__obj
        c = self
        ls = []
        p = c.__parent
        while True:
            pp = p.__parent
            if p is pp: break
            ls.append(c)
            c, p = p, pp
        # [ls ->] c -> p <-> p
        # maybe: p is c
        assert (c is self) == (not ls)

        obj = p.__obj
        for c in ls:
            #c.__obj = obj
            c.__parent = p

        # error: assert self.__obj is obj
        # now: self.obj is self.__parent.__obj
        return obj
    def __ne__(self, other):
        return not (self == other)
    def __eq__(self, other):
        if self is other: return True
        if not isinstance(other, type(self)):
            return NotImplemented
        if self.obj is other.obj: return True

        b = self.obj == other.obj
        if b:
            # share/merge
            if id(self.obj) < id(other.obj):
                other.__parent.__parent = self.__parent
            else:
                self.__parent.__parent = other.__parent
        return b
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.obj)
# end SharedEqualObj__AfterEq

class HashableSharedEqualObj__AfterEq(SharedEqualObj__AfterEq):
    def __init__(self, obj):
        super().__init__(obj)
        self.__hash = hash(obj)
    def __hash__(self):
        return self.__hash
# end HashableSharedEqualObj__AfterEq



def _test_SharedEqualObj__AfterEq():
    a = SharedEqualObj__AfterEq((1,2,3))
    b = SharedEqualObj__AfterEq((1,2,3))
    c = SharedEqualObj__AfterEq((1,2,))
    assert a.obj is not b.obj
    assert a.obj is not c.obj
    a == b
    assert a.obj is b.obj
    a == c
    assert a.obj is not c.obj
    return True
assert _test_SharedEqualObj__AfterEq()



def _test_SharedEqualObj__WeakRef():
    import gc, sys
    T = mk_subclass_SharedEqualObj__WeakRef(tuple)
    d = T.__shared_weak_key_dict__
    def show(s = ''):
        print(s)
        print('global dict', dict(d))
        for ref in d.keyrefs():
            k = ref()
            if k is None: continue
            count = weakref.getweakrefcount(k)
            print('weakref count', k, count, ref)
            print('weakref list', weakref.getweakrefs(k))
            print('ref count', k, sys.getrefcount(k)) # == 4??????????
        print('\n'*2)
    def show(s):pass

    assert not d
    a = T((1,2,3))
    show('after: def a')
    assert len(d) == 1
    b = T((1,2,3))
    show('after: def b')
    assert len(d) == 1
    assert a is b
    del a
    show('after: del a')
    assert len(d) == 1
    del b
    show('after: del b')
    gc.collect()
    show('after: gc.collect()')
    assert not d
    return True

assert _test_SharedEqualObj__WeakRef()


