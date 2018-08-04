


__all__ = '''
    FrozenSeq
    ReadonlySeq
    PermuteSeq
    FixedLenSeq
    GrowingSeq
    ShrinkingSeq

    GrowingPermuteSeq
    ShrinkingPermuteSeq
    GrowingFixedLenSeq
    ShrinkingFixedLenSeq
    Seq
    '''.split()


from itertools import chain
from collections.abc import Sequence
FrozenSeq = tuple








'''
# readonly
__getitem__, __len__
__contains__, __iter__, __reversed__, index, count
'''
class _ReadSeqBase(Sequence): #(SeqView):
    # FrozenSeq = tuple
    'immutable; .__s should not be assigned again!'
    def __init__(self, seq):
        # subclass: super().__init__(list(iterable))
        if not isinstance(seq, Sequence):
            raise TypeError('not a seq')
        if isinstance(seq, __class__):
            seq = seq.__s
            assert not isinstance(seq, __class__)
        self.__s = seq

    #def __getitem__(self, i): return self.__s.__getitem__(i)

    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__s == other.__s
    def __ne__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return not (self == other)
    def __lt__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__s < other.__s
    def __le__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__s <= other.__s
    def __gt__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__s > other.__s
    def __ge__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__s >= other.__s

    def __repr__(self):
        return repr_helper(self, self.__s) # ? list(self.__s)
    def copy(self):
        return type(self)(self.__s)

    @classmethod
    def from_sequence(cls, seq): return cls(seq)
    def __getitem__(self, i):
        t = type(i)
        if t is tuple: raise TypeError
        if t is slice:
            r = self.__s[i]
            assert isinstance(r, Sequence):
            r = type(self).from_sequence(r)
        else:
            i = __index__(i)
            r = self.__s[i]
        return r


    def __len__(self):
        return len(self.__s)
    def __contains__(self, x):
        return x in self.__s
    def __iter__(self):
        return iter(self.__s)
    def __reversed__(self):
        return reversed(self.__s)
    def index(self, *args):
        return self.__s.index(*args)
    def count(self, *args):
        return self.__s.count(*args)

class ReadonlySeq(_ReadSeqBase):
    # tuple
    @property
    def __s(self): return self._ReadSeqBase__s
    def __init__(self, iterable):
        if type(iterable) is tuple:
            t = iterable
        elif isinstance(iterable, __class__):
            t = iterable.__s
        else:
            t = tuple(iterable)
        assert type(t) is tuple
        super().__init__(t)

    def __eq__(self, other):
        return _ReadSeqBase.__eq__(self, other)
    def __hash__(self):
        return hash(self.__s)

'''
# full_mutable
# == readonly+...
__setitem__
    s[i]
    s[i:j]
    s[i:j:k]
    # s[i,...] # not support
insert
__delitem__
    del s[i]
    del s[i:j]
    del s[i:j:k]
    # del s[i,...] # not support

reverse
copy
append, extend, __iadd__, __imul__<n>
pop(), clear
pop(i)
remove

### mine
permute
'''

'''
# readonly
__getitem__, __len__
__contains__, __iter__, __reversed__, index, count
copy
'''

'''
# permute
# == readonly+...
reverse
permute
'''

'''
# fixed_length
# == permute+...
__setitem__<length_eq>
'''

'''
# growing
# == readonly+...
append, extend, __iadd__, __imul__<n>
'''

'''
# shrinking
# == readonly+...
pop(), clear
'''


'''
# growing + permute
    insert
    append, extend, __iadd__, __imul__<n>
    reverse permute
# shrinking + permute
    __delitem__
    reverse permute
    pop(), clear
    pop(i)
    remove
# growing + shrinking ==>> full_mutable
    # growing+shrinking+permute +...
    __setitem__
# growing + fixed_length ==>> length_ge
    # growing + permute +...
    __setitem__<length_ge>
# shrinking + fixed_length ==>> length_le
    # shrinking + permute +...
    __setitem__<length_le>
'''

# 4.6.3. Mutable Sequence Types
def __index__(self):
    #from operator import __index__
    return type(self).__index__(self)
class _ReadSeq(_ReadSeqBase):
    # list  # v.s. ReadonlySeq
    @property
    def __s(self): return self._ReadSeqBase__s
    def __init__(self, iterable):
        ls = list(iterable)
        super().__init__(ls)
