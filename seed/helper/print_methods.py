

__all__ = '''
    print_methods
    wrapped_print_methods
    '''.split()



from seed.str_tools.write_lines import write_lines as old_write_lines
from seed.pkg_tools.import_object import import_object
import sys
from itertools import chain
from abc import ABC



assert hasattr(property, '__isabstractmethod__')
    # ==>> getattr(obj, '__isabstractmethod__', False)
    # instead of hasattr(obj, '__isabstractmethod__')

def is_abstract_method_attr(cls, attr):
    obj = getattr(cls, attr)
    # bug: return hasattr(obj, '__isabstractmethod__')
    return getattr(obj, '__isabstractmethod__', False)







old_print = print
def write_lines(fout, lines):
    old_write_lines(fout, lines, line_prefix=' '*4, line_sep='\n', line_suffix='')
    #old_write_lines(fout, lines, line_prefix='\t', line_sep='\n', line_suffix='')

def to_abstract_attr(attr):
    return '`' + attr




exclude_bases_ex = [object, ABC]
exclude_attrs_ex = '''
    __doc__
    __dict__
    __module__
    __weakref__

    __init_subclass__
    __subclasshook__

    __abstractmethods__
    _abc_registry
    _abc_cache
    _abc_negative_cache
    _abc_negative_cache_version
    _abc_impl
    '''.split()#'''
def __():
    class _B(ABC):
        '...'
        pass
    names = {*dir(_B())}-{*dir(object())}
    return names
if 0:
    print(dir(object()))
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    print(__())
    {'_abc_impl', '__abstractmethods__', '__slots__', '__module__', '__dict__', '__weakref__'}
    print(__() - {*exclude_attrs_ex})
    {'__slots__'}
    print({*exclude_attrs_ex} - __())
    {'__subclasshook__', '_abc_cache', '_abc_negative_cache', '__init_subclass__', '_abc_negative_cache_version', '_abc_registry', '__doc__'}
    raise
exclude_attrs_ex = (__() - {'__slots__'}) | {*r'''
    __doc__
    __dict__
    __module__
    __weakref__
    '''.split()#'''
    }

if 0:
    def wrapped_print_methods(XXX, fout=None
        , *, exclude_bases=None, exclude_attrs=None, exclude=None):
        if not isinstance(XXX, type):
            XXXs = iter(XXX)
        else:
            XXXs = [XXX]
def wrapped_print_methods(*XXXs, fout=None
    , exclude_bases=None, exclude_attrs=None, exclude_prefixes=None, exclude=None, exclude_attrs5listed_in_cls_doc=False):
    # __doc__ SHOULD NOT BE f''
    #   see below: [wrapped_print_methods.__doc__ := .format(...)]
    r'''
exclude_bases += {exclude_bases_ex}
exclude_attrs += {exclude_attrs_ex}
exclude_prefixes += []
'''#'''

    if exclude_bases is None:
        exclude_bases = exclude_bases_ex
    else:
        exclude_bases = chain(exclude_bases, exclude_bases_ex)
    if exclude_attrs is None:
        exclude_attrs = exclude_attrs_ex
    else:
        exclude_attrs = chain(exclude_attrs, exclude_attrs_ex)

    for XXX in XXXs:
        print(f'>>>>>{XXX!r}<<<<<', file=fout)
        print_methods(XXX, fout=fout
                , exclude_bases=exclude_bases
                , exclude_attrs=exclude_attrs
                , exclude_prefixes=exclude_prefixes
                , exclude=exclude
                , exclude_attrs5listed_in_cls_doc=exclude_attrs5listed_in_cls_doc
                )
    return
wrapped_print_methods.__doc__ = wrapped_print_methods.__doc__.format(
        exclude_bases_ex=exclude_bases_ex
        , exclude_attrs_ex=exclude_attrs_ex)

#import re
#re.compile(f'^(?:[ ]{4})?`?\w+$')
def find_attrs5listed_in_cls_doc(exclude_attrs5listed_in_cls_doc, XXX):
    nms5doc4concrete = set()
    nms5doc4abstract = set()
    if not exclude_attrs5listed_in_cls_doc:
        return nms5doc4concrete, nms5doc4abstract

    doc = XXX.__doc__
    if doc is None:
        doc = ''
    nmss = nms5doc4concrete, nms5doc4abstract
    for line in doc.split('\n'):
        ls = line.split()
        if not len(ls) == 1:
            continue
        [s] = ls
        decl_abstract = s[0] == '`'
        if decl_abstract:
            s = s[1:]
        if s.isidentifier():
            nm = s
            nmss[decl_abstract].add(nm)
    return nms5doc4concrete, nms5doc4abstract


