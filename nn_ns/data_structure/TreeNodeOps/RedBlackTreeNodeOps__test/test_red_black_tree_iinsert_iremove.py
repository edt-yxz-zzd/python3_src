
r'''
see: def - test_data_text.txt


now use:
    copy_from_another_ops_subtree_as_tree
    + RedBlackTreeNodeOps__TargetTree::plain_node


## using
test_data_text2iter_test_data
    <<== case_text2iter_test_data
test_user_ops
    <<== tree_description_text2user_tree_node
        <<== tree_description_text2tree_description
        <<== tree_description2user_tree_node
            <<== tree_description2standard_tree_node
                <<== tree_description2standard_tree_plain_node
                <<== check_red_black_tree_properties
    <<== action_description_text2action_description
        <<== action_description_text2iter_action_description
    <<== full_apply_op_ls
        <<== get_node


testing:
    >>> main() is None
    True
'''

__all__ = '''
    test_data_text2iter_test_data
    test_user_ops

    full_apply_op_ls
    action_description_text2action_description

    tree_description_text2tree_description
    tree_description2user_tree_node
    '''.split()



from ast import literal_eval
from seed.recognize.py_ast import Expr2Obj, parse_expr
from operator import __eq__
from .test_data_text2iter_test_data import test_data_text2iter_test_data


from ..RedBlackTreeNodeOps__concrete.RedBlackTreeNodeOps__TargetTree import \
    RedBlackTreeNodeOps__TargetTree
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__imodify import \
    IRedBlackTreeNodeOps__imodify
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__parent_info_plain_node import \
    IRedBlackTreeNodeOps__parent_info_plain_node




the_std_ops = RedBlackTreeNodeOps__TargetTree()
ImodifyOps = IRedBlackTreeNodeOps__imodify
StdImodifyOps = IRedBlackTreeNodeOps__parent_info_plain_node

assert issubclass(StdImodifyOps, ImodifyOps)
assert isinstance(the_std_ops, StdImodifyOps)

def check_red_black_tree_properties(ops, root):
    ops.check_red_black_tree_properties(root, as_root=True)

expr2tree_description = Expr2Obj('tuple name num str'.split(),
                                 {'red':False, 'black':True})
def tree_description_text2tree_description(text):
    expr = parse_expr(text)
    return expr2tree_description(expr)
    # fix me: what if StringLiteral contains 'red' or 'black'?
    text = text.strip().replace('red', 'False').replace('black', 'True')
    return literal_eval(text)
assert tree_description_text2tree_description('(black, "", (), ())') == (True, '', (), ())





def full_apply_op_ls(ops, root, op_ls):
    '''
op_ls :: [action_stmt]
    # action_stmt   = ('remove_leaf', leaf_path)
    #               | ('remove_nonleaf', nonleaf_path, options)
    #               | ('insert', entity, leaf_path)
    #               | ('replace', entity, nonleaf_path)
leaf_path = nonleaf_path = [('left' | 'right')]

'''
    assert ops.is_root(root)
    insert = ops.rbt_iinsert_entity_at_leaf
    remove_leaf = ops.rbt_iremove_leaf_and_its_parent
    replace = ops.rbt_irepalce_entity_at_nonleaf
    remove_nonleaf = ops.rbt_iremove_entity_at_nonleaf

    is_leaf = ops.is_leaf
    old_root = root
    for op in op_ls:
        action = op[0]
        if action == 'insert':
            _, entity, path = op
            leaf = get_node(ops, root, path)
            if not is_leaf(leaf): raise ValueError
            try:
                # XXX
                root = insert(leaf, entity)
            except:
                if False:
                    print('old_root')
                    print(old_root)
                    print('root')
                    print(root)
                    print('leaf')
                    print(leaf)
                    print('entity')
                    print(entity)
                raise
        elif action == 'remove_leaf':
            _, path = op
            leaf = get_node(ops, root, path)
            if not is_leaf(leaf): raise ValueError
            root = remove_leaf(leaf)
        elif action == 'replace':
            _, entity, path = op
            nonleaf = get_node(ops, root, path)
            if is_leaf(nonleaf): raise ValueError
            root = replace(nonleaf, entity)
        elif action == 'remove_nonleaf':
            _, path, options = op
            nonleaf = get_node(ops, root, path)
            if is_leaf(nonleaf): raise ValueError
            root = remove_nonleaf(nonleaf
                    , child_leaf_first=options['ChildLeafFirst']
                    , prefer_succ_leaf=options['PreferSuccLeaf']
                    )
        else:
            raise NotImplementedError('see:ActionDescription')
    return root


