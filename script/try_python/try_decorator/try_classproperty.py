
'''
class C:
    A = 0
    @property
    @classmethod
    def A(cls):
        return 0
'''
class C:
    A = 0
    @property
    @classmethod
    def A(cls):
        return 0

assert type(C.A) is property
class C:
    A = 0
    @classmethod
    @property
    def A(cls):
        return 0

assert type(C.A) not in {classmethod, property, int}


class classproperty:
    def __new__(self, f):
        return f()
class C:
    A = 0
    @classproperty
    def A():
        return 0

assert C.A == 0





class classproperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance_or_None, owner_class):
        # type(instance) is owner_class
        return self.func(owner_class)

class C:
    A = 0
    @classproperty
    def A(cls):
        return 0
assert C.A == 0



class C:
    A = 0
    @classproperty
    def A(cls):
        raise NotImplementedError
    
assert C.A == 0
help(C.A)























