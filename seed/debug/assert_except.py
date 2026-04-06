__all__ = 'assert_except'.split()
def assert_except(ERROR, f, *args, **kwargs):
    try:
        f(*args, **kwargs)
    except ERROR:
        return
    else:
        raise logic-error

from seed.debug.assert_except import assert_except
