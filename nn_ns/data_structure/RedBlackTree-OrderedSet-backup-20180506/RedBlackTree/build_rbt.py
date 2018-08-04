
'''

// how to reconstruct a given red-black-tree 
//    using only insert_at_leaf/remove_leaf_and_its_parent
//    begin from an empty tree (i.e. leaf_root)??

'''


__all__ = '''

    build_rbt
    apply_op_ls

    oriented_tree_struct_le
    red_black_tree_struct_color_eq
    check_red_black_tree_properties
    holds_red_black_tree_properties

    make_TupleBoth_MostBaised_RBT
    make_TupleBoth_AllBlack_RBT

    _refresh_up_down
    get_directions
    get_attr_path
    get_node
    NeedTrinodeRestructorError
    node2sub_nonleaf_paths
'''.split()

from operator import attrgetter
from .RedBlackTreeNodeABC import \
     MutableRedBlackTreeNodeABC, \
     RBT_Node_TupleBothPlainParented as Node,\
     RBT_Node_TupleBothPlainParented_ABC as NodeABC
from seed.variables import null_iterable

def holds_red_black_tree__RootProperty(root):
    if not root.is_root():
        raise ValueError('not root')
    return root.is_black()

def holds_red_black_tree__ExternalProperty(node):
    # return True # since leaf contains no data
    if node.is_leaf():
        return node.is_black()
    return all(map(holds_red_black_tree__ExternalProperty, node.children))

def holds_red_black_tree__InternalProperty(node):
    if node.is_leaf():
        return True
    if node.is_red():
        if not all(child.is_black() for child in node.children):
            return False
    return all(map(holds_red_black_tree__InternalProperty, node.children))

def get_all_black_depthes(node):
    if node.is_leaf():
        return {node2self_black_count(node)}
    lds, rds = map(get_all_black_depthes, node.children)
    depthes = lds | rds
    if node.is_black():
        depthes = set(d+1 for d in depthes)
    return depthes

def node2self_black_count(node):
    return int(bool(node.is_black()))

def get_one_black_depth(node):
    return node2self_black_count(node) + \
           (0 if node.is_leaf() else get_one_black_depth(node.left))
    
def holds_red_black_tree__DepthProperty(node):
    return len(get_all_black_depthes(node)) == 1

def holds_red_black_tree_properties(root):
    fs = (holds_red_black_tree__RootProperty,
          holds_red_black_tree__ExternalProperty,
          holds_red_black_tree__InternalProperty,
          holds_red_black_tree__DepthProperty)
    return all(f(root) for f in fs)


def check_red_black_tree_properties(root):
    '''
    
    Root Property:
        The root is black.
    External Property:
        Every external node is black.
    Internal Property:
        The children of a red node are black.
    Depth Property:
        All the external nodes have the same black depth,
        defined as the number of black ancestors minus one.
        (Recall that a node is an ancestor of itself.)
'''
    assert isinstance(root, MutableRedBlackTreeNodeABC)
    assert holds_red_black_tree_properties(root)
    










def make_TupleBoth_AllBlack_RBT(black_height, entity=1, Node=Node):
    assert issubclass(Node, NodeABC)
    plain = make_plain__TupleBoth_AllBlack_RBT(black_height, entity=entity, Node=Node)
    return Node.from_root_plain_node(plain)
def make_TupleBoth_MostBaised_RBT(black_height, entity=1, Node=Node):
    assert issubclass(Node, NodeABC)
    plain = make_plain__TupleBoth_MostBaised_RBT(black_height, entity=entity, Node=Node)
    return Node.from_root_plain_node(plain)



def make_plain__TupleBoth_AllBlack_RBT(black_height, entity=1, Node=Node):
    assert issubclass(Node, NodeABC)
    if black_height < 1:
        raise ValueError('black_height < 1')
    if black_height == 1:
        return Node.PLAIN_LEAF
    left = right = make_plain__TupleBoth_AllBlack_RBT(black_height-1, entity=entity, Node=Node)
    return (Node.BLACK, entity, left, right)
