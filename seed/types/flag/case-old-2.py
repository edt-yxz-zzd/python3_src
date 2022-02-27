
#goto:new_start
#[[[[[[[[[[
r"""
e ../../python3_src/seed/helper/case.py
  -->> e ../../python3_src/seed/types/flag/Flag.py
!mv -n ../../python3_src/seed/helper/case.py ../../python3_src/seed/types/flag/case-old.py

py -m seed.helper.case
py -m nn_ns.app.debug_cmd   seed.helper.case
#[[[[[
#[[[
r'''
减少同一值的重复对象
e ../../python3_src/seed/helper/reduce_number_of_objects_with_same_value.py
    mutex_group_set for hybrid flag
        __init__([key4discrete_mutex_group...], [{*keys4nondiscrete_mutex_group}...])
        this config should save global...


----

update doctest_examples
+to_ImmutableCase()
+to_new_MutableCase()
+to_ImmutableFlag()
+to_new_MutableFlag()

infinite?
    arbitrary?prefix?suffix?
mutex group
"[tmp_mutex_group_name]:+attr"
":+attr"
    the_default_tmp_mutex_group_name
"@+attr"
    new_tmp_mutex_group_name
",+attr"
    the_prev_or_default_tmp_mutex_group_name
classified by mutex group pattern:
    discrete mutex group
    single mutex group
    hybrid mutex group
classified by possible keys pattern:
    * who offer constraint<key>:
        * cls constraint -> KeyTypeError(of_obj_ops_at_obj_ops)/KeyValueError(of_obj_at_obj_ops)
        * obj constraint -> KeyValueError(of_obj_at_obj)
    * key set:
        * arbitrary if s.t. constraint
        * finite set
        * prefix set
        * complement of prefix set


class:
    possible_keys=potential_keys
        KeyTypeError
    legal_keys | illegal_keys
        KeyValueError
    active_keys=present_keys | passive_keys=absent_keys=inactive_keys
    possible_keys = legal_keys+illegal_keys
    legal_keys = active_keys+passive_keys

    __contains__
        # key in legal_keys
    __bool__
        since "if not case:" is common op
        bool(active_keys)
    __repr__
        since io read/write case by human is importance op as symbol value
    if turnon_keys_known_finite:
        __iter__#iter turnon_keys not possible_keys
            iter(active_keys)
        __len__
            len(active_keys)
    __eq__
    if immutable:
        __hash__
    else:
        __setattr__
        __delattr__
        __setitem__
        __delitem__
    __getattribute__
    __getitem__

    key_is_str
    if active_keys_at_cls:
        assert mutex_groups_setting_at_cls
        assert legal_keys_at_cls
        __init__()
    else:
        assert active_keys_at_obj
        #not if legal_keys_at_cls:
        if mutex_groups_setting_at_cls:
            assert legal_keys_at_cls
            __init__(echo.xxx, ...) #list active_keys

        else:
            ###assert legal_keys_at_obj
            assert mutex_groups_setting_at_obj
            assert active_keys_at_obj
            if legal_keys_finite:
                if hybrid:
                    __init__([*active_keys4discrete_mutex_groups], [*passive_keys4discrete_mutex_groups], {active_key:[*passive_keys_in_same_active_mutex_group]}, [[*keys_in_passive_mutex_group]...])
                    __init__([on.xxx, off.yyy, ...], ..., init_style=???) #list  legal_keys as mutex_groups with +- prefix group
                        [[+-key | key<-mutex_group] | mutex_group<-mutex_groups]
                        array_section_per_mutex_group&prefix_per_key
                    __init__(on.xxx, off.yyy, ..., 0, on.xxx, off.yyy, ..., 0, ...) #list  legal_keys as mutex_groups sep by 0 with +- prefix
                        (join 0 [[+-key | key<-mutex_group] | mutex_group<-mutex_groups])
                        0sep_section_per_mutex_group&prefix_per_key
                    __init__(echo.xxx, echo.yyy, ..., 0, echo.xxx, 1, echo.yyy, ..., 0, ...) #list  legal_keys as mutex_groups sep by 0 put 1 before active_keys or 0 or at end #1 must occur per mutex_group, at end or before 0 to indicate no active_key for such mutex_group
                        (join 0 [[1?key? | key<-mutex_group] | mutex_group<-mutex_groups])
                        0sep_section_per_mutex_group&1mark_per_section
                    __init__([echo.xxx, echo.yyy, ..., 0, echo.xxx, echo.yyy, ..., 0, ...], [echo.xxx, echo.yyy, ..., 0, echo.xxx, echo.yyy, ..., 0, ...]) #list  legal_keys as mutex_groups sep by 0 cut mutex_groups into 2 part: 1st part one active_key per mutex_group(the 1st key), 2nd part no active_key per group
                        (join 0 [[key | key<-mutex_group] | mutex_group<-mutex_groups, active mutex_group], join 0 [[key | key<-mutex_group] | mutex_group<-mutex_groups, passive mutex_group])
                        array1[0sep_section_per_active_mutex_group]&array2[0sep_section_per_passive_mutex_group]
                    __init__([active_keys4discrete_mutex_groups...], [passive_keys4discrete_mutex_groups], echo.xxx, echo.yyy, ..., 0, echo.xxx, 1, echo.yyy, ..., 0, ...) #list  legal_keys as mutex_groups sep by 0 put 1 before active_keys, but group active_keys+passive_keys of all discrete_mutex_groups
                        (([key | mutex_group<-mutex_groups, 1 == len mutex_group, active mutex_group, key<-mutex_group], [key | mutex_group<-mutex_groups, 1 == len mutex_group, passive mutex_group, key<-mutex_group]) ++ join 0 [[1?key? | key<-mutex_group] | mutex_group<-mutex_groups, 2 <= len mutex_group])
                        active_keys4discrete_mutex_groups&passive_keys4discrete_mutex_groups&0sep_section_per_len_ge2_mutex_group&1mark_per_section
                elif discrete:
                    __init__(on.xxx, off.yyy, ...) #list legal_keys with +- prefix
                    __init__([echo.xxx, ...], [echo.yyy, ...]) #list active_keys+passive_keys
                elif single:
                    __init__(echo.xxx, ..., 1, echo.yyy, ...) #list legal_keys put 1 before the maybe active_key #1 must occur, at end to indicate no active_key




    if turnon_keys_known_finite:
        ###只考虑 开启的标志
        __isub__ -=
        if lhs discrete or rhs single or ...?
            #__iadd__ +=
            __ilshift__ <<=
    if turnon_keys_known_finite and legal_keys are eq and mutex_groups are same:
        __and__ &
        if discrete:
            __xor__ ^
            __or__ |
            __invert__



#'''
#]]]
#[[[

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
#]]]
#]]]]]


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

#"""
#]]]]]]]]]]





#new_start

import weakref#WeakKeyDictionary, ref
import collections#Counter


from seed.types.FrozenDict import FrozenDict, mk_FrozenDict, HalfFrozenDict
from seed.types.view.View import SetView, MapView, SeqView

from seed.helper.get4may import nmay2tmay#, get4nmay, fget4nmay, fget4nmay__human, xget4nmay__human

from seed.helper.reduce_number_of_objects_with_same_value import mk_new_register_point, get_or_mk_named_register_point, StdValue2FastKeyWrapper, Value2Weakable, get_or_register_the_std_obj_with_same_value_at, is3_the_std_obj_with_same_value_at, get_the_std_obj_with_same_value_at, SpecialKeyByNonHashable, SpecialKey, ALL_KEYS

r'''
if value_obj is not weakable:
    register_name = ...
    value_obj = ...
    standardize_all_subobj4weakable_value_obj = ...
    weakable_value_obj = Value2Weakable(value_obj)
    del value_obj
    register_point = get_or_mk_named_register_point(register_name)
    std_weakable_value_obj = get_the_std_obj_with_same_value_at(register_point, weakable_value_obj)
        #std_weakable_value_obj = get_or_register_the_std_obj_with_same_value_at(register_point, weakable_value_obj, standardize_all_subobj=standardize_all_subobj4weakable_value_obj)
    del weakable_value_obj
    std_value_obj = std_weakable_value_obj.the_value_obj
    ##################################
    ######using std_value_obj but hold std_weakable_value_obj
    #################################
if value_obj is weakable:
    register_name = ...
    value_obj = ...
    standardize_all_subobj4value_obj = ...
    register_point = get_or_mk_named_register_point(register_name)
    std_value_obj = get_the_std_obj_with_same_value_at(register_point, value_obj)
        #std_weakable_value_obj = get_or_register_the_std_obj_with_same_value_at(register_point, value_obj, standardize_all_subobj=standardize_all_subobj4value_obj)
    del value_obj
    #################################
    #####using&hold std_value_obj
    #################################
if use std_value_obj as mapping key:
    #use wrapped_std_value_obj instead
    wrapped_std_value_obj = StdValue2FastKeyWrapper(std_weakable_value_obj)


#'''




