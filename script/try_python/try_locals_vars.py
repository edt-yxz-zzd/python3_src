

'''
with scoped_names('xxx yyy'):
    ...

==>>
try:
    ...
finally:
    del xxx, yyy
'''

'''
locals() 
Note
The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.


Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.
help(vars) ==>> Without arguments, equivalent to locals().
'''

def f():
    print(locals())
    locals()['a'] = 'af'
    print(locals())
    
    print(vars())
    vars()['b'] = 'b'
    print(vars())
    
f()