def make_plain__TupleBoth_MostBaised_RBT(black_height, entity=1, Node=Node):
    assert issubclass(Node, NodeABC)
    if black_height < 1:
        raise ValueError('black_height < 1')
    if black_height == 1:
        return Node.PLAIN_LEAF
    left = right_left = make_plain__TupleBoth_AllBlack_RBT(black_height-1, entity=entity, Node=Node)
    right_right = make_plain__TupleBoth_MostBaised_RBT(black_height-1, entity=entity, Node=Node)
    right = (Node.RED, entity, right_left, right_right)
    return (Node.BLACK, entity, left, right)




def _test_make_plain__TupleBoth_MostBaised_RBT():
    plain = make_plain__TupleBoth_MostBaised_RBT(5)
    root = Node.from_root_plain_node(plain)
    assert root.left.oriented_subtree_eq(root.right.left)

def _test_target_tree2raw_tree():
    plain = make_plain__TupleBoth_MostBaised_RBT(5)
    root = Node.from_root_plain_node(plain)
    op_ls, new_root = target_tree2raw_tree(root)
    #print(op_ls)















class NeedTrinodeRestructorError(Exception):pass



def apply_op_ls(root, op_ls):
    '''op_ls :: [(insert, entity, leaf_path)|(remove, leaf_path)]
where path is a string of s.t. rex'|\w+(.\w+)*'
'''
    insert = insert_at_leaf__without_trinode_restructure
    remove = remove_leaf_and_its_parent__without_trinode_restructure
    for op in op_ls:
        action = op[0]
        if action == 'insert':
            _, entity, path = op
            leaf = get_node(root, path)
            assert leaf.is_leaf()
            root = insert(leaf, entity)
        elif action == 'remove':
            _, path = op
            leaf = get_node(root, path)
            assert leaf.is_leaf()
            root = remove(leaf)
        else:
            raise...
    return root



def build_rbt(target):
    # :: rbt<...> -> ([op], rbt<TuplePlainParented>)
    # let op_ls, new = build_rbt(target)
    # assert apply_op_ls(new.make_leaf_root(), op_ls) == new
    # assert red_black_tree_struct_color_eq(new, target)
    assert isinstance(target, MutableRedBlackTreeNodeABC)
    op_ls, raw = target_tree2raw_tree(target)
    assert oriented_tree_struct_le(target, raw)
    
    black_depth = get_one_black_depth(target)
    op_ls, raw = set_raw_tree_black_depth(op_ls, raw, black_depth)
    assert get_one_black_depth(raw) == get_one_black_depth(target)
    
    op_ls, raw = set_raw_tree_color_as_target_tree(op_ls, raw, target)
    op_ls, raw = remove_useless_bottom_red_nodes(op_ls, raw, target)

    # test red_black_tree_struct_color_eq
    assert red_black_tree_struct_color_eq(target, target)
    # test raw == target
    assert red_black_tree_struct_color_eq(raw, target)

    # test empty_tree+op_ls ==>> raw
    new = Node.make_leaf_root()
    new = apply_op_ls(new, op_ls)
    assert new.oriented_subtree_eq(raw)
    return op_ls, raw

def _test_build_rbt():
    from pprint import pprint as print
    target = make_TupleBoth_AllBlack_RBT(5)
    op_ls, raw = build_rbt(target)
    #print(op_ls)
    
    target = make_TupleBoth_MostBaised_RBT(5)
    op_ls, raw = build_rbt(target)
    #print(op_ls)

    plain = (Node.BLACK, 7, (Node.BLACK, 3, (Node.BLACK, 1, Node.PLAIN_LEAF, (Node.RED, 2, Node.PLAIN_LEAF, Node.PLAIN_LEAF)), (Node.RED, 5, (Node.BLACK, 4, Node.PLAIN_LEAF, Node.PLAIN_LEAF), (Node.BLACK, 6, Node.PLAIN_LEAF, Node.PLAIN_LEAF))), (Node.BLACK, 9, (Node.BLACK, 8, Node.PLAIN_LEAF, Node.PLAIN_LEAF), (Node.BLACK, 10, Node.PLAIN_LEAF, Node.PLAIN_LEAF)))
    target = Node.from_root_plain_node(plain)
    op_ls, raw = build_rbt(target)
    














    

