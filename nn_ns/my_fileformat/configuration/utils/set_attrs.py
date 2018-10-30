
def set_attrs(**kwargs):
    '''
set_attrs decorator
usage:
    @set_attrs(__doc__ = ...)
    def f():pass
'''
    def decorator(f):
        for attr, obj in kwargs.items():
            setattr(f, attr, obj)
        return f
    return decorator

