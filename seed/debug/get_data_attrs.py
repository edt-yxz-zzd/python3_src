
__all__ = '''
    get_data_attrs get_data_attrs_of_class
    show_attrs show_data_attrs show_data_attrs__func
'''.split()


import inspect

def get_data_attrs_of_class(cls):
    '''get names of all data descriptors of cls'''
    for attr, x in vars(cls).items():
        if inspect.isdatadescriptor(x):
            yield attr
            
def get_data_attrs(obj):
    '''get names of all data descriptors of obj'''
    return get_data_attrs_of_class(type(obj))


def show_attrs(obj, attrs, exclude=(), print=print):
    exclude = frozenset(exclude)
    for name in attrs:
        if name not in exclude:
            print(name, getattr(obj, name))
def show_data_attrs(obj, exclude=(), print=print):
    show_attrs(obj, sorted(get_data_attrs(obj)), exclude=exclude, print=print)


def show_data_attrs__func(f, exclude=('__globals__',), print=print):
    assert inspect.isfunction(f) or inspect.ismethod(f)
    show_data_attrs(f, exclude=exclude, print=print)

    


    