def oriented_tree_struct_le(self, other):
    # can embed self in other??
    # partial order
    # donot consider node properties
    if self.is_leaf():
        return True
    if other.is_leaf():
        return False
    if self.num_children > other.num_children:
        return False
    return all(oriented_tree_struct_le(a, b)
               for a, b in zip(self.iter_children(), other.iter_children()))


        
    


def red_black_tree_struct_color_eq(self, other):
    if self.is_leaf():
        return other.is_leaf()
    if other.is_leaf():
        return False
    
    if bool(self.is_red()) != bool(other.is_red()): # bug: "other.is_red" without "()"
        return False
    
    f = red_black_tree_struct_color_eq
    return f(self.left, other.left) and f(self.right, other.right)



def _refresh_up_down(node):
    path = get_attr_path(node)
    root = node.fixed_the_only_broken_above_until_root()
    node = get_node(root, path)
    return node


def get_directions(node):
    ds = []
    while not node.is_root():
        ds.append(node.direction)
        node = node.parent
    ds.reverse()
    return ds
def get_attr_path(node):
    ds = get_directions(node)
    attr_path = ''.join('.left' if d == node.LEFT
                        else '.right' for d in ds) # directions2attr_path(ds)
    return attr_path[1:]

def get_node(root, path):
    try:
        return attrgetter(path)(root) if path else root
    except:
        print(path)
        print(root)
        print(root.underlying)
        raise



    
    

def node2sub_nonleaf_paths(node):
    'return {"", "left", "right", "left.left", ...}'
    nonleaf_paths = ['']
    if node.is_leaf():
        return set() # bug: once return []/{} instead of set()
    #nonleaf_paths.add('')
    
    ancestors = [node.iter_children()]
    attr_path = ['']
    while ancestors:
        for child in ancestors[-1]:
            if not child.is_leaf():
                break
        else:
            
            ancestors.pop()
            attr_path.pop()
            continue # bug: forgot "continue"
    
        ancestors.append(child.iter_children())
        attr_path.append('.left' if child.is_left() else '.right')
        nonleaf_paths.append(''.join(attr_path)) # in prefix_order

    # cut off prefix '.'
    return set(path[1:] for path in nonleaf_paths)


































def target_tree2raw_tree(target):
    op_ls, root = _target_tree2raw_tree(target)

    # check root >= target
    nonleaf_paths = node2sub_nonleaf_paths(target)
    assert not any(get_node(root, path).is_leaf() for path in nonleaf_paths)

    # check empty_tree + op_ls ==>> root
    new = Node.make_leaf_root()
    new = apply_op_ls(new, op_ls)
    assert new.oriented_subtree_eq(root)
    return op_ls, root

