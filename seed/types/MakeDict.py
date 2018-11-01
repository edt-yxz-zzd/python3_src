
'''
usage:

>>> class d(MakeDict):
...     __ # for arbitrary keys:
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True

>>> class d(MakeDict):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is dict
True
>>> class d(MakeDict, dict=OrderedDict()):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is OrderedDict
True

'''
__all__ = '''
    MakeDict
    '''.split()

from collections import OrderedDict, UserDict #, defaultdict
class _D(UserDict, dict):# reqire dict
    r'''for MakeDict_Meta

>>> sep = '____'
>>> THIS = lambda ks: _D({}, ks, sep)

>>> set_at_most_once_keys = o1, o2 = '12'
>>> k1, k2 = 'ab'
>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[o1] = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError

>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[o2] = 1
>>> d[o1] = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[k1] = 1
>>> d[o1] = 1 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[sep] = 1 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[k1] = 1
>>> d[k1] = 2
>>> d = THIS(set_at_most_once_keys)
>>> d[sep]
>>> d[o1] = 1
>>> d[o1] = 2
>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[k1] = 1
>>> d[k2] = 1
>>> d[sep]
>>> d[o1] = 2
>>> d[o1] = 3
>>> d[o2] = 1
>>> d[k2] = 2
>>> d.moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key() == {o1:3, o2:1, k1:1, k2:2}
True

'''
    #def __new__(cls, data, set_at_most_once_keys, sep_key='__'):
    #   # fail!!!!
    #   return object.__new__(cls) # donot init type<'dict'>
    def __init__(self, data, set_at_most_once_keys, sep_key='__'):
        set_at_most_once_keys = set(set_at_most_once_keys)
        if sep_key in set_at_most_once_keys:
            raise ValueError(f'sep_key in set_at_most_once_keys: {sep_key}')
        #super().__init__() donot init type<'dict'>
        super().__init__()
        self.data = data
        self.sep_key = sep_key
        self.set_at_most_once_keys = set_at_most_once_keys
        self.sep_key_occured = False
        self.non_set_at_most_once_keys_written = False
        self.set_at_most_once_keys = set_at_most_once_keys
        self.set_at_most_once_key2count = {k:0 for k in set_at_most_once_keys}
            #defaultdict(int)
            #bug: after sep_key first read: all += 1
            #bug: after sep_key first read: all := 1
    def __getitem__(self, key):
        if not self.sep_key_occured and key == self.sep_key:
            # first read sep_key
            self.sep_key_occured = True
            if not all(v < 2 for v in self.set_at_most_once_key2count.values()): raise logic-error
            self.set_at_most_once_key2count = {k:1 for k in self.set_at_most_once_keys}
            return None
        return self.data[key]
    def __setitem__(self, key, obj):
        if not self.sep_key_occured:
            # before first read sep_key

            if key in self.set_at_most_once_keys:
                if key in self:
                    raise KeyError(f'set more than once: {key}')
                elif self.non_set_at_most_once_keys_written:
                    raise KeyError(f'set once-key after non-once-key: {key}')
            elif key == self.sep_key:
                # write sep_key before first read sep_key
                raise KeyError(f'should read sep_key first before write it!: {key}')
            else:
                # write non_set_at_most_once_keys
                self.non_set_at_most_once_keys_written = True
        if key in self.set_at_most_once_keys:
            self.set_at_most_once_key2count[key] += 1
        self.data[key] = obj
    def moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key(self):
        if not all(v > 0 for v in self.set_at_most_once_key2count.values()): raise logic-error # must set at least once!!!

        keys_to_del = [k for k, v in self.set_at_most_once_key2count.items() if v < 2]
        data, self.data = self.data, None # donot use me from now on
        for k in keys_to_del:
            del data[k]
        return data

        return {k:v for k, v in self.items()
                if k not in self.set_at_most_once_key2count
                    or self.set_at_most_once_key2count[k] > 1
                }


def _is_first_def_MakeDict(name):
    try:
        MakeDict
    except NameError:
        if name == 'MakeDict':
            return True
    return False
class MakeDict_Meta(type):
    r'''

>>> class d(metaclass=MakeDict_Meta):
...     __module__
...     __qualname__
...     a = 1
...     __
...     __module__ = 2
>>> d == {'a': 1, '__module__':2}
True
>>> class d(MakeDict): #doctest: +IGNORE_EXCEPTION_DETAIL
...     __module__ = 2
Traceback (most recent call last):
    ...
KeyError
>>> class d(MakeDict): #doctest: +IGNORE_EXCEPTION_DETAIL
...     __qualname__
...     a = 1
...     __
...     __module__ = 2
>>> d == {'a': 1, '__module__':2}
True
>>> class d(MakeDict):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is dict
True
>>> class d(MakeDict, dict=OrderedDict()):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is OrderedDict
True
'''
    def __new__(cls, name, bases, namespace, *, dict=None, **kwargs):
        if _is_first_def_MakeDict(name):
            return super().__new__(cls, name, bases, namespace, **kwargs)
        return namespace.moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key()
    #def __init__(self, name, bases, namespace, **kwargs):

    @classmethod
    def __prepare__(metacls, name, bases, *, dict=None, **kwargs):
        # fail!!!! must return dict!!!!
        if dict is None:
            dict = {}
        return _D(dict, _set_at_most_once_keys_MakeDict)

_set_at_most_once_keys_MakeDict = ()
class MakeDict(metaclass=MakeDict_Meta):
    pass
if True:
    # initial _set_at_most_once_keys_MakeDict
    class d(MakeDict):pass
    _set_at_most_once_keys_MakeDict = tuple(d.keys())
    del d


'''
class MakeDict_Type:
    def __call__(*args, **kwargs):
        print(args)
        print(kwargs)
MakeDict_Meta = MakeDict_Type()
class MakeDict(metaclass=MakeDict_Meta): pass
'''

def _t0():
    class k(metaclass=MakeDict_Meta):
        __module__
        __qualname__
        pass
    class d(MakeDict):
        a = 1
    class x(MakeDict, dict=OrderedDict()):
        a = 1
    #print(k)
    #print(d)
    assert k == {}
    assert d == {'a':1}
    assert x == {'a':1}
    assert type(d) is dict
    assert type(x) is OrderedDict
_t0()
if __name__ == "__main__":
    #_t0()
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