class Ops4MkStdFlagKeySet:
    r'''
    key may be str, but str is not weakable, we wrap it into flag_key

    =====
    see: reduce_number_of_objects_with_same_value::_try_builtins_weakable()
        ok_ls=[frozenset(), set(), TypeError, repr, type]
        bad_ls=[(), '', b'', 1, True, None, Ellipsis, NotImplemented, [], {}]


    =====
    =====
    #key
    #fkey = flag_key = nonstd_flag_key = key | Value2Weakable(key)
    #sfkey = std_flag_key #via register_point
    #wsfkey = wrapped_std_flag_key #by StdValue2FastKeyWrapper
    #
    # _set = _nonstd_set
    # _sset = _std_set
    # _wsset = _wrapped_std_set
    #
    # _2_ = _to_ = _nonstdto_ #nonstd_mapping
    # _s2_ = _sto_ = _stdto_
    # _ws2_ = _wsto_ = _wrapped_stdto_

    =====
    default-impl:
        std_flag_key
            =sfkey
        std_wrapped_std_flag_key_set
            #old:std_std_flag_key_set
            =wsfkey_sset
            #sset<wsfkey>
        wrapped_std_flag_key_stdto_std_wrapped_std_flag_key_set
            #old:std_flag_key_stdto_std_std_flag_key_set
            =wsfkey_s2wsfkey_sset
            #s2<wsfkey, sset<wsfkey> >
        wrapped_std_wrapped_std_flag_key_set_stdto_std_flag_key
            #old:std_std_flag_key_set_stdto_std_flag_key
            =wsfkey_wsset_s2sfkey
            #s2<wsset<wsfkey>, sfkey>
            ===new:
                vs fkey
                vs wsfkey_set
                vs wsfkey2wsfkey_sset
                vs wsfkey_wsset2sfkey
            ===old:
                vs nonstd_flag_key
                vs nonstd_std_flag_key_set
                vs std_flag_key_nonstdto_std_std_flag_key_set
                vs std_std_flag_key_set_nonstdto_std_flag_key
        ===
        std_flag_key = cached-Value2Weakable<key>
                       ^^^std  ^^^flag
        wsfkey_sset
            = std_wrapped_std_flag_key_set
            = cached-frozenset<StdValue2FastKeyWrapper<std_flag_key> >
               ^^^std  ^^^set   ^^^wrapped             ^^^std_flag_key
            #discrete_mutex_groups
                #all-in-one
            #non_discrete_mutex_group
                #one-in-one
            #to find out whether key contained in discrete_mutex_group
            #to query whether discrete_mutex_group unloaded
                #only-for-ImmutableFlag
        wsfkey_s2wsfkey_sset = cached-FrozenDict<wsfkey, wsfkey_sset>
            #to find out the containing non_discrete_mutex_group of a given key
        wsfkey_wsset_s2sfkey = cached-FrozenDict<wsfkey_wsset, std_flag_key>
            #to query whether non_discrete_mutex_group unloaded, which key if loaded
                #only-for-ImmutableFlag

    =====
    wsfkey_sset:
        * all keys of all discrete_mutex_groups of a given mutex_groups_setting
        * all keys of a non_discrete_mutex_group of a given mutex_groups_setting
    =====
    =====
    #'''

    _register_point4sfkey = mk_new_register_point()
        #sfkey
    _register_point4wsfkey_sset = mk_new_register_point()
        #sset<wsfkey>
        #wsfkey_sset
    _register_point4wsfkey_s2wsfkey_sset = mk_new_register_point()
        #s2<wsfkey, sset<wsfkey> >
        #wsfkey_s2wsfkey_sset
    _register_point4wsfkey_wsset_s2sfkey = mk_new_register_point()
        #s2<wsset<wsfkey>, sfkey>
        #wsfkey_wsset_s2sfkey
    def get_register_point4sfkey(sf, /):
        return sf._register_point4sfkey
    def get_register_point4wsfkey_sset(sf, /):
        return sf._register_point4wsfkey_sset
    def get_register_point4wsfkey_s2wsfkey_sset(sf, /):
        return sf._register_point4wsfkey_s2wsfkey_sset
    def get_register_point4wsfkey_wsset_s2sfkey(sf, /):
        return sf._register_point4wsfkey_wsset_s2sfkey

    def is_key_weakable(sf, /):
        return False

    def get_key_from_flag_key(sf, flag_key, /):
        '#get_key_from_flag_key<->_mk_nonstd_flag_key'
        if sf.is_key_weakable():
            return flag_key
        else:
            return flag_key.the_value_obj
    def _mk_nonstd_flag_key(sf, key, /):
        'nonstd_flag_key is used for tmp query;   # get_key_from_flag_key<->_mk_nonstd_flag_key'
        if sf.is_key_weakable():
            return key
        else:
            return Value2Weakable(key)
    def mk_std_flag_key(sf, key, /):
        'std_flag_key is used for long-term storage'
        nonstd_flag_key = sf._mk_nonstd_flag_key(key)
        std_flag_key = get_the_std_obj_with_same_value_at(sf.get_register_point4flag_key(), nonstd_flag_key)
        return std_flag_key
    def _mk_wsfkey_set_from_std_flag_keys(sf, std_flag_keys, /):
        'Iter sfkey -> wsfkey_set'
        #new:wsfkey_set
        return frozenset(map(StdValue2FastKeyWrapper, std_flag_keys))
        #old:nonstd_std_flag_key_set
        return frozenset(std_flag_keys)
    def mk_wsfkey_sset_from_std_flag_keys(sf, std_flag_keys, /):
        'Iter sfkey -> wsfkey_sset'
        #old:std_std_flag_key_set
        #new:wsfkey_sset
        wsfkey_set = sf._mk_wsfkey_set_from_std_flag_keys(std_flag_keys)
        wsfkey_sset = get_the_std_obj_with_same_value_at(sf.get_register_point4wsfkey_sset(), wsfkey_set)
        return wsfkey_sset
    def mk_wsfkey_sset_from_keys(sf, keys, /):
        'Iter key -> wsfkey_sset'
        std_flag_keys = map(sf.mk_std_flag_key, keys)
        wsfkey_sset = sf.mk_wsfkey_sset_from_std_flag_keys(std_flag_keys)
        return wsfkey_sset
    def _mk_wsfkey2wsfkey_sset_from_partition__wsfkey_ssets(sf, partition__wsfkey_ssets, /):
        'wsfkey_ssets@partition -> wsfkey2wsfkey_sset@grouping'
        #partition__wsfkey_ssets -> grouping__wsfkey2wsfkey_sset
        len(partition__wsfkey_ssets)
        L = sum(map(len, partition__wsfkey_ssets))
        wsfkey2wsfkey_sset = mk_FrozenDict((wsfkey, wsfkey_sset) for wsfkey_sset in partition__wsfkey_ssets for wsfkey in wsfkey_sset)
        if not L == len(wsfkey2wsfkey_sset): raise ValueError(f'not partition since not mutex')
        if not all(T is StdValue2FastKeyWrapper for T in map(type, wsfkey2wsfkey_sset)): raise TypeError
        return wsfkey2wsfkey_sset
    def _mk_wsfkey_s2wsfkey_sset_from_partition__wsfkey_ssets(sf, partition__wsfkey_ssets, /):
        'wsfkey_ssets@partition -> wsfkey_s2wsfkey_sset@grouping'
        #partition__wsfkey_ssets -> grouping__wsfkey_s2wsfkey_sset
        wsfkey2wsfkey_sset = sf._mk_wsfkey2wsfkey_sset_from_partition__wsfkey_ssets(partition__wsfkey_ssets)

        wsfkey_s2wsfkey_sset = get_the_std_obj_with_same_value_at(sf.get_register_point4wsfkey_s2wsfkey_sset(), wsfkey2wsfkey_sset)
        assert L == len(wsfkey_s2wsfkey_sset)
        return wsfkey_s2wsfkey_sset
    def _mk_iter_wsfkey_ssets_from_partition__keyss(sf, partition__keyss, /):
        'keyss@partition -> (Iter wsfkey_ssets)@partition'
        #partition__keyss -> partition__iter_wsfkey_ssets
        #tuple to mk partition__wsfkey_ssets
        return map(sf.mk_wsfkey_sset_from_keys, keyss)
    def mk_wsfkey_s2wsfkey_sset_from_partition__keyss(sf, partition__keyss, /):
        'keyss@partition -> wsfkey_s2wsfkey_sset@grouping'
        #partition__keyss -> grouping__wsfkey_s2wsfkey_sset
        iter_wsfkey_ssets = sf._mk_iter_wsfkey_ssets_from_partition__keyss(partition__keyss)
        partition__wsfkey_ssets = tuple(iter_wsfkey_ssets)
        wsfkey_s2wsfkey_sset = sf._mk_wsfkey_s2wsfkey_sset_from_partition__wsfkey_ssets(partition__wsfkey_ssets)
        return wsfkey_s2wsfkey_sset
    def _verify_is_active_wsfkey_set_mutex(sf, discrete_mutex_groups__may_wsfkey_sset, grouping__wsfkey_s2wsfkey_sset, active_wsfkey_set, /):
        #active_wsfkey_set:  wsfkey_set = sf._mk_wsfkey_set_from_std_flag_keys(std_flag_keys)
        discrete_mutex_groups__tmay_wsfkey_sset = nmay2tmay(discrete_mutex_groups__may_wsfkey_sset)
        del discrete_mutex_groups__may_wsfkey_sset
        return _verify_is_active_wsfkey_set_mutex__tmay(discrete_mutex_groups__tmay_wsfkey_sset, grouping__wsfkey_s2wsfkey_sset, active_wsfkey_set, wsf_vs_sf__group_descriptor=True)