def _target_tree2raw_tree(target):
    '''return ([insert op], new_root)

TargetTree = () | (bool is_black, TargetTree left, TargetTree right)

RawTree = replace some leaves of target tree by subtrees and random recolored

'''
    assert target.is_root()
    check_red_black_tree_properties(target) # invariant
    # iter_red_black_tree_nonleaves()
    nonleaf_paths = node2sub_nonleaf_paths(target)

    new = Node.make_leaf_root()
    if not nonleaf_paths:
        return [], new
    root = new

    insert = insert_at_leaf__without_trinode_restructure
    # path not startswith '.'

    op_ls = []
    def get_entity(path, old_tree_paths):
        entity = 1 if path in old_tree_paths else -1
        return entity
    def add_insert_op(op_ls, entity, path):
        op_ls.append(('insert', entity, path))
    
    assert get_node(root, '').is_leaf()
    
    def on_new_inserted_path(path, old_tree_paths, handled_paths, next_round):
        assert path not in handled_paths
        handled_paths.add(path)
        for more in ('.left', '.right') if path else ('left', 'right'):
            child = path + more
            if child in old_tree_paths and child not in handled_paths:
                next_round.add(child)
    def process_path(root, path, old_tree_paths,
                     handled_paths, next_round, op_ls):
        assert path in old_tree_paths and path not in handled_paths
        leaf = get_node(root, path)
        entity = get_entity(path, old_tree_paths)
        try:
            root = insert(leaf, entity)
        except NeedTrinodeRestructorError:
            # fail
            next_round.add(path)
        else:
            add_insert_op(op_ls, entity, path)
            on_new_inserted_path(path, old_tree_paths, handled_paths, next_round)
        return root
    def handle_dead_lock(root, path, old_tree_paths, handled_paths, op_ls):
        # path not in old_tree_paths with entity == -1
        # otherwise +1
        assert path in old_tree_paths
        assert path not in handled_paths
        leaf = get_node(root, path)
        try:
            insert(leaf, Exception) # must fail
        except NeedTrinodeRestructorError as e:
            # fail
            
            # bug:
            #   follow black_uncle contains the new node with entity Exception!
            black_uncle_with_modified_parent, = e.args
            black_uncle_path = get_attr_path(black_uncle_with_modified_parent)
            black_uncle = get_node(root, black_uncle_path)
            begin = len(op_ls)
            red_uncle = to_red(black_uncle, old_tree_paths, op_ls)
            another_root = red_uncle.fixed_the_only_broken_above_until_root()
            root = apply_op_ls(root, op_ls[begin:])
            try:
                assert root.underlying == another_root.underlying
            except:
                from pprint import pprint as print
                print(root.underlying[0])
                print(another_root.underlying[0])
                raise

            new_inserted_paths = set(path for _, _, path in op_ls[begin:])
            new_inserted_old_paths = old_tree_paths & new_inserted_paths
            return new_inserted_old_paths, root, black_uncle_path
        else: raise ...

    def to_red(node, old_tree_paths, op_ls):
        'grey ==>> red by insert...'
        if node.is_leaf():
            path = get_attr_path(node)
            entity = get_entity(path, old_tree_paths)
            root = insert(node, entity)
            add_insert_op(op_ls, entity, path)
            node = get_node(root, path)
            assert node.is_red()
            return node
        if node.is_red():
            return node
        node = to_red(node.left, old_tree_paths, op_ls).parent
        node = to_red(node.right, old_tree_paths, op_ls).parent
        node = push_down_black(node, old_tree_paths, op_ls)
        assert node.is_red()
        return node

    def push_down_black(node, old_tree_paths, op_ls):
        '(black, (red...), (red...)) ==>> (red, (black...), (black...)) by insert...'
        assert not node.is_leaf()
        assert node.is_black()
        assert node.left.is_red()
        assert node.right.is_red()
        node = to_red(node.left.left, old_tree_paths, op_ls).parent.parent
        assert node.is_red()
        assert node.left.is_black()
        assert node.right.is_black()
        assert node.left.left.is_red()
        return node
    
        
    prev_round = set()
    curr_round = {''}
    handled_paths = set()
    root = new
    while curr_round:
        if curr_round == prev_round:
            # dead-lock
            path = curr_round.pop()
            assert path not in curr_round
            assert path not in handled_paths
            prev_black_uncle_path_len = float('inf')
            while True:
                assert path not in curr_round
                new_inserted_old_paths, root, black_uncle_path = handle_dead_lock(root, path, nonleaf_paths, handled_paths, op_ls)
                curr_black_uncle_path_len = len(black_uncle_path.split('.'))
                assert curr_black_uncle_path_len < prev_black_uncle_path_len
                prev_black_uncle_path_len = curr_black_uncle_path_len

                
                #assert new_inserted_old_paths.isdisjoint(handled_paths)
                for new_path in new_inserted_old_paths:
                    on_new_inserted_path(new_path, old_tree_paths, handled_paths, curr_round)
                curr_round -= new_inserted_old_paths
                #assert curr_round.isdisjoint(handled_paths)
                #assert curr_round <= nonleaf_paths
                assert path not in new_inserted_old_paths
                assert path not in handled_paths
                assert path not in curr_round
                try:
                    root = process_path(root, path, nonleaf_paths, handled_paths, curr_round, op_ls)
                except:
                    #raise
                    assert path in set(path for _, path in op_ls)
                    print(path)
                    print(op_ls)
                    print(get_node(root, path).underlying[0])
                    raise
                
                if path not in curr_round:
                    break
                curr_round.remove(path) # bug: forgot remove "path"

                
            assert path not in curr_round
            assert path in handled_paths
            #assert curr_round != prev_round
        assert curr_round != prev_round
        #assert curr_round.isdisjoint(handled_paths)
        #assert curr_round <= nonleaf_paths
        
        to_process = curr_round.copy()
        next_round = set()

        while to_process:
            path = to_process.pop()
            
            try:
                root = process_path(root, path, nonleaf_paths, handled_paths, next_round, op_ls)
            except:
                print(path)
                print(op_ls)
                raise
        prev_round = curr_round
        curr_round = next_round
        del to_process, next_round

    try:
        assert nonleaf_paths <= handled_paths
    except:
        print(nonleaf_paths - handled_paths)
        raise
    return op_ls, root



