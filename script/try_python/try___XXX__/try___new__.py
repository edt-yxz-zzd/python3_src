


# it seems __new__ and __init__ should have same signature


from inspect import signature, Signature, Parameter
import inspect

class GroupTemplate:
    def __new__(cls):
        self = super(__class__, cls).__new__(cls)
        return self
    def __init__(self, template):
        pass
s = str(signature(GroupTemplate))

GroupTemplate() # fail
# TypeError: __init__() missing 1 required positional argument: 'template'


