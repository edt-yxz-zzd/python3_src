
'''
RedBlackTreeNodeTest

each test case contains:
    1) initial tree description
    2) modifying action description
    3) result tree description
test framework:
    1) use build initial/result tree (of user class) from their description
    2) modify it
    3) compare

but how to build a tree?
    0) use text to descript a tree (provided by user)
    1) translate the description into a standard tree
       by directly construct the underlying node.
       # standard tree - RBT_Node_TupleBothPlainParented
    2) check red-black tree properties
    3) decompose the standard tree into some limited actions
        see: build_rbt
    4) build the user tree from an empty tree by those actions
       NOTE: tree type (hence action) are provided by user
    5) compare user tree and standard tree
        to make sure that no bugs occur in construction
        # entity should be comparable

tree description:
    RBTreeDescription ::= Node
    Node ::= Leaf | Nonleaf
    Leaf ::= '(' ')'
    Nonleaf ::= '(' Color ',' Entity ',' Node ',' Node ')'
    Color ::= 'red' | 'black'
    # Entity see below
action description:
    ActionDescription ::= ActionStatement*
    ActionStatement ::= LeafPath '=' Entity # insert
                      | 'del' LeafPath
                      | EntityPath '=' Entity # replace
                      | 'del' EntityPath
                      | SetOption
                      | OptionScope
    OptionScope ::= '{' ActionDescription '}'
    SetOption ::= [+-] Option
    Option ::= 'ChildLeafFirst' | 'PreferSuccLeaf' # default turn on
    Path ::= 'root' ('.left' | '.right')*
    LeafPath ::= Path
    NonleafPath ::= Path
    EntityPath ::= NonleafPath '.entity'
    Entity ::= IntLiteral | StringLiteral
    IntLiteral ::= [+-]?(0|[1-9][0-9]*)
    StringLiteral ::= \"([^\"\s]| )*\"

    # path = ... where path should be a leaf - create a nonleaf to replace leaf
    # del path where path should be a leaf - remove leaf and its parent
    #    since remove nonleaf is a more complex operation

    e.g.
    
    root = 4
    root.left = 3
    root.right = 5
    del root.left.left

    ==>>
        begin with an empty tree
            (though not required in general,
            in the above example, "root=3" ==>> must begin with an empty tree)
        end up with (black, 4, (), (red, 5, (), ()))
'''

'''

        Tree a = () | (bool, a, Tree a, Tree a)
        i.e. empty tuple () - leaf
             4-tuple     (is_black, entity, left_child, right_child)
'''

from ast import literal_eval
from seed.recognize.py_ast import Expr2Obj, parse_expr


from .RedBlackTreeNodeABC import \
     MutableRedBlackTreeNodeABC, \
     RBT_Node_TupleBothPlainParented as Node,\
     RBT_Node_TupleBothPlainParented_ABC as NodeABC
from .build_rbt import build_rbt, apply_op_ls, get_node, \
     check_red_black_tree_properties
from seed.iters.icut_to import icut_seq_to

expr2tree_description = Expr2Obj('tuple name num str'.split(),
                                 {'red':False, 'black':True})
def tree_description_text2tree_description(text):
    expr = parse_expr(text)
    return expr2tree_description(expr)
    # fix me: what if StringLiteral contains 'red' or 'black'?
    text = text.strip().replace('red', 'False').replace('black', 'True')
    return literal_eval(text)
assert tree_description_text2tree_description('(black, "", (), ())') == (True, '', (), ())





def full_apply_op_ls(root, op_ls):
    '''op_ls :: [(insert, entity, leaf_path)|(remove, leaf_path)]
where path is a string of s.t. rex'|\w+(.\w+)*'
'''
    insert = type(root).insert_entity_at_leaf
    remove = type(root).remove_leaf_and_its_parent
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
            raise NotImplementedError('see:ActionDescription')
    return root
    



def action_description_text2action_description(text):
    return list(action_description_text2iter_action_description(text))
def action_description_text2iter_action_description(text):

    def to_path(s, lineno, line):
        path = s.strip()
        ls = path.split('.')
        if not ls or ls[0] != 'root' or not set(ls[1:]) <= {'left', 'right'}:
            raise ValueError('bad format at {} line: {!r}'
                             .format(lineno, line))
        return path[len('root.'):]
        if path != '.':
            if path.startswith('.') and set(path[1:].split('.')) <= {'left', 'right'}:
                pass
            else:
                raise ValueError('bad format at {} line: {!r}'
                                 .format(lineno, line))
        return path[1:]
    
    for lineno, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        if line.startswith('del'):
            path = to_path(line[3:], lineno, line)
            yield 'remove', path
        elif '=' in line:
            path, entity = line.split('=', 1)
            path = to_path(path, lineno, line)
            entity = literal_eval(entity.strip()) # why need strip!!
            yield 'insert', entity, path
            
        