def remove_useless_bottom_red_nodes(op_ls, raw, target):
    remove = remove_leaf_and_its_parent__without_trinode_restructure
    target_paths = node2sub_nonleaf_paths(target)
    raw_paths = node2sub_nonleaf_paths(raw)
    assert raw_paths >= target_paths

    to_remove = raw_paths - target_paths
    ls = []
    for path in to_remove:
        node = get_node(raw, path)
        assert node.is_red()
        assert node.left.is_leaf()
        assert node.right.is_leaf()
        assert get_attr_path(node.parent) in target_paths
        leaf = node.left
        leaf_path = get_attr_path(leaf)
        ls.append(('remove', leaf_path))
        raw = remove(leaf)

    assert all(get_node(raw, path).entity > 0 for path in target_paths)
    return op_ls+ls, raw








def set_raw_tree_color_as_target_tree(op_ls, raw, target):
    assert get_one_black_depth(raw) == get_one_black_depth(target)
    for more_op_ls, new_raw in _color_as(raw, target):
        return op_ls + more_op_ls, new_raw
    else:
        raise cannot-find-one-solution; logic-error

def _color_as(raw, target):
    # :: node -> other_node_t -> iter[([op], node)]
    funcs = []
    if bool(raw.is_red()) != bool(target.is_red()):
        if target.is_red():
            funcs.append(black2red)
        else:
            funcs.append(red2black)
    if not target.is_leaf():
        assert not raw.is_leaf()
        funcs += [lambda node: iter_parallel_mul(node,
                                                 lambda left: _color_as(left, target.left),
                                                 lambda right: _color_as(right, target.right))]
    return iter_serial_mul([([], raw)], *funcs)

def grey2red(node):
    # invariant black_height[node]
    # postcondition: should be red
    #    though red will affect parent (self is not root)
    #    if parent.is_red() + not use trinode_restructure
    #       ==>> uncle.is_red()
    #       ==>> postcondition: self.is_red(); parent/uncle.is_black()
    assert not node.is_root()
    if node.is_red():
        return iter_unmodify(node) # identity
    return black2red(node)
def black2red(node):
    # invariant black_height[node]
    # postcondition: should be red
    assert node.is_black()
    assert not node.is_root()
    return push_down_black(node)
