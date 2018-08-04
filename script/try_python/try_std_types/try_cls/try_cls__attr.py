
'''
try
    __mro__
    __name__
    __qualname__
'''


# try instance of type or other metaclass

assert int.__mro__ == (int, object)

class A:
    class B:pass

# qualname
# A dotted name showing the “path” from a module’s global scope to a class, function or method defined in that module
assert A.B.__name__ == 'B'
assert A.B.__qualname__ == 'A.B'









