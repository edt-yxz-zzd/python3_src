

from seed.tiny import fst
from .list_all_orders_of_finite_simple_groups_lt import (
    list_all_orders_of_finite_simple_groups_lt__without_repetition
    ,list_all_shared_orders_of_finite_simple_groups_lt__without_repetition
    ,_inplace_mk_name__order_parameterized_names_pairs
    )
def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='show info about orders of finite simple groups'
        , epilog='''
format per line (non-verbose):
    group_order is_order_shared [group_name]
  e.g.
    60 False ['Alt[5]', 'A[1](4)', 'A[1](5)']
    20160 True ['Alt[8]', 'A[2](4)', 'A[3](2)']
  meaning:
    False - there are only one simple group of order 60
        ['Alt[5]', 'A[1](4)', 'A[1](5)'] are diff names for same group
    True - there are two simple groups of order 20160
        Alt[8] == A[3](2) != A[2](4)
format per line (verbose):
    group_order is_order_shared [(group_name, family_long_name, family_short_name, argument_dict)]

'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('upper_bound', type=int
                        #, required=True
                        , help='upper_bound of ouput group order')
    parser.add_argument('--with_cyclic', action='store_true'
                        , default = False
                        , help='include orders of cyclic simple groups; excluded by default')
    parser.add_argument('--only_shared_orders', action='store_true'
                        , default = False
                        , help='output orders where there are more than one groups')
    parser.add_argument('-py', '--show_as_python_object', action='store_true'
                        , default = False
                        , help='show the final result as python object')
    parser.add_argument('--verbose', action='store_true'
                        , default = False
                        , help='show detail')


    args = parser.parse_args(args)
    output = make_main_result(args.upper_bound
        ,only_shared_orders = args.only_shared_orders
        ,with_cyclic = args.with_cyclic
        ,to_group_name = True
        )

    if args.verbose:
        def extract_ls(ls):
            return ls
    else:
        def extract_ls(ls):
            return [xname for xname, long, short, args in ls]

    if args.show_as_python_object:
        print(output)
    else:
        for order, is_shared, ls in output:
            print(order, is_shared, extract_ls(ls))
    return

def make_main_result(upper_bound, *
    , only_shared_orders:bool, with_cyclic:bool, to_group_name:bool
    ):
    only_shared_orders = bool(only_shared_orders)
    with_cyclic = bool(with_cyclic)
    to_group_name = bool(to_group_name)

    # __w - with_parameterized_names
    shared_orders__w = list_all_shared_orders_of_finite_simple_groups_lt__without_repetition(upper_bound, with_parameterized_names=True)
    if only_shared_orders:
        orders__w = shared_orders__w
    else:
        orders__w = list_all_orders_of_finite_simple_groups_lt__without_repetition(
            upper_bound
            ,with_cyclic = with_cyclic
            ,with_parameterized_names = True
            )

    orders__w; shared_orders__w
    shared_order_set = set(map(fst, shared_orders__w))

    long_short_arg_tripless = []
        # [[(family_long_name, family_short_name, argument_dict)]]
    for order, parameterized_names in orders__w:
        long_short_arg_triples = []
        for aEval, argument_dict in parameterized_names:
            family_long_name = aEval.get_family_long_name()
            family_short_name = aEval.get_family_short_name()
            triple = family_long_name, family_short_name, argument_dict
            long_short_arg_triples.append(triple)
        long_short_arg_tripless.append(long_short_arg_triples)

    if to_group_name:
        _inplace_mk_name__order_parameterized_names_pairs(orders__w)

    output = []
        # [(order, is_shared, [(parameterized_name, family_long_name, family_short_name, argument_dict)])]
        # [(UInt, Bool, [(parameterized_name, String, String, argument_dict)]]
        # [(UInt, Bool, [(String, String, String, argument_dict)]]
        # [(UInt, Bool, [((aEval, argument_dict), String, String, argument_dict)]]
    for (order, parameterized_names), long_short_arg_triples in zip(orders__w, long_short_arg_tripless):
        is_shared = order in shared_order_set
        ls = [(xname, long, short, args)
            for xname, (long, short, args)
            in zip(parameterized_names, long_short_arg_triples)
            ]
        output.append((order, is_shared, ls))
    return output


if __name__ == "__main__":
    main()


