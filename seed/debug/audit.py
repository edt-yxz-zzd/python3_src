
r'''

seed.debug.audit
    see: sys.audit/addaudithook
    audit 旁听


location/params_schema
    any hashable obj, not only str

threading.Lock
    acquire(blocking=True, timeout=-1)
    release()
    locked()->bool



location@[156]
    kwarg_name_set@[64, 156, 173]
    num_args@[156]
    num_args2kwarg_name_set2onoff_just_hooks@[173]
#'''

___begin_mark_of_excluded_global_names__0___ = ...
__all__ = '''
    define_location_api
    undefine_location_api

    register_hook
    unregister_hook

    audit
        call_hooks_at

    turn_onoff_location_api__full
        turn_onoff_location_api__flip
        turn_onoff_location_api__on
        turn_onoff_location_api__off

    get_locations
    get_location_apis_of


    AuditError
        AuditLocationApiExistError
        AuditLocationApiNotExistError
        AuditLocationApiHooksNotEmptyError
    '''.split()


import threading
___end_mark_of_excluded_global_names__0___ = ...



class _Globals:
    lock = threading.Lock()
    #location2num_args2kwarg_name_set2onoff_just_hooks
    _location2num_args2kwarg_name_set2onoff_just_hooks = {}
    @classmethod
    def get_location2num_args2kwarg_name_set2onoff_just_hooks(cls):
        if not cls.lock.locked(): raise logic-err
        return cls._location2num_args2kwarg_name_set2onoff_just_hooks

class AuditError(Exception):pass
class AuditLocationApiExistError(AuditError):pass
class AuditLocationApiNotExistError(AuditError):pass
class AuditLocationApiHooksNotEmptyError(AuditError):pass


def unregister_hook(location, num_args, kwarg_names, key4hook, /):
    def f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /):
        #_test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, nonexist_ok=False)
        onoff, just_hooks = may_onoff_just_hooks
        just_hook = key4hook
        #bug:i = just_hooks.index(just_hook)
        for i in reversed(range(len(just_hooks))):
            if just_hooks[i] is just_hook:
                break
        else:
            raise LookupError(fr'not found key4hook @unregister_hook: location={location!r}, num_args={num_args!r}, kwarg_name_set={kwarg_name_set!r}, key4hook={key4hook!r}')
        del just_hooks[i]
        return

    def main():
        if not type(key4hook) is tuple and len(key4hook)==1: raise TypeError
        [hook] = just_hook = key4hook
        if not callable(hook): raise TypeError
        _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, nonexist_ok=False)


def register_hook(location, num_args, kwarg_names, hook, /):
    r'''-> key4hook
    #'''
    def f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /):
        #_test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, nonexist_ok=False)
        onoff, just_hooks = may_onoff_just_hooks
        key4hook = just_hook = (hook,)
        just_hooks.append(just_hook)
        return key4hook

    def main():
        if not callable(hook): raise TypeError
        key4hook = _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, nonexist_ok=False)
        return key4hook

    key4hook = main()
    if 1:
        [_hook] = just_hook = key4hook
        assert _hook is hook
    return key4hook

def _to_std_api(location, num_args, kwarg_names, /):
    '-> (location, num_args, kwarg_name_set)'
    hash(location)
    if not type(num_args) is int: raise TypeError
    if not num_args >= 0: raise ValueError

    kwarg_name_set = frozenset(kwarg_names)
    del kwarg_names
    if not all(type(name) is str for name in kwarg_name_set): raise TypeError
    if not all(name.isidentifier() for name in kwarg_name_set): raise ValueError
    return location, num_args, kwarg_name_set