class PartitionFlag:
    r'''
    partition :: set<nonempty_set<key> >
    mutex_groups_setting:
        partition == mutex_groups_setting
    legal_keys:
        legal_keys == reduce (\-/) partition
        ; legal_keys is definition-domain of partition/mutex_groups_setting
    ===
    active_key:
        each mutex_group has at most one active_key #==>> mutex
    passive_key:
        key that is not active_key
    active_mutex_group
        mutex_group that contains active_key
    passive_mutex_group
        mutex_group that not contain active_key
    ===
    flag:
        flag ==[logic-conceptual]== (partition, active_key_set, proof_active_keys_not_conflict)
    ===
    __new__ args:
        if ___of_cls_at_cls__known_active_keys_without_instance___:
            __new__()
            #<<== ___of_obj_at_cls__is_empty_partition___
        elif not ___of_cls_at_cls__known_to_have_only_finite_active_keys___:
            NotImplemented
        elif ___of_cls_at_cls__known_partition_without_instance___:
            __new__(active_keys)
            #important partition with infinite legal_keys: ___of_obj_at_cls__is_single_partition___, ___of_obj_at_cls__is_discrete_partition___, prefix_group_style_for_seq_key
        elif not ___of_cls_at_cls__known_to_have_only_finite_legal_keys___:
            NotImplemented
        elif ___of_obj_at_cls__is_single_partition___&___of_obj_at_cls__is_discrete_partition___:
            __new__(is_active_key, the_only_key)
        elif ___of_obj_at_cls__is_single_partition___:
            __new__(tmay_active_key, passive_keys)
        elif ___of_obj_at_cls__is_discrete_partition___:
            __new__(active_keys, passive_keys)
            #TODO: hybrid+prefix_group_style_for_seq_key




    ##########
    all func named by ___xxx___
        use xxx(cls, ...) instead of call cls.___xxx___(...)
            example: see body of ___of_obj_at_obj__is_mutable_instance___
                use of_cls_at_cls__is_mutable_class(cls)

    all query func named by ___xxx___
        can be callable/bool/NotImplemented

    all non-query func named by ___xxx___
        can be callable/NotImplemented

    of_obj_at_obj:
    of_obj_at_cls:
    of_cls_at_cls:
        of_obj vs of_cls:
            this piece info were conceptual belong to obj or cls
        at_obj vs at_cls:
            this piece info is physical belong to obj or cls
        there are 3 possible combination, all list above
            #of_cls_at_obj is meaningless

    #'''
    @classmethod
    @abstractmethod
    def ___of_cls_at_cls__is_abstract_class___(cls, /):
        'if not abstract, then perform constraint-check on this class'
        return True

    def ___of_obj_at_obj__is_mutable_instance___(sf, /):
        'mutable instance, ie. is this instance mutable'
        cls = type(sf)
        if of_cls_at_cls__is_mutable_class(cls):
            return True
        if of_cls_at_cls__is_immutable_class(cls):
            return False
        raise NotImplementedError

    @classmethod
    def ___of_cls_at_cls__is_mutable_class___(cls, /):
        'mutable class, ie. all instances are mutable'
        return False

    @classmethod
    def ___of_cls_at_cls__is_immutable_class___(cls, /):
        'immutable class, ie. all instances are immutable'
        return False

    @classmethod
    def ___of_cls_at_cls__known_legal_keys_without_instance___(cls, /):
        'legal_keys is info of_cls; may or may infinite; can call is_elem_of-test without instance; repr neednot show info about legal_keys'
        return False

    @classmethod
    def ___of_cls_at_cls__known_partition_without_instance___(cls, /):
        '___of_cls_at_cls__known_partition_without_instance___ ==>> ___of_cls_at_cls__known_legal_keys_without_instance___; repr neednot show info about partition'
        return False

    @classmethod
    def ___of_cls_at_cls__known_active_keys_without_instance___(cls, /):
        '___of_cls_at_cls__known_active_keys_without_instance___ ==>> ___of_cls_at_cls__known_partition_without_instance___; repr neednot show info about active_keys, hence only show class name, ie. __new__ takes no input!'
        return False

    @classmethod
    def ___of_cls_at_cls__known_to_have_only_finite_active_keys___(cls, /):
        'each instance has only finite active_keys; but legal_keys can be infinite, no upperbound for len of active_keys of an instance; required by enum-style-repr needed to list all active_keys'
        return False

    @classmethod
    def ___of_cls_at_cls__known_to_have_only_finite_legal_keys___(cls, /):
        'each instance has only finite legal_keys;  required by enum-style-repr needed to list all legal_keys/partition'
        return False

    @classmethod
    def ___of_obj_at_cls__is_discrete_partition___(cls, /):
        'all mutex_groups are of len 1 of_obj'
        return False

    @classmethod
    def ___of_obj_at_cls__is_single_partition___(cls, /):
        'only one mutex_group'
        return False

    @classmethod
    def ___of_obj_at_cls__is_empty_partition___(cls, /):
        'no mutex_groups; ___of_obj_at_cls__is_empty_partition___ ==>> ___of_cls_at_cls__known_active_keys_without_instance___&___of_obj_at_cls__is_discrete_partition___&not ___of_obj_at_cls__is_single_partition___'
        return False

    @classmethod
    def ___of_obj_at_cls__legal_key2mutex_group_name___(cls, key, /):
        '___of_obj_at_cls__legal_key2mutex_group_name___ impled <==> ___of_cls_at_cls__known_partition_without_instance___'
        raise NotImplementedError

    @classmethod
    def ___of_obj_at_cls__is_key_a_legal_key___(cls, key, /):
        'not legal -> KeyError; ___of_obj_at_cls__is_key_a_legal_key___ impled <==> ___of_cls_at_cls__known_legal_keys_without_instance___'
        raise NotImplementedError

    @classmethod
    def ___of_cls_at_cls__is_obj_a_key___(cls, obj, /):
        'not key -> TypeError/ValueError'
        return True
        raise NotImplementedError

    @classmethod
    def ___of_cls_at_cls__get_ops4MkStdFlagKeySet___(cls, /):
        '-> Ops4MkStdFlagKeySet'
        raise NotImplementedError


is_key_a_seq
prefix_group_style_when_key_is_seq
    group can be described by a prefix
"prefix" abstract to "group_descriptor"+"verify_all_groups_mutex_pairwise"
can abstract to opaque_partition obj
    opaque_partition :: key -> tmay group_descriptor

std_:
    std_xxx is std_yyy
        instead of: std_xxx == std_yyy
flag
    .ops4partition
        #immutable
        of_obj_at_cls
        of_obj_at_obj
    .std_partition#partition==>>legal_keys
        #immutable
        of_obj_at_cls
        of_obj_at_obj
    .active_wsfkey_set#active_keys
        mutable
            .non_discrete_wsfgroup_descriptor2active_wsfkey
                #mutable ==>> _2_ not _s2_
                #   hence wsfkey not sfkey
        immutable
            #.active_wsfkey_sset === .active_wsfkey_set
            of_obj_at_cls
            of_obj_at_obj
    ====
    repr(flag)
    flag == other
        #cmp: (.std_partition, .active_wsfkey_set)
        #   since flag[key] ==>> legal_keys
    get_active_keys_view_of(flag)
        not flag
        len(flag)
        iter(flag)
    get_the_std_partition_of(flag)
        #legal_keys
        key in flag
        flag[key] #bool
            # + wsfkey in .std_partition #legal_keys:KeyError
            # + wsfkey in .active_wsfkey_set #active_keys:bool
            ====identifier
            hasattr(flag, key)
                #using "key in flag" instead
                #since __getattribute__ uniform to raise KeyError, hasattr catch AttributeError
                #or: raise KeyError_AttributeError
            getattr(flag, key)
    #neednot non_discrete_wsfgroup_descriptor2active_wsfkey
        flag - other
        flag - keys
        flag << other
        flag << keys
            # + .partition.verify_active_wsfkey_set(other.active_keys)
            # + for k in other: flag[k]=True
            #   required ???non_discrete_wsfgroup_descriptor2active_wsfkey???
            #   no, since create new obj, O(N), neednot lookup
    ====mutable
    del flag[key]
    flag[key] = True
        # + .std_partition[wsfkey]
        # + .std_partition.tmay_wsfgroup_descriptor4discrete_mutex_groups
        # + .non_discrete_wsfgroup_descriptor2active_wsfkey
        ====identifier
        delattr(flag, key)
        setattr(flag, key, True)
        flag -= other
        flag -= keys
        flag <<= other
        flag <<= keys
            # + .partition.verify_active_wsfkey_set(other.active_keys)
            # + for k in other: flag[k]=True
    ====immutable
    hash(flag)