def get_node(ops, self, path):
    # path :: [direction]
    # direction = 'left' | 'right'
    get_left_child = ops.get_left_child
    get_right_child = ops.get_right_child
    node = self
    for direction in path:
        if direction == 'left':
            node = get_left_child(node)
        elif direction == 'right':
            node = get_right_child(node)
        else:
            raise NotImplementedError(
                f"direction in path is not 'left' or 'right': {direction}")
    return node




def action_description_text2action_description(text):
    return list(action_description_text2iter_action_description(text))
def action_description_text2iter_action_description(text):
    # -> [action_stmt]
    # action_stmt   = ('remove_leaf', leaf_path)
    #               | ('remove_nonleaf', nonleaf_path, options)
    #               | ('insert', entity, leaf_path)
    #               | ('replace', entity, nonleaf_path)

    def to_path_ex(s, lineno, line):
        # -> (False, leaf_path) | (True, nonleaf_path)
        path = s.strip()
        ls = path.split('.')


        is_entity_path = ls[-1] == 'entity'
        if is_entity_path:
            ls.pop()

        if not ls or ls[0] != 'root' or not set(ls[1:]) <= {'left', 'right'}:
            raise ValueError('bad format at {} line: {!r}'
                             .format(lineno, line))

        assert ls[0] == 'root'
        return is_entity_path, ls[1:]


    optionss = [{'ChildLeafFirst':True, 'PreferSuccLeaf':True}]

    for lineno, line in enumerate(text.splitlines()):
        assert optionss

        line = line.strip()
        if not line:
            continue
        if line.startswith('del'):
            is_entity_path, path = to_path_ex(line[3:], lineno, line)
            if not is_entity_path:
                yield 'remove_leaf', path
            else:
                yield 'remove_nonleaf', path, optionss[-1].copy()
        elif '=' in line:
            path, entity = line.split('=', 1)
            is_entity_path, path = to_path_ex(path, lineno, line)
            entity = literal_eval(entity.strip()) # why need strip!!
            if not is_entity_path:
                yield 'insert', entity, path
            else:
                yield 'replace', entity, path
        elif line[0] in '+-':
            # turn on/off option
            turn_on = line[0] == '+'
            options = line[1:].strip()
            if not options:
                raise ValueError('bad format at {} line: {!r}'
                                 .format(lineno, line))
            options = set(options)
            if not (options <= {'ChildLeafFirst', 'PreferSuccLeaf'}):
                raise ValueError('unknown options at {} line: {!r}'
                                 .format(lineno, line))

            optionss[-1].update((option, turn_on) for option in options)
        elif len(line) == 1 and line in '{}':
            # option scope
            is_option_scope_close = line == '}'
            if is_option_scope_close:
                if len(optionss) <= 1:
                    raise ValueError('too many scope closes at {} line: {!r}'
                                 .format(lineno, line))
                optionss.pop()
                assert optionss
            else:
                # open
                assert optionss
                optionss.append(optionss[-1].copy())
        else:
            raise ValueError('unknown line case at {} line: {!r}'
                         .format(lineno, line))






