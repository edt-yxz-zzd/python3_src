
'''
dynamic_missing_dict of module
    to dynamic support __missing__

if missing,
    DynamicMissingDict call the input missing function, and not set the result.
    ModuleMissingDict will get the __missing__ entity in module (i.e. the dict itself), and then call it, and set the value auto.

MissingModule
    a moduler obj, whose __dict__ is a ModuleMissingDict

'''

__all__ = '''
    MissingModule

    ModuleMissingDict
        module_missing


    dynamic_missing_dict
    DynamicMissingDict
    '''.split()



class DynamicMissingDict(dict):
    # missing :: dict -> name -> (value|raise KeyError)
    #   missing should set value itself
    __slots__ = '__missing'
    def __init__(self, missing, *args, **kwargs):
        self.__missing = missing
        super().__init__(*args, **kwargs)
    def __missing__(self, name):
        return self.__missing(self, name)
    def missing_get(self, name, fdefault):
        # call __getitem__; may forward to __missing__
        #   NOTE: dict.get donot call __getitem__
        try:
            return self[name]
        except KeyError:
            return fdefault()
        return


def dynamic_missing_dict(missing):
    # return a callable(maybe a type)
    return lambda *args, **kwargs: DynamicMissingDict(missing, *args, **kwargs)
def module_missing(d, name):
    # assume d is global dict of a module
    f = d.get('__missing__')
    if f is None:
        raise KeyError(f'{name!r}')
    r = f(d, name)
    d[name] = r
    return r

ModuleMissingDict = dynamic_missing_dict(module_missing)
class MissingModule:
    # override __dict__ by a ModuleMissingDict
    __slots__ = ('__dict',)
    def __init__(self):
        #self.__dict = ModuleMissingDict()
        d = ModuleMissingDict()
        object.__setattr__(self, '_MissingModule__dict', d)
    @property
    def __dict__(self):
        d = object.__getattribute__(self, '_MissingModule__dict')
        return d
    def __getattribute__(self, name):
        d = object.__getattribute__(self, '_MissingModule__dict')
        if name == '__dict__':
            return d
        try:
            return d[name]
        except KeyError:
            raise AttributeError
    def __setattr__(self, name, obj):
        d = object.__getattribute__(self, '_MissingModule__dict')
        d[name] = obj

mm = MissingModule()
assert type(mm.__dict__) is DynamicMissingDict
assert not mm.__dict__
mm.abc = 'A'
assert mm.abc == 'A'
assert len(mm.__dict__) == 1



def t():
    from seed.tiny import expectError
    def missing1(d, name):
        return name # not setitem!!
    D = dynamic_missing_dict(missing1)
    d = D()
    assert not d
    assert 0 == d[0]
    assert not d # dict donot set it!!
    assert d.get(0) is None # get donot call __getitem__!!


    d = ModuleMissingDict()
    assert not d
    assert expectError(KeyError, lambda:d[0])
    d['__missing__'] = missing1
    assert 0 == d[0]
    assert d # set it!!


t()


'''
class DynamicMissingDict(dict):
    # missing :: dict -> name -> called_by_get -> (value|raise KeyError)
    #   called_by_get :: () | (default,)
    #   missing should set value itself
    __slots__ = '__missing'
    def __init__(self, missing):
        self.__missing = missing
    def __contains__(self, key):
    def keys # how???
    def __getitem__(self, name):
    def get(self, name, default=None):
    def __missing__(self, name):
        self.__missing(self, name, ())
'''

