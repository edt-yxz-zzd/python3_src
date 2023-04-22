
#################################
#[[[__doc__-begin
r'''

py -m seed.helper.get4may
py -m nn_ns.app.debug_cmd   seed.helper.get4may
used by:
    seed.mapping_tools.fdefault

see:
    from seed.tiny_.mk_fdefault import eliminate_tmay, eliminate_tmay__cased, eliminate_tmay__mix, eliminate_tmay_or_raise, eliminate_tmay_or_raise__simple


from seed.helper.get4may import nmay2tmay, get4nmay, fget4nmay, fget4nmay__human, xget4nmay__human
    ====
    nmay2tmay(nmay)
    get4nmay(may_f, echo)
    fget4nmay(nmay, fdefault)
    fget4nmay__human(nmay, fdefault, *args, **kwargs)
    xget4nmay__human(nmay, default)
        xget4nmay__human(nmay, fdefault=fdefault)
        xget4nmay__human(nmay, ..., Nothing=, on_old_value=, on_default=)
    ====

from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human
    ====
    fgetP4nmay_
    xget4nmay_
    nmay2tmay__Nothing(Nothing, nmay)
    get4nmay__Nothing(Nothing, nmay, default)
    fget4nmay__Nothing
    fgetP4nmay__Nothing_
    fget4nmay__Nothing__human

naming explanation:
    get:
        get - default
        fget - fdefault
        xget - default xor fdefault
    P:
        fgetP - fdefault with parameters
    4:
        "for"
    nmay:
        may - Haskell.Maybe
        n - None/input.Nothing used as Haskell.Nothing
        nmay__Nothing - input.Nothing used as Haskell.Nothing
    "_"suffix vs "__human"suffix:
        "_"suffix
            each parameter required argument to avoid argument-forwading-omission
        "__human"suffix:
            provider all possible defaults







py -m nn_ns.app.debug_cmd   seed.helper.get4may
def nmay2tmay__Nothing(Nothing, nmay, /):
def nmay2tmay(nmay, /):
def get4nmay__Nothing(Nothing, nmay, default, /):
def get4nmay(nmay, default, /):
def fget4nmay__Nothing(Nothing, nmay, fdefault, /):
def fget4nmay(nmay, fdefault, /):
def fgetP4nmay__Nothing_(Nothing, nmay, fdefault, args, kwargs, /):
def fgetP4nmay_(nmay, fdefault, args, kwargs, /):
def fget4nmay__human(nmay, fdefault, /,*args, **kwargs):
def fget4nmay__Nothing__human(Nothing, nmay, fdefault, /,*args, **kwargs):
def xget4nmay_(nmay, xdefault, may_args_kwargs, /,*, Nothing, may_on_old_value, may_on_default):
def xget4nmay__human(nmay, /, *tmay_default, fdefault=None, args=None, kwargs=None, Nothing=None, on_old_value=None, on_default=None):



#[[[doctest_examples-begin
>>> Nothing = object()
>>> default = object()
>>> old_value = object()
>>> fdefault_0_0 = lambda: default
>>> fdefault_1_0 = lambda x, /: default
>>> fdefault_1_a = lambda x, /,*, a: default
>>> on_default = lambda x, /: [x]
>>> on_old_value = lambda x, /: {x}


def nmay2tmay__Nothing(Nothing, nmay, /):
>>> nmay2tmay__Nothing(Nothing, Nothing)
()
>>> (old_value,) == nmay2tmay__Nothing(Nothing, old_value)
True

def nmay2tmay(nmay, /):
>>> nmay2tmay(None)
()
>>> (old_value,) == nmay2tmay(old_value)
True

def get4nmay__Nothing(Nothing, nmay, default, /):
>>> default is get4nmay__Nothing(Nothing, Nothing, default)
True
>>> old_value is get4nmay__Nothing(Nothing, old_value, default)
True
>>> None is get4nmay__Nothing(Nothing, None, default)
True


def get4nmay(nmay, default, /):
>>> default is get4nmay(None, default)
True
>>> old_value is get4nmay(old_value, default)
True


def fget4nmay__Nothing(Nothing, nmay, fdefault, /):
>>> default is fget4nmay__Nothing(Nothing, Nothing, fdefault_0_0)
True
>>> old_value is fget4nmay__Nothing(Nothing, old_value, fdefault_0_0)
True



def fget4nmay(nmay, fdefault, /):
>>> default is fget4nmay(None, fdefault_0_0)
True
>>> old_value is fget4nmay(old_value, fdefault_0_0)
True



def fgetP4nmay__Nothing_(Nothing, nmay, fdefault, args, kwargs, /):
>>> default is fgetP4nmay__Nothing_(Nothing, Nothing, fdefault_0_0, (), {})
True
>>> old_value is fgetP4nmay__Nothing_(Nothing, old_value, fdefault_0_0, (), {})
True

>>> default is fgetP4nmay__Nothing_(Nothing, Nothing, fdefault_1_0, (1,), {})
True
>>> old_value is fgetP4nmay__Nothing_(Nothing, old_value, fdefault_1_0, (1,), {})
True

>>> default is fgetP4nmay__Nothing_(Nothing, Nothing, fdefault_1_a, (1,), {})
Traceback (most recent call last):
TypeError: <lambda>() missing 1 required keyword-only argument: 'a'

>>> old_value is fgetP4nmay__Nothing_(Nothing, old_value, fdefault_1_a, (1,), {})
True

>>> default is fgetP4nmay__Nothing_(Nothing, Nothing, fdefault_1_a, (1,), {'a':3})
True
>>> old_value is fgetP4nmay__Nothing_(Nothing, old_value, fdefault_1_a, (1,), {'a':3})
True


def fgetP4nmay_(nmay, fdefault, args, kwargs, /):
>>> default is fgetP4nmay_(None, fdefault_0_0, (), {})
True
>>> old_value is fgetP4nmay_(old_value, fdefault_0_0, (), {})
True

>>> default is fgetP4nmay_(None, fdefault_1_0, (1,), {})
True
>>> old_value is fgetP4nmay_(old_value, fdefault_1_0, (1,), {})
True

>>> default is fgetP4nmay_(None, fdefault_1_a, (1,), {})
Traceback (most recent call last):
TypeError: <lambda>() missing 1 required keyword-only argument: 'a'

>>> old_value is fgetP4nmay_(old_value, fdefault_1_a, (1,), {})
True

>>> default is fgetP4nmay_(None, fdefault_1_a, (1,), {'a':3})
True
>>> old_value is fgetP4nmay_(old_value, fdefault_1_a, (1,), {'a':3})
True



def fget4nmay__human(nmay, fdefault, /,*args, **kwargs):
>>> default is fget4nmay__human(None, fdefault_0_0)
True
>>> old_value is fget4nmay__human(old_value, fdefault_0_0)
True

>>> default is fget4nmay__human(None, fdefault_1_0, 1)
True
>>> old_value is fget4nmay__human(old_value, fdefault_1_0, 1)
True

>>> default is fget4nmay__human(None, fdefault_1_a, 1)
Traceback (most recent call last):
TypeError: <lambda>() missing 1 required keyword-only argument: 'a'

>>> old_value is fget4nmay__human(old_value, fdefault_1_a, 1)
True

>>> default is fget4nmay__human(None, fdefault_1_a, 1, a=3)
True
>>> old_value is fget4nmay__human(old_value, fdefault_1_a, 1, a=3)
True



def fget4nmay__Nothing__human(Nothing, Nothing, nmay, fdefault, /,*args, **kwargs):
>>> default is fget4nmay__Nothing__human(Nothing, Nothing, fdefault_0_0)
True
>>> old_value is fget4nmay__Nothing__human(Nothing, old_value, fdefault_0_0)
True

>>> default is fget4nmay__Nothing__human(Nothing, Nothing, fdefault_1_0, 1)
True
>>> old_value is fget4nmay__Nothing__human(Nothing, old_value, fdefault_1_0, 1)
True

>>> default is fget4nmay__Nothing__human(Nothing, Nothing, fdefault_1_a, 1)
Traceback (most recent call last):
    ...
TypeError: <lambda>() missing 1 required keyword-only argument: 'a'

>>> old_value is fget4nmay__Nothing__human(Nothing, old_value, fdefault_1_a, 1)
True

>>> default is fget4nmay__Nothing__human(Nothing, Nothing, fdefault_1_a, 1, a=3)
True
>>> old_value is fget4nmay__Nothing__human(Nothing, old_value, fdefault_1_a, 1, a=3)
True




def xget4nmay_(nmay, xdefault, may_args_kwargs, /,*, Nothing, may_on_old_value, may_on_default):
def xget4nmay__human(nmay, /, *tmay_default, fdefault=None, args=None, kwargs=None, Nothing=None, on_old_value=None, on_default=None):
>>> default is xget4nmay__human(None, default)
True
>>> default is xget4nmay__human(Nothing, default, Nothing=Nothing)
True

>>> old_value is xget4nmay__human(old_value, default)
True
>>> old_value is xget4nmay__human(old_value, default, Nothing=Nothing)
True



>>> old_value is xget4nmay__human(old_value)
Traceback (most recent call last):
    ...
TypeError: should input: default xor fdefault
>>> old_value is xget4nmay__human(old_value, default, fdefault=fdefault_0_0)
Traceback (most recent call last):
    ...
TypeError: should input: default xor fdefault
>>> old_value is xget4nmay__human(old_value, default, args=())
Traceback (most recent call last):
    ...
TypeError: [fdefault is None][not (args is None is kwargs)]
>>> old_value is xget4nmay__human(old_value, default, kwargs={})
Traceback (most recent call last):
    ...
TypeError: [fdefault is None][not (args is None is kwargs)]



>>> default is xget4nmay__human(None, fdefault=fdefault_0_0)
True
>>> default is xget4nmay__human(Nothing, fdefault=fdefault_0_0, Nothing=Nothing)
True
>>> default is xget4nmay__human(None, fdefault=fdefault_1_0, args=[1])
True
>>> default is xget4nmay__human(Nothing, fdefault=fdefault_1_a, args=[1], kwargs={'a':3}, Nothing=Nothing)
True

>>> old_value is xget4nmay__human(old_value, fdefault=fdefault_0_0)
True
>>> old_value is xget4nmay__human(old_value, fdefault=fdefault_0_0, Nothing=Nothing)
True
>>> old_value is xget4nmay__human(old_value, fdefault=fdefault_1_0)
True
>>> old_value is xget4nmay__human(old_value, fdefault=fdefault_1_a, Nothing=Nothing)
True



>>> [default] == xget4nmay__human(None, default, on_default=on_default, on_old_value=on_old_value)
True
>>> {old_value} == xget4nmay__human(old_value, default, on_default=on_default, on_old_value=on_old_value)
True

>>> [default] == xget4nmay__human(None, fdefault=fdefault_0_0, on_default=on_default, on_old_value=on_old_value)
True
>>> {old_value} == xget4nmay__human(old_value, fdefault=fdefault_0_0, on_default=on_default, on_old_value=on_old_value)
True




#]]]doctest_examples-end



#'''
#]]]__doc__-end

