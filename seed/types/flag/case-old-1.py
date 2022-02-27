
update doctest_examples
+to_ImmutableCase()
+to_new_MutableCase()
+to_ImmutableFlag()
+to_new_MutableFlag()
r'''

seed.helper.case
py -m seed.helper.case
from seed.helper.case import otherwise, Case, ImmutableCase, MutableCase, clear_case, case2may_key, Flag, ImmutableFlag, MutableFlag, clear_flag, _flag2keys


goto:
    class_Case
    class_MutableCase
    class_Flag
    class_MutableFlag

choice only one path to exec/debug

case = Case(xxx=True)
case = Case()
case.xxx = True
if 0:pass
elif case.xxx:
    ...
elif case.yyy:
    ...
elif case.zzz:
    ...
elif otherwise(case):
    #like "else" but can put front!!!
    #<==> elif not (case):
else:
    ...

for the_only_key in case:
    ...
else:
    #all False, not any



#################################
#################################
#################################
#[[[doctest_examples-begin

#################################
#[[[doctest_examples_Case-begin

>>> case = Case()
>>> case
Case()
>>> not case
True
>>> otherwise(case)
True
>>> len(case)
0
>>> list(case)
[]
>>> case._may_key
False
>>> case.__getattribute__
False
>>> case.xxx
False

>>> del case.xxx
>>> not case
True
>>> case.xxx = False
>>> not case
True
>>> case
Case()

>>> case.xxx = True
>>> case
Case(xxx = True)
>>> case != Case(yyy=True)
True
>>> case == Case(xxx=True)
True
>>> case != Case()
True

>>> case
Case(xxx = True)
>>> not case
False
>>> otherwise(case)
False
>>> len(case)
1
>>> list(case)
['xxx']
>>> case._may_key
False
>>> case.__getattribute__
False
>>> case.xxx
True

>>> del case.yyy
>>> case != Case(yyy=True)
True
>>> case == Case(xxx=True)
True
>>> case != Case()
True

>>> case.yyy = True
>>> case == Case(yyy=True)
True
>>> case != Case(xxx=True)
True
>>> case != Case()
True

>>> del case.yyy
>>> case != Case(yyy=True)
True
>>> case != Case(xxx=True)
True
>>> case == Case()
True



##_may_legal_keys
>>> case = Case()
>>> case
Case()
>>> 1 in case
False
>>> '+++' in case
False
>>> 'zzz' in case
True
>>> case.zzz
False
>>> case.zzz = True
>>> case.zzz
True
>>> case.zzz = False
>>> case.zzz
False


>>> case = Case([])
>>> case
Case([])
>>> 1 in case
False
>>> '+++' in case
False
>>> 'zzz' in case
False
>>> case.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz = False
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'

>>> case = Case(['xxx'])
>>> case
Case(['xxx'])
>>> 1 in case
False
>>> '+++' in case
False
>>> 'zzz' in case
False
>>> case.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz = False
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> 'xxx' in case
True
>>> case.xxx
False
>>> case.xxx = True
>>> case.xxx
True
>>> case.xxx = False
>>> case.xxx
False


>>> case = Case(['xxx'], zzz=True)
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case = Case(['xxx'], zzz=False)
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> case = Case(['xxx'], xxx=True)
>>> case
Case(['xxx'], xxx = True)
>>> case = Case(['xxx', 'yyy'], xxx=True, yyy=False)
>>> case
Case(['xxx', 'yyy'], xxx = True)
>>> case = Case(['xxx', 'yyy'], xxx=False, yyy=False)
>>> case
Case(['xxx', 'yyy'])
>>> case = Case(['xxx', 'yyy'], xxx=True, yyy=True)
Traceback (most recent call last):
    ...
ValueError
>>> case = Case(['xxx', 'yyy'], xxx=True, zzz=True)
Traceback (most recent call last):
    ...
ValueError
>>> case = Case(['xxx', 'yyy'], xxx=0)
Traceback (most recent call last):
    ...
TypeError


>>> case = Case(['xxx', 'yyy'], xxx=False, yyy=True)
>>> case
Case(['xxx', 'yyy'], yyy = True)
>>> case.xxx
False
>>> case.yyy
True
>>> case.xxx = True
>>> case
Case(['xxx', 'yyy'], xxx = True)
>>> case.xxx
True
>>> case.yyy
False
>>> case.xxx = 1
Traceback (most recent call last):
    ...
TypeError
>>> case[1] = True
Traceback (most recent call last):
    ...
TypeError
>>> case['+++'] = True
Traceback (most recent call last):
    ...
ValueError: attr is not identifier: '+++'
>>> case['zzz'] = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'



>>> case = Case(['xxx', 'yyy'], xxx=False, yyy=True)
>>> case
Case(['xxx', 'yyy'], yyy = True)
>>> del case.xxx
>>> del case.xxx
>>> del case.xxx
>>> case
Case(['xxx', 'yyy'], yyy = True)
>>> del case.yyy
>>> case
Case(['xxx', 'yyy'])
>>> del case.yyy
>>> del case.yyy
>>> del case.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> del case['xxx']
>>> del case['yyy']
>>> del case['zzz']
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> del case['+++']
Traceback (most recent call last):
    ...
ValueError: attr is not identifier: '+++'
>>> del case[0]
Traceback (most recent call last):
    ...
TypeError


>>> case = Case(['xxx', 'yyy'], xxx=False, yyy=True)
>>> 'zzz' in case
False
>>> 'yyy' in case
True
>>> 'xxx' in case
True
>>> sorted(case)
['yyy']
>>> len(case)
1
>>> bool(case)
True
>>> case = Case(xxx=False, yyy=True)
>>> 'zzz' in case
True
>>> 'yyy' in case
True
>>> 'xxx' in case
True
>>> sorted(case)
['yyy']
>>> len(case)
1
>>> bool(case)
True


#]]]doctest_examples_Case-end
#################################






#################################
#[[[doctest_examples_Flag-begin

>>> flag = Flag()
>>> flag
Flag()
>>> not flag
True
>>> otherwise(flag)
True
>>> len(flag)
0
>>> list(flag)
[]
>>> flag._keys
False
>>> flag.__getattribute__
False
>>> flag.xxx
False
>>> flag.yyy
False
>>> flag.zzz
False

>>> del flag.xxx
>>> not flag
True
>>> flag.xxx = False
>>> not flag
True
>>> flag
Flag()

>>> flag.xxx = True
>>> flag
Flag(xxx = True)
>>> flag != Flag(yyy=True)
True
>>> flag == Flag(xxx=True)
True
>>> flag != Flag()
True

>>> flag
Flag(xxx = True)
>>> not flag
False
>>> otherwise(flag)
False
>>> len(flag)
1
>>> list(flag)
['xxx']
>>> flag._keys
False
>>> flag.__getattribute__
False
>>> flag.xxx
True
>>> flag.yyy
False
>>> flag.zzz
False

>>> del flag.yyy
>>> flag != Flag(yyy=True)
True
>>> flag == Flag(xxx=True)
True
>>> flag != Flag()
True

>>> flag.yyy = True
>>> flag == Flag(xxx=True,yyy=True, kkk=False)
True
>>> flag == Flag(xxx=True,yyy=True)
True
>>> flag != Flag(yyy=True)
True
>>> flag != Flag(xxx=True)
True
>>> flag != Flag()
True

>>> flag
Flag(xxx = True, yyy = True)
>>> not flag
False
>>> otherwise(flag)
False
>>> len(flag)
2
>>> sorted(flag)
['xxx', 'yyy']
>>> flag._keys
False
>>> flag.__getattribute__
False
>>> flag.xxx
True
>>> flag.yyy
True
>>> flag.zzz
False





>>> del flag.yyy
>>> flag != Flag(yyy=True)
True
>>> flag == Flag(xxx=True)
True
>>> flag != Flag()
True



##_may_legal_keys
>>> flag = Flag()
>>> flag
Flag()
>>> 1 in flag
False
>>> '+++' in flag
False
>>> 'zzz' in flag
True
>>> flag.zzz
False
>>> flag.zzz = True
>>> flag.zzz
True
>>> flag.zzz = False
>>> flag.zzz
False


>>> flag = Flag([])
>>> flag
Flag([])
>>> 1 in flag
False
>>> '+++' in flag
False
>>> 'zzz' in flag
False
>>> flag.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz = False
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'

>>> flag = Flag(['xxx'])
>>> flag
Flag(['xxx'])
>>> 1 in flag
False
>>> '+++' in flag
False
>>> 'zzz' in flag
False
>>> flag.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz = False
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> 'xxx' in flag
True
>>> flag.xxx
False
>>> flag.xxx = True
>>> flag.xxx
True
>>> flag.xxx = False
>>> flag.xxx
False


>>> flag = Flag(['xxx'], zzz=True)
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag = Flag(['xxx'], zzz=False)
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag = Flag(['xxx'], xxx=True)
>>> flag
Flag(['xxx'], xxx = True)
>>> flag = Flag(['xxx', 'yyy'], xxx=True, yyy=False)
>>> flag
Flag(['xxx', 'yyy'], xxx = True)
>>> flag = Flag(['xxx', 'yyy'], xxx=False, yyy=False)
>>> flag
Flag(['xxx', 'yyy'])
>>> flag = Flag(['xxx', 'yyy'], xxx=True, yyy=True)
>>> flag
Flag(['xxx', 'yyy'], xxx = True, yyy = True)
>>> flag = Flag(['xxx', 'yyy'], xxx=True, zzz=True)
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> flag = Flag(['xxx', 'yyy'], xxx=0)
Traceback (most recent call last):
    ...
TypeError


>>> flag = Flag(['xxx', 'yyy'], xxx=False, yyy=True)
>>> flag
Flag(['xxx', 'yyy'], yyy = True)
>>> flag.xxx
False
>>> flag.yyy
True
>>> flag.xxx = True
>>> flag
Flag(['xxx', 'yyy'], xxx = True, yyy = True)
>>> flag.xxx
True
>>> flag.yyy
True
>>> flag.yyy = False
>>> flag
Flag(['xxx', 'yyy'], xxx = True)
>>> flag.xxx = False
>>> flag
Flag(['xxx', 'yyy'])
>>> flag.xxx = 1
Traceback (most recent call last):
    ...
TypeError
>>> flag[1] = True
Traceback (most recent call last):
    ...
TypeError
>>> flag['+++'] = True
Traceback (most recent call last):
    ...
ValueError: attr is not identifier: '+++'
>>> flag['zzz'] = True
Traceback (most recent call last):
    ...
KeyError: 'zzz'



>>> flag = Flag(['xxx', 'yyy'], xxx=False, yyy=True)
>>> flag
Flag(['xxx', 'yyy'], yyy = True)
>>> del flag.xxx
>>> del flag.xxx
>>> del flag.xxx
>>> flag
Flag(['xxx', 'yyy'], yyy = True)
>>> del flag.yyy
>>> flag
Flag(['xxx', 'yyy'])
>>> del flag.yyy
>>> del flag.yyy
>>> del flag.zzz
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> del flag['xxx']
>>> del flag['yyy']
>>> del flag['zzz']
Traceback (most recent call last):
    ...
KeyError: 'zzz'
>>> del flag['+++']
Traceback (most recent call last):
    ...
ValueError: attr is not identifier: '+++'
>>> del flag[0]
Traceback (most recent call last):
    ...
TypeError




>>> flag = Flag(['xxx', 'yyy'], xxx=False, yyy=True)
>>> 'zzz' in flag
False
>>> 'yyy' in flag
True
>>> 'xxx' in flag
True
>>> sorted(flag)
['yyy']
>>> len(flag)
1
>>> bool(flag)
True
>>> flag = Flag(xxx=False, yyy=True)
>>> 'zzz' in flag
True
>>> 'yyy' in flag
True
>>> 'xxx' in flag
True
>>> sorted(flag)
['yyy']
>>> len(flag)
1
>>> bool(flag)
True


#]]]doctest_examples_Flag-end
#################################



#]]]doctest_examples-end
#################################
#################################
#################################

#'''


