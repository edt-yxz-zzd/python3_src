


def on_open_fail(exception, file, args, kwargs):
    raise exception
_on_open_fail = on_open_fail
def as_file(func, file, *args, **kwargs):
    return as_file_ex(_on_open_fail, func, file, *args, **kwargs)

def is_file_obj(obj):
    return hasattr(obj, 'write') or hasattr(obj, 'read')
def as_file_ex(on_open_fail, func, file, *args, **kwargs):
    # on_open_fail = None | (exception, file, args, kwargs) -> file_obj
    # func(file_obj)
    # file = path | file_obj
    # file_obj = open(fname, *args, **kwargs)
    if on_open_fail is None:
        on_open_fail = _on_open_fail

    if is_file_obj(file):
        file_obj = file
        return func(file_obj)
    else:
        try:
            file_obj = open(file, *args, **kwargs)
        except Exception as e:
            file_obj = on_open_fail(e, file, args, kwargs)

        with file_obj:
            return func(file_obj)
    pass


'''
def curry_file(file, *args, **kwargs):
    def partial_applied(func_, *args_, **kwargs_):
        # return func_(file_obj, *args_, **kwargs_)
        func = lambda file_obj: func_(file_obj, *args_, **kwargs_)
        return as_file(func, file, *args, **kwargs)
    return partial_applied
'''
def curry_file_ex(on_open_fail):
    # on_open_fail = None | (exception, file, args, kwargs) -> file_obj
    def curry_file(file, *args, **kwargs):
        def partial_applied(func_, *args_, **kwargs_):
            # return func_(file_obj, *args_, **kwargs_)
            func = lambda file_obj: func_(file_obj, *args_, **kwargs_)
            return as_file_ex(on_open_fail, func, file, *args, **kwargs)
        return partial_applied
    return curry_file
curry_file = curry_file_ex(None)



