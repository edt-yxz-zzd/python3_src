
r'''
seed.types.pair_based_leftward_list
seed.helper.AttrCollector

py -m seed.helper.AttrCollector
from seed.helper.AttrCollector import AttrCollector

to mk/build flag:
    AttrCollector(Flag).xxx.yyy()
    AttrCollector().xxx.yyy(Flag)


>>> AttrCollector()()
()
>>> AttrCollector().xxx()
('xxx',)
>>> AttrCollector().xxx.yyy()
('xxx', 'yyy')
>>> AttrCollector(list).xxx.yyy()
['xxx', 'yyy']
>>> AttrCollector().xxx.yyy(list)
['xxx', 'yyy']

>>> builder = AttrCollector()
>>> builder()
()
>>> builder.xxx()
('xxx',)
>>> builder.xxx.yyy()
('xxx', 'yyy')
>>> builder.xxx.yyy(list)
['xxx', 'yyy']


#'''

__all__ = ['AttrCollector']

from seed.types.pair_based_leftward_list import to_reversed_leftward_list, leftward, leftward_list2list

def _get_func(attr_collector, /):
    return object.__getattribute__(attr_collector, '_func')
def _get_reversed_attrs(attr_collector, /):
    return object.__getattribute__(attr_collector, '_reversed_attrs')
class AttrCollector:
    def __init__(sf, func=tuple,  _attrs___reversed_leftward_list=(), /):
        assert callable(func)
        assert type(_attrs___reversed_leftward_list) is tuple
        sf._reversed_attrs = _attrs___reversed_leftward_list
        sf._func = func
    def __getattribute__(sf, attr, /):
        f = _get_func(sf)
        reversed_attrs = leftward(attr, _get_reversed_attrs(sf))
        return AttrCollector(f, reversed_attrs)
    def __call__(sf, may_func=None, /):
        if may_func is None:
            f = _get_func(sf)
        else:
            f = may_func
        reversed_attrs = leftward_list2list(_get_reversed_attrs(sf), tuple)
        return f(reversed(reversed_attrs))

assert AttrCollector()() == ()
assert AttrCollector().xxx() == ('xxx',)
assert AttrCollector().xxx.yyy() == ('xxx', 'yyy')
assert AttrCollector(list).xxx.yyy() == ['xxx', 'yyy']

if __name__ == "__main__":
    import doctest
    doctest.testmod()