def tree_description2standard_tree_plain_node(tree_description):
    ops = the_std_ops
    assert isinstance(ops, StdImodifyOps)
    BLACK = ops.get_BLACK()
    RED = ops.get_RED()
    make_plain_leaf = ops.make_plain_leaf

    def this(tree_description):
        if type(tree_description) is not tuple:
            raise ValueError('bad format : not tuple')
        if len(tree_description) not in (0, 4):
            raise ValueError('bad format: not 0-/4-tuple')

        if tree_description == ():
            return make_plain_leaf()

        is_black, entity, left, right = tree_description
        left = this(left)
        right = this(right)
        color = BLACK if is_black else RED
        return color, entity, left, right
    return this(tree_description)


def tree_description2standard_tree_node(tree_description):
    ops = the_std_ops
    assert isinstance(ops, StdImodifyOps)

    plain = tree_description2standard_tree_plain_node(tree_description)
    root = ops.plain_node_to_root(plain)
    try:
        check_red_black_tree_properties(ops, root)
    except:
        print('tree_description')
        print(tree_description)
        print('root')
        print(root)
        raise
    return root


def tree_description2user_tree_node(tree_description, user_ops):
    assert isinstance(user_ops, IRedBlackTreeNodeOps__imodify)
    std_root = tree_description2standard_tree_node(tree_description)
    check_red_black_tree_properties(the_std_ops, std_root)

    user_root = user_ops.copy_from_another_ops_subtree_as_tree(the_std_ops, std_root)
    if not user_ops.verify_result_of_copy_from_another_red_black_tree(
            user_root, the_std_ops, std_root):
        print('the_std_ops')
        print(the_std_ops)
        print('std_root')
        print(std_root)
        print('user_ops')
        print(user_ops)
        print('user_root')
        print(user_root)
        raise ValueError('{} implement has bugs: fail to construct a tree'
                         .format(user_ops))
    check_red_black_tree_properties(user_ops, user_root)
    return user_root

def tree_description_text2user_tree_node(text, user_ops):
    try:
        tree_description = tree_description_text2tree_description(text)
        return tree_description2user_tree_node(tree_description, user_ops)
    except:
        print('user_ops')
        print(user_ops)
        print('tree_description_text')
        print(text)
        raise

def _test_user_ops(user_ops, initial_tree_text, action_text, result_tree_text):
    initial_tree = tree_description_text2user_tree_node(initial_tree_text, user_ops)
    result_tree_from_answer = tree_description_text2user_tree_node(result_tree_text, user_ops)
    actions = action_description_text2action_description(action_text)

    result_tree_from_actions = full_apply_op_ls(user_ops, initial_tree, actions)

    r = user_ops.verify_result_of_copy_from_another_red_black_tree(
            result_tree_from_answer
            , user_ops, result_tree_from_actions, entity_eq = __eq__
            )
    if not r:
        get_plain_node = user_ops.get_plain_node
        plain_node_from_answer = get_plain_node(result_tree_from_answer)
        plain_node_from_actions = get_plain_node(result_tree_from_actions)
        print('plain_node_from_answer')
        print(plain_node_from_answer)
        print('plain_node_from_actions')
        print(plain_node_from_actions)
    return r

def test_user_ops(user_ops, initial_tree_text, action_text, result_tree_text):
    # test input first
    if not _test_user_ops(the_std_ops, initial_tree_text, action_text, result_tree_text):
        raise ValueError('std node implement error or test data error:\n{}'
                         .format('=====\n{}\n-----\n{}\n-----\n{}\n'
                                 .format(initial_tree_text,
                                         action_text,
                                         result_tree_text)))
    return _test_user_ops(user_ops, initial_tree_text, action_text, result_tree_text)




def test_std_ops():
    from .test_data_text import test_data_text
    data_ls = list(test_data_text2iter_test_data(test_data_text))

    for initial_txt, actions_txt, result_txt in data_ls:
        try:
            test_user_ops(the_std_ops, initial_txt, actions_txt, result_txt)
        except:
            print('initial_txt')
            print(initial_txt)
            print('actions_txt')
            print(actions_txt)
            print('result_txt')
            print(result_txt)
            raise
main = test_std_ops


if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
