def push_down_black(node):
    # if not root: invariant black_height[node]
    # otherwise : black_height[node]++
    # postcondition: black if root else red
    #
    assert node.is_black()
    if node.is_leaf():
        # even new_tree >= old_tree
        # black_height[new] may still < black_height[old]
        #    since called by set_raw_tree_black_depth
        insert = insert_at_leaf__without_trinode_restructure
        entity = -1
        path = get_attr_path(node)
        op_ls = [('insert', entity, path)]
        root = insert(node, entity)
        node = get_node(root, path)
        return iter([(op_ls, node)])
        return null_iterable # nothing means fail
        raise logic-error # since new >= old
        op_ls = [('insert', -1, path)]

    def node_filter(op_ls_node_pairs, *node_fs):
        for op_ls, node in op_ls_node_pairs:
            for f in node_fs:
                node = f(node)
            yield op_ls, node

    to_parent = lambda node: node.parent
    lift_iterf_to_grandpa = lambda f: lambda *args:\
                            node_filter(f(*args), to_parent, to_parent)
    it = iter_parallel_mul(node, grey2red, grey2red)
    funcs = [lambda node:black2red(node.left.left),
             lambda node:black2red(node.left.right),
             lambda node:black2red(node.right.left),
             lambda node:black2red(node.right.right),]
    funcs = map(lift_iterf_to_grandpa, funcs)
    return iter_branch_mul(it, *funcs)

def iter_unmodify(node):
    return iter([([], node)])
def grey2black(node):
    # invariant black_height[node]
    # postcondition: should be black
    if node.is_black():
        return iter_unmodify(node)
    return red2black(node)
def red2black(node):
    # invariant black_height[node]
    # postcondition: should be black
    assert node.is_red()
    return more_black(node)
def black2double_black(node):
    # black_height[node]--
    # black -> double black -> black # pass 1 black to parent
    # postcondition: should be black ; since double_black will affect parent
    assert node.is_black()
    return more_black(node)

def more_black(node):
    # red->black or black2double_black
    # red->black : invariant black_height[node]
    # black2double_black : black_height[node]--
    # postcondition: should be black
    if node.is_leaf():
        return null_iterable # fail

    # basic case
    if node.left.is_leaf():
        leaf = node.left
    elif node.right.is_leaf():
        leaf = node.right
    else:
        leaf = None
        
    if leaf is not None:
        # input node = (black, (), (red, (), ()))
        # input node = (black, (red, (), ()), ())
        # input node = (black, (), ())
        # input node = (red, (), ())
        e = node.entity
        if e < 0: # not a nonleaf node in target tree
            node_path = get_attr_path(node)
            leaf_path = get_attr_path(leaf)
            op_ls = [('remove', leaf_path)]
            remove = remove_leaf_and_its_parent__without_trinode_restructure
            root = remove(leaf)
            new_node = get_node(root, node_path)
            
            # black+red->black;
            # black+black->double_black
            # red+black->black
            assert new_node.is_black()
            
            if not new_node.is_leaf():
                # input node = (black, (), (red, (), ()))
                # input node = (black, (red, (), ()), ())
                # new_node = (black+red->black, (), ())
                assert new_node.left.is_leaf()
                assert new_node.right.is_leaf()
                
                op_ls += op_ls
                root = remove(new_node.left) # bug: remove(node.left)
                new_node = get_node(root, node_path)
                assert new_node.is_leaf()
                # new_node = () # red->black->double_black
            return iter([(op_ls, new_node)])
        else:
            # an target tree node
            return null_iterable
            

    def children2black(node):
        return iter_parallel_mul(node, grey2black, grey2black)
    def node_filter(op_ls_node_pairs, *node_fs):
        for op_ls, node in op_ls_node_pairs:
            for f in node_fs:
                node = f(node)
            yield op_ls, node

    # TypeError: 'property' object is not callable
    to_parent = lambda node: node.parent # type(node).parent
    to_left = lambda node: node.left # type(node).left
    to_right = lambda node: node.right # type(node).right
    def one_branch(to_one_child, to_another):
        def branch(node):
            it = node_filter(children2black(to_one_child(node)),
                             to_parent, to_another)
            return node_filter(iter_serial_mul_step(it, black2double_black), to_parent)
        return branch
    funcs = [one_branch(to_left, to_right), one_branch(to_right, to_left)]

    it = children2black(node)
    return iter_branch_mul(it, *funcs)


    
