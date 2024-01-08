#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/if_else_expr.py


seed.lang.if_else_expr
py -m nn_ns.app.debug_cmd   seed.lang.if_else_expr -x
py -m nn_ns.app.doctest_cmd seed.lang.if_else_expr:__doc__ -ff -v
py_adhoc_call   seed.lang.if_else_expr   @f
from seed.lang.if_else_expr import *


[(xxx if a else yyy if b else zzz) =[def]= (xxx if a else (yyy if b else zzz))]
    # infixl
>>> 999 if 1 else 777 if 0 else 555
999
>>> 999 if 1 else 777 if 1 else 555
999
>>> 999 if 0 else 777 if 0 else 555
555
>>> 999 if 0 else 777 if 1 else 555
777

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

if __name__ == "__main__":
    pass
__all__


from seed.lang.if_else_expr import *
