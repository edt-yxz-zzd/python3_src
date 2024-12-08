#e ../../python3_src/seed/debug/with_expect_error.py
#view ../../python3_src/seed/debug/expectError.py

import contextlib
@contextlib.contextmanager
def with_expect_error(Error, Error_if_no_exc=None, /):
    if Error is None:
        Error = Exception
    if Error_if_no_exc is None:
        Error_if_no_exc = Exception
    try:
        yield
    except Error:
        pass
    else:
        raise Error_if_no_exc
del contextlib

with with_expect_error(KeyError):
    raise KeyError
try:
    with with_expect_error(KeyError):
        raise SyntaxError
except SyntaxError:
    pass
else:
    raise 000
try:
    with with_expect_error(KeyError, IndexError):
        pass
except IndexError:
    pass
else:
    raise 000

from seed.debug.with_expect_error import with_expect_error