def define_location_api(location, num_args, kwarg_names, /,*, exist_ok:bool=False, onoff:bool=True):
    if not type(onoff) is bool: raise TypeError

    (location, num_args, kwarg_name_set) = _to_std_api(location, num_args, kwarg_names)
    with _Globals.lock:
        num_args2kwarg_name_set2onoff_just_hooks = _Globals.get_location2num_args2kwarg_name_set2onoff_just_hooks().setdefault(location, {})
        kwarg_name_set2onoff_just_hooks = num_args2kwarg_name_set2onoff_just_hooks.setdefault(num_args, {})

        new_just_hooks = []
        _onoff, _just_hooks = kwarg_name_set2onoff_just_hooks.setdefault(kwarg_name_set, (onoff, new_just_hooks))
        if not exist_ok and _just_hooks is not new_just_hooks: raise AuditLocationApiExistError(fr'location/schema api already existed @define_location_api: location={location!r}, num_args={num_args!r}, kwarg_name_set={kwarg_name_set!r}')





def _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, /, *, nonexist_ok:bool):
    '-> f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks)'
    (location, num_args, kwarg_name_set) = _to_std_api(location, num_args, kwarg_names)
    del kwarg_names
    with _Globals.lock:
        may_num_args2kwarg_name_set2onoff_just_hooks = _Globals.get_location2num_args2kwarg_name_set2onoff_just_hooks().get(location)
        if may_num_args2kwarg_name_set2onoff_just_hooks is None:
            return f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, None, None)
        num_args2kwarg_name_set2onoff_just_hooks = may_num_args2kwarg_name_set2onoff_just_hooks

        may_kwarg_name_set2onoff_just_hooks = num_args2kwarg_name_set2onoff_just_hooks.get(num_args)
        if may_kwarg_name_set2onoff_just_hooks is None:
            return f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, None)
        kwarg_name_set2onoff_just_hooks = may_kwarg_name_set2onoff_just_hooks

        may_onoff_just_hooks = kwarg_name_set2onoff_just_hooks.get(kwarg_name_set)

        _test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, nonexist_ok=nonexist_ok)

        return f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks)



def _test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /, *, nonexist_ok):
    if nonexist_ok and may_num_args2kwarg_name_set2onoff_just_hooks is None: return
    if may_num_args2kwarg_name_set2onoff_just_hooks is None: raise AuditLocationApiNotExistError(fr'location/schema not exists: location={location!r}')


    if nonexist_ok and may_kwarg_name_set2onoff_just_hooks is None: return
    if may_kwarg_name_set2onoff_just_hooks is None: raise AuditLocationApiNotExistError(fr'location/schema exists, but num_args not exists: location={location!r}, num_args={num_args!r}')


    if nonexist_ok and may_onoff_just_hooks is None: return
    if may_onoff_just_hooks is None: raise AuditLocationApiNotExistError(fr'location/schema+num_args exists, but kwarg_name_set not exists: location={location!r}, num_args={num_args!r}, kwarg_name_set={kwarg_name_set!r}')


    onoff, just_hooks = may_onoff_just_hooks
    return

def undefine_location_api(location, num_args, kwarg_names, /,*, nonexist_ok=False, nonempty_just_hooks_ok4remove=False):
    def f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /):
        #_test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, nonexist_ok=nonexist_ok)
        if may_onoff_just_hooks is None: return

        num_args2kwarg_name_set2onoff_just_hooks = may_num_args2kwarg_name_set2onoff_just_hooks
        kwarg_name_set2onoff_just_hooks = may_kwarg_name_set2onoff_just_hooks
        onoff, just_hooks = may_onoff_just_hooks
        if not nonempty_just_hooks_ok4remove and just_hooks: raise AuditLocationApiHooksNotEmptyError(fr'location/schema api holds non-empty hooks @undefine_location_api: location={location!r}, num_args={num_args!r}, kwarg_name_set={kwarg_name_set!r}')

        r = kwarg_name_set2onoff_just_hooks.pop(kwarg_name_set)
        assert not r
        if not kwarg_name_set2onoff_just_hooks:
            r = num_args2kwarg_name_set2onoff_just_hooks.pop(num_args)
            assert not r
            if not num_args2kwarg_name_set2onoff_just_hooks:
                r = _Globals.get_location2num_args2kwarg_name_set2onoff_just_hooks().pop(location)
                assert not r
    def main():
        _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, nonexist_ok=nonexist_ok)
    main()