API_ops4key_standardize
API_ops4partition
API_partition



API_ops4key_standardize:
ops4key_standardize:
    #TODO: global_funcs -> ops.funcs
    #TODO: global_type_fmt_style_register_point_name
    #TODO: is3 update to is
    #   register_point add .weak_value_dict<weakref<wrapped_std>, std>
    #   or: weakref.finialize/override __setitem__ + set<id<std> >
    is_std<xxx>
    to_std<xxx>
        #mk/get
        xxx =
            fkey
            wsfkey_set
            ...
    local_register_point_name2global_type_fmt_style_register_point_name
        local_register_point_name =
            "sfkey"
            "wsfkey_sset"
            "wsfkey_s2wsfkey_sset"
            "wsfkey_wsset_s2sfkey"
        global_type_fmt_style_register_point_name example:
            #str - key
            #Value2Weakable<str> - fkey
            #get_or_register_the_std_obj_with_same_value_at$<Value2Weakable<str> > - sfkey
            #StdValue2FastKeyWrapper<get_or_register_the_std_obj_with_same_value_at$<Value2Weakable<str> > > - wsfkey
            #
            #
            #using 3 builtins ops:
            #   id4hash$
            #   std$
            #   weakable$
            #
            #
            #whole global name should startswith "std$"
            #   frozenset[id4hash$std$...]
            #   FrozenDict[id4hash$std$...,std$...]
            "std$weakable$str"
            "std$frozenset[id4hash$std$weakable$str]"
            "std$FrozenDict[id4hash$std$weakable$str,std$frozenset[id4hash$std$weakable$str]]"
            "std$FrozenDict[id4hash$std$frozenset[id4hash$std$weakable$str,std$weakable$str]]"

    is_key_weakable
    is__key2fkey__echo
        #is__key2fkey__echo ==>> is_key_weakable
    key2fkey
        #key maynot weakable
        #fkey is weakable key
    std_value2wrapped_std_value
        #use id<std_value> as hash<wrapped_std_value>
        #use is<std_value> as eq<wrapped_std_value>


    is_std__fkey(fkey) == is_std_("sfkey", fkey)
    fkey2sfkey
        #standardize<fkey> :: fkey -> sfkey
        #detect whether std first
        #is_std__fkey
    sfkey2wsfkey = std_value2wrapped_std_value
        #wrap<sfkey> :: sfkey -> wsfkey

    is_std__wsfkey_set(wsfkey_set) == is_std_("wsfkey_sset", wsfkey_set)
    #xxx wsfkey_set2wsfkey_sset
    to_std__wsfkey_set
        #detect whether std first
        #is_std__wsfkey_set
        #required to mk .active_wsfkey_sset for immutable flag

    mk_weakable_frozenset__wrapped_std_KEY(local_register_point_name4sKEY, wsKEYs)
        #verify wrapped&std
        #local_register_point_name<sKEY> -> Iter<wsKEY> -> frozenset<wsKEY>
    mk_weakable_frozendict__wrapped_std_KEY__std_VALUE(local_register_point_name4sKEY, local_register_point_name4sVALUE, wsKEY_sVALUE_pairs)
        #verify wrapped&std
        #local_register_point_name<sKEY> -> local_register_point_name<sVALUE> -> Iter<(wsKEY,sVALUE)> -> FrozenDict<wsKEY,sVALUE>

    wsfkey2key
        #for __repr__ show active_keys from active_wsfkey_set
    key2wsfkey = sfkey2wsfkey . fkey2sfkey . key2fkey


    is_std__wsfkey_set(wsfkey_set)
    to_std__wsfkey_set(wsfkey_set) -> wsfkey_sset
        #wsfkey_set2wsfkey_sset

    is_std__wsfkey2wsfkey_wsset(wsfkey2wsfkey_wsset)
    to_std__wsfkey2wsfkey_wsset(wsfkey2wsfkey_wsset) -> wsfkey_s2wsfkey_wsset

API_ops4partition:
ops4partition:
    .ops4key_standardize
    ===
    get_ops4key_standardize
    #possible_keys
    type_check__is_key_a_possible_key(key)
    to_std__partition(partition) -> std_partition
    is_std__partition(partition)

    ##group_descriptor
    # example:
    #   'prefix_end_by_colon:' :: str
    #   {k1,k2,... } :: wsfkey_sset
    #
    # although one key may belong to many group_descriptors
    #       (hence a partition be used to ensure mutex)
    #       , we can test whether mutex between group_descriptors without partition
    #
    are_wsfgroup_descriptors_pairwise_mutex(wsfgroup_descriptors)
    is_wsfgroup_descriptor_of_key_size_0(wsfgroup_descriptor)
    is_wsfgroup_descriptor_of_key_size_1(wsfgroup_descriptor)


API_partition:
partition:
    #immutable, hashable, std
    .tmay_wsfgroup_descriptor4discrete_mutex_groups #all-in-one#compress
    .ops4partition.ops4key_standardize
    ===
    get_ops4partition
    #xxx   get_ops4key_standardize
        #   since if use type(partition) as ops4partition
        #   then whether instance-method or classmethod get_ops4key_standardize should be???
    get_tmay_wsfgroup_descriptor4discrete_mutex_groups
    #xxx   _get_wsfkey_s2wsfgroup_descriptor
        # since legal_keys may be infinite
        #       # legal_keys === wsfkey_s2wsfgroup_descriptor.keys()
        #
    verify_active_wsfkey_set(wsfkey_set) -> bool
    #legal_keys
    wsfkey in partition
    partition[wsfkey] #->wsfgroup_descriptor

    #no active_keys, which stored in flag
    #xxx   mk_flag(active_keys)







def get_ops4key_standardize_of_flag(flag, /):
    ops4partition = get_ops4partition_of_flag(flag)
    ops4key_standardize = ops4partition.get_ops4key_standardize()
    return ops4key_standardize
def get_ops4partition_of_flag(flag, /):
    cls = type(flag)
    if cls.___ops4partition_of_obj_is_at_cls___ is False:
        return object.__getattribute__(flag, '_ops4partition')
    elif cls.___ops4partition_of_obj_is_at_cls___ is True:
        return cls.___the_ops4partition_of_obj_at_cls___
    raise NotImplementedError



def get_std_partition_of_flag(flag, /):
    cls = type(flag)
    if cls.___std_partition_of_obj_is_at_cls___ is False:
        return object.__getattribute__(flag, '_std_partition')
    elif cls.___std_partition_of_obj_is_at_cls___ is True:
        return cls.___the_std_partition_of_obj_at_cls___
    raise NotImplementedError


def get_view_of_active_wsfkey_set_of_flag(flag, /):
    'set view or immutable set'
    cls = type(flag)
    if cls.___flag_is_mutable___ is True:
        return SetView(_get_mutable_active_wsfkey_set_of_flag(flag))
    return get_active_wsfkey_sset_of_flag(flag)
def _get_mutable_active_wsfkey_set_of_flag(flag, /):
    '_mutable_active_wsfkey_set'
    cls = type(flag)
    if cls.___flag_is_mutable___ is True:
        if cls.___active_wsfkey_set_of_obj_is_at_cls___ is False:
            return object.__getattribute__(flag, '_mutable_active_wsfkey_set')
    raise NotImplementedError



def get_active_wsfkey_sset_of_flag(flag, /):
    'immutable: _active_wsfkey_sset'
    cls = type(flag)
    if cls.___flag_is_mutable___ is False:
        if cls.___active_wsfkey_set_of_obj_is_at_cls___ is False:
            return object.__getattribute__(flag, '_active_wsfkey_sset')
        elif cls.___active_wsfkey_set_of_obj_is_at_cls___ is True:
            return cls.___the_active_wsfkey_sset_of_obj_at_cls___
    raise NotImplementedError



def get_view_of_non_discrete_wsfgroup_descriptor2active_wsfkey_of_flag(flag, /):
    return MapView(_get_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey_of_flag(flag))
def _get_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey_of_flag(flag, /):
    cls = type(flag)
    if cls.___flag_is_mutable___ is True:
        return object.__getattribute__(flag, '_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey')
    raise NotImplementedError
def get_instance_state_of_flag(flag, /):
    'flag -> (tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_set_view, tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view)'
    cls = type(flag)
    if cls.___ops4partition_of_obj_is_at_cls___ is False:
        ops4partition = get_ops4partition_of_flag(flag)
        tmay_ops4partition = (ops4partition,)
    else:
        tmay_ops4partition = ()

    if cls.___std_partition_of_obj_is_at_cls___ is False:
        std_partition = get_std_partition_of_flag(flag)
        tmay_std_partition = (std_partition,)
    else:
        tmay_std_partition = ()

    if cls.___active_wsfkey_set_of_obj_is_at_cls___ is False:
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(flag)
        tmay_active_wsfkey_set_view = (active_wsfkey_set_view,)
    else:
        tmay_active_wsfkey_set_view = ()

    if cls.___flag_is_mutable___ is True:
        non_discrete_wsfgroup_descriptor2active_wsfkey_view = get_view_of_non_discrete_wsfgroup_descriptor2active_wsfkey_of_flag(flag)
        tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view = (non_discrete_wsfgroup_descriptor2active_wsfkey_view,)
    else:
        tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view = ()

    return (tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_set_view, tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view)