__all__ = '''
    otherwise

    Case
        clear_case
        case2may_key
        case2may_legal_keys
        _check_identifier_is_a_legal_key_of_case
        is_identifier_a_legal_key_of_case
    Flag
        clear_flag
        flag2keys
        _flag2keys
        flag2may_legal_keys
        _check_identifier_is_a_legal_key_of_flag
        is_identifier_a_legal_key_of_flag
    '''.split()


from types import MappingProxyType
from seed.helper.repr_input import repr_helper

def otherwise(case, /):
    r = type(case).__otherwise__(case)
    if type(r) is not bool: raise TypeError
    return r


#section_Case, section_Flag

############################
############################
####### section_Case #######
############################
############################

def clear_case(case, /):
    r = type(case).__clear_case__(case)
    if r is not None: raise TypeError
def case2may_key(case, /):
    may_key = type(case).__case2may_key__(case)
    if not (may_key is None or type(may_key) is str): raise TypeError
    return may_key
def case2may_legal_keys(case, /):
    may_legal_keys = type(case).__case2may_legal_keys__(case)
    if not (may_legal_keys is None or type(may_legal_keys) is frozenset): raise TypeError
    return may_legal_keys

def _check_identifier_is_a_legal_key_of_case(case, attr, attr2Exception, /):
    if not is_identifier_a_legal_key_of_case(case, attr): raise attr2Exception(attr)
