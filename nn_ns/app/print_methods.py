

r'''
E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods --exclude_attrs "get_the_key iter_entities" "get_entity_at"

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods --exclude_attrs "get_the_key iter_entities" "get_entity_at" --exclude_base_names IKeyOrderedTreeNodeOps

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods --exclude_attrs "get_the_key iter_entities" "get_entity_at" --exclude_base_names IKeyOrderedTreeNodeOps IBinaryTreeNodeOps

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods --exclude_attrs "get_the_key iter_entities" "get_entity_at" --exclude_base_names IKeyOrderedUnbalancedMultiWayTreeNodeOps IBinaryTreeNodeOps

E:\my_data\program_source\python3_src\nn_ns\data_structure\RedBlackTreeOps\KeyOrderedTreeNodeOps>print_methods IKeyOrderedBinaryTreeNodeOps IKeyOrderedBinaryTreeNodeOps.py --wrapped_print_methods --exclude_attrs "get_the_key iter_entities" "get_entity_at" --exclude_base_names IKeyOrderedBinaryTreeNodeOps

'''

__all__ = ()

from .guess_package_name import path2package_or_module_name
from seed.helper.print_methods import print_methods, wrapped_print_methods
from seed.pkg_tools.import_object import import_object
from itertools import chain
from collections import defaultdict

def split_exclude_attrs(s):
    attrs = s.split()
    assert all(attr.isidentifier() for attr in attrs)
    return attrs
def is_qname(s):
    return s and s[0] != '.' != s[-1] and all(n.isidentifier() for n in s.split())
def split_exclude_bases(s):
    base_names = s.split()
    assert all(map(is_qname, base_names))
    return base_names

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='print methods of class.')
    parser.add_argument('partial_name', type=str
                        , help='full name of class; e.g. abc.ABC; partial name if given the path')
    parser.add_argument('path', type=str, nargs='?', default=None
                        , help='the path of package_folder or module_file')
    parser.add_argument('--exclude_base_qnames', type=str, nargs='*', default=[]
                        , help='base class qual_names whose methods will be excluded if not overrided')
    parser.add_argument('--exclude_base_names', type=str, nargs='*', default=[]
                        , help='base class basenames whose methods will be excluded if not overrided')
    parser.add_argument('--exclude_attrs', type=str, nargs='*', default=[]
                        , help='attrnames which will be excluded')

    parser.add_argument('--wrapped_print_methods', action='store_true')




    args = parser.parse_args()

    partial_name = args.partial_name
    maybe_path = args.path

    if maybe_path is None:
        qual_name = partial_name
    else:
        path = maybe_path
        prefix = path2package_or_module_name(path)
        if prefix:
            qual_name = '.'.join([prefix, partial_name])
        else:
            qual_name = partial_name
    # qual_name
    del partial_name, maybe_path


    obj = import_object(qual_name)
    if not isinstance(obj, type):
        raise TypeError(f'{qual_name!r} is not a class')
    XXX = cls = obj



    exclude_attrss = args.exclude_attrs
    exclude_attrs = chain.from_iterable(map(split_exclude_attrs, exclude_attrss))
    exclude_basess = args.exclude_base_qnames
    exclude_bases = chain.from_iterable(map(split_exclude_bases, exclude_basess))
    exclude_bases = map(import_object, exclude_bases)


    exclude_base_namess = args.exclude_base_names
    exclude_base_names = chain.from_iterable(map(split_exclude_attrs, exclude_base_namess))

    #base_name2base = {base.__name__ : base for base in XXX.mro()}
    base_name2bases = defaultdict(list)
    for base in XXX.mro():
        base_name2bases[base.__name__].append(base)

    exclude_base_names = set(exclude_base_names) & set(base_name2bases)
    exclude_bases_ex = chain.from_iterable(map(base_name2bases.__getitem__, exclude_base_names))
    exclude_bases = chain(exclude_bases, exclude_bases_ex)



    f = wrapped_print_methods if args.wrapped_print_methods else print_methods
    f(XXX, exclude_attrs=exclude_attrs, exclude_bases=exclude_bases)


if __name__ == "__main__":
    main()