def key2wsfkey_of_flag__with_legal_key_check(flag, key, /):
    'raise TypeError/ValueError/KeyError'
    wsfkey = key2wsfkey_of_flag(flag, key)
        #raise TypeError/ValueError
    std_partition = get_std_partition_of_flag(flag)
    if wsfkey not in std_partition: raise KeyError
    return wsfkey
def key2wsfkey_of_flag(flag, key, /):
    'raise TypeError/ValueError'
    ops4partition = get_ops4partition_of_flag(flag)
    ops4partition.type_check__is_key_a_possible_key(key)
        #raise TypeError/ValueError
    ops4key_standardize = get_ops4key_standardize_of_flag(flag)
    wsfkey = ops4key_standardize.key2wsfkey(key)
    return wsfkey



def keys2wsfkey_set_view(flag, ot_or_keys, /):
    if 0:
        ot = ot_or_keys
        del ot_or_keys
        if not isinstance(ot, BaseFlag): raise TypeError
        #if get_std_partition_of_flag(ot) is not get_std_partition_of_flag(flag): raise ValueError
        #if get_ops4partition_of_flag(ot) != get_ops4partition_of_flag(flag): raise ValueError
        if get_ops4key_standardize_of_flag(ot) != get_ops4key_standardize_of_flag(flag): raise ValueError

        ot_active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(ot)
        del ot

    try:
        ot = ot_or_keys
        b = isinstance(ot, BaseFlag) and get_ops4key_standardize_of_flag(ot) == get_ops4key_standardize_of_flag(flag)
    except Exception:
        b = False
    if b:
        ot_active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(ot)
        del ot
    else:
        del ot
        ot_keys = iter(ot_or_keys)
        del ot_or_keys
        ops4key_standardize = get_ops4key_standardize_of_flag(flag)
        ot_active_wsfkey_set_view = frozenset(key2wsfkey_of_flag(flag, key) for key in ot_keys)
        del ot_keys
    return ot_active_wsfkey_set_view
def decompose_active_wsfkey_set_into_configuration_of_flag(flag, /):
    std_partition = get_std_partition_of_flag(flag)
    active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(flag)
    return decompose_active_wsfkey_set_into_configuration_of_partition(std_partition, active_wsfkey_set_view)
    (tmay_ok, active_wsfkey_set4discrete_mutex_groups, non_discrete_wsfgroup_descriptor2active_wsfkey) = decompose_active_wsfkey_set_into_configuration_of_partition(std_partition, active_wsfkey_set_view)
        #tmay_ok is tmay_wsfgroup_descriptor4discrete_mutex_groups
def decompose_active_wsfkey_set_into_configuration_of_partition(std_partition, active_wsfkey_set_view, /):
    active_wsfkey_set4discrete_mutex_groups = set()
    non_discrete_wsfgroup_descriptor2active_wsfkey = {}
    tmay_ok = std_partition.get_tmay_wsfgroup_descriptor4discrete_mutex_groups()
        #[the_duplicates_ok_wsfgroup]
        #[the_duplicates_ok_group]
    for active_wsfkey in active_wsfkey_set_view:
        wsfgroup_descriptor = std_partition[active_wsfkey]
        if wsfgroup_descriptor in tmay_ok:
            active_wsfkey_set4discrete_mutex_groups.add(active_wsfkey)
        else:
            non_discrete_wsfgroup_descriptor2active_wsfkey[wsfgroup_descriptor] = active_wsfkey
    #new func here: return (tmay_ok, active_wsfkey_set4discrete_mutex_groups, non_discrete_wsfgroup_descriptor2active_wsfkey)
    return (tmay_ok, active_wsfkey_set4discrete_mutex_groups, non_discrete_wsfgroup_descriptor2active_wsfkey)
        #tmay_ok is tmay_wsfgroup_descriptor4discrete_mutex_groups


class KeyError_AttributeError(KeyError, AttributeError):pass


class BaseFlag:
    #__slots__ = ('_ops4partition', '_std_partition', '_active_wsfkey_sset', '_mutable_active_wsfkey_set', '_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey',)
    __slots__ = ()
    __doc__ = r'''
    .ops4partition
        #immutable
        of_obj_at_cls
        of_obj_at_obj
    .std_partition#partition==>>legal_keys
        #immutable
        of_obj_at_cls
        of_obj_at_obj
    .active_wsfkey_set#active_keys
        mutable
            .non_discrete_wsfgroup_descriptor2active_wsfkey
                #mutable ==>> _2_ not _s2_
                #   hence wsfkey not sfkey
        immutable
            #.active_wsfkey_sset === .active_wsfkey_set
            of_obj_at_cls
            of_obj_at_obj

    __getattribute__
    __getitem__
    __contains__
    __bool__
    __len__
    __iter__
    __repr__
    __eq__
    __lshift__
    __sub__
    #'''
    ___ops4partition_of_obj_is_at_cls___ = NotImplemented
    ___std_partition_of_obj_is_at_cls___ = NotImplemented
        # [___std_partition_of_obj_is_at_cls___] ==>> [___ops4partition_of_obj_is_at_cls___]
    ___active_wsfkey_set_of_obj_is_at_cls___ = NotImplemented
        # [___active_wsfkey_set_of_obj_is_at_cls___] ==>> [___std_partition_of_obj_is_at_cls___]
    ___flag_is_mutable___ = NotImplemented
        # [___flag_is_mutable___] ==>> [not ___active_wsfkey_set_of_obj_is_at_cls___]

    ___repr_head___ = NotImplemented
        #since BaseFlag only accept std-xxx, literal-value is not ok, ...


    def __getattribute__(sf, attr, /):
        #KeyError not AttributeError
        try:
            return sf[attr]
        except KeyError as e:
            raise KeyError_AttributeError(e)
    def __getitem__(sf, key, /):
        'is legal_key in active_keys'
        #if key not in sf: raise KeyError
        wsfkey = key2wsfkey_of_flag__with_legal_key_check(sf, key)
            #raise TypeError/ValueError/KeyError
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        return key in active_wsfkey_set_view
    def __contains__(sf, key, /):
        'is key in legal_keys'
        wsfkey = key2wsfkey_of_flag(sf, key)
            #raise TypeError/ValueError
        std_partition = get_std_partition_of_flag(sf)
        return wsfkey in std_partition
    def __bool__(sf, /):
        'active_keys'
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        return bool(active_wsfkey_set_view)
    def __len__(sf, /):
        'active_keys'
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        return len(active_wsfkey_set_view)
    def __iter__(sf, /):
        'active_keys'
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        ops4key_standardize = get_ops4key_standardize_of_flag(sf)
        iter_active_keys = map(ops4key_standardize.wsfkey2key, active_wsfkey_set_view)
        return iter_active_keys

    def __repr__(sf, /):
        (tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_set_view, tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view) = get_instance_state_of_flag(sf)
        del tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view

        if tmay_active_wsfkey_set_view:
            [active_wsfkey_set_view] = tmay_active_wsfkey_set_view
            ops4partition = get_ops4partition_of_flag(sf)
            ops4key_standardize = get_ops4key_standardize_of_flag(sf)
            active_keys = set(map(ops4key_standardize.wsfkey2key, active_wsfkey_set_view))
            if not active_keys:
                active_keys = []
            tmay_active_keys = (active_keys,)
        else:
            tmay_active_keys = ()
        del tmay_active_wsfkey_set_view

        args = sum(tmay_ops4partition, tmay_std_partition, tmay_active_keys)

        repr_head = type(sf).___repr_head___
        if repr_head is NotImplemented: raise NotImplementedError
        if type(repr_head) is not str: raise TypeError
        return repr_helper(repr_head, *args)

    def __eq__(sf, ot, /):
        if (ot) is (sf):
            return True
        #if type(ot) is not type(sf): return NotImplemented
        if not isinstance(ot, BaseFlag):
            return NotImplemented

        if get_std_partition_of_flag(ot) is not get_std_partition_of_flag(sf):
            return False
        if get_ops4partition_of_flag(ot) != get_ops4partition_of_flag(sf):
            return False
        ##[sf or ot mutable][sf is not ot] ==>> [1 active_wsfkey_set is mutable private][the 2 active_wsfkey_set are diff obj]
        ##[both immutable][active_wsfkey_set is std]
        sf_ks = active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        ot_ks = active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(ot)
        return ot_ks is sf_ks or (len(ot_ks) == len(sf_ks) and ot_ks == sf_ks)

    def __sub__(sf, ot_or_keys, /):
        std_partition = get_std_partition_of_flag(sf)
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        active_wsfkey_set = set(active_wsfkey_set_view)
        del active_wsfkey_set_view

        ot_active_wsfkey_set_view = keys2wsfkey_set_view(sf, ot_or_keys)
        for active_wsfkey in ot_active_wsfkey_set_view:
            #NOTE sf::std_partition[ot::wsfkey]
            wsfgroup_descriptor = std_partition[active_wsfkey]
                #check ot::key in sf::legal_keys
                #raise KeyError

        active_wsfkey_set -= ot_active_wsfkey_set_view
        return mk_flag_by_replace_active_wsfkey_set(sf, active_wsfkey_set)