def tree_description2standard_tree_plain_node(tree_description, Node=Node):
    assert issubclass(Node, NodeABC)
    if type(tree_description) is not tuple:
        raise ValueError('bad format : not tuple')
    if len(tree_description) not in (0, 4):
        raise ValueError('bad format: not 0-/4-tuple')
    if tree_description == ():
        return Node.PLAIN_LEAF
    is_black, entity, left, right = tree_description
    left = tree_description2standard_tree_plain_node(left, Node=Node)
    right = tree_description2standard_tree_plain_node(right, Node=Node)
    color = Node.BLACK if is_black else Node.RED
    return color, entity, left, right

def tree_description2standard_tree_node(tree_description, Node=Node):
    assert issubclass(Node, NodeABC)
    plain = tree_description2standard_tree_plain_node(tree_description, Node=Node)
    root = Node.from_root_plain_node(plain)
    check_red_black_tree_properties(root)
    return root

def standard_tree_node2iter_actions(root):
    assert isinstance(root, NodeABC)
    op_ls, raw = build_rbt(root)

    # replace entity
    for op in op_ls:
        action = op[0]
        if action == 'insert':
            _, entity, path = op
            if entity > 0:
                entity = get_node(root, path).entity
            else:
                entity = None
            yield action, entity, path
        elif action == 'remove':
            _, path = op
            yield action, path
        else:
            raise ...

def actions2user_tree_node(actions, UserNode):
    node = apply_op_ls(UserNode.make_leaf_root(), actions)
    return node


def tree_description2user_tree_node(tree_description, UserNode):
    assert issubclass(UserNode, MutableRedBlackTreeNodeABC)
    std_root = tree_description2standard_tree_node(tree_description)
    it = standard_tree_node2iter_actions(std_root)
    try:
        usr_root = actions2user_tree_node(it, UserNode)
    except:
        print(std_root.plain)
        print(list(standard_tree_node2iter_actions(std_root)))
        raise
    if not std_root.oriented_subtree_eq(usr_root):
        raise ValueError('{} implement has bugs: fail to construct a tree'
                         .format(UserNode))
    return usr_root

def tree_description_text2user_tree_node(text, UserNode):
    try:
        description = tree_description_text2tree_description(text)
        return tree_description2user_tree_node(description, UserNode)
    except:
        print(text)
        raise

def _test(UserNode, initial_tree_text, action_text, result_tree_text):
    initial = tree_description_text2user_tree_node(initial_tree_text, UserNode)
    result = tree_description_text2user_tree_node(result_tree_text, UserNode)
    actions = action_description_text2action_description(action_text)
    other_result = full_apply_op_ls(initial, actions) # apply_op_ls is incomplete version
    
    r = other_result.oriented_subtree_eq(result)
    if not r:
        print(result.plain, other_result.plain)
    return r

def test_UserNode(UserNode, initial_tree_text, action_text, result_tree_text):
    # test input first
    if not _test(Node, initial_tree_text, action_text, result_tree_text):
        raise ValueError('std node implement error or test data error:\n{}'
                         .format('=====\n{}\n-----\n{}\n-----\n{}\n'
                                 .format(initial_tree_text,
                                         action_text,
                                         result_tree_text)))
    return _test(UserNode, initial_tree_text, action_text, result_tree_text)



