

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
    old_write_lines(fout, lines, line_prefix='\t', line_sep='\n', line_suffix='')

def to_abstract_attr(attr):
    return '`' + attr




exclude_bases_ex = [object, ABC]
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

def wrapped_print_methods(XXX, fout=None
    , *, exclude_bases=None, exclude_attrs=None, exclude=None):
    '''
exclude_bases += {exclude_bases_ex}
exclude_attrs += {exclude_attrs_ex}
'''

    if exclude_bases is None:
        exclude_bases = exclude_bases_ex
    else:
        exclude_bases = chain(exclude_bases, exclude_bases_ex)
    if exclude_attrs is None:
        exclude_attrs = exclude_attrs_ex
    else:
        exclude_attrs = chain(exclude_attrs, exclude_attrs_ex)

    print_methods(XXX, fout=fout
                , exclude_bases=exclude_bases
                , exclude_attrs=exclude_attrs
                , exclude=exclude)
    return
wrapped_print_methods.__doc__ = wrapped_print_methods.__doc__.format(
        exclude_bases_ex=exclude_bases_ex
        , exclude_attrs_ex=exclude_attrs_ex)

def print_methods(XXX, fout=None
    , *, exclude_bases=None, exclude_attrs=None, exclude=None):
    '''

input:
    XXX :: type
    fout :: None | ostream
    exclude_bases :: None | Iter type
    exclude_attrs :: None | Iter str
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
    assert all(isinstance(base, type) for base in exclude_bases)
    assert all(isinstance(attr, str) for attr in exclude_attrs)

    # exclude :: None | (attr -> bool)
    if exclude is None:
        def exclude(attr:str):
            return False
    else:
        assert callable(exclude)

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