d
    def __lshift__(sf, ot_or_keys, /):
        #new:def __lshift__(sf, keys, /):
        ''
        ot_active_wsfkey_set_view = keys2wsfkey_set_view(sf, ot_or_keys)

        std_partition = get_std_partition_of_flag(sf)
        if not std_partition.verify_active_wsfkey_set(ot_active_wsfkey_set_view): raise ValueError


        (tmay_ok, active_wsfkey_set4discrete_mutex_groups, non_discrete_wsfgroup_descriptor2active_wsfkey) = decompose_active_wsfkey_set_into_configuration_of_flag(sf)
            #tmay_ok is tmay_wsfgroup_descriptor4discrete_mutex_groups

        for active_wsfkey in ot_active_wsfkey_set_view:
            #NOTE sf::std_partition[ot::wsfkey]
            wsfgroup_descriptor = std_partition[active_wsfkey]
                #no KeyError
                #   since verify_active_wsfkey_set() prevent illegal_keys

            if wsfgroup_descriptor in tmay_ok:
                active_wsfkey_set4discrete_mutex_groups.add(active_wsfkey)
            else:
                non_discrete_wsfgroup_descriptor2active_wsfkey[wsfgroup_descriptor] = active_wsfkey
                    #may overwrite once
                    #   since verify_active_wsfkey_set() prevent conflict

        active_wsfkey_set4discrete_mutex_groups
        non_discrete_wsfgroup_descriptor2active_wsfkey
        active_wsfkey_set = {*active_wsfkey_set4discrete_mutex_groups, *non_discrete_wsfgroup_descriptor2active_wsfkey.values()}
        return mk_flag_by_replace_active_wsfkey_set(sf, active_wsfkey_set)

    #_type_check_at_post_new__xxx
    @classmethod
    def _type_check_at_post_new__ops4partition(cls, flag_init_ing, ops4partition):
        cls = type(flag_init_ing)
        pass
        return
    @classmethod
    def _type_check_at_post_new__std_partition(cls, flag_init_ing, std_partition):
        cls = type(flag_init_ing)
        ops4partition = get_ops4partition_of_flag(flag_init_ing)
        if not ops4partition.is_std__partition(std_partition): raise TypeError
        return

    @classmethod
    def _type_check_at_post_new__active_wsfkey_sset(cls, flag_init_ing, active_wsfkey_sset):
        cls = type(flag_init_ing)
        if not cls.___flag_is_mutable___ is False: raise logic-err
        ops4key_standardize = get_ops4key_standardize_of_flag(flag_init_ing)
        if not ops4key_standardize.is_std__wsfkey_set(active_wsfkey_sset): raise logic-err
    @classmethod
    def _type_check_at_post_new___mutable_active_wsfkey_set(cls, flag_init_ing, _mutable_active_wsfkey_set):
        cls = type(flag_init_ing)
        if not cls.___flag_is_mutable___ is True: raise logic-err
        if not type(_mutable_active_wsfkey_set) is set: raise TypeError
        if not all(type(wsfkey) is StdValue2FastKeyWrapper for wsfkey in _mutable_active_wsfkey_set): raise TypeError
        ops4key_standardize = get_ops4key_standardize_of_flag(flag_init_ing)
        if not all(ops4key_standardize.is_std__fkey(wsfkey()) for wsfkey in _mutable_active_wsfkey_set): raise TypeError
        return


def mk_flag_by_replace_active_wsfkey_set(flag, active_wsfkey_set, /):
    cls = type(flag)
    if cls.___flag_is_mutable___ is False and get_active_wsfkey_sset_of_flag(flag) == active_wsfkey_set:
        return flag

    if not cls.___active_wsfkey_set_of_obj_is_at_cls___ is True:
        #cls is not ok, obj hold no state
        ops4partition = get_ops4partition_of_flag(flag)
        std_partition = get_std_partition_of_flag(flag)
        return mk_ImmutableFlag3(ops4partition, std_partition, active_wsfkey_set)

    (tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_set_view, tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view) = get_instance_state_of_flag(flag)
    del tmay_non_discrete_wsfgroup_descriptor2active_wsfkey_view
    if not tmay_active_wsfkey_set_view:
        raise logic-error
    del tmay_active_wsfkey_set_view
    if 0:
        ops4key_standardize = get_ops4key_standardize_of_flag(flag)
        active_wsfkey_sset = ops4key_standardize.to_std__wsfkey_set(active_wsfkey_set)
        #args = sum(tmay_ops4partition, tmay_std_partition, (active_wsfkey_sset,))

        return mk_flag__cls(cls, tmay_ops4partition, tmay_std_partition, (active_wsfkey_sset,))
    return mk_flag__cls(cls, tmay_ops4partition, tmay_std_partition, (active_wsfkey_set,))
def mk_ImmutableFlag3(ops4partition, std_partition, active_wsfkey_set, /):
    #return mk_flag__cls(ImmutableFlag3, (ops4partition,), (std_partition,), (active_wsfkey_set,))
    ops4key_standardize = ops4partition.get_ops4key_standardize()
    active_wsfkey_sset = ops4key_standardize.to_std__wsfkey_set(active_wsfkey_set)
    del active_wsfkey_set
    return ImmutableFlag3(ops4partition, std_partition, active_wsfkey_sset)
def mk_flag__cls(cls, tmay_ops4partition, tmay_partition, tmay_active_wsfkey_set, /):
    if not (not tmay_ops4partition) is cls.___ops4partition_of_obj_is_at_cls___: raise TypeError
    if not (not tmay_partition) is cls.___std_partition_of_obj_is_at_cls___: raise TypeError
    if not (not tmay_active_wsfkey_set) is cls.___active_wsfkey_set_of_obj_is_at_cls___: raise TypeError
    #
    #std:
    if tmay_ops4partition:
        [ops4partition] = tmay_ops4partition
    else:
        ops4partition = cls.___the_ops4partition_of_obj_at_cls___
    ops4partition
    tmay_ops4partition

    if tmay_partition:
        [partition] = tmay_partition
        std_partition = ops4partition.to_std__partition(partition)
        del partition
        tmay_std_partition = (std_partition,)
    else:
        tmay_std_partition = ()
        std_partition = cls.___the_std_partition_of_obj_at_cls___
    del tmay_partition
    std_partition
    tmay_std_partition
    if not ops4partition.is_std__partition(std_partition): raise logic-err


    if cls.___flag_is_mutable___ is False:
        ops4key_standardize = ops4partition.get_ops4key_standardize()
        if tmay_active_wsfkey_set:
            [active_wsfkey_set] = tmay_active_wsfkey_set
            if ops4key_standardize.is_std__wsfkey_set(active_wsfkey_set):
                active_wsfkey_sset = active_wsfkey_set
            else:
                active_wsfkey_sset = ops4key_standardize.to_std__wsfkey_set(active_wsfkey_set)
            del active_wsfkey_set
            tmay_active_wsfkey_sset = (active_wsfkey_sset,)
        else:
            tmay_active_wsfkey_sset = ()
            active_wsfkey_sset = cls.___the_active_wsfkey_sset_of_obj_at_cls___
        del tmay_active_wsfkey_set
        active_wsfkey_sset
        tmay_active_wsfkey_sset
        if not ops4key_standardize.is_std__wsfkey_set(active_wsfkey_sset): raise logic-err

        args = sum(tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_sset)
    elif cls.___flag_is_mutable___ is True:
        args = sum(tmay_ops4partition, tmay_std_partition, tmay_active_wsfkey_set)
    elif cls.___flag_is_mutable___ is NotImplemented: raise NotImplementedError
    else:
        raise TypeError
    return cls(*args)