# test_data_text ::= Case*
# Case ::= '=====' initial_tree_text ActionResult+
# ActionResult ::= '-----' action_text '-----' result_tree_text
test_data_text = '''
=====
()
-----
    root = 0
-----
        (black, 0, (), ())



=====
(black, 1, (), ())
-----
    root.left = 0
-----
        (black, 1, (red, 0, (), ()), ())
-----
    root.right = 2
-----
        (black, 1, (), (red, 2, (), ()))

=====

(black, 3, (), (red, 5, (), ()))
-----
    root.right.left = 4
-----
        (black, 4, (red, 3, (), ()), (red, 5, (), ()))
-----
    root.right.right = 6
-----
        (black, 5, (red, 3, (), ()), (red, 6, (), ()))

=====

(black, 3, (red, 1, (), ()), ())
-----
    root.left.left = 0
-----
        (black, 1, (red, 0, (), ()), (red, 3, (), ()))
-----
    root.left.right = 2
-----
        (black, 2, (red, 1, (), ()), (red, 3, (), ()))

=====

(black, 3, (red, 1, (), ()), (red, 5, (), ()))
-----
    root.left.left = 0
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 5, (), ()))
-----
    root.left.right = 2
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 5, (), ()))
-----
    root.right.left = 4
-----
        (black, 3, (black, 1, (), ()), (black, 5, (red, 4, (), ()), ()))
-----
    root.right.right = 6
-----
        (black, 3, (black, 1, (), ()), (black, 5, (), (red, 6, (), ())))

=====
(black, 1, (black, 0, (), ()), 
       (red, 3, (black, 2, (), ()), 
                (black, 7, (red, 5, (), ()), 
                           (red, 9, (), ()))))
-----
    root.right.right.left.left = 4
-----
        (black, 3, (red, 1, (black, 0, (), ()), (black, 2, (), ())), 
                   (red, 7, (black, 5, (red, 4, (), ()), ()), 
                            (black, 9, (), ())))




=====

(black, 0, (), (red, 1, (), ()))
-----
    del root.right.left
-----
        (black, 0, (), ())
-----
    del root.right.right
-----
        (black, 0, (), ())



=====

(black, 0, (), (red, 1, (), ()))
-----
    del root.left
-----
        (black, 1, (), ())



=====

(black, 0, (), ())
-----
    del root.left
-----
        ()
   
-----
    del root.right
-----
        ()


 
=====

(black, 3, (red, 1, (black, 0, (), ()), (black, 2, (), ())), 
           (black, 4, (), ()))
-----
    del root.right.left
-----
        (black, 1, (black, 0, (), ()), (black, 3, (red, 2, (), ()), ()))

-----
    del root.right.right
-----
        (black, 1, (black, 0, (), ()), (black, 3, (red, 2, (), ()), ()))


=====

(black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.left.left
-----
        (black, 1, (), (red, 2, (), ()))
-----
    del root.right.left
-----
        (black, 1, (red, 0, (), ()), ())

-----
    del root.left.right
-----
        (black, 1, (), (red, 2, (), ()))
-----
    del root.right.right
-----
        (black, 1, (red, 0, (), ()), ())




=====

(black, 3, (red, 1, (black, 0, (), ()), 
                    (black, 2, (), ())), 
           (black, 4, (), ()))
-----
    del root.left.left.left
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 4, (), ()))
-----
    del root.left.right.left
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 4, (), ()))

-----
    del root.left.left.right
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 4, (), ()))
-----
    del root.left.right.right
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 4, (), ()))







        

=====



(black, 7, (red, 3, (black, 1, (black, 0, (), ()), 
                               (black, 2, (), ())), 
                    (black, 5, (black, 4, (), ()), 
                               (black, 6, (), ()))),
           (black, 9, (black, 8, (), ()), 
                      (black, 10, (), ())))
-----
    del root.left.left.left.left
-----
    (black, 7, (black, 3, (black, 1, (), 
                                     (red, 2, (), ())), 
                          (red, 5, (black, 4, (), ()), 
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()), 
                          (black, 10, (), ())))
-----
    del root.left.left.right.left
-----
    (black, 7, (black, 3, (black, 1, (red, 0, (), ()), 
                                     ()), 
                          (red, 5, (black, 4, (), ()), 
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()), 
                          (black, 10, (), ())))


-----
    del root.left.left.left.right
-----
    (black, 7, (black, 3, (black, 1, (), 
                                     (red, 2, (), ())), 
                          (red, 5, (black, 4, (), ()), 
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()), 
                          (black, 10, (), ())))
-----
    del root.left.left.right.right
-----
    (black, 7, (black, 3, (black, 1, (red, 0, (), ()), 
                                     ()), 
                          (red, 5, (black, 4, (), ()), 
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()), 
                          (black, 10, (), ())))







=====





(black, 2, (black, 0, (), (red, 1, (), ())), (black, 3, (), ()))
-----
    del root.right.left 
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.right.right 
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
=====
(black, 2, (black, 1, (red, 0, (), ()), ()), (black, 3, (), ()))
-----
    del root.right.left 
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.right.right 
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))





=====




(black, 4, (red, 2, (black, 0, (), (red, 1, (), ())), 
                    (black, 3, (), ())), 
           (black, 5, (), ()))
-----
    del root.left.right.left
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
-----
    del root.left.right.right
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
=====
(black, 4, (red, 2, (black, 1, (red, 0, (), ()), ()), (black, 3, (), ())), (black, 5, (), ()))
-----
    del root.left.right.left
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
-----
    del root.left.right.right
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))


'''


def test_data_text2iter_test_data(test_data_text):
    cases = test_data_text.split('=====')
    if cases[0].strip():
        raise ValueError('nonspaces before first =====')
    cases = cases[1:]
    for case in cases:
        yield from case_text2iter_test_data(case)

def case_text2iter_test_data(case_text):
    slots = case_text.split('-----')
    if not len(slots) & 1:
        raise ValueError('bad format: actions without result tree. \n{}'
                         .format(case_text))
    initial_text = slots[0]
    for action_text, result_text in icut_seq_to(slots[1:], 2):
        yield initial_text, action_text, result_text


data_ls = list(test_data_text2iter_test_data(test_data_text))

for initial, actions, result in data_ls:
    test_UserNode(Node, initial, actions, result)
    




        