def is_identifier_a_legal_key_of_case(case, attr, /):
    #__is_identifier_a_legal_key_of_case__
    if type(attr) is not str: raise TypeError
    if not attr.isidentifier(): raise ValueError(f'attr is not identifier: {attr!r}')
    r = type(case).__is_identifier_a_legal_key_of_case__(case, attr)
    if not (type(r) is bool): raise TypeError
    return r
def to_ImmutableCase(case, /):
        __to_ImmutableCase__
def to_new_MutableCase(case, /):
        __to_new_MutableCase__
        check type and new-obj

#class_Case:[[[
class Case:
    #ImmutableCase
    __slots__ = ('_may_key', '_may_legal_keys')
    def __repr__(sf, /):
        it = iter(sf)
        for the_only_key in it:
            kwargs = {the_only_key:True}
            break
        else:
            kwargs = {}
        kwargs
        for _ in it:
            raise logic-err

        may_legal_keys = case2may_legal_keys(sf)
        if may_legal_keys is None:
            args = []
        else:
            legal_keys = may_legal_keys
            args = [sorted(legal_keys)]

        return repr_helper(sf, *args, **kwargs)


    __is_immutable_case__ = True
        #now immutable: Case is ImmutableCase
        #   see:MutableCase
    def __init__(sf, may_legal_keys=None, /, **kwargs):
        cls = type(sf)
        is_immutable_case = cls.__is_immutable_case__
        cls._XXX__init__(sf, is_immutable_case, may_legal_keys, **kwargs)
    def _XXX__init__(sf, is_immutable_case:bool, may_legal_keys=None, /, **kwargs):
        ###########################
        if not all(T is bool for T in map(type, kwargs.values())):raise TypeError
        if not sum(map(int, kwargs.values())) <= 1:raise ValueError
        if 1:
            #does py check kwargs?
            if not all(T is str for T in map(type, kwargs.keys())):raise TypeError
            if not all(k.isidentifier() for k in kwargs.keys()):raise ValueError
        kw_keys = frozenset(kwargs)

        #init_assign:_may_legal_keys
        if may_legal_keys is not None:
            legal_keys = frozenset(may_legal_keys)
            if not all(type(legal_key) is str for legal_key in legal_keys): raise TypeError
            if not all(legal_key.isidentifier() for legal_key in legal_keys): raise ValueError
            if not kw_keys <= legal_keys: raise KeyError
            may_legal_keys = legal_keys
            del legal_keys
        if not (may_legal_keys is None or type(may_legal_keys) is frozenset): raise logic-err
        object.__setattr__(sf, '_may_legal_keys', may_legal_keys)

            #update: __init__-API/__repr__/__getitem__/__setitem__/__delitem__/__eq__
            #add: case2may_legal_keys/__case2may_legal_keys__/_check_identifier_is_a_legal_key_of_case/is_identifier_a_legal_key_of_case/__is_identifier_a_legal_key_of_case__/__contains__

        #init_assign:_may_key
        Set = frozenset if is_immutable_flag else set
        _keys = Set(k for k,b in kwargs.items() if b)
        if _keys:
            [key] = _keys
            _may_key = key
        else:
            _may_key = None
        _may_key
        object.__setattr__(sf, '_may_key', _may_key)
        return
        r'''
        if 0:
            #init by no key
            clear_case(sf)
            #now immutable: Case is ImmutableCase
        for k, v in kwargs.items():
            if 1:
                # check all k!!! no "if v" + no "break"
                sf[k] = v
            elif 0:
                #bug: should check all k!!! "break"
                _check_identifier_is_a_legal_key_of_case(sf, k, KeyError)
                if v:
                    sf[k] = v
                    break
            elif 0:
                #bug: should check all k!!! "v==False"+"break"
                if v:
                    sf[k] = v
                    break
            else:
                raise logic-err
        else:
            #init by no key
            #bug:clear_case(sf)
            #   sine now no break above!
            pass
        #'''
    def __getattribute__(sf, attr, /):
        #KeyError not AttributeError
        return sf[attr]
        #######
        try:
            return sf[attr]
        except KeyError:
            raise AttributeError(attr)
    __setattr__ = None
    def _XXX__setattr__(sf, attr, v, /):
        #KeyError not AttributeError
        sf[attr] = v
        return
        #######
        try:
            sf[attr] = v
        except KeyError:
            raise AttributeError(attr)
    def _XXX__delattr__(sf, attr, /):
        #KeyError not AttributeError
        del sf[attr]
        return
        #######
        try:
            del sf[attr]
        except KeyError:
            raise AttributeError(attr)
    def _XXX__delitem__(sf, attr, /):
        #del sf[...] <==> clear_case(sf)
        #del sf[attr] <==> sf[attr] = False
        if attr is ... or sf[attr]:
            #attr:True->False
            #sf[attr] # check attr
            #   __getitem__:_check_identifier_is_a_legal_key_of_case(sf, attr, KeyError)
            clear_case(sf)
    def __contains__(sf, attr, /):
        return type(attr) is str and attr.isidentifier() and is_identifier_a_legal_key_of_case(sf, attr)
    def __is_identifier_a_legal_key_of_case__(sf, attr, /):
        r'precondition: attr is identifier'
        #is_identifier_a_legal_key_of_case(sf, attr)

        may_legal_keys = case2may_legal_keys(sf)
        if may_legal_keys is not None:
            legal_keys = may_legal_keys
            #if attr not in legal_keys: raise KeyError(attr)
            return attr in legal_keys
        else:
            #any identifier is legal
            return True

    def __getitem__(sf, attr, /):
        _check_identifier_is_a_legal_key_of_case(sf, attr, KeyError)

        may_key = case2may_key(sf)
        if may_key is None:
            return False
        else:
            key = may_key
            return key == attr
    def _XXX__setitem__(sf, attr, v, /):
        #if type(attr) is not str: raise TypeError
        if type(v) is not bool: raise TypeError
        #is_identifier_a_legal_key_of_case(sf, attr)
        if v:
            #at most one flag turn on
            #if not attr.isidentifier(): raise ValueError(f'attr={attr!r}')
            #bug: sf[attr] # check attr
            #   may not hold key as attr yet!!!
            _check_identifier_is_a_legal_key_of_case(sf, attr, KeyError)
            object.__setattr__(sf, '_may_key', attr)
        else:
            del sf[attr]
                #__delitem__:_check_identifier_is_a_legal_key_of_case(sf, attr, KeyError)



    def __iter__(sf, /):
        may_key = case2may_key(sf)
        if may_key is not None:
            key = may_key
            yield key
    def __len__(sf, /):
        may_key = case2may_key(sf)
        return int(may_key is not None)
    def __bool__(sf, /):
        may_key = case2may_key(sf)
        return (may_key is not None)
    def __otherwise__(sf, /):
        return not sf
    def _XXX__clear_case__(sf, /):
        object.__setattr__(sf, '_may_key', None)
    def __case2may_key__(sf, /):
        may_key = object.__getattribute__(sf, '_may_key')
        return may_key
    def __case2may_legal_keys__(sf, /):
        may_legal_keys = object.__getattribute__(sf, '_may_legal_keys')
        return may_legal_keys

    __hash__ = None
        #mutable obj has no hash
    #now immutable: Case is ImmutableCase
    def __hash__(sf, /):
        may_key = object.__getattribute__(sf, '_may_key')
        may_legal_keys = object.__getattribute__(sf, '_may_legal_keys')
        return hash((may_key, may_legal_keys))
    def __eq__(sf, other, /):
        if type(other) is not __class__:
            return NotImplemented

        return case2may_key(sf) == case2may_key(other) and case2may_legal_keys(sf) == case2may_legal_keys(other)

        lhs_may_key = case2may_key(sf)
        rhs_may_key = case2may_key(other)
        return lhs_may_key == rhs_may_key

    def __to_ImmutableCase__(sf, /):
        if type(sf) is ImmutableCase:
            return sf
        #may_key = case2may_key(sf)
        may_legal_keys = case2may_legal_keys(sf)
        kwargs = dict.fromkeys(it, True)
        return ImmutableCase(may_legal_keys, **kwargs)
    def __to_new_MutableCase__(sf, /):
        may_legal_keys = case2may_legal_keys(sf)
        kwargs = dict.fromkeys(it, True)
        return MutableCase(may_legal_keys, **kwargs)