def _post_new_(property_exist_attrs, property_attrs, cls, sf, /,*args):
    ls = [getattr(cls, attr) for attr in property_exist_attrs]
    if any(at_cls is NotImplemented for at_cls in ls): raise NotImplementedError
    if not all(type(at_cls) is bool for at_cls in ls): raise TypeError

    if not len(args) == sum(not(at_cls) for at_cls in ls): raise TypeError
    [*xs] = reversed(args)
    for at_cls, attr in zip(ls, property_attrs):
        if not at_cls:
            object.__setattr__(sf, attr, xs.pop())
    assert not xs

    ##
    #... ...type check???
    for at_cls, attr in zip(ls, property_attrs):
        if not at_cls:
            x = object.__getattribute__(sf, attr)
            func_name = f'_type_check_at_post_new__{attr!s}'
            if 1:
                _type_check_at_post_new__xxx = getattr(cls, func_name)
            else:
                _type_check_at_post_new__xxx = globals()[func_name]
            _type_check_at_post_new__xxx(sf, x)
    ##
    ops4partition = get_ops4partition_of_flag(flag)
    std_partition = get_std_partition_of_flag(sf)
    if not ops4partition == std_partition.get_ops4partition(): raise TypeError
    if not (cls.___std_partition_of_obj_is_at_cls___ is False or cls.___ops4partition_of_obj_is_at_cls___ is True): raise TypeError
    if not (cls.___active_wsfkey_set_of_obj_is_at_cls___ is False or cls.___std_partition_of_obj_is_at_cls___ is True): raise TypeError
    if not (cls.___flag_is_mutable___ is False or cls.___active_wsfkey_set_of_obj_is_at_cls___ is False): raise TypeError
    ##
    active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
    if not std_partition.verify_active_wsfkey_set(active_wsfkey_set_view): raise ValueError


class ImmutableFlag(BaseFlag):
    r'''
    __hash__
    __new__
    ___flag_is_mutable___
    #'''

    ___flag_is_mutable___ = False
    def __hash__(sf, /):
        ops4partition = get_ops4partition_of_flag(sf)
        std_partition = get_std_partition_of_flag(sf)
        active_wsfkey_sset = get_active_wsfkey_sset_of_flag(sf)
        return hash((id(BaseFlag), ops4partition, id(std_partition), id(active_wsfkey_sset)))




    __property_exist_attrs = '''
        ___ops4partition_of_obj_is_at_cls___
        ___std_partition_of_obj_is_at_cls___
        ___active_wsfkey_set_of_obj_is_at_cls___
        '''.split()
    __property_attrs = '''
        _ops4partition
        _std_partition
        _active_wsfkey_sset
        '''.split()
    __property_exist_attrs = tuple(__property_exist_attrs)
    __property_attrs = tuple(__property_attrs)
    def __new__(cls, /,*args):
        property_exist_attrs = cls.__property_exist_attrs
        property_attrs = cls.__property_attrs
        sf = super(cls, __class__).__new__(cls)
        _post_new_(property_exist_attrs, property_attrs, cls, sf, *args)
        return sf

class MutableFlag(BaseFlag):
    r'''
    __init__
    __ilshift__
    __isub__
    __delitem__
    __setitem__
    __delattr__
    __setattr__
    ___flag_is_mutable___
    #'''


    ___flag_is_mutable___ = True
    def __setattr__(sf, attr, v, /):
        #KeyError not AttributeError
        try:
            sf[attr] = v
        except KeyError as e:
            raise KeyError_AttributeError(e)
        return
    def __delattr__(sf, attr, /):
        #KeyError not AttributeError
        try:
            del sf[attr]
        except KeyError as e:
            raise KeyError_AttributeError(e)
        return
    def __delitem__(sf, key, /):
        _mutable_active_wsfkey_set = _get_mutable_active_wsfkey_set_of_flag(sf)
        if key is ALL_KEYS:
            _mutable_active_wsfkey_set.clear()
        #elif key not in sf: raise KeyError
        else:
            sf[key] = False
    def __setitem__(sf, key, v, /):
        if sf[key] is v:
            return
        #legal_keys
        elif type(v) is not bool: raise TypeError
        else:
            _mutable_active_wsfkey_set = _get_mutable_active_wsfkey_set_of_flag(sf)
            #legal_keys
            wsfkey = key2wsfkey_of_flag__with_legal_key_check(sf, key)
            del key

            if not v is (wsfkey not in _mutable_active_wsfkey_set): raise logic-err
            #_mutable_active_wsfkey_set ^= {wsfkey}
            if v is False:
                _mutable_active_wsfkey_set.remove(wsfkey)
            elif v is True:
                _mutable_active_wsfkey_set.add(wsfkey)
            else: raise logic-err

            std_partition = get_std_partition_of_flag(sf)
            wsfgroup_descriptor = std_partition[wsfkey]
            is_key_in_discrete_mutex_group = wsfgroup_descriptor in std_partition.get_tmay_wsfgroup_descriptor4discrete_mutex_groups() #tmay_ok
            if is_key_in_discrete_mutex_group:
                #discrete_mutex_group
                pass
            else:
                _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey = _get_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey_of_flag(sf)
                if v is False:
                    if _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey[wsfgroup_descriptor] is not wsfkey: raise logic-err
                    del _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey[wsfgroup_descriptor]
                elif v is True:
                    if wsfgroup_descriptor in _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey: raise logic-err
                    _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey[wsfgroup_descriptor] = wsfkey
                else: raise logic-err

        return

    def __isub__(sf, ot_or_keys, /):
        'allow duplicate delete on same key or same mutex_group'
        ot_active_wsfkey_set_view = keys2wsfkey_set_view(sf, ot_or_keys)
        for ot_active_wsfkey in ot_active_wsfkey_set_view:
            del sf[ot_active_wsfkey]
                #raise KeyError
        return sf
d
    def __ilshift__(sf, ot_or_keys, /):
        'not allow duplicate set-flag/turn-on-key on same key or same mutex_group'
        ot_active_wsfkey_set_view = keys2wsfkey_set_view(sf, ot_or_keys)

        std_partition = get_std_partition_of_flag(sf)
        if not std_partition.verify_active_wsfkey_set(ot_active_wsfkey_set_view): raise ValueError
            #avoid duplicate on mutex_group
        for ot_active_wsfkey in ot_active_wsfkey_set_view:
            sf[ot_active_wsfkey] = True
        return sf







    __property_exist_attrs = '''
        ___ops4partition_of_obj_is_at_cls___
        ___std_partition_of_obj_is_at_cls___
        ___active_wsfkey_set_of_obj_is_at_cls___
        '''.split()
        #___flag_is_mutable___
    __property_attrs = '''
        _ops4partition
        _std_partition
        _mutable_active_wsfkey_set
        '''.split()
        #_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey
    __property_exist_attrs = tuple(__property_exist_attrs)
    __property_attrs = tuple(__property_attrs)
    def __init__(sf, /,*args):
        cls = type(sf)
        assert cls.___flag_is_mutable___ is True
        if not args: raise TypeError
        active_wsfkey_set = args[-1]
        #mutable+private
        _mutable_active_wsfkey_set = set(active_wsfkey_set)
        del active_wsfkey_set
        args = (*args[:-1], _mutable_active_wsfkey_set)
        property_exist_attrs = cls.__property_exist_attrs
        property_attrs = cls.__property_attrs
        _post_new_(property_exist_attrs, property_attrs, cls, sf, *args)

        if 0:
            r'''
        cls._value_check_at_post_new___mutable_non_discrete_wsfgroup_descriptor2active_wsfkey(sf)
    def _value_check_at_post_new___mutable_non_discrete_wsfgroup_descriptor2active_wsfkey(sf, /):
        #map to exactly active_keys of non_discrete_mutex_groups
        #'''
        #mk inside __init__ instead of check, since mutable
        #mutable+private
        std_partition = get_std_partition_of_flag(sf)
        active_wsfkey_set_view = get_view_of_active_wsfkey_set_of_flag(sf)
        _d = mk_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey(std_partition, active_wsfkey_set_view)
        object.__setattr__(sf, '_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey', _d)

def mk_mutable_non_discrete_wsfgroup_descriptor2active_wsfkey(std_partition, active_wsfkey_set_view, /):
    (tmay_ok, active_wsfkey_set4discrete_mutex_groups, non_discrete_wsfgroup_descriptor2active_wsfkey) = decompose_active_wsfkey_set_into_configuration_of_partition(std_partition, active_wsfkey_set_view)
        #tmay_ok is tmay_wsfgroup_descriptor4discrete_mutex_groups
    _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey = non_discrete_wsfgroup_descriptor2active_wsfkey
    return _mutable_non_discrete_wsfgroup_descriptor2active_wsfkey

class Flag3(BaseFlag):
    '3 args'
    ___ops4partition_of_obj_is_at_cls___ = False
    ___std_partition_of_obj_is_at_cls___ = False
    ___active_wsfkey_set_of_obj_is_at_cls___ = False
class Flag2(BaseFlag):
    '2 args'
    ___ops4partition_of_obj_is_at_cls___ = True
    ___std_partition_of_obj_is_at_cls___ = False
    ___active_wsfkey_set_of_obj_is_at_cls___ = False
class Flag1(BaseFlag):
    '1 args'
    ___ops4partition_of_obj_is_at_cls___ = True
    ___std_partition_of_obj_is_at_cls___ = True
    ___active_wsfkey_set_of_obj_is_at_cls___ = False
class Flag0(BaseFlag):
    '0 args'
    ___ops4partition_of_obj_is_at_cls___ = True
    ___std_partition_of_obj_is_at_cls___ = True
    ___active_wsfkey_set_of_obj_is_at_cls___ = True


class ImmutableFlag3(Flag3, ImmutableFlag):pass
class ImmutableFlag2(Flag2, ImmutableFlag):pass
class ImmutableFlag1(Flag1, ImmutableFlag):pass
class ImmutableFlag0(Flag0, ImmutableFlag):pass


