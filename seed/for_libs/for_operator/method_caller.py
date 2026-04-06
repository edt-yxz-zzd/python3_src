
__all__ = 'method_caller'.split()

class method_caller:
    'operator.methodcaller(attr, *args, **kwargs)(obj) # no more args!'
    def __init__(self, method_name, *args, **kwargs):
        self.method_name = method_name
        self.args = args
        self.kwargs = kwargs
    def __call__(self, obj, *args, **kwargs):
        return getattr(obj, self.method_name)(
                *self.args, *args, **self.kwargs, **kwargs)

from seed.for_libs.for_operator.method_caller import method_caller
