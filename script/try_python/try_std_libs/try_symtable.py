
'''
which identifiers I forgot to import ??

I can start with star import
after debugging, using 'symtable' to auto list the id needed to be imported

'''


import symtable
from numbers import Integral
import inspect #.getsource(object) 

def f(i):
    if isinstance(i, Integral):
        return
    def h():
        a = b
        return
    c = d
    pass


def get_symtable_of_file(fname):pass
def get_symtable_of_module(module):
    src = inspect.getsource(module)
    table = symtable.symtable(src, module.__name__, "exec")
    print(table)
    return table
table = get_symtable_of_module(__import__(f.__module__))

table.get_symbols()
s=table.lookup('f')
n=s.get_namespace()
print(n.get_globals())
print(n.get_frees())
print(n.get_children())
hs, = n.get_children()
hn = hs#.get_namespace()
print(hn.get_globals())
print(hn.get_frees())
print(hn.get_children())




