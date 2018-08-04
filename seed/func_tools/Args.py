

__all__ = '''
    act
    Args
    '''.split()

def isArgs(obj):
    return isinstance(obj, Args)
class Args:
    # to be a immutable object
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    @classmethod
    def from_args_kwargs(cls, *args, **kwargs):
        return cls(*args, **kwargs)
    def call(self, func):
        return func(*self.args, **self.kwargs)
    def call_self_after(self, func, *args):
        return self.call_ex(False, None, func, *args)
    def new_self_after(self, *args):
        return self.new_ex(False, None, *args)
    def new_ex(self, self_args_before, self_kwargs_overwrited
                , *args, **kwargs):
        return self.call_ex(self_args_before, self_kwargs_overwrited
                            , self.from_args_kwargs, *args, **kwargs)
    def call_ex(self, self_args_before, self_kwargs_overwrited
                , func, *args, **kwargs):
        # self_args_before = None | bool
        #   apply self.args before the input *args
        # self_kwargs_overwrited = None | bool
        #   overwrite self.kwargs by input **kwargs
        # None means one of the [kw]args should be empty or no key overlay
        if self_args_before is None:
            if not args:
                args_ = self.args
            elif not self.args:
                args_ = args_
            else:
                raise ValueError(
                    'self_args_before is None'
                    ' but both self.args and input args are not empty')
        elif self_args_before:
            args_ = self.args + args
        else:
            args_ = args + self.args

        if self_kwargs_overwrited is None:
            if not kwargs:
                kwargs_ = self.kwargs
            elif not self.kwargs:
                kwargs_ = kwargs
            else:
                L = len(kwargs) + len(self.kwargs)
                kwargs_ = kwargs
                kwargs_.update(self.kwargs)
                if len(kwargs_) != L:
                    raise ValueError(
                        'self_kwargs_overwrited is None'
                        ' but both self.kwargs and input kwargs are not empty'
                        ' and they have some keys overlay')
        elif self_kwargs_overwrited:
            kwargs_ = self.kwargs.copy()
            kwargs_.update(kwargs)
        else:
            kwargs_ = kwargs
            kwargs_.update(self.kwargs)

        return func(*args_, **kwargs_)
        try:
            return func(*args_, **kwargs_)
        except:
            print(func, args_, kwargs_)
            raise


def _call(func, *args, **kwargs):
    return func(*args, **kwargs)
def act(args:Args):
    assert isArgs(args)
    return args.call(_call)


def get_args(*args, **kwargs):
    return (args, kwargs)

#r = act(Args(lambda *args, **kwargs: (args, kwargs), 1, 2, a=3,b=4))
#print(r)
assert ((1,2), {'a':3, 'b':4}) == act(Args(get_args, 1, 2, a=3,b=4))
assert ((1,2,3), {'a':5}) == Args(3, a=5).call_self_after(get_args, 1,2)
assert ((1,2,3), {'a':5, 'b':4}) == \
    Args(3, a=5).call_ex(False, None, get_args, 1,2, b=4)
