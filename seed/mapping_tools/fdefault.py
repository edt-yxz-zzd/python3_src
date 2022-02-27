
#################################
#[[[__doc__-begin
r'''

seed.mapping_tools.fdefault
py -m seed.mapping_tools.fdefault
py -m nn_ns.app.debug_cmd   seed.mapping_tools.fdefault

from seed.mapping_tools.fdefault import mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay
from seed.mapping_tools.fdefault import mapping_reversable_update__tmay
from seed.mapping_tools.fdefault import mapping_contain_, mapping_set__overwrite_or_raise__pair_, mapping_set__new_or_raise__return_, mapping_set__new_or_overwrite__pair__uniform_, mapping_set__new_or_overwrite__pair__onthen_, mapping_set__new_or_pass__cased_, mapping_set__overwrite_or_pass__may_pair_

from seed.mapping_tools.fdefault import mapping_on_key, get_fdefault, set_fdefault, getitem_fdefault, setitem_fdefault, add_new_item




from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError, mk_default

from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human

======================
mapping ops:
    get:
        get__raise -> value|KeyError
            #expect existed
        get__tmay -> tmay value
            #Maybe value
            #testing and further process
        get__fdefault -> (is_old_value, default|value)
            #Either default value
            #channel and further process
    set:
        set__overwrite_or_raise -> (old_value, new_value)
            #donot want the mapping size grow
            #donot want use deprecated key
        set__new_or_raise -> new_value
            #when init a mapping, we want to avoid duplicate keys, hence avoid overwrite
        set__new_or_overwrite -> (tmay old_value, new_value)
            defaultdict(int/set/list)
            d[k] += ...
            d[k].add(x)
            d[k].append(x)
            ##err:set__new_or_overwrite -> tmay old_value
                #err:use new_value directly instead of fvalue
                d[k] = new_value
        set__new_or_pass -> (is_old_value, new_value|old_value)
            =set__fdefault
        set__overwrite_or_pass -> may (old_value, new_value)
        #total 5 main cases; see below 15 cases
            new&overwrite
            (new|overwrite)*(pass|raise)
        ... ...
        ... ...

        on_key_present:
            #5
            * raise #not allow_key_present
            * not_get_not_set #not allow_overwrite
            * get_not_set #not allow_overwrite
            * set_not_get #allow_overwrite
            * get_set #allow_overwrite
        on_key_absent:
            #3
            * raise #not allow_key_absent
            * not_set
            * set #allow_new
        ==>> total 5*3=15 cases
        * [on_key_present=raise][on_key_absent=raise]:
            #No:0
            meaningless
        * [on_key_present=raise][on_key_absent=new]:
            #No:1
            set__new_or_raise
        * [on_key_present=raise][on_key_absent=not_set]:
            #No:2
            meaningless
        * [on_key_present=not_get_not_set][on_key_absent=raise]:
            #No:3
            meaningless
        * [on_key_present=not_get_not_set][on_key_absent=new]:
            #No:4
            weak set__new_or_pass
        * [on_key_present=not_get_not_set][on_key_absent=not_set]:
            #No:5
            meaningless
        * [on_key_present=get_not_set][on_key_absent=raise]:
            #No:6
            get__raise
            meaningless for "set"
        * [on_key_present=get_not_set][on_key_absent=new]:
            #No:7
            set__new_or_pass
        * [on_key_present=get_not_set][on_key_absent=not_set]:
            #No:8
            get__tmay=weak get__fdefault
            meaningless for "set"
        * [on_key_present=set_not_get][on_key_absent=raise]:
            #No:9
            weak set__overwrite_or_raise
        * [on_key_present=set_not_get][on_key_absent=new]:
            #No:10
            weak set__new_or_overwrite
        * [on_key_present=set_not_get][on_key_absent=not_set]:
            #No:11
            weak set__overwrite_or_pass
        * [on_key_present=get_set][on_key_absent=raise]:
            #No:12
            set__overwrite_or_raise
        * [on_key_present=get_set][on_key_absent=new]:
            #No:13
            set__new_or_overwrite
        * [on_key_present=get_set][on_key_absent=not_set]:
            #No:14
            set__overwrite_or_pass


======================
======================


#[[[doctest_examples-begin
>>> d = {1:2}
>>> gk = 1 #good-key
>>> bk = 3 #bad-key
>>> _get = False; _pop = True
>>> _try = False; _Nothing = None; _in = True

>>> option2mapping_get__tmay(get_vs_pop=_get, try_vs_Nothing_vs_in=_try).__name__
'mapping_get__tmay__try_getitem'

>>> option2mapping_get__tmay(get_vs_pop=_pop, try_vs_Nothing_vs_in=_try).__name__
'mapping_get__tmay__try_pop'

>>> option2mapping_get__tmay(get_vs_pop=_get, try_vs_Nothing_vs_in=_Nothing).__name__
'mapping_get__tmay__get_Nothing'

>>> option2mapping_get__tmay(get_vs_pop=_pop, try_vs_Nothing_vs_in=_Nothing).__name__
'mapping_get__tmay__pop_Nothing'

>>> option2mapping_get__tmay(get_vs_pop=_get, try_vs_Nothing_vs_in=_in).__name__
'mapping_get__tmay__contains_getitem'

>>> option2mapping_get__tmay(get_vs_pop=_pop, try_vs_Nothing_vs_in=_in).__name__
'mapping_get__tmay__contains_pop'


def mapping_get__tmay_(mapping, key, /,*, get_vs_pop, try_vs_Nothing_vs_in):
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
()


def mapping_get_fdefault__cased_(mapping, key, imay_xdefault_rank, xdefault, /,*, get_vs_pop, try_vs_Nothing_vs_in):
>>> mapping_get_fdefault__cased_({1:2}, 1, 0, ..., get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(True, 2)
>>> mapping_get_fdefault__cased_({1:2}, 3, -1, 4, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(False, 4)
>>> mapping_get_fdefault__cased_({1:2}, 3, 0, lambda:4, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(False, 4)
>>> mapping_get_fdefault__cased_({1:2}, 3, 1, lambda x, /:(x, 4), get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(False, (3, 4))
>>> mapping_get_fdefault__cased_({1:2}, 3, 2, lambda y, x, /:(y, x, 4), get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(False, ({1: 2}, 3, 4))
>>> mapping_get_fdefault__cased_({1:2}, 3, 3, lambda z, y, x, /:(z, y, x, 4), get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
Traceback (most recent call last):
    ...
TypeError


def mapping_set_fdefault__cxxxvalue_(mapping, key, imay_xdefault_rank, xdefault, /,*, get_vs_pop, try_vs_Nothing_vs_in):
>>> from collections import OrderedDict
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 1, 0, ..., try_vs_Nothing_vs_in=_try)
(True, 2)
>>> d
OrderedDict([(1, 2)])
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 3, -1, 4, try_vs_Nothing_vs_in=_try)
(False, 4)
>>> d
OrderedDict([(1, 2), (3, 4)])
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 3, 0, lambda:4, try_vs_Nothing_vs_in=_try)
(False, 4)
>>> d
OrderedDict([(1, 2), (3, 4)])
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 3, 1, lambda x, /:(x, 4), try_vs_Nothing_vs_in=_try)
(False, (3, 4))
>>> d
OrderedDict([(1, 2), (3, (3, 4))])
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 3, 2, lambda y, x, /:(y, x, 4), try_vs_Nothing_vs_in=_try)
(False, (OrderedDict([(1, 2), (3, (...))]), 3, 4))
>>> d
OrderedDict([(1, 2), (3, (..., 3, 4))])
>>> d = OrderedDict({1:2})
>>> mapping_set_fdefault__cxxxvalue_(d, 3, 3, lambda z, y, x, /:(z, y, x, 4), try_vs_Nothing_vs_in=_try)
Traceback (most recent call last):
    ...
TypeError
>>> d
OrderedDict([(1, 2)])
>>> d = OrderedDict({1:2})


#################################
#################################
#################################
#################################
#################################
#################################
#################################
#################################
def mapping_get__tmay_(mapping, key, /,*, get_vs_pop, try_vs_Nothing_vs_in):
#x:0
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_get, try_vs_Nothing_vs_in=_try)
()

#x:1
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_pop, try_vs_Nothing_vs_in=_try)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_pop, try_vs_Nothing_vs_in=_try)
()

#x:2
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_get, try_vs_Nothing_vs_in=_Nothing)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_get, try_vs_Nothing_vs_in=_Nothing)
()

#x:3
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_pop, try_vs_Nothing_vs_in=_Nothing)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_pop, try_vs_Nothing_vs_in=_Nothing)
()

#x:4
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_get, try_vs_Nothing_vs_in=_in)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_get, try_vs_Nothing_vs_in=_in)
()

#x:5
>>> mapping_get__tmay_({1:2}, 1, get_vs_pop=_pop, try_vs_Nothing_vs_in=_in)
(2,)
>>> mapping_get__tmay_({1:2}, 3, get_vs_pop=_pop, try_vs_Nothing_vs_in=_in)
()





#################################
#################################
#################################
#################################
#later add-in:
#5 main-mapping-set cases(see above), 1-case has 2 API, hence 6
#6 +mapping_contain_ ==>> 7 funcs this patch


def mapping_contain_(mapping, key, /,*, try_vs_Nothing_vs_in):
>>> mapping_contain_({1:2}, 1, try_vs_Nothing_vs_in=_try)
True
>>> mapping_contain_({1:2}, 1, try_vs_Nothing_vs_in=_Nothing)
True
>>> mapping_contain_({1:2}, 1, try_vs_Nothing_vs_in=_in)
True

>>> mapping_contain_({1:2}, 3, try_vs_Nothing_vs_in=_try)
False
>>> mapping_contain_({1:2}, 3, try_vs_Nothing_vs_in=_Nothing)
False
>>> mapping_contain_({1:2}, 3, try_vs_Nothing_vs_in=_in)
False


>>> from collections import OrderedDict
>>> f = lambda mapping_set, mapping, key, /,*args, **kwargs: (mapping_set(mapping, key, *args, **kwargs), mapping)

def mapping_set__overwrite_or_raise__pair_(mapping, key, imay_xvalue_rank, xvalue, /):
>>> f(mapping_set__overwrite_or_raise__pair_, OrderedDict({1:2}), 1, -1, 3)
((2, 3), OrderedDict([(1, 3)]))
>>> f(mapping_set__overwrite_or_raise__pair_, OrderedDict({1:2}), 1, 1, lambda x:(x,3))
((2, (2, 3)), OrderedDict([(1, (2, 3))]))
>>> f(mapping_set__overwrite_or_raise__pair_, OrderedDict({1:2}), 4, -1, 3)
Traceback (most recent call last):
    ...
KeyError: 4

def mapping_set__new_or_raise__return_(mapping, key, imay_xvalue_rank, xvalue, /,*, try_vs_Nothing_vs_in):
>>> f(mapping_set__new_or_raise__return_, OrderedDict({1:2}), 4, -1, 3, try_vs_Nothing_vs_in=_try)
(3, OrderedDict([(1, 2), (4, 3)]))
>>> f(mapping_set__new_or_raise__return_, OrderedDict({1:2}), 4, 1, lambda x:(x,3), try_vs_Nothing_vs_in=_try)
((4, 3), OrderedDict([(1, 2), (4, (4, 3))]))
>>> f(mapping_set__new_or_raise__return_, OrderedDict({1:2}), 1, -1, 3, try_vs_Nothing_vs_in=_try)
Traceback (most recent call last):
    ...
KeyError: 1



def mapping_set__new_or_overwrite__pair__uniform_(mapping, key, imay_xvalue_rank, xvalue, /,*, get_vs_pop, try_vs_Nothing_vs_in):
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 4, -1, 3, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((), 3), OrderedDict([(1, 2), (4, 3)]))
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 4, 1, lambda x:(x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((), ((), 3)), OrderedDict([(1, 2), (4, ((), 3))]))
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 4, 2, lambda y,x:(y,x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((), (4, (), 3)), OrderedDict([(1, 2), (4, (4, (), 3))]))
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 1, -1, 3, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((2,), 3), OrderedDict([(1, 3)]))
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 1, 1, lambda x:(x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((2,), ((2,), 3)), OrderedDict([(1, ((2,), 3))]))
>>> f(mapping_set__new_or_overwrite__pair__uniform_, OrderedDict({1:2}), 1, 2, lambda y,x:(y,x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((2,), (1, (2,), 3)), OrderedDict([(1, (1, (2,), 3))]))


def mapping_set__new_or_overwrite__pair__onthen_(mapping, key, imay_on_new_rank, on_new, imay_on_overwrite_rank, on_overwrite, /,*, new_then_overwrite:bool, get_vs_pop, try_vs_Nothing_vs_in):
>>> f(mapping_set__new_or_overwrite__pair__onthen_, OrderedDict({1:2}), 4, 1, lambda x:(x,5), 2, lambda y,x:(y,x,6), new_then_overwrite=False, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((), (4, 5)), OrderedDict([(1, 2), (4, (4, 5))]))
>>> f(mapping_set__new_or_overwrite__pair__onthen_, OrderedDict({1:2}), 4, 1, lambda x:(x,5), 2, lambda y,x:(y,x,6), new_then_overwrite=True, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((), (4, (4, 5), 6)), OrderedDict([(1, 2), (4, (4, (4, 5), 6))]))

>>> f(mapping_set__new_or_overwrite__pair__onthen_, OrderedDict({1:2}), 1, 1, lambda x:(x,5), 2, lambda y,x:(y,x,6), new_then_overwrite=False, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((2,), (1, 2, 6)), OrderedDict([(1, (1, 2, 6))]))
>>> f(mapping_set__new_or_overwrite__pair__onthen_, OrderedDict({1:2}), 1, 1, lambda x:(x,5), 2, lambda y,x:(y,x,6), new_then_overwrite=True, try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(((2,), (1, 2, 6)), OrderedDict([(1, (1, 2, 6))]))


def mapping_set__new_or_pass__cased_(mapping, key, imay_xvalue_rank, xvalue, /,*, try_vs_Nothing_vs_in):
>>> f(mapping_set__new_or_pass__cased_, OrderedDict({1:2}), 4, 1, lambda x:(x,3), try_vs_Nothing_vs_in=_try)
((False, (4, 3)), OrderedDict([(1, 2), (4, (4, 3))]))
>>> f(mapping_set__new_or_pass__cased_, OrderedDict({1:2}), 1, 1, lambda x:(x,3), try_vs_Nothing_vs_in=_try)
((True, 2), OrderedDict([(1, 2)]))

def mapping_set__overwrite_or_pass__may_pair_(mapping, key, imay_xvalue_rank, xvalue, /,*, get_vs_pop, try_vs_Nothing_vs_in):
>>> f(mapping_set__overwrite_or_pass__may_pair_, OrderedDict({1:2}), 4, 2, lambda y,x:(y,x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
(None, OrderedDict([(1, 2)]))
>>> f(mapping_set__overwrite_or_pass__may_pair_, OrderedDict({1:2}), 1, 2, lambda y,x:(y,x,3), try_vs_Nothing_vs_in=_try, get_vs_pop=_get)
((2, (1, 2, 3)), OrderedDict([(1, (1, 2, 3))]))


#################################




#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################




__all__ = '''
    mapping_reversable_update__tmay

    mapping_get__tmay_
        mapping_get_fdefault__cased_
            mapping_set_fdefault__cxxxvalue_
        option2mapping_get__tmay
            mapping_get__tmay__try_getitem
            mapping_get__tmay__try_pop
            mapping_get__tmay__get_Nothing
            mapping_get__tmay__pop_Nothing
            mapping_get__tmay__contains_getitem
            mapping_get__tmay__contains_pop

    mapping_contain_

    mapping_set__overwrite_or_raise__pair_
    mapping_set__new_or_raise__return_
    mapping_set__new_or_overwrite__pair__uniform_
    mapping_set__new_or_overwrite__pair__onthen_
    mapping_set__new_or_pass__cased_
    mapping_set__overwrite_or_pass__may_pair_












    mapping_on_key

    get_fdefault
    set_fdefault
    getitem_fdefault
    setitem_fdefault
    add_new_item




    '''.split()
    #mapping_on_key_with_set_fdefault
    #getset_fdefault

from seed.tiny import echo
from seed.tiny_.mk_fdefault import mk_tmay_from_try_fvalue_KeyError, mk_tmay_from_default2value, mk_tmay_from_is_safe_fvalue, mk_default
from seed.mapping_tools.mapping_reversable_update__tmay import mapping_reversable_update__tmay


mapping_reversable_update__tmay = mapping_reversable_update__tmay

def mapping_get__tmay__try_getitem(mapping, key):
    return mk_tmay_from_try_fvalue_KeyError(lambda:mapping[key])
def mapping_get__tmay__try_pop(mapping, key):
    return mk_tmay_from_try_fvalue_KeyError(lambda:mapping.pop(key))

def mapping_get__tmay__get_Nothing(mapping, key):
    return mk_tmay_from_default2value(lambda default:mapping.get(key, default))
def mapping_get__tmay__pop_Nothing(mapping, key):
    return mk_tmay_from_default2value(lambda default:mapping.pop(key, default))

def mapping_get__tmay__contains_getitem(mapping, key):
    return mk_tmay_from_is_safe_fvalue(key in mapping, lambda:mapping[key])
def mapping_get__tmay__contains_pop(mapping, key):
    return mk_tmay_from_is_safe_fvalue(key in mapping, lambda:mapping.pop(key))

_mapping_get__tmay__ls = (
    mapping_get__tmay__try_getitem
    ,mapping_get__tmay__try_pop
    ,mapping_get__tmay__get_Nothing
    ,mapping_get__tmay__pop_Nothing
    ,mapping_get__tmay__contains_getitem
    ,mapping_get__tmay__contains_pop
    )
def mapping_get__tmay_(mapping, key, /,*, get_vs_pop:'get-False|pop-True', try_vs_Nothing_vs_in:'try-False|Nothing-None|in-True'):
    r'''
    -> tmay_old_value

    .get(k, Nothing)
    try  .__getitem__(k)
    .__contains__(k) .__getitem__(k)
    .pop(k, Nothing)
    try .pop(k)
    .__contains__(k) .pop(k)
    ???no setdefault
    ==>> (try|in|Nothing)*(get|pop)

    #'''
    mapping_get__tmay = option2mapping_get__tmay(get_vs_pop=get_vs_pop, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    return mapping_get__tmay(mapping, key)
def option2mapping_get__tmay(*, get_vs_pop:'get-False|pop-True', try_vs_Nothing_vs_in:'try-False|Nothing-None|in-True'):
    if not type(get_vs_pop) is bool: raise TypeError
    if not (try_vs_Nothing_vs_in is None or type(try_vs_Nothing_vs_in) is bool): raise TypeError
    LSB = int(get_vs_pop)
    MSB = 1 if try_vs_Nothing_vs_in is None else 2*int(try_vs_Nothing_vs_in)
    i = MSB*2+LSB
    return _mapping_get__tmay__ls[i]

assert mapping_get__tmay__try_getitem is option2mapping_get__tmay(try_vs_Nothing_vs_in=False, get_vs_pop=False)
assert mapping_get__tmay__try_pop is option2mapping_get__tmay(try_vs_Nothing_vs_in=False, get_vs_pop=True)

assert mapping_get__tmay__get_Nothing is option2mapping_get__tmay(try_vs_Nothing_vs_in=None, get_vs_pop=False)
assert mapping_get__tmay__pop_Nothing is option2mapping_get__tmay(try_vs_Nothing_vs_in=None, get_vs_pop=True)

assert mapping_get__tmay__contains_getitem is option2mapping_get__tmay(try_vs_Nothing_vs_in=True, get_vs_pop=False)
assert mapping_get__tmay__contains_pop is option2mapping_get__tmay(try_vs_Nothing_vs_in=True, get_vs_pop=True)


#def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):

def mapping_get_fdefault__cased_(mapping, key, imay_xdefault_rank, xdefault, /,*, get_vs_pop:'get-False|pop-True', try_vs_Nothing_vs_in:'try-False|Nothing-None|in-True'):
    r'''
    -> cased_xvalue@(is_old_value, default|old_value)
    imay_xdefault_rank :: [-1..2]
    xdefault = default | fdefault | key2default | mapping_key2default
        imay_xdefault_rank - xdefault
        -1 - default
        0 - fdefault
        1 - key2default
        2 - mapping_key2default

    #get_vs_pop, try_vs_Nothing_vs_in
    #   see: mapping_get__tmay_
    get_vs_pop :: bool
        False - get/__getitem__
        True - pop
    try_vs_Nothing_vs_in:
        False - try __getitem__/pop KeyError
        None - setup (default=Nothing) for get/pop
        True - if key in mapping then __getitem__/pop
    ====
    default :: default
    fdefault :: (() -> default)
    key2default :: (key -> default)
    mapping_key2default :: (mapping -> key -> default)
    #'''
    tmay = mapping_get__tmay_(mapping, key, get_vs_pop=get_vs_pop, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    if not tmay:
        default = mk_default(imay_xdefault_rank, xdefault, mapping, key)
        is_old_value = False
        xvalue = default
    else:
        [old_value] = tmay
        is_old_value = True
        xvalue = old_value
    cased_xvalue = (is_old_value, xvalue)
    return cased_xvalue



def mapping_set_fdefault__cxxxvalue_(mapping, key, imay_xdefault_rank, xdefault, /,*, try_vs_Nothing_vs_in:'try-False|Nothing-None|in-True'):
    'cxxxvalue = (is_old_value, default|old_value)@cased_xvalue | (None, default, new_value) if new_value is not default'
    cased_xvalue = mapping_get_fdefault__cased_(mapping, key, imay_xdefault_rank, xdefault, get_vs_pop=False, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    (is_old_value, xvalue) = cased_xvalue
    cxxxvalue = cased_xvalue
    if not is_old_value:
        default = xvalue
        new_value = mapping.setdefault(key, default)
        if 0:
            if new_value is not default: raise Exception
            if new_value is not default:
                xvalue = is_old_value, new_value
        if new_value is not default:
            cxxxvalue = None, default, new_value
    return cxxxvalue





def mapping_set__overwrite_or_raise__pair_(mapping, key, imay_xvalue_rank, xvalue, /):
    #def mapping_set__overwrite_or_raise__pair_(mapping, key, imay_xvalue_rank, xvalue, /,*, get_vs_pop, try_vs_Nothing_vs_in):
    r'''
    set__overwrite_or_raise -> (old_value, new_value)
        #donot want the mapping size grow
        #donot want use deprecated key

    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, old_value)
    #'''
    old_value = mapping[key]
        #raise KeyError here
    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, old_value)
    #old_value is mapping.setdefault(key, new_value)
    mapping[key] = new_value
    return (old_value, new_value)


def mapping_contain_(mapping, key, /,*, try_vs_Nothing_vs_in):
    if try_vs_Nothing_vs_in is False:
        try:
            mapping[key]
        except KeyError:
            return False
        return True
    elif try_vs_Nothing_vs_in is True:
        return key in mapping
    elif try_vs_Nothing_vs_in is None:
        return bool(mapping_get__tmay__get_Nothing(mapping, key))
    elif not (try_vs_Nothing_vs_in is None or type(try_vs_Nothing_vs_in) is bool): raise TypeError
    raise logic-err
def mapping_set__new_or_raise__return_(mapping, key, imay_xvalue_rank, xvalue, /,*, try_vs_Nothing_vs_in, mk_Exception=Exception):
    r'''
    set__new_or_raise -> new_value
        #when init a mapping, we want to avoid duplicate keys, hence avoid overwrite
    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key)
    mk_Exception :: (key, old_value, new_value) -> Exception
    #'''
    if mapping_contain_(mapping, key, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in): raise KeyError(key)

    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key)
    x = mapping.setdefault(key, new_value)
    if x is new_value:
        return new_value
        return (None, new_value,)
    else:
        old_value = x
        raise mk_Exception((key, old_value, new_value))
        return (False, old_value, new_value)


def mapping_set__new_or_overwrite__pair__uniform_(mapping, key, imay_xvalue_rank, xvalue, /,*, get_vs_pop, try_vs_Nothing_vs_in):
    r'''
    set__new_or_overwrite -> (tmay old_value, new_value)
        defaultdict(int/set/list)
        d[k] += ...
        d[k].add(x)
        d[k].append(x)
        ##err:set__new_or_overwrite -> tmay old_value
            #err:use new_value directly instead of fvalue
            d[k] = new_value

    * 1:uniform(imay_xvalue_rank, xvalue)
        new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, tmay_old_value)
    * 2:onthen(on_new, on_overwrite, new_then_overwrite=False)
        new_value = mk_default(imay_on_new_rank, on_new, mapping, key)
        new_value = mk_default(imay_on_overwrite_rank, on_overwrite, mapping, key, old_value)
    * 3:onthen(on_new, on_overwrite, new_then_overwrite=True)
        init_value = mk_default(imay_on_new_rank, on_new, mapping, key)
        new_value = mk_default(imay_on_overwrite_rank, on_overwrite, mapping, key, init_value|old_value)
    #'''
    tmay_old_value = mapping_get__tmay_(mapping, key, get_vs_pop=get_vs_pop, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, tmay_old_value)
    mapping[key] = new_value
    return (tmay_old_value, new_value)

def mapping_set__new_or_overwrite__pair__onthen_(mapping, key, imay_on_new_rank, on_new, imay_on_overwrite_rank, on_overwrite, /,*, new_then_overwrite:bool, get_vs_pop, try_vs_Nothing_vs_in):
    tmay_old_value = mapping_get__tmay_(mapping, key, get_vs_pop=get_vs_pop, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    if not tmay_old_value:
        #new
        init_value = mk_default(imay_on_new_rank, on_new, mapping, key)
    #
        if new_then_overwrite:
            new_value = mk_default(imay_on_overwrite_rank, on_overwrite, mapping, key, init_value)
        else:
            new_value = init_value
    else:
        #overwrite
        [old_value] = tmay_old_value
        new_value = mk_default(imay_on_overwrite_rank, on_overwrite, mapping, key, old_value)

    mapping[key] = new_value
    return (tmay_old_value, new_value)


def mapping_set__new_or_pass__cased_(mapping, key, imay_xvalue_rank, xvalue, /,*, try_vs_Nothing_vs_in):
    r'''
    set__new_or_pass -> (is_old_value, new_value|old_value)
        =set__fdefault

    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key)
    #'''
    (is_old_value, new_value_or_old_value) = cased_result = mapping_set_fdefault__cxxxvalue_(mapping, key, imay_xvalue_rank, xvalue, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    return cased_result


def mapping_set__overwrite_or_pass__may_pair_(mapping, key, imay_xvalue_rank, xvalue, /,*, get_vs_pop, try_vs_Nothing_vs_in):
    r'''
    set__overwrite_or_pass -> may (old_value, new_value)

    new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, old_value)
    #'''

    tmay_old_value = mapping_get__tmay_(mapping, key, get_vs_pop=get_vs_pop, try_vs_Nothing_vs_in=try_vs_Nothing_vs_in)
    if not tmay_old_value:
        #new
        may_pair = None
    else:
        #overwrite
        [old_value] = tmay_old_value
        new_value = mk_default(imay_xvalue_rank, xvalue, mapping, key, old_value)

        mapping[key] = new_value
        may_pair = (old_value, new_value)
    return may_pair

r"""
#[[[TODO

def get4mapping__human(mapping, key, imay_xdefault_rank=None, /,*tmay_xdefault, get_vs_pop=False, try_vs_Nothing_vs_in=None, on_old_value=None, on_default=None, default=None, fdefault=None, key2default=None, mapping_key2default=None, args4mk_default=None, kwargs4mk_default=None, to_remove_old_value=False, to_set_default=False, to_raise_default:'default as exc'=False, set_default_before_raise=False):
    r'''
    imay_xdefault_rank :: may [-1..2]
    tmay_xdefault :: tmay xdefault
        imay_xdefault_rank - xdefault/or search kwargs
        -1 - default
        0 - fdefault
        1 - key2default
        2 - mapping_key2default

    #get_vs_pop, try_vs_Nothing_vs_in
    #   see: mapping_get__tmay_
    get_vs_pop :: bool
        False - get/__getitem__
        True - pop
    try_vs_Nothing_vs_in:
        False - try __getitem__/pop KeyError
        None - setup (default=Nothing) for get/pop
        True - if key in mapping then __getitem__/pop
    on_old_value :: may (old_value -> result)
    on_default :: may (default -> result)
    default :: default
    fdefault :: may ((*args4mk_default, **kwargs4mk_default) -> default)
    key2default :: may (key -> (*args4mk_default, **kwargs4mk_default) -> default)
    mapping_key2default :: may (mapping -> key -> (*args4mk_default, **kwargs4mk_default) -> default)
    args4mk_default :: may [arg]
    kwargs4mk_default :: may {kw:arg}
    #'''
    return get4mapping_(mapping, key, get_vs_getitem=get_vs_getitem, may_on_old_value=on_old_value, may_on_default=on_default, may_default=default, may_fdefault=fdefault, may_key2default=key2default, may_mapping_key2default=mapping_key2default, may_args4mk_default=args4mk_default, may_kwargs4mk_default=kwargs4mk_default)


def get4mapping_(mapping, key, /,*, get_vs_getitem:bool, may_on_old_value=None, may_on_default=None, may_default=None, may_fdefault=None, may_key2default=None, may_mapping_key2default=None, may_args4mk_default=None, may_kwargs4mk_default=None):
    if not sum(x is not None for x in [default, may_fdefault, may_key2default, may_mapping_key2default]) < 2: raise TypeError('too many kwargs: fdefault/key2default/mapping_key2default at most one should be provided!')
    tmay_old_value = mapping_get__tmay_(mapping, key, get_vs_getitem=get_vs_getitem)
    if tmay_old_value:
        [old_value] = tmay_old_value
        if may_on_old_value is None:
            on_old_value = echo
        else:
            on_old_value = may_on_old_value
        result = on_old_value(old_value)
    else:
        if may_on_default is None:
            on_default = echo
        else:
            on_default = may_on_default

        if args4mk_default is None:
            args4mk_default = ()
        if kwargs4mk_default is None:
            kwargs4mk_default = {}

        if fdefault is not None:
            default = fdefault(*args4mk_default, **kwargs4mk_default)
        elif key2default is not None:
            default = key2default(key, *args4mk_default, **kwargs4mk_default)
        elif mapping_key2default is not None:
            default = mapping_key2default(mapping, key, *args4mk_default, **kwargs4mk_default)
        else:
            default
        result = on_default(default)
    return result

def mapping_set_fdefault(mapping, key, /,*, get_vs_getitem:bool, on_old_value=None, on_default=None, default=None, fdefault=None, key2default=None, mapping_key2default=None, args4mk_default=None, kwargs4mk_default=None):
#]]]TODO
#"""



#########################################
#########################################
#########################################
#########################################
#########################################
##old version

def mapping_on_key(mapping, key, payload, handler, /,*, get_vs_getitem=False):
    r'''
    handler :: mapping->key->payload->tmay_old_value->result
    #'''
    if get_vs_getitem:
        mapping_get__tmay = mapping_get__tmay__try_getitem
    else:
        mapping_get__tmay = mapping_get__tmay__get_Nothing
    tmay_old_value = mapping_get__tmay(mapping, key)
    return handler(mapping, key, payload, tmay_old_value)

r"""[[[tmp_coding
def mapping_on_key(mapping, key, payload, handler, /,*, get_vs_getitem=False):
    r'''
    handler :: mapping->key->payload->tmay_old_value->result
    #'''
    return handler(mapping, key, payload, tmay_old_value)
def mapping_on_key_with_set_fdefault(mapping, key, payload, handler, /, fdefault, *, get_vs_getitem=False, setdefault_vs_setitem=False):
    r'''
    handler :: mapping->key->payload->old_value_or_default->result
    #'''
    #def handler(mapping, key, payload, old_value_or_default, /):
    def _handler(mapping, key, payload, tmay_old_value, /):
        #assert _payload is payload
        if tmay_old_value:
            [old_value] = tmay_old_value
            old_value_or_default = old_value
        else:
            #miss, add_new_item
            default = fdefault()
            if setdefault_vs_setitem:
                # .__setitem__()
                mapping[key] = default
                old_value_or_default = default
            else:
                # .setdefault()
                old_value_or_default = mapping.setdefault(key, default)
                    # old_value_or_default may not be default
            pass
        old_value_or_default
        return handler(mapping, key, payload, old_value_or_default)
    return mapping_on_key(mapping, key, payload, _handler)
def getset_fdefault(mapping, key, /, fdefault, may_on_old_value=None, *, get_vs_set:bool, get_vs_getitem=False, setdefault_vs_setitem=False):
    r'''
    fdefault :: () -> default
    may_on_old_value :: may (old_value -> result)
    #'''
    if may_on_old_value is None:
        on_old_value = echo
    else:
        on_old_value = may_on_old_value

    if get_vs_set:
        #set_fdefault
    else:
        #get_fdefault
    def _handler(mapping, key, payload, tmay_old_value, /):
        #assert _payload is payload
        if tmay_old_value:
            [old_value] = tmay_old_value
            result = on_old_value(old_value)
        else:
            #miss, add_new_item
            default = fdefault()
            if setdefault_vs_setitem:
                # .__setitem__()
                mapping[key] = default
                old_value_or_default = default
            else:
                # .setdefault()
                old_value_or_default = mapping.setdefault(key, default)
                    # old_value_or_default may not be default
            pass
        old_value_or_default
        return handler(mapping, key, payload, old_value_or_default)
    return mapping_on_key(mapping, key, payload, _handler)
#]]]tmp_coding
#"""


def get_fdefault(mapping, key, /, fdefault):
    # vs mapping.get(key, default)
    # fdefault :: () -> d
    # get_fdefault :: Map k v -> k -> (()->d) -> (v|d)
    Nothing = []
    r = mapping.get(key, Nothing)
    return fdefault() if r is Nothing else r
def set_fdefault(mapping, key, /, fdefault):
    # vs mapping.setdefault(key, default)
    # fdefault :: () -> d
    # set_fdefault :: Map k v -> k -> (()->v) -> (v|d)
    def miss():
        r = mapping[key] = fdefault()
        return r
    #bug:return mapping.get(key, miss)
    return get_fdefault(mapping, key, miss)


def getitem_fdefault(mapping, key, /, fdefault):
    # fdefault :: () -> d
    # getitem_fdefault :: Map k v -> k -> (()->d) -> (v|d)
    # v.s. get_fdefault:
    #   using try...except
    #   so, __missing__ may be called
    try:
        return mapping[key]
    except KeyError:
        return fdefault()
def setitem_fdefault(mapping, key, /, fdefault):
    # vs mapping.setdefault(key, default)
    # fdefault :: () -> d
    # setitem_fdefault :: Map k v -> k -> (()->v) -> (v|d)
    # v.s. set_fdefault:
    #   using try...except
    #   so, __missing__ may be called
    def miss():
        r = mapping[key] = fdefault()
        return r
    return getitem_fdefault(mapping, key, miss)

def add_new_item(mapping, key, new_value, /, op_oldnew=None):
    if op_oldnew is None:
        def op_oldnew(old_value, new_value):
            raise KeyError('key existed!')
    def _handler(mapping, key, payload, tmay_old_value, /):
        new_value = payload
        if tmay_old_value:
            [old_value] = tmay_old_value
            new_value = op_oldnew(old_value, new_value)
        else:
            #miss, add_new_item
            pass
        mapping[key] = new_value
    payload = new_value
    mapping_on_key(mapping, key, payload, _handler)









if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

