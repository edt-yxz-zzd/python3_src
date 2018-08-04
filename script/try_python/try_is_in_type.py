

try:
    assert 1 in int
except Exception as e:
    print(repr(e))
    #TypeError("argument of type 'type' is not iterable",)


try:
    type.__contains__ = lambda cls, obj: isinstance(obj, cls)
    type.__le__ = lambda base, subcls: issubclass(subcls, base)
    assert 1 in int
    assert object <= int
except Exception as e:
    print(repr(e))
    # TypeError("can't set attributes of built-in/extension type 'type'",)





