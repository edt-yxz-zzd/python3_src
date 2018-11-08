'''

reformat python source code: only constructor expression

pprint donot work for user data type
autopep8 is ugly



AcceptAll
    >>> globals = GlobalDict_for_AcceptAll()
    >>> obj = eval('A(B(), n=C())', globals)
    >>> easy_print_for_AcceptAll(obj, indent='    ', depth=0, file=None)
    A
        (B()
        ,n = C()
        )

namedtuple
    >>> A = namedtuple('A', 'a b'.split())
    >>> B = namedtuple('B', ''.split())
    >>> C = namedtuple('C', 'c'.split())
    >>> a = A(a=B(), b=C(c=1))
    >>> a
    A(a=B(), b=C(c=1))
    >>> easy_print_for_namedtuple(a, indent=' '*4, depth=0, file=None)
    A
        (a = B()
        ,b = C
            (c = 1
            )
        )

    >>> easy_print_for_namedtuple(((), [], {}, set(), [1], {1:2, 3:4}), indent=' '*4, depth=0, file=None)
    tuple(
        [tuple([])
        ,list([])
        ,dict({})
        ,set([])
        ,list(
            [1
            ])
        ,dict(
            {1
            :2
            ,3
            :4
            })
        ])
'''


class EasyPrint:
    def __init__(self, may_get_name_args_kwargs, otherwise_repr):
        'may_get_name_args_kwargs :: object -> None|(name, [arg], [(name, arg)])'
        self.may_get_name_args_kwargs = may_get_name_args_kwargs
        self.otherwise_repr = otherwise_repr
    def __call__(self, obj, *, indent, depth, file, end='\n'):
        self.dprint(obj, indent=indent, depth=depth, file=file)
        print(end=end, file=file)
    def __dprint_dict(self, d, *, indent, depth, file):
        def dprint(*args):
            print(*args, sep='', end='', file=file)

        dprint(type(d).__name__, '(')
        if not d:
            dprint('{})')
            return
        first_char = '{'
        indents1 = indent*(depth+1)
        depth1 = depth + 1
        for key, val in d.items():
            dprint('\n', indents1, first_char)
            self.dprint(key, indent=indent, depth=depth1, file=file)
            first_char = ':'
            dprint('\n', indents1, first_char)
            self.dprint(val, indent=indent, depth=depth1, file=file)
            first_char = ','
        dprint('\n', indents1, '})')
    def __dprint_TLS(self, s, *, indent, depth, file):
        def dprint(*args):
            print(*args, sep='', end='', file=file)

        dprint(type(s).__name__, '(')
        if not s:
            dprint('[])')
            return
        first_char = '['
        indents1 = indent*(depth+1)
        depth1 = depth + 1
        for arg in s:
            dprint('\n', indents1, first_char)
            first_char = ','
            self.dprint(arg, indent=indent, depth=depth1, file=file)
        dprint('\n', indents1, '])')
    def __dprint_other_obj(self, obj, *, indent, depth, file):
        def dprint(*args):
            print(*args, sep='', end='', file=file)
        if isinstance(obj, dict):
            self.__dprint_dict(obj, indent=indent, depth=depth, file=file)
        elif isinstance(obj, (tuple, list, set)):
            self.__dprint_TLS(obj, indent=indent, depth=depth, file=file)
        else:
            dprint(self.otherwise_repr(obj))
    def dprint(self, obj, *, indent, depth, file):
        def dprint(*args):
            print(*args, sep='', end='', file=file)
        m = self.may_get_name_args_kwargs(obj)
        if m is None:
            self.__dprint_other_obj(obj, indent=indent, depth=depth, file=file)
            return
        name, args, pairs = m
        dprint(name)
        if not args and not pairs:
            dprint('()')
            return

        first_char = '('
        indents1 = indent*(depth+1)
        depth1 = depth + 1
        for arg in args:
            dprint('\n', indents1, first_char)
            first_char = ','
            self.dprint(arg, indent=indent, depth=depth1, file=file)
        for name, arg in pairs:
            dprint('\n', indents1, first_char, name, ' = ')
            first_char = ','
            self.dprint(arg, indent=indent, depth=depth1, file=file)
        #dprint('\n', indent*depth, ')')
        dprint('\n', indents1, ')')


from seed.types.namedtuple import _ChangeEq, namedtuple

def may_get_name_args_kwargs__for_namedtuple(obj):
    if not isinstance(obj, _ChangeEq):
        return None
    else:
        name = type(obj).__name__
        args = ()
        kwargs = [(attr, getattr(obj, attr)) for attr in obj._fields]
        return name, args, kwargs

easy_print_for_namedtuple = EasyPrint(
        may_get_name_args_kwargs__for_namedtuple, repr)



from collections import UserDict #defaultdict

def may_get_name_args_kwargs__for_AcceptAll(obj):
    if not isinstance(obj, AcceptAll):
        return None
    else:
        return obj.name, obj.args, obj.kwargs

easy_print_for_AcceptAll = EasyPrint(
    may_get_name_args_kwargs__for_AcceptAll, repr)


def _bad_default_factory():
    raise logic-error

class GlobalDict_for_AcceptAll(UserDict, dict):
    def __getitem__(self, key):
        #ls = self.data.setdefault(key, [])
        obj = AcceptAll(key)
            # !!!diff obj for same name!!!
            # since occur at diff position
        #ls.append(obj)
        return obj

class AcceptAll:
    '''
eval an expr
provide a global dict whose __missing__ return AcceptAll(key)

e.g.
    >>> globals = GlobalDict_for_AcceptAll()
    >>> obj = eval('A(B(), n=C())', globals)
    >>> easy_print_for_AcceptAll(obj, indent='    ', depth=0, file=None)
    A
        (B()
        ,n = C()
        )

'''
    def __init__(self, constructor_name):
        self.name = constructor_name
        self.args = None
        self.kwargs = None
    def __call__(__self, *args, **kwargs):
        __self.args = args
        __self.kwargs = tuple(kwargs.items())
        return __self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


