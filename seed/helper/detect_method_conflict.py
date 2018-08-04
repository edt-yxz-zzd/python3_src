
__all__ = '''
    detect_method_conflict
    print_detect_method_conflict
    wrapped_print_detect_method_conflict
    '''.split()

from itertools import chain
#from pprint import pprint

exclude_attrs_ex = '''
    __doc__
    __dict__
    __init_subclass__
    __module__
    __subclasshook__
    __weakref__

    __abstractmethods__
    _abc_registry
    _abc_cache
    _abc_negative_cache
    _abc_negative_cache_version
    '''.split()


def wrapped_print_detect_method_conflict(*classes
                , exclude_attrs=None
                , exclude=None):
    '''
exclude_attrs += {exclude_attrs_ex}
'''
    if exclude_attrs is None:
        exclude_attrs = exclude_attrs_ex
    else:
        exclude_attrs = chain(exclude_attrs, exclude_attrs_ex)

    print_detect_method_conflict(*classes
                , exclude_attrs=exclude_attrs
                , exclude=exclude)
    return

wrapped_print_detect_method_conflict.__doc__ = \
    wrapped_print_detect_method_conflict.__doc__.format(
        exclude_attrs_ex=exclude_attrs_ex)



def print_detect_method_conflict(*classes
                , exclude_attrs=None
                , exclude=None):
    '''
input:
    classes :: Iter type
    exclude_attrs :: None | Iter str
    exclude :: None | (str -> bool)
        exclude attr?
'''
    exclude_attrs = () if exclude_attrs is None else frozenset(exclude_attrs)
    # exclude :: None | (attr -> bool)
    if exclude is None:
        def exclude(attr:str):
            return False
    else:
        assert callable(exclude)



    conflicts = detect_method_conflict(classes)
    if not conflicts:
        return

    def get_name(cls):
        return cls.__name__.split('.')[-1]

    conflicts = sorted(conflicts)
    prev_conflict_case = ''
    for conflict_case, attr, example_classes, classes in conflicts:
        if exclude(attr) or attr in exclude_attrs:
            continue

        if conflict_case != prev_conflict_case:
            prev_conflict_case = conflict_case
        print(f'{conflict_case}:')

        example_classes = tuple(map(get_name, example_classes))
        classes = list(map(get_name, classes))
        print(f'\t{attr}\n\t\t{example_classes}\n\t\t{classes}')
    return

def are_well_ordered_classes(classes):
    # if A before B, then require not issubclass(B, A)
    # O(n^2)
    classes = list(classes)
    if not all(isinstance(cls, type) for cls in classes): raise TypeError
    while classes:
        after = classes.pop()
        for before in classes:
            if issubclass(after, before): return False
    return True


def detect_method_conflict(classes):
    '''Iter cls -> [(conflict_case, attr, example_classes, classes)]



normally:
    len(classes) == 1
    or classes will be bases of some a cls

let X <: Y =[def]= issubclass(X, Y)
let X has method =[def]= method in X.__dict__
conflict:
    merge_override
        A before B before C
        A <: B
        A <: C
        not (B <: C)

        any X before A, not (X has f)
        A has f
        B has f
        C has f

        then f is merge_override in A

    conflict_override_or_super_depend
        A before B
        not (A <: B)

        any X before A, not (X has f)
        A has f
        B has f

        then f is conflict_override_or_super_depend

'''
    classes = tuple(classes)
    assert are_well_ordered_classes(classes)

    T = type('X', classes, {}) # what if metaclass Error??
    classes = T.__mro__[1:]

    attrs = dir(T)
    attr2classes = {attr:[] for attr in attrs}
    for cls in classes:
        for attr in cls.__dict__:
            ls = attr2classes.get(attr)
            if ls is None:
                continue
            ls.append(cls)

    conflicts = chain.from_iterable(
            detect_method_conflict1(attr, classes)
            for attr, classes in attr2classes.items())
    conflicts = sorted(conflicts)
    return conflicts


def detect_method_conflict1(attr, classes):
    classes = tuple(classes)

    assert are_well_ordered_classes(classes)
    assert all(attr in cls.__dict__ for cls in classes)
    if len(classes) < 2:
        return []

    A = classes[0]
    for B in classes[1:]:
        if not issubclass(A, B):
            return [('conflict_override_or_super_depend', attr, (A, B), classes)]

    for i, B in enumerate(classes[1:], 1):
        for C in classes[i+1:]:
            if not issubclass(B, C):
                return [('merge_override', attr, (A, B, C), classes)]
    return []