#################################

___begin_mark_of_excluded_global_names__1___ = ...
__all__ = '''
    nmay2tmay__Nothing
    nmay2tmay
    get4nmay__Nothing
    get4nmay
    fget4nmay__Nothing
    fget4nmay
    fgetP4nmay__Nothing_
    fgetP4nmay_
    fget4nmay__human
    fget4nmay__Nothing__human
    xget4nmay_
    xget4nmay__human
    '''.split()

from seed.helper.Echo import echo, theEcho
from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefaultP_from_default, Mk_fdefault_from_default
___end_mark_of_excluded_global_names__1___ = ...


def nmay2tmay__Nothing(Nothing, nmay, /):
    return () if nmay is Nothing else (nmay,)
def nmay2tmay(nmay, /):
    return nmay2tmay__Nothing(None, nmay)

def get4nmay__Nothing(Nothing, nmay, default, /):
    return default if nmay is Nothing else nmay
def get4nmay(nmay, default, /):
    return get4nmay__Nothing(None, nmay, default)

def fget4nmay__Nothing(Nothing, nmay, fdefault, /):
    return fdefault() if nmay is Nothing else nmay
def fget4nmay(nmay, fdefault, /):
    return fget4nmay__Nothing(None, nmay, fdefault)

def fgetP4nmay__Nothing_(Nothing, nmay, fdefault, args, kwargs, /):
    return fget4nmay__Nothing(Nothing, nmay, Mk_fdefault(fdefault, args, kwargs))