#class_Case:]]]
#class Case:
ImmutableCase = Case

#class_MutableCase:[[[
class MutableCase(Case):
    __slots__ = ()
    __is_immutable_case__ = False
    __setattr__ = Case._XXX__setattr__
    __delattr__ = Case._XXX__delattr__
    __delitem__ = Case._XXX__delitem__
    __setitem__ = Case._XXX__setitem__
    __clear_case__ = Case._XXX__clear_case__
    __hash__ = None
        #mutable obj has no hash
#class_MutableCase:]]]
#class MutableCase(Case):





############################
############################
####### section_Flag #######
############################
############################

def clear_flag(flag, /):
    r = type(flag).__clear_flag__(flag)
    if r is not None: raise TypeError
def flag2keys(flag, /):
    r'!!!return view of set!!!'
    return MappingProxyType(_flag2keys(flag))
def _flag2keys(flag, /):
    r'!!!return mutable set!!!'
    keys = type(flag).__flag2keys__(flag)
    if not (type(keys) in[set, frozenset]): raise TypeError
    return keys
def flag2may_legal_keys(flag, /):
    may_legal_keys = type(flag).__flag2may_legal_keys__(flag)
    if not (may_legal_keys is None or type(may_legal_keys) is frozenset): raise TypeError
    return may_legal_keys

