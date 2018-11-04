

__all__ = '''
    all_decorated_by_if
    '''.split()

def all_decorated_by_if(pred, decorator):
    if not callable(pred): raise TypeError
    if not callable(decorator): raise TypeError

    def class_decorator(cls):
        d = cls.__dict__
        for name, obj in list(d.items()):
            if pred(name, obj):
                #d[name] = decorator(obj)
                setattr(cls, name, decorator(obj))
        return cls
    return class_decorator


