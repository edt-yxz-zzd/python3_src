



def expectError(f, Error):
    try:
        f()
    except Error:
        return
    raise logic-error



class A:
    __slots__ = ()
    def __init__(self):
        self.a=0
        #AttributeError: 'A' object has no attribute 'a'
expectError(lambda:A(), AttributeError)

class A:
    '''
'''
    __slots__ = ()
    def __init__(self):
        self.a=0
        #AttributeError: 'A' object has no attribute 'a'
expectError(lambda:A(), AttributeError)

class A:
    '''
'''
    ''
    __slots__ = ()
    def __init__(self):
        self.a=0
        #AttributeError: 'A' object has no attribute 'a'
expectError(lambda:A(), AttributeError)


class A:
    '''
'''
    ''
    gagagdg = 0
    __slots__ = ()
    def __init__(self):
        self.a=0
        #AttributeError: 'A' object has no attribute 'a'
expectError(lambda:A(), AttributeError)



class A(object):
    __slots__ = ()
    def __init__(self):
        self.a=0
        #AttributeError: 'A' object has no attribute 'a'
expectError(lambda:A(), AttributeError)


#################### all parents should define __slots__!

class B:pass # NOTE: B does not define __slots__!!
class A(B):
    __slots__ = ()
    def __init__(self):
        self.a=0
assert A().a == 0 # now A.__slots__ is useless



######### multiple inheritance: at most one parent have nonempty __slots__
class A:
    __slots__ = ['a']
class B:
    __slots__ = ['b']
def f():
    class C(A,B):pass
    # TypeError: multiple bases have instance lay-out conflict
expectError(f, TypeError)
class B:
    __slots__ = ['a']
expectError(f, TypeError)








