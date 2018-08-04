from .canonical_Cartesian_tree_definition import canonical_Cartesian_tree_definition
from .canonical_Cartesian_tree import canonical_Cartesian_tree
from .CanonicalCartesianRightOpenTree import canonical_Cartesian_tree__via_CanonicalCartesianRightOpenTree
from .FreeCanonicalCartesianRightOpenReverseTree import canonical_Cartesian_tree__via_FreeCanonicalCartesianRightOpenReverseTree
from sys import stderr

fs =[ canonical_Cartesian_tree__via_FreeCanonicalCartesianRightOpenReverseTree
    , canonical_Cartesian_tree__via_CanonicalCartesianRightOpenTree
    , canonical_Cartesian_tree
    ]


def print_err(x):
    print(x, file=stderr)
def test_canonical_Cartesian_tree(array):
    f = canonical_Cartesian_tree_definition
    array = tuple(array)
    ans = f(array)
    for f in fs:
        ans2 = f(array)
        if ans != ans2:
            print_err(array)
            print_err(f)
            print_err(ans)
            print_err(ans2)
            assert ans == ans2


def test():
    from itertools import chain, product
    import random
    chains = chain.from_iterable

    data = [[], [1], [1,2], [2,2], [2,1]
        ] + [[random.randint(0, 10) for _ in range(9)] for _ in range(1000)
        ]
    data.extend(chains(product(range(n), repeat=n) for n in range(4)))
    data.extend(chains(product(range(3), repeat=r) for r in range(4)))

    for array in data:
        test_canonical_Cartesian_tree(array)

test()





