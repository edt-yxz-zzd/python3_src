#from seed.tiny_.catched_call__either import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either
__all__ = '''
    catched_call__either
    cached_catched_call__either
    get_or_cached_catched_call__either
    '''.split()

from seed.tiny_.check import check_type_is, check_pair

def catched_call__either(may_Base4Exception, calc_value, /):
    '-> (False, exc)/(True, value)'
    #def catched_call__either(f, /, *args, **kwargs):
    #   eval args/kwargs may be too slow!!
    #   catched_call__either(..., lambda:...)
    #   vs catched_call__either(..., f, g(), **h())
    if may_Base4Exception is None:
        Base4Exception = Exception
    else:
        Base4Exception = may_Base4Exception
    try:
        value = calc_value()
    except Base4Exception as exc:
        is_value = False
        exc_vs_value = exc
    else:
        is_value = True
        exc_vs_value = value
    either = (is_value, exc_vs_value)
    return either
def cached_catched_call__either(may_cached_either, may_Base4Exception, calc_value, set_cached_either, /):
    '-> (False, exc)/(True, value)'
    if may_cached_either is None:
        either = catched_call__either(may_Base4Exception, calc_value)
    else:
        either = may_cached_either
    check_pair(either)
    (is_value, exc_vs_value) = either
    check_type_is(bool, is_value)
    if may_cached_either is None:
        set_cached_either(either)
    return either


def get_or_cached_catched_call__either(get_may_cached_either, may_Base4Exception, calc_value, set_cached_either, /):
    '-> (False, exc)/(True, value)'
    may_cached_either = get_may_cached_either()
    if may_cached_either is None:
        either = cached_catched_call__either(may_cached_either, may_Base4Exception, calc_value, set_cached_either)
        may_cached_either = get_may_cached_either()
        if not may_cached_either is either: raise logic-err
    either = may_cached_either
    check_pair(either)
    (is_value, exc_vs_value) = either
    check_type_is(bool, is_value)
    return either
