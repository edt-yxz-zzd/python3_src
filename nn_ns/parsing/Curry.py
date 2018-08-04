
class Curry:
    def __init__(self, args):
        ...
    @property
    def ARGS_TYPES(self):
        # if len(ARGS_TYPES)==0: then is a value # arity
        # return a tuple
        pass
    @property
    def arity(self):
        return len(self.ARGS_TYPES)
    @property
    def value(self):
        # (self) == self.value # howto impl??
        # using (self)() instead
        if self.arity == 0:
            return self.value
        else:
            return self

    def curry(self, ...):pass # worker
    def __call__(self):
        return self.value
    def __truediv__(self, other):
        if self.arity == 0:
            raise TypeError
        if self.arity == 1:
            if isinstance(other, curry):
                other = other()
            args = self.args + (other,)
            value = self.worker(args)
            return ValueCurry(args, value)
            
        
