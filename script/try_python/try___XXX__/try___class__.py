
# Special attributes: __dict__ is the attribute dictionary; __class__ is the instance’s class.
# Special method names: Class instances can pretend to be numbers, sequences, or mappings if they have methods with certain special names. See section Special method names.


class Try___class___EX:
    def __getattribute__(self, name):
        if name == '__class__':
            return '@Try___class___EX.__class__'
        if name == '__dict__':
            return {'Try___class___EX_DOT__dict__':None} # '@Try___class___EX.__dict__'
        return super(__class__, type(self)).__getattribute__(self, name)
    def __repr__(self):
        return '@Try___class___EX.__repr__'

class Try___class__:
    def __getattribute__(self, name):
        if name == '__class__':
            return '@Try___class__.__class__'
        return super(__class__, type(self)).__getattribute__(self, name)

    def __init__(self):
        # TypeError: __class__ must be set to a class, not 'str' object
        #     self.__class__ = '@Try___class__.__init__'
        self.__class__ = Try___class___EX

        # TypeError: __dict__ must be set to a dictionary, not a 'NoneType'
        #     self.__dict__ = None
        self.__dict__ = {'Try___class__DOT__init__':None}

    def __repr__(self):
        return '@Try___class__.__repr__'

a = Try___class__()
assert a.__class__ == '@Try___class___EX.__class__'
assert type(a) is Try___class___EX
assert a.__dict__ == vars(a) == {'Try___class___EX_DOT__dict__':None}
assert dir(a) == ['Try___class___EX_DOT__dict__']
assert repr(a) == '@Try___class___EX.__repr__'

r'''
type(a) passby __getattribute__ to get .__class__
xx.__class__ = type(a).__getattribute__(a, '__class__')
xx.__dict__ = type(a).__getattribute__(a, '__dict__')
'''





class TransformAttribute:
    def __getattribute__(self, name):
        return type(self).__transform__(self, name)
    


class Echo(TransformAttribute):
    def __transform__(self, name):
        return name
    



echo = Echo()
assert echo.abc == 'abc'

import sys # for modules
sys.modules['echo'] = echo

from echo import aaa, bbb
assert (aaa, bbb) == ('aaa', 'bbb')





