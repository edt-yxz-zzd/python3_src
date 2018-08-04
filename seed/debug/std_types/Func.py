

from .show_excepts import *
#from pprint import pprint
not_show_names = frozenset(['__call__', '__class__', '__delattr__', '__dir__',
                  '__eq__', '__format__', '__ge__', '__get__',
                  '__getattribute__', '__gt__', '__hash__', '__init__',
                  '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
                  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
                  '__str__', '__subclasshook__'])


def func2vars(func):
    # print(dir(func))
    return {name : getattr(func, name) for name in dir(func) if name not in not_show_names}

def show_func(func, excepts = ('__globals__', '__code__')):
    d = func2vars(func)
    d.update(dict.fromkeys(excepts, ...))
    pprint(d)
    
_pred = lambda name: name not in not_show_names
func2vars = Obj2Vars(_pred)
show_func = ShowExcepts(func2vars.pred, ['__globals__', '__code__'])
#show_func(show_func)