def iter_parallel_mul(node, left_f, right_f):
    # :: node -> (node->iter[([op], node)]) -> (node->iter[([op], node)]) -> iter[([op], node)]

    left_ls = left_f(node.left)
    right_ls = None # right_f(node.right)
    def first_iter():
        nonlocal right_ls
        assert right_ls is None
        right_ls = []
        for x in right_f(node.right):
            right_ls.append(x)
            yield x
    def other_iter():
        assert right_ls is not None
        return iter(right_ls)

    node_plain = node.plain
    for left_op_ls, left in left_ls:
        it = first_iter() if right_ls is None else other_iter()
        for more_op_ls, right in it:
            node = left.parent # since underlying is immutable
            node.right = right
            new_node = _refresh_up_down(node)
            yield left_op_ls + more_op_ls, new_node
        
            
            

        
        
def set_raw_tree_black_depth(op_ls, raw, black_depth):
    '([op], new_raw)'

    mine = get_one_black_depth(raw)
    begin = [(op_ls, raw)]
    if mine < black_depth:
        it = iter_serial_mul(begin, *[push_down_black]*(black_depth - mine))
    elif mine > black_depth:
        it = iter_serial_mul(begin, *[black2double_black]*(mine - black_depth))
    else:
        it = iter(begin)

    try:
        return next(it)
    except:
        print(mine, black_depth)
        raise

def iter_serial_mul_step(op_ls_node_pairs, func):
    # :: iter[([op], node)] -> (node->iter[([op], node)]) -> iter[([op], node)]
    
    op_ls_node_pairs = iter(op_ls_node_pairs)
    for op_ls, node in op_ls_node_pairs:
        assert type(op_ls) is list
        for more_op_ls, new_node in func(node):
            yield op_ls + more_op_ls, new_node
def iter_serial_mul(op_ls_node_pairs, *funcs):
    # :: iter[([op], node)] -> [node->iter[([op], node)]] -> iter[([op], node)]
    op_ls_node_pairs = iter(op_ls_node_pairs)
    for func in funcs:
        op_ls_node_pairs = iter_serial_mul_step(op_ls_node_pairs, func)
    return op_ls_node_pairs
def iter_branch_mul(op_ls_node_pairs, *funcs):
    # :: iter[([op], node)] -> [node->iter[([op], node)]] -> iter[([op], node)]
    op_ls_node_pairs = iter(op_ls_node_pairs)
    for op_ls, node in op_ls_node_pairs:
        assert type(op_ls) is list
        node_underlying= node.underlying # save
        for func in funcs:
            node = node.from_underlying_node(node_underlying) # restore
            for more_op_ls, new_node in func(node):
                yield op_ls + more_op_ls, new_node




















































def insert_at_leaf__without_trinode_restructure(leaf, entity):
    # if this is an ordered tree,
    # then leaf should be between find_range(root, key);
    # otherwise this call will disrupt order
    assert isinstance(leaf, MutableRedBlackTreeNodeABC)
    assert leaf.is_leaf()
    
    # replace u by red(null, e, null)
    me = leaf.make_red_nonleaf_node(entity, leaf.parent_info)
    del leaf
    # broken above me

    while True:
        # broken above me
        assert me.is_red()
        if me.is_root():
            me.recolor()
            break
        parent = me.refresh_up()
        # broken above parent
        
    
        if parent.is_black():
            me = parent
            # broken above me
            break
        
        # double-red ::= parent and me are both red
        assert not parent.is_root()
        grandpa = parent.refresh_up()
        # old2new broken above grandpa
        # !AND! new2old broken above me
        me, = parent.refresh_downs(me.direction)
        # broken above grandpa
        
        assert grandpa.is_black()
        uncle = parent.sibling
        
        
        if uncle.is_black():
            raise NeedTrinodeRestructorError(uncle)
            
        else:
            # uncle is red