def fgetP4nmay_(nmay, fdefault, args, kwargs, /):
    # no "Nothing=None" since fget4nmay__human can not accept extra kwargs
    return fgetP4nmay__Nothing_(None, nmay, fdefault, args, kwargs)

def fget4nmay__human(nmay, fdefault, /,*args, **kwargs):
    return fgetP4nmay_(nmay, fdefault, args, kwargs)
def fget4nmay__Nothing__human(Nothing, nmay, fdefault, /,*args, **kwargs):
    return fgetP4nmay__Nothing_(Nothing, nmay, fdefault, args, kwargs)





#Nothing=?
def xget4nmay_(nmay, xdefault, may_args_kwargs, /,*, Nothing, may_on_old_value, may_on_default):
    if nmay is not Nothing:
        old_value = nmay
        middle_result = old_value
        may_on_middle_result = may_on_old_value
    else:
        if may_args_kwargs is None:
            default = xdefault
        else:
            fdefault = xdefault
            may_args, may_kwargs = may_args_kwargs
            args = get4nmay(may_args, ())
            kwargs = get4nmay(may_kwargs, {})
            default = fdefault(*args, **kwargs)
        middle_result = default
        may_on_middle_result = may_on_default
    on_middle_result = get4nmay(may_on_middle_result, echo)
    result = on_middle_result(middle_result)
    return result
def xget4nmay__human(nmay, /, *tmay_default, fdefault=None, args=None, kwargs=None, Nothing=None, on_old_value=None, on_default=None):
    if not len(tmay_default) <= 1: raise TypeError(f'not: tmay<default>')
    if not ((not tmay_default) ^ (fdefault is None)): raise TypeError(f'should input: default xor fdefault')
    if not ((fdefault is not None) or (args is None is kwargs)): raise TypeError(f'[fdefault is None][not (args is None is kwargs)]')
    if fdefault is None:
        [default] = tmay_default
        #bug:return get4nmay__Nothing(Nothing, nmay, default)
        xdefault = default
        may_args_kwargs = None
    else:
        xdefault = fdefault
        may_args_kwargs = (args, kwargs)
    return xget4nmay_(nmay, xdefault, may_args_kwargs, Nothing=Nothing, may_on_old_value=on_old_value, may_on_default=on_default)


if __name__ == '__main__':
    #show globals
    "py -m nn_ns.app.debug_cmd   seed.helper.get4may"




if __name__ == "__main__":
    import doctest
    doctest.testmod()

