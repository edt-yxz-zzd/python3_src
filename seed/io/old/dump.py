
import pickle
from .as_file import as_file


def _dump(obj, file_obj):
    pickle.dump(obj, file_obj)
def _load(file_obj):
    return pickle.load(file_obj)
def dump(obj, file, *, force=False):
    f = lambda file_obj: _dump(obj, file_obj)
    mode = 'wb' if force else 'xb'
    as_file(f, file, mode)

def _make_on_open_fail(calc_and_dump_if_absent):
    def _on_open_fail(exception, file, args, kwargs):
        try:
            raise exception
        except FileNotFoundError:
            pass
        obj = calc_and_dump_if_absent()
        dump(obj, file)
        return open(file, *args, **kwargs)
    return _on_open_fail
def load(file, calc_and_dump_if_absent=None):
    # obj = calc_and_dump_if_absent()
    if calc_and_dump_if_absent is None:
        return as_file(_load, file, 'rb')
    else:
        on_open_fail = _make_on_open_fail(calc_and_dump_if_absent)
        return as_file_ex(on_open_fail, _load, file, 'rb')

