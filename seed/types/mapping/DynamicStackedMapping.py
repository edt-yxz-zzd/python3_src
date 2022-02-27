#################################
#[[[__doc__-begin
r'''
seed.types.mapping.DynamicStackedMapping
py -m seed.types.mapping.DynamicStackedMapping
py -m nn_ns.app.debug_cmd   seed.types.mapping.DynamicStackedMapping
from seed.types.mapping.DynamicStackedMapping import DynamicStackedMapping

used as dynamic environment for recur call
    mapping.reversable_update +push/pop for env


#[[[doctest_examples-begin
>>> from collections import OrderedDict
>>> od = OrderedDict(a=1)
>>> d = DynamicStackedMapping(od)

>>> od
OrderedDict([('a', 1)])
>>> d['a']
1
>>> list(d)
['a']
>>> len(d)
1
>>> d['b']
Traceback (most recent call last):
    ...
KeyError: 'b'

>>> od
OrderedDict([('a', 1)])
>>> del d['a']
>>> od
OrderedDict()


>>> p1 = d.env_tell()
>>> p1
PositionObj(0, 1)
>>> p1 is d.env_tell()
True

>>> d['b'] = 2
>>> d['b'] = 3
>>> p2 = d.env_tell()
>>> p2
PositionObj(1, 3)
>>> d['c'] = 4
>>> d['d'] = 5
>>> del d['c']
>>> p3 = d.env_tell()
>>> p3
PositionObj(2, 6)
>>> od
OrderedDict([('b', 3), ('d', 5)])
>>> d.env_pop_tmay()
('c', ())
>>> od
OrderedDict([('b', 3), ('d', 5), ('c', 4)])
>>> d.env_pop_tmay()
('d', (5,))
>>> od
OrderedDict([('b', 3), ('c', 4)])
>>> d.env_pop_tmay()
('c', (4,))
>>> od
OrderedDict([('b', 3)])
>>> p2 is d.env_tell()
True

>>> d.env_pop_until(p1)
>>> od
OrderedDict()
>>> p1 is d.env_tell()
True
>>> d.env_pop_tmay()
('a', ())
>>> od
OrderedDict([('a', 1)])
>>> d.env_pop_tmay()
Traceback (most recent call last):
    ...
KeyError

>>> od
OrderedDict([('a', 1)])
>>> with d.mk_contextmanager() as p0:
...     assert p0 is d.env_tell()
...     d['e'] = 6
>>> od
OrderedDict([('a', 1)])





#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################
__all__ = '''
    IDynamicStackedMapping
    DynamicStackedMapping
    '''.split()
#################################



from collections.abc import Mapping, MutableMapping
from seed.abc.abc import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
#from seed.types.AddrAsHash import AddrAsHash as EqById
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
from seed.mapping_tools.mapping_reversable_update__tmay import mapping_reversable_update__tmay
import contextlib

class IDynamicStackedMapping(MutableMapping, ABC):
    __slots__ = ()

    @abstractmethod
    def env_tell(sf, /):
        '-> position_obj'
    @abstractmethod
    def env_pop_until(sf, position_obj, /):
        'position_obj -> None'
    @abstractmethod
    def env_push_tmay(sf, key, tmay_value, /,*, exist_ok, nonexist_ok):
        '-> None'
    @abstractmethod
    def env_pop_tmay(sf, /):
        '-> (key, tmay_value)'
    def env_push(sf, key, value, /,*, exist_ok):
        '-> None'
        sf.env_push_tmay(key, (value,), exist_ok=exist_ok, nonexist_ok=True)
    def env_delete(sf, key, /,*, nonexist_ok):
        '-> None'
        sf.env_push_tmay(key, (), exist_ok=True, nonexist_ok=nonexist_ok)
    def __setitem__(sf, key, value, /):
        sf.env_push(key, value, exist_ok=True)
    def __delitem__(sf, key, /):
        sf.env_delete(key, nonexist_ok=False)

    @contextlib.contextmanager
    def mk_contextmanager(sf, /):
        position_obj = sf.env_tell()

        try:
            yield position_obj
        finally:
            sf.env_pop_until(position_obj)




class PositionObj(EqById):
    '__eq__ is "is"'
    __slots__ = ()
    __slots__ = '__args'
    def __init__(sf, /,*args):
        sf.__args = args
    @property
    def args(sf, /):
        return sf.__args
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
_PositionObj = PositionObj
del PositionObj


class DynamicStackedMapping(IDynamicStackedMapping, ABC__no_slots):
    def __init__(sf, mapping, /):
        sf._mapping = mapping
        sf._key_mval_pairs = []
        sf._position_objs = []

    def _does_tell_fresh(sf, /):
        if sf._position_objs:
            p = sf._position_objs[-1]
            idx4position, idx4pair = p.args
            assert 0 <= idx4position == len(sf._position_objs)-1
            assert 0 <= idx4pair <= len(sf._key_mval_pairs)
            if idx4pair == len(sf._key_mval_pairs):
                return True
        return False

    @override
    def env_tell(sf, /):
        '-> position_obj'
        def f():
            if sf._does_tell_fresh():
                return sf._position_objs[-1]
            return None
        ##################
        def g():
            idx4position = len(sf._position_objs)
            idx4pair = len(sf._key_mval_pairs)
            position_obj = _PositionObj(idx4position, idx4pair)
            sf._position_objs.append(position_obj)
            return position_obj
        ##################
        def main():
            tmay_position_obj = f()
            if tmay_position_obj is None:
                position_obj = g()
                tmay_position_obj = f()
                assert tmay_position_obj is position_obj
            else:
                position_obj = tmay_position_obj
            return position_obj
        return main()

    def _check_position_obj(sf, position_obj, /):
        if type(position_obj) is not _PositionObj: raise TypeError
        idx4position, idx4pair = position_obj.args
        if not (type(idx4position) is int and 0 <= idx4position < len(sf._position_objs) and sf._position_objs[idx4position] is position_obj): raise ValueError
        assert 0 <= idx4pair <= len(sf._key_mval_pairs)
    @override
    def env_pop_until(sf, position_obj, /):
        'position_obj -> None'
        sf._check_position_obj(position_obj)
        idx4position, idx4pair = position_obj.args

        del sf._position_objs[idx4position+1:]
        for _ in range(len(sf._key_mval_pairs) - idx4pair):
            sf.env_pop_tmay()
        assert 0 <= idx4pair == len(sf._key_mval_pairs)
        assert sf._does_tell_fresh()
        assert sf.env_tell() is position_obj

    @override
    def env_push_tmay(sf, key, tmay_value, /,*, exist_ok, nonexist_ok):
        '-> None'
        if not (type(tmay_value) is tuple and len(tmay_value)<=1): raise TypeError

        m = sf._mapping
        if (not exist_ok) and key in m: raise KeyError
        if (not nonexist_ok) and key not in m: raise KeyError
        tmay_old_value = mapping_reversable_update__tmay(m, key, tmay_value)
        sf._key_mval_pairs.append((key, tmay_old_value))
        assert not sf._does_tell_fresh()

    @override
    def env_pop_tmay(sf, /):
        '-> (key, tmay_value)'
        if not sf._key_mval_pairs: raise KeyError

        if sf._does_tell_fresh():
            sf._position_objs.pop()
        assert not sf._does_tell_fresh()
        assert sf._key_mval_pairs
        key, tmay_old_value = sf._key_mval_pairs.pop()
        tmay_new_value = mapping_reversable_update__tmay(sf._mapping, key, tmay_old_value)
        return key, tmay_new_value

    #__getitem__, __iter__, __len__
    def __len__(sf, /):
        return len(sf._mapping)
    def __iter__(sf, /):
        return iter(sf._mapping)
    def __getitem__(sf, key, /):
        return sf._mapping[key]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