def turn_onoff_location_api__flip(location, num_args, kwarg_names, /):
    turn_onoff_location_api__full(location, num_args, kwarg_names, onoff_if_on=False, onoff_if_off=True)
def turn_onoff_location_api__on(location, num_args, kwarg_names, /):
    turn_onoff_location_api__full(location, num_args, kwarg_names, onoff_if_on=True, onoff_if_off=True)
def turn_onoff_location_api__off(location, num_args, kwarg_names, /):
    turn_onoff_location_api__full(location, num_args, kwarg_names, onoff_if_on=False, onoff_if_off=False)
def turn_onoff_location_api__full(location, num_args, kwarg_names, /,*, onoff_if_on:bool, onoff_if_off:bool):
    if not type(onoff_if_on) is bool: raise TypeError
    if not type(onoff_if_off) is bool: raise TypeError

    (location, num_args, kwarg_name_set) = _to_std_api(location, num_args, kwarg_names)
    kwarg_names = kwarg_name_set
    def f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /):
        old_onoff, just_hooks = may_onoff_just_hooks
        new_onoff = onoff_if_on if old_onoff else onoff_if_off

        kwarg_name_set2onoff_just_hooks = may_kwarg_name_set2onoff_just_hooks
        kwarg_name_set2onoff_just_hooks[kwarg_name_set] = new_onoff, just_hooks
    def main():
        _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, nonexist_ok=False)
    main()



def audit(location, /, *args, **kwargs):
    def f(kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, /):
        #_test_on_may_onoff_just_hooks_ex(location, num_args, kwarg_name_set, may_num_args2kwarg_name_set2onoff_just_hooks, may_kwarg_name_set2onoff_just_hooks, may_onoff_just_hooks, nonexist_ok=False)
        onoff, just_hooks = may_onoff_just_hooks
        just_hooks = list(just_hooks)
        return onoff, just_hooks

    def main():
        num_args = len(args)
        kwarg_names = set(kwargs)
        onoff, just_hooks = _call_on_may_onoff_just_hooks_ex(location, num_args, kwarg_names, f, nonexist_ok=False)
        if onoff:
            for [hook] in just_hooks:
                hook(*args, **kwargs)
    main()


call_hooks_at = audit


def get_locations():
    with _Globals.lock:
        return frozenset(_Globals.get_location2num_args2kwarg_name_set2onoff_just_hooks())
def get_location_apis_of(location, /,*, with_onoff:bool=False):
    'location -> (num_args2kwarg_name_sets if not with_onoff else num_args2kwarg_name_set2onoff)'
    if not type(with_onoff) is bool: raise TypeError

    with _Globals.lock:
        num_args2kwarg_name_set2onoff_just_hooks = _Globals.get_location2num_args2kwarg_name_set2onoff_just_hooks()[location]#KeyError
        assert num_args2kwarg_name_set2onoff_just_hooks

        d = {}
        for num_args, kwarg_name_set2onoff_just_hooks in num_args2kwarg_name_set2onoff_just_hooks.items():
            assert kwarg_name_set2onoff_just_hooks
            if not with_onoff:
                #kwarg_name_sets = frozenset(kwarg_name_set2onoff_just_hooks)
                kwarg_name_sets = set(kwarg_name_set2onoff_just_hooks)
                either = kwarg_name_sets
            else:
                kwarg_name_set2onoff = {kwarg_name_set:onoff for kwarg_name_set, (onoff, just_hooks) in kwarg_name_set2onoff_just_hooks.items()}
                either = kwarg_name_set2onoff
            d[num_args] = either
    if not with_onoff:
        num_args2kwarg_name_sets = d
        return num_args2kwarg_name_sets
    else:
        num_args2kwarg_name_set2onoff = d
        return num_args2kwarg_name_set2onoff


