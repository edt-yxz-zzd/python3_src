

'''
test all submodules/subpackages of a package
'''

__all__ = '''
    doctest_all
    '''.split()

from importlib import import_module
from doctest import testmod
from seed.pkg_tools.iter_submodules import iter_submodules
from seed.helper.find_bases_without_slots import print_bases_without_slots


def is_defined_in(cls, module_object):
    qname = cls.__module__
    r = qname == module_object.__name__
    '''
    if issubclass(cls, tuple) and r:
        print(module_object, qname)
        print(cls)
        raise logic-error
    '''
    return r

def iter_classes_of_module(module_object):
    for attr in dir(module_object):
        obj = getattr(module_object, attr)
        if isinstance(obj, type):
            yield obj
    return

def doctest_all(package_or_qname, *
        , recursive:bool
        , list_qnames=False # module_qual_name
        , list_classes_without_slots=True
        , filter_classes_if_defined_in_this_module=True
            # when list_classes_without_slots is True
        , **kwargs)->None:
    '''
input:
    package_or_qname :: pkg_obj | str
    recursive :: bool

    kwargs
        see: doctest.testmod(m, verbose=None, report=True, optionflags=0, raise_on_error=False, exclude_empty=False)
output:
    does_success

'''
    list_qnames = bool(list_qnames)
    list_classes_without_slots = bool(list_classes_without_slots)
    filter_classes_if_defined_in_this_module = bool(filter_classes_if_defined_in_this_module)

    if list_qnames:
        def show_qname(m):
            print(m.__name__)
    else:
        def show_qname(m):pass

    if list_classes_without_slots:
        classes = set()
        if not filter_classes_if_defined_in_this_module:
            def collect_classes_of_module(m):
                classes.update(iter_classes_of_module(m))
        else:
            def collect_classes_of_module(m):
                classes.update(cls for cls in iter_classes_of_module(m)
                    if is_defined_in(cls, m))
    else:
        def collect_classes_of_module(m):pass

    for m in iter_submodules(package_or_qname, recursive=recursive):
        collect_classes_of_module(m)
        show_qname(m)
        (failure_count, test_count) = testmod(m, **kwargs)
        if failure_count:
            return False

    if list_classes_without_slots:
        # tuple may be introduced by namedtuple
        print_bases_without_slots(*classes)
    return True

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='doctest all submodules/subpackages')
    parser.add_argument('package_qname', type=str, help='package qual_name')
    parser.add_argument('-v', '--verbose', action='store_true'
                        , default=False
                        , help='see: doctest.testmod')
    parser.add_argument('--not_report', action='store_true'
                        , default=False
                        , help='see: doctest.testmod')
    parser.add_argument('--optionflags', type=int
                        , default=0
                        , help='see: doctest.testmod')
    parser.add_argument('--raise_on_error', action='store_true'
                        , default=False
                        , help='see: doctest.testmod')
    parser.add_argument('--exclude_empty', action='store_true'
                        , default=False
                        , help='see: doctest.testmod')

    parser.add_argument('-r', '--recursive', action='store_true'
                        , default=False
                        , help='recursive or only direct children')
    parser.add_argument('-l', '--list_qnames', action='store_true'
                        , default=False
                        , help='show qnames')
    args = parser.parse_args(argv)

    if True:
        package_qname = args.package_qname
        verbose = args.verbose
        not_report = args.not_report
        optionflags = args.optionflags
        raise_on_error = args.raise_on_error
        exclude_empty = args.exclude_empty

        recursive = args.recursive
        list_qnames = args.list_qnames


    report = not not_report
    pkg_obj = import_module(package_qname)
    doctest_all(pkg_obj
            , recursive=recursive
            , verbose=verbose
            , report=report
            , optionflags=optionflags
            , raise_on_error=raise_on_error
            , exclude_empty=exclude_empty
            , list_qnames = list_qnames
            )

    return 0


if __name__ == '__main__':
    main()