def _check_identifier_is_a_legal_key_of_flag(flag, attr, attr2Exception, /):
    if not is_identifier_a_legal_key_of_flag(flag, attr): raise attr2Exception(attr)
def is_identifier_a_legal_key_of_flag(flag, attr, /):
    #__is_identifier_a_legal_key_of_flag__
    if type(attr) is not str: raise TypeError
    if not attr.isidentifier(): raise ValueError(f'attr is not identifier: {attr!r}')
    r = type(flag).__is_identifier_a_legal_key_of_flag__(flag, attr)
    if not (type(r) is bool): raise TypeError
    return r

#class_Flag:[[[
class Flag:
    __slots__ = ('_keys', '_may_legal_keys')
    def __repr__(sf, /):
        it = iter(sf)
        kwargs = dict.fromkeys(it, True)
        for _ in it:
            raise logic-err

        may_legal_keys = flag2may_legal_keys(sf)
        if may_legal_keys is None:
            args = []
        else:
            legal_keys = may_legal_keys
            args = [sorted(legal_keys)]

        return repr_helper(sf, *args, **kwargs)

    r'''
    def __init__(sf, /, **kwargs):
        if not all(T is bool for T in map(type, kwargs.values())):raise TypeError
        if 1:
            #init by empty set
            clear_flag(sf)
        for k, v in kwargs.items():
            if v:
                sf[k] = v
    #'''
    __is_immutable_flag__ = True
        #now immutable: Flag is ImmutableFlag
        #   see:MutableFlag
    def __init__(sf, may_legal_keys=None, /, **kwargs):
        cls = type(sf)
        is_immutable_flag = cls.__is_immutable_flag__
        cls._XXX__init__(sf, is_immutable_flag, may_legal_keys, **kwargs)
    def _XXX__init__(sf, is_immutable_flag:bool, may_legal_keys=None, /, **kwargs):
        if not all(T is bool for T in map(type, kwargs.values())):raise TypeError
        if 1:
            #does py check kwargs?
            if not all(T is str for T in map(type, kwargs.keys())):raise TypeError
            if not all(k.isidentifier() for k in kwargs.keys()):raise ValueError
        kw_keys = frozenset(kwargs)

        #init_assign:_may_legal_keys
        if may_legal_keys is not None:
            legal_keys = frozenset(may_legal_keys)
            if not all(type(legal_key) is str for legal_key in legal_keys): raise TypeError
            if not all(legal_key.isidentifier() for legal_key in legal_keys): raise ValueError
            if not kw_keys <= legal_keys: raise KeyError
            may_legal_keys = legal_keys
            del legal_keys
        if not (may_legal_keys is None or type(may_legal_keys) is frozenset): raise logic-err
        object.__setattr__(sf, '_may_legal_keys', may_legal_keys)
            #update: __init__-API/__repr__/__getitem__/__setitem__/__delitem__/__eq__
            #add: flag2may_legal_keys/__flag2may_legal_keys__/_check_identifier_is_a_legal_key_of_flag/is_identifier_a_legal_key_of_flag/__is_identifier_a_legal_key_of_flag__/__contains__

        #init_assign:_keys
        Set = frozenset if is_immutable_flag else set
        _keys = Set(k for k,b in kwargs.items() if b)
        object.__setattr__(sf, '_keys', _keys)
        return
        r'''
        if 0:
            #init by empty set
            object.__setattr__(sf, '_keys', set())
            clear_flag(sf)
            #now immutable: Flag is ImmutableFlag
        else:
            object.__setattr__(sf, '_keys', frozenset())
        for k, v in kwargs.items():
            if 1:
                # check all k!!! no "if v" + no "break"
                sf[k] = v
            elif 0:
                #bug: should check all k!!! "break"
                _check_identifier_is_a_legal_key_of_flag(sf, k, KeyError)
                if v:
                    sf[k] = v
                    break
            elif 0:
                #bug: should check all k!!! "v==False"+"break"
                if v:
                    sf[k] = v
                    break
            else:
                raise logic-err
        else:
            #init by no key
            #bug:clear_flag(sf)
            #   sine now no break above!
            pass
        #'''
    def __getattribute__(sf, attr, /):
        return sf[attr]
    def _XXX__setattr__(sf, attr, v, /):
        sf[attr] = v
    def _XXX__delattr__(sf, attr, /):
        del sf[attr]
    def _XXX__delitem__(sf, attr, /):
        #del sf[...] <==> clear_flag(sf)
        #del sf[attr] <==> sf[attr] = False
        if attr is ...:
            clear_flag(sf)
        else:
            sf[attr] = False
                #__setitem__: _check_identifier_is_a_legal_key_of_flag(sf, attr, KeyError)
    def __contains__(sf, attr, /):
        return type(attr) is str and attr.isidentifier() and is_identifier_a_legal_key_of_flag(sf, attr)
    def __is_identifier_a_legal_key_of_flag__(sf, attr, /):
        r'precondition: attr is identifier'
        #is_identifier_a_legal_key_of_flag(sf, attr)

        may_legal_keys = flag2may_legal_keys(sf)
        if may_legal_keys is not None:
            legal_keys = may_legal_keys
            #if attr not in legal_keys: raise KeyError(attr)
            return attr in legal_keys
        else:
            #any identifier is legal
            return True


    def __getitem__(sf, attr, /):
        _check_identifier_is_a_legal_key_of_flag(sf, attr, KeyError)

        keys = _flag2keys(sf)
        return attr in keys
    def _XXX__setitem__(sf, attr, v, /):
        if type(v) is not bool: raise TypeError
        _check_identifier_is_a_legal_key_of_flag(sf, attr, KeyError)

        keys = _flag2keys(sf)
        if v:
            #many flags turn on at same time
            keys.add(attr)
        else:
            keys.discard(attr)



    def __iter__(sf, /):
        keys = _flag2keys(sf)
        return iter(keys)
    def __len__(sf, /):
        keys = _flag2keys(sf)
        return len(keys)
    def __bool__(sf, /):
        keys = _flag2keys(sf)
        return bool(keys)
    def __otherwise__(sf, /):
        return not sf
    def _XXX__clear_flag__(sf, /):
        #bug: since new-def flag2keys() return set-view: object.__setattr__(sf, '_keys', set())
        keys = _flag2keys(sf)
        keys.clear()
    def __flag2keys__(sf, /):
        r'!!!return mutable set!!!'
        keys = object.__getattribute__(sf, '_keys')
        return keys
    def __flag2may_legal_keys__(sf, /):
        may_legal_keys = object.__getattribute__(sf, '_may_legal_keys')
        return may_legal_keys

    __hash__ = None
        #mutable obj has no hash
    #now immutable: Flag is ImmutableFlag
    def __hash__(sf, /):
        keys = _flag2keys(sf)
        may_legal_keys = object.__getattribute__(sf, '_may_legal_keys')
        return hash((keys, may_legal_keys))
    def __eq__(sf, other, /):
        if type(other) is not __class__:
            return NotImplemented

        return _flag2keys(sf) == _flag2keys(other) and flag2may_legal_keys(sf) == flag2may_legal_keys(other)

        lhs_keys = _flag2keys(sf)
        rhs_keys = _flag2keys(other)
        return lhs_keys == rhs_keys

#class_Flag:]]]
#class Flag:
ImmutableFlag = Flag

#class_MutableFlag:[[[
class MutableFlag(Flag):
    __slots__ = ()
    __is_immutable_flag__ = False
    __setattr__ = Flag._XXX__setattr__
    __delattr__ = Flag._XXX__delattr__
    __delitem__ = Flag._XXX__delitem__
    __setitem__ = Flag._XXX__setitem__
    __clear_flag__ = Flag._XXX__clear_flag__
    __hash__ = None
        #mutable obj has no hash
#class_MutableFlag:]]]
#class MutableFlag(Flag):












if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


