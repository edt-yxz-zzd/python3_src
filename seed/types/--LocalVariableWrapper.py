

def getobj(lvw):
    return type(lvw).__getobj__(lvw)

class LocalVariableWrapper:
    '''
since me represent a local variable,
    should not return me or put me into container

def i_xxx(self, ...):
    self.obj, result = self.obj.xxx(...)
    return result
'''
    def __init__(self, obj, inplace_names):
        self.__obj = obj
        self.__names = set(inplace_names)
    def __getobj__(self):
        return self.__obj
    def __getattr__(self, name):
        if name.startswith('i_'):
            if name not in self.__names:
                raise AttributeError('not found: {!r}'.format(name))
            m = getattr(self.__obj, name)
            def _(*args, **kwds):
                obj, result = m(*args, **kwds)
                self.__obj = obj
                return result
        return getattr(self.__obj, name)
    def __setattr__(self, name, value):
        return setattr(self.__obj, name, value)

    
        