class MutableFlag3(Flag3, MutableFlag):pass
class MutableFlag2(Flag2, MutableFlag):pass
class MutableFlag1(Flag1, MutableFlag):pass
class MutableFlag0(Flag0, MutableFlag):pass



def _verify_is_active_wsfkey_set_mutex__tmay(discrete_mutex_groups__tmay_wsfgroup_descriptor, grouping__wsfkey2wsfgroup_descriptor, active_wsfkey_set, /,*, wsf_vs_sf__group_descriptor:bool):
    r'''
def _verify_is_active_wsfkey_set_mutex__tmay(discrete_mutex_groups__tmay_wsfgroup_descriptor, grouping__wsfkey2wsfgroup_descriptor, active_wsfkey_set, /,*, wsf_vs_sf__group_descriptor=False):
    using wsfgroup_descriptor
def _verify_is_active_wsfkey_set_mutex__tmay(discrete_mutex_groups__tmay_sfgroup_descriptor, grouping__wsfkey2sfgroup_descriptor, active_wsfkey_set, /,*, wsf_vs_sf__group_descriptor=True):
    using sfgroup_descriptor
    #
    #wsf_vs_sf__group_descriptor:
    #   wsfgroup_descriptor vs sfgroup_descriptor
    #   False vs True
    #   echo vs id
    #
    #'''
    f = id if wsf_vs_sf__group_descriptor else echo
        # f(group) -> name
        # test name by (==)
    tmay_ok = tmay_the_duplicates_ok_group = tmay_wsfgroup_descriptor4discrete_mutex_groups = discrete_mutex_groups__tmay_wsfgroup_descriptor
        #the_duplicates_ok_group
    tmay_the_duplicates_ok_groupname = (*map(f, tmay_the_duplicates_ok_group),)
    wsfkey2group = grouping__wsfkey2wsfgroup_descriptor
    del tmay_ok, tmay_the_duplicates_ok_group, tmay_wsfgroup_descriptor4discrete_mutex_groups, discrete_mutex_groups__tmay_wsfgroup_descriptor
    del grouping__wsfkey2wsfgroup_descriptor



    if not active_wsfkey_set <= wsfkey2group.keys():
        return False

    groupname_count_pairs = collections.Counter(f(wsfkey2group[wsfkey]) for wsfkey in active_wsfkey_set).most_common(2)
    return all(count <= 1 or groupname in tmay_the_duplicates_ok_groupname for groupname, count in group_count_pairs)






key_is_str
group_type_style:
    group_descriptor_is_enum_set
    group_descriptor_is_seq_prefix
group_storage_style:
    enum_group_descriptors at_obj
    static_group_descriptors at_ops
        finite vs infinite group_descriptors
            all_mutex_groups_are_discrete
            single_mutex_group
        infinite:
            #all_possible_keys_are_legal_keys
            #all_possible_group_descriptorss_are_legal
            all_possible_group_descriptorss_are_pairwise_mutex
                seq_prefix_nongreedy_end_by_fixed_pattern

ops4key_standardize
ops4partition
std_partition
def _mk_wsfgroup_descriptor__set_style(ops4key_standardize, keys, /):
    wsfgroup_descriptor = wsfkey_wsset = ops4key_standardize.std_value2wrapped_std_value(ops4key_standardize.to_std__wsfkey_set(set(map(ops4key_standardize.key2wsfkey, keys))))
    return wsfgroup_descriptor
class Partition_SEE:
    r'''
    SEE - key_is_str, group_descriptor_is_enum_set, enum_group_descriptors
    #'''
    _attrs_of_API_of_partition = (
        #only required access in form "sf.xxx"
        'get_ops4partition'
        ,'verify_active_wsfkey_set'
        ,'get_tmay_wsfgroup_descriptor4discrete_mutex_groups'
        )
        #exclude: # access in form "cls.xxx(sf, ...)"
        #__getitem__
        #__contains__
    def __getattribute__(sf, attr, /):
        cls = type(sf)
        if attr not in cls._attrs_of_API_of_partition: raise AttributeError(attr)
        return super(cls, __class__).__getattribute__(sf, attr)
    @classmethod
    def _get_wsfkey_s2wsfgroup_descriptor(cls, sf, /):
        r'''
        #not public API
        #private API only when legal_keys is finite
        #'''
        return object.__getattribute__(sf, 'wsfkey_s2wsfgroup_descriptor')
    #[[[API_partition
    def get_ops4partition(sf, /):
        return type(sf)
    def get_tmay_wsfgroup_descriptor4discrete_mutex_groups(sf, /):
        return object.__getattribute__(sf, 'tmay_wsfgroup_descriptor4discrete_mutex_groups')
    def verify_active_wsfkey_set(sf, active_wsfkey_set, /) -> bool:
        #see:_verify_is_active_wsfkey_set_mutex__tmay
        discrete_mutex_groups__tmay_wsfgroup_descriptor = sf.get_tmay_wsfgroup_descriptor4discrete_mutex_groups()
        cls = type(sf)
        grouping__wsfkey2wsfgroup_descriptor = cls._get_wsfkey_s2wsfgroup_descriptor(sf)
        return _verify_is_active_wsfkey_set_mutex__tmay(discrete_mutex_groups__tmay_wsfgroup_descriptor, grouping__wsfkey2wsfgroup_descriptor, active_wsfkey_set, wsf_vs_sf__group_descriptor=False)


    def __getitem__(sf, wsfkey, /):
        if not type(wsfkey) is StdValue2FastKeyWrapper: raise TypeError
        cls = type(sf)
        grouping__wsfkey2wsfgroup_descriptor = cls._get_wsfkey_s2wsfgroup_descriptor(sf)
        return grouping__wsfkey2wsfgroup_descriptor[wsfkey]
    def __contains__(sf, wsfkey, /):
        if not type(wsfkey) is StdValue2FastKeyWrapper: raise TypeError
        cls = type(sf)
        grouping__wsfkey2wsfgroup_descriptor = cls._get_wsfkey_s2wsfgroup_descriptor(sf)
        return wsfkey in grouping__wsfkey2wsfgroup_descriptor
    #]]]API_partition

    _ops4key_standardize = ???
    #[[[API_ops4partition
    @classmethod
    def get_ops4key_standardize(cls, /):
        return cls._ops4key_standardize
    ... ...TODO
        add more API_ops4partition
    #]]]API_ops4partition
    def __init__(sf, keys__discrete, keyss__non_discrete, /):
        keys__discrete = frozenset(keys__discrete)
        keyss__non_discrete = frozenset(map(frozenset, keyss__non_discrete))
        iter_keyss = itertools.chain([keys__discrete], keyss__non_discrete)
        if not all(type(key) is str for keys in iter_keyss for key in keys): raise TypeError
        #sf.get_tmay_wsfgroup_descriptor4discrete_mutex_groups()
        ops4partition = sf.get_ops4partition()
        ops4key_standardize = ops4partition.get_ops4key_standardize()
        wsfgroup_descriptor4discrete = wsfkey_wsset__discrete = _mk_wsfgroup_descriptor__set_style(ops4key_standardize, keys__discrete)
        if wsfgroup_descriptor4discrete:
            tmay_ok =(wsfgroup_descriptor4discrete,)
        else:
            tmay_ok =()

        wsfgroup_descriptors4non_discrete = [_mk_wsfgroup_descriptor__set_style(ops4key_standardize, keys) for keys in keyss__non_discrete if keys]
        wsfkey2wsfkey_wsset = wsfkey2wsfgroup_descriptor = {}
        iter_wsfkey_wssets = itertools.chain([wsfgroup_descriptor4discrete], wsfgroup_descriptors4non_discrete)
        for wsfkey_wsset in iter_wsfkey_wssets:
            wsfgroup_descriptor = wsfkey_wsset
            wsfkey_sset = wsfkey_wsset()
            for wsfkey in wsfkey_sset:
                wsfkey2wsfgroup_descriptor[wsfkey] = wsfgroup_descriptor#wsset
        if len(wsfkey2wsfgroup_descriptor) != len(wsfgroup_descriptor4discrete) + sum(map(len, wsfgroup_descriptors4non_discrete)): raise ValueError('groups of partition are not mutex')
        wsfkey_s2wsfgroup_descriptor = wsfkey_s2wsfkey_wsset = ops4key_standardize.to_std__wsfkey2wsfkey_wsset(wsfkey2wsfkey_wsset)



        sf.tmay_wsfgroup_descriptor4discrete_mutex_groups = tmay_ok
        sf.wsfkey_s2wsfgroup_descriptor = wsfkey_s2wsfgroup_descriptor
            # wsfkey _s2_ wsfkey_wsset/wsfgroup_descriptor
            # wsfkey_s2wsfkey_wsset
            # wsfkey_s2wsfgroup_descriptor
        return

class Partition4Flag__key_is_str__enum_group_descriptors:
class Partition4Flag__key_is_str__all_mutex_groups_are_discrete:
class Partition4Flag__key_is_str__single_mutex_group:

