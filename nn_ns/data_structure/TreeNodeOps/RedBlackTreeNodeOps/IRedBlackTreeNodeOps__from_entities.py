

'''

[black_height_of_whole_tree >= 1][BLACK root][num_entities >= 0]
    [(ceil_log2(num_entities+1)+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities+1)]
    proof:
    min_num_entities_of_whole_tree
        # tree_height = black_height_of_whole_tree
        # max_nonleaf_height = black_height_of_whole_tree-1
        = sum 2^i {i=0..black_height_of_whole_tree-2}
        = -1 + 2^(black_height_of_whole_tree-1)
        black_height_of_whole_tree      = 1 2 3 4 5
        min_num_entities_of_whole_tree  = 0 1 3 7 15
    max_num_entities_of_whole_tree
        # tree_height = 2*black_height_of_whole_tree-1
        # max_nonleaf_height = 2*black_height_of_whole_tree-2
        = sum 2^i {i=0..2*black_height_of_whole_tree-3}
        = -1 + 2^(2*black_height_of_whole_tree-2)
        = -1 + 4^(black_height_of_whole_tree-1)
        black_height_of_whole_tree      = 1 2 3
        max_num_entities_of_whole_tree  = 0 3 15
    min_num_entities_of_whole_tree
        <= num_entities <= max_num_entities_of_whole_tree
    -1 + 2^(black_height_of_whole_tree-1)
        <= num_entities <= -1 + 4^(black_height_of_whole_tree-1)
    black_height_of_whole_tree-1
        <= log2(num_entities+1)
        <= (black_height_of_whole_tree-1)*2
    log2(num_entities+1)/2
        <= black_height_of_whole_tree-1
        <= log2(num_entities+1)

    (ceil_log2(num_entities+1)+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities+1)
        num_entities                    = 0 1 2 3 4 5 6 7 8 ... 14 15 16 31
        min_black_height_of_whole_tree  = 1 2 2 2 3 3 3 3 3 ... 3  3  4  4
        max_black_height_of_whole_tree  = 1 2 2 3 3 3 3 4 4 ... 4  5 ... 6

[black_height_of_whole_tree >= 1][RED root][num_entities >= 1][num_entities != 2]
    # root should be BLACK
    # but temp root which will be a child, can be red
    [(ceil_log2(num_entities+1)+2)//2
        <= black_height_of_whole_tree
        <= floor_log2(num_entities+1)]

    proof:
    min_num_entities_of_whole_tree' = 1+2*min_num_entities_of_whole_tree
    max_num_entities_of_whole_tree' = 1+2*max_num_entities_of_whole_tree
    num_entities' = (num_entities-1)/2
    num_entities'' = (num_entities+1)/2

    (ceil_log2(num_entities'+1)+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities'+1)

    (ceil_log2(num_entities'')+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities'')

    (ceil_log2(num_entities+1))//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities+1)-1

    (ceil_log2(num_entities+1)+2)//2
        <= black_height_of_whole_tree
        <= floor_log2(num_entities+1)
        num_entities                    = 1 2 3 4 5 6 7 8 ... 14 15 31 32
        min_black_height_of_whole_tree  = 1 2 2 2 2 2 2 3 ... 3  3  3  4
        max_black_height_of_whole_tree  = 1 1 2 2 2 2 3 3 ... 3  4
'''

__all__ = '''
    red_black_tree__from_entities
    '''.split()

from seed.math.floor_ceil import floor_log2, ceil_log2, floor_div, ceil_div

def num_entities2black_height_of_whole_tree_range__black_root(num_entities):
    m = num_entities2min_black_height_of_whole_tree__black_root(num_entities)
    M = num_entities2max_black_height_of_whole_tree__black_root(num_entities)
    return m, M

def num_entities2black_height_of_whole_tree_range__red_root(num_entities):
    m = num_entities2min_black_height_of_whole_tree__red_root(num_entities)
    M = num_entities2max_black_height_of_whole_tree__red_root(num_entities)
    return m, M

def num_entities2min_black_height_of_whole_tree__black_root(num_entities):
    '''
[black_height_of_whole_tree >= 1][BLACK root][num_entities >= 0]
    [(ceil_log2(num_entities+1)+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities+1)]
'''
    assert num_entities >= 0
    # 1 + (ceil_log2(num_entities+1)+1)//2
    return 1 + (ceil_log2(num_entities+1)+1)//2
def num_entities2max_black_height_of_whole_tree__black_root(num_entities):
    '''
[black_height_of_whole_tree >= 1][BLACK root][num_entities >= 0]
    [(ceil_log2(num_entities+1)+1)//2
        <= black_height_of_whole_tree-1
        <= floor_log2(num_entities+1)]
'''
    assert num_entities >= 0
    # 1 + floor_log2(num_entities+1)
    return 1 + floor_log2(num_entities+1)


def num_entities2min_black_height_of_whole_tree__red_root(num_entities):
    '''
[black_height_of_whole_tree >= 1][RED root][num_entities >= 1][num_entities != 2]
    [(ceil_log2(num_entities+1)+2)//2
        <= black_height_of_whole_tree
        <= floor_log2(num_entities+1)]
'''
    assert num_entities >= 1 and num_entities != 2
    # (ceil_log2(num_entities+1)+2)//2
    return (ceil_log2(num_entities+1)+2)//2
def num_entities2max_black_height_of_whole_tree__red_root(num_entities):
    '''
[black_height_of_whole_tree >= 1][RED root][num_entities >= 1][num_entities != 2]
    [(ceil_log2(num_entities+1)+2)//2
        <= black_height_of_whole_tree
        <= floor_log2(num_entities+1)]
'''
    assert num_entities >= 1 and num_entities != 2
    # floor_log2(num_entities+1)
    return floor_log2(num_entities+1)



def split_num_entities(
        num_entities, pseudo_parent_is_black, black_height_of_subtree:[None, int]):
    # -> (black_height_of_subtree::int, subtree_root_is_black::bool, num_entities0, num_entities1) | raise ValueError
    assert num_entities >= 0
    assert black_height_of_subtree is None or black_height_of_subtree >= 1
    num_entities0 = (num_entities-1)//2
    num_entities1 = num_entities - 1 - num_entities0
    assert 0 <= num_entities0 <= num_entities1 < num_entities
    assert 0 <= num_entities1 - num_entities0 <= 1


    # try BLACK first
    subtree_root_is_black = None
    m, M = num_entities2black_height_of_whole_tree_range__black_root(
                num_entities)
    if black_height_of_subtree is None:
        black_height_of_subtree = M

    if m <= black_height_of_subtree <= M:
        subtree_root_is_black = True
    elif pseudo_parent_is_black and num_entities >= 1 and num_entities != 2:
        # subtree_root can be RED
        # try RED
        m, M = num_entities2black_height_of_whole_tree_range__red_root(
                num_entities)
        if m <= black_height_of_subtree <= M:
            subtree_root_is_black = False

    if subtree_root_is_black is None:
        raise ValueError(
                f'black_height_of_subtree={black_height_of_subtree} not suit for num_entities={num_entities}')

    assert num_entities0 + 1 + num_entities1 == num_entities
    return black_height_of_subtree, subtree_root_is_black, num_entities0, num_entities1

r = split_num_entities(
        num_entities=3
        , pseudo_parent_is_black=False
        , black_height_of_subtree=None)


def red_black_tree__from_entities(ops, num_entities, entities, *
            , pseudo_parent_is_black=False
            , black_height_of_subtree=None # >= 1
            , more_than_num_entities=False
            , reverse=False
            ):
    ''' -> (black_height_of_subtree, subtree)

requires:
    ops.make_root_leaf
    ops.make_root_nonleaf
    ops.get_RED
    ops.get_BLACK
    ops.check_red_black_tree_properties

input:
    more_than_num_entities :: bool
        if more_than_num_entities:
            assert len(entities) >= num_entities
        else:
            assert len(entities) == num_entities

    pseudo_parent_is_black :: bool
        if pseudo_parent_is_black:
            root may be RED
        else:
            root must be BLACK

    black_height_of_subtree :: None | PInt

    reverse :: bool
        reverse entities

output:
    black_height_of_subtree::PInt
    subtree :: Node<ops>
        subtree.root.color may be RED
    OR raise ValueError

'''
    assert black_height_of_subtree is None or black_height_of_subtree >= 1
    it = iter(entities); del entities
    pseudo_parent_is_black = bool(pseudo_parent_is_black)
    more_than_num_entities=bool(more_than_num_entities)
    reverse=bool(reverse)


    make_root_leaf = ops.make_root_leaf
    make_root_nonleaf = ops.make_root_nonleaf
    BLACK = ops.get_BLACK()
    RED = ops.get_RED()
    check_red_black_tree_properties = ops.check_red_black_tree_properties

    def this(num_entities, pseudo_parent_is_black, black_height_of_subtree):
        # (black_height_of_subtree, subtree may with red root)
        if num_entities == 0:
            if black_height_of_subtree is None:
                black_height_of_subtree = 1
            elif black_height_of_subtree != 1:
                raise ValueError('leaf should have black_height_of_subtree 1')
            return black_height_of_subtree, make_root_leaf()

        (black_height_of_subtree, subtree_root_is_black
            , num_entities0, num_entities1) = \
                split_num_entities(
                    num_entities
                    , pseudo_parent_is_black
                    , black_height_of_subtree)

        subtree_root_is_black = bool(subtree_root_is_black)
        black_height_of_subtree_child = black_height_of_subtree - subtree_root_is_black

        color = BLACK if subtree_root_is_black else RED
        black_height_of_left_child, left_child = this(\
          num_entities0, subtree_root_is_black, black_height_of_subtree_child)
        entity = next(it) # may StopIteration
        black_height_of_right_child, right_child = this(\
          num_entities1, subtree_root_is_black, black_height_of_subtree_child)

        if black_height_of_left_child != black_height_of_right_child:
            raise logic-error
        elif black_height_of_left_child != black_height_of_subtree_child:
            raise logic-error

        if reverse:
            left_child, right_child = right_child, left_child
        subtree = make_root_nonleaf(color, entity, left_child, right_child)
        return black_height_of_subtree, subtree

    try:
        r = this(num_entities, pseudo_parent_is_black, black_height_of_subtree)
    except StopIteration:
        raise ValueError(f'num_entities == {num_entities} > len(entities)')

    if not more_than_num_entities:
        for _ in it:
            raise ValueError(f'num_entities == {num_entities} < len(entities)')

    black_height_of_subtree, subtree = r

    as_root = not pseudo_parent_is_black
    check_red_black_tree_properties(subtree, as_root)
    return black_height_of_subtree, subtree