def print_methods(XXX, fout=None
    , *, exclude_bases=None, exclude_attrs=None, exclude_prefixes=None, exclude=None, exclude_attrs5listed_in_cls_doc=False):
    '''

input:
    XXX :: type
    fout :: None | ostream
    exclude_bases :: None | Iter type
    exclude_attrs :: None | Iter str
    exclude_prefixes :: None | Iter str
    exclude :: None | (str -> bool)
        exclude attr?

usage:
    class YYY:
        ...

    if __name__ == '__main__':
        XXX = YYY

        from seed.helper.print_methods import print_methods
        print_methods(XXX)

example:
    >>> from abc import abstractmethod
    >>> class B: # neednot ABC for testing
    ...     @abstractmethod
    ...     def aB(self):pass
    ...     def cB(self):pass
    >>> class C(B):
    ...     @abstractmethod
    ...     def aC(self):pass
    ...     def cC(self):pass
    >>> print_methods(C) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    all_methods:
        ...
        `aB
        `aC
        cB
        cC
    new_methods:
        ...
        `aC
        cC
        ...
    abstract_methods:
        `aB
        `aC
    concrete_methods:
        ...
        cB
        cC
    new_abstract_methods:
        `aC
    new_concrete_methods:
        ...
        cC
        ...

    >>> exclude = lambda attr: attr.endswith('__')
    >>> print_methods(C, exclude_bases=(object,), exclude_attrs='__doc__ __module__'.split(), exclude=exclude) # doctest: +NORMALIZE_WHITESPACE
    all_methods:
        `aB
        `aC
        cB
        cC
    new_methods:
        `aC
        cC
    abstract_methods:
        `aB
        `aC
    concrete_methods:
        cB
        cC
    new_abstract_methods:
        `aC
    new_concrete_methods:
        cC

    >>> wrapped_print_methods(C, exclude=exclude) # doctest: +NORMALIZE_WHITESPACE
    all_methods:
        `aB
        `aC
        cB
        cC
    new_methods:
        `aC
        cC
    abstract_methods:
        `aB
        `aC
    concrete_methods:
        cB
        cC
    new_abstract_methods:
        `aC
    new_concrete_methods:
        cC

'''
    assert isinstance(XXX, type)
    exclude_bases = () if exclude_bases is None else tuple(exclude_bases)
    exclude_attrs = () if exclude_attrs is None else frozenset(exclude_attrs)
    exclude_prefixes = () if exclude_prefixes is None else frozenset(exclude_prefixes)
    assert all(isinstance(base, type) for base in exclude_bases)
    assert all(isinstance(attr, str) for attr in exclude_attrs)
    assert all(isinstance(prefix, str) for prefix in exclude_prefixes)

    # exclude :: None | (attr -> bool)
    if exclude is None:
        def exclude(attr:str):
            return False
    else:
        assert callable(exclude)

    ######################
    nms5doc4concrete, nms5doc4abstract = find_attrs5listed_in_cls_doc(exclude_attrs5listed_in_cls_doc, XXX)
    ######################

    if fout is None:
        fout = sys.stdout
    def print(*args, **kwargs):
        old_print(*args, file=fout, **kwargs)
    def print_block_end():
        print()
    def rename(attr):
        if is_abstract_method_attr(XXX, attr):
            return to_abstract_attr(attr)
        return attr

    def include(attr):
        if exclude(attr):
            return False
        if attr in exclude_attrs:
            return False
        if any(attr.startswith(prefix) for prefix in exclude_prefixes):
            return False
        ######################
        if exclude_attrs5listed_in_cls_doc:
            if is_abstract_method_attr(XXX, attr):
                if attr in nms5doc4abstract:
                    return False
            else:
                if attr in nms5doc4concrete:
                    return False
        ######################

        obj = getattr(XXX, attr)
        Nothing = []
        for base in exclude_bases:
            if obj is getattr(base, attr, Nothing):
                return False
        return True

    def new_write_lines(lines):
        lines = filter(include, lines)
        lines = map(rename, lines)
        write_lines(fout, lines)
        print_block_end()

    print('all_methods:')
    #print('\n'.join(dir(XXX)))
    lines = dir(XXX)
    new_write_lines(lines)

    print('new_methods:')
    #print('\n'.join(XXX.__dict__))
    lines = XXX.__dict__
    new_write_lines(lines)

    print('abstract_methods:')
    lines = (n for n in dir(XXX) if is_abstract_method_attr(XXX, n))
    new_write_lines(lines)

    print('concrete_methods:')
    lines = (n for n in dir(XXX) if not is_abstract_method_attr(XXX, n))
    new_write_lines(lines)

    print('new_abstract_methods:')
    lines = (n for n in XXX.__dict__ if is_abstract_method_attr(XXX, n))
    new_write_lines(lines)

    print('new_concrete_methods:')
    lines = (n for n in XXX.__dict__ if not is_abstract_method_attr(XXX, n))
    new_write_lines(lines)


def main(argv=None):
    ## see: nn_ns.app.print_methods.main
    import argparse

    parser = argparse.ArgumentParser(description='print methods of class.')
    parser.add_argument('qual_name', type=str
                        , help='full name of class; e.g. abc.ABC')
    args = parser.parse_args()
    qual_name = args.qual_name

    obj = import_object(qual_name)
    if not isinstance(obj, type):
        raise TypeError(f'{qual_name!r} is not a class')

    XXX = cls = obj
    print_methods(XXX)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    if len(sys.argv) >= 2:
        main()