class _PermuteSeq(_ReadSeq):
    # fixed_length
    @property
    def __s(self): return self._ReadSeqBase__s
    def permute(self, indices):
        # (i,j,...,k) ==>> (s[i]->s[j]->...->s[k]->s[i])
        indices = map(__index__, indices)
        indices = tuple(indices)
        if len(indices) < 2: return
        pairs = chain(zip(indices, indices[1:]), [(indices[-1], indices[0])])
        s = self.__s
        nothing = []
        nothing_idx = indices[0]
        val = s[nothing_idx]
        s[nothing_idx] = nothing
        for to_idx in chain(indices[1:], [indices[0]]):
            # swap
            val, s[to_idx] = s[to_idx], val
        if val is nothing: return
        for i in indices:
            if s[i] is nothing:
                s[i] = nothing
                break
        else:
            raise logic-error
        pass
    def reverse(self):
        self.__s.reverse()
class PermuteSeq(_PermuteSeq):pass



class _FixedLenSeq(_PermuteSeq):
    # fixed_length
    @property
    def __s(self): return self._ReadSeqBase__s
    def __setitem__(self, i, value):
        return self.__setitem(i, value)
    def __setitem_slice(self, i, value):
        # to be overrided
        # return (i, value) or raise
        if not isinstance(value, Sequence):
            value = tuple(value)
        if len(self.__s.__getitem__(i)) != len(value): raise ValueError
        return i, value
    def __setitem_verify(self, org_len):
        # to be overrided
        # return bool
        return org_len == len(self)
    def __setitem(self, i, value):
        t = type(i)
        L = len(self)
        if t is tuple: raise TypeError
        if t is slice:
            i, value = self.__setitem_slice(i, value)
        else:
            i = __index__(i)

        self.__s.__setitem__(i, value)
        if not self.__setitem_verify(L): raise logic-error
class FixedLenSeq(_FixedLenSeq):pass


class _GrowingSeq(_ReadSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def append(self, x): self.__s.append(x)
    def extend(self, iterable): self.__s.extend(iterable)
    def __iadd__(self, other):
        s = self.__s
        r = s.__iadd__(other.__s)
        if r is not s: raise logic-error
        return self
    def __imul__(self, n):
        s = self.__s
        r = s.__imul__(self, n)
        if r is not s: raise logic-error
        return self
class GrowingSeq(_GrowingSeq):pass
class _ShrinkingSeq(_ReadSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def __pop_None(self, i):
        if i is not None: raise TypeError
        return self.__s.pop()
    def pop(self, i=None):
        return self.__pop_None(i)
    def clear(self):
        self.__s.clear()
class ShrinkingSeq(_ShrinkingSeq):pass

class _GrowingPermuteSeq(_GrowingSeq, _PermuteSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def insert(self, i, x):
        self.__s.insert(i, x)
class GrowingPermuteSeq(_GrowingPermuteSeq):pass
class _ShrinkingPermuteSeq(_ShrinkingSeq, _PermuteSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def __delitem__(self, i):
        self.__s.__delitem__(i)
    def pop(i=None):
        self.__s.pop(i)
    def remove(self, x):
        self.__s.remove(x)
class ShrinkingPermuteSeq(_ShrinkingPermuteSeq):pass

class _GrowingFixedLenSeq(_GrowingPermuteSeq, _FixedLenSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def __setitem_slice(self, i, value):
        # to be overrided
        # return (i, value) or raise
        if not isinstance(value, Sequence):
            value = tuple(value)
        if len(self.__s.__getitem__(i)) > len(value): raise ValueError
        return i, value
    def __setitem_verify(self, org_len):
        # to be overrided
        # return bool
        return org_len <= len(self)
class GrowingFixedLenSeq(_GrowingFixedLenSeq):pass
class _ShrinkingFixedLenSeq(_ShrinkingPermuteSeq, _FixedLenSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def __setitem_slice(self, i, value):
        # to be overrided
        # return (i, value) or raise
        if not isinstance(value, Sequence):
            value = tuple(value)
        if len(self.__s.__getitem__(i)) < len(value): raise ValueError
        return i, value
    def __setitem_verify(self, org_len):
        # to be overrided
        # return bool
        return org_len >= len(self)
class ShrinkingFixedLenSeq(_ShrinkingFixedLenSeq):pass


class _Seq(_ShrinkingFixedLenSeq, _GrowingFixedLenSeq):
    @property
    def __s(self): return self._ReadSeqBase__s
    def __setitem__(self, i, value):
        self.__s.__setitem__(i, value)

class Seq(_Seq):pass