##            -           grandpa:black
##            - uncle:red,            parent:red
##            -                     ....   me:red
            # recolor(self, grandpa, parent, uncle)
            

            # broken above grandpa
            left, right = grandpa.children
            left.recolor()
            right.recolor()
            # broken above grandpa, left, right
            grandpa.children = left, right
            del left, right # to ignore the new2old broken points above them
            # broken above grandpa
            grandpa.recolor()
            # brken above grandpa
            assert grandpa.is_red()
            
##            
##            -           grandpa:red
##            - uncle:black,          parent:black
##            -                     ....   me:red

            
            me = grandpa
            # broken above me
            continue    
    
    # broken above me

    assert me.is_black()
    root = me.fixed_the_only_broken_above_until_root(); del me
    # broken above root
    return root # ignore broken above root










def remove_leaf_and_its_parent__without_trinode_restructure(leaf):
    assert leaf.is_leaf()
    assert not leaf.is_root()
    me, is_me_double_black = __remove__raw__node_with_zombie_entity_and_an_leaf_child(
                                leaf)
    assert me.is_black()

    # broken above me
    if is_me_double_black:
        # double black : me contain two black!! since nonleaf was removed
        assert me.is_black() # indeed double black

        # broken above me
        return handle_double_black__without_trinode_restructure(me)[0]
    if me.is_root() and me.is_red():
        me.recolor()
    root = me.fixed_the_only_broken_above_until_root()
    is_root_double_black = False
    return root

def handle_double_black__without_trinode_restructure(me):
    '''
precondition:
    root.is_black()
return root, is_root_double_black
postcondition:
    root may be black or double_black

'''
    is_root_double_black = False
    is_me_double_black = True
    while is_me_double_black:
        assert me.is_black() # indeed double black


        # broken above (maybe parent), me
        #   maybe parent from maybe grandpa when "me:=parent" see below
        
        if me.is_root():
            is_root_double_black = is_me_double_black # for output
            
            # color me black ; ...
            is_me_double_black = False
            continue


        parent = me.refresh_up()
        # broken above parent
        sibling = me.sibling
        # me double black ==>> me maybe a leaf
        #                 ==>> sibling should not be a leaf
        assert not sibling.is_leaf() 
        
        if sibling.is_red():
            raise NeedTrinodeRestructorError

    
        nephews = sibling.children
        # if both nephews are black:
        if all(nephew.is_black() for nephew in nephews):
            # broken above (parent or grandpa)
            parent, is_parent_double_black = __remove__black_sibling_and_no_red_nephews(parent, me, sibling)
            del me, sibling
            # broken above (maybe grandpa), parent
            # [BLACK me]

        else:
            raise NeedTrinodeRestructorError


        # broken above (maybe grandpa), parent
        me = parent ; del parent
        # broken above (maybe parent), me
        is_me_double_black = is_parent_double_black
        continue

    # broken above (maybe parent), me
    if me.is_root():
        # no parent
        pass
        # broken above me
    else:
        parent = me.refresh_up()
        # broken above parent
        me = parent ; del parent
        # broken above me

    
    # broken above me
    root = me.fixed_the_only_broken_above_until_root()
    # broken above root
    # ignore broken above root
    return root, is_root_double_black


















############################ copy from _remove

from ._remove import __remove__raw__node_with_zombie_entity_and_an_leaf_child,\
     __remove__black_sibling_and_no_red_nephews



























def test():pass

_test_make_plain__TupleBoth_MostBaised_RBT()
_test_target_tree2raw_tree()
_test_build_rbt()










