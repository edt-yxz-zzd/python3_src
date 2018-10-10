
'''
Trie - prefix tree
    is a kind of search tree -- an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings.


Trie a v = Trie {size :: UInt
                ,nullable_root :: ITrieNullableRoot
                }

ITrieNullableRoot = TrieEmptyRoot | TrieNonEmptyRoot a v
TrieNonEmptyRoot a v =
    {nullable_common_prefix :: [a]
        # may empty
    ,maybe_symbol2child__ge1 :: NonEmpty(Map (Maybe a) (ITrieNode a v))
        # len >= 1
    }
    # TrieNonEmptyRoot vs TrieNonLeafNode

ITrieBranch = TrieNonEmptyRoot | TrieNonLeafNode
IXTrieNode a v = ITrieNullableRoot a v | ITrieNode a v
# nonroot-node
ITrieNode a v = TrieNonLeafNode a v | TrieLeafNode a v
TrieNonLeafNode a v = TrieNonLeafNode
                {nonempty_common_prefix :: NonEmpty[a]
                    # len >= 1
                ,maybe_symbol2child__ge2 :: NonEmpty(Map (Maybe a) (ITrieNode a v))
                    # len >= 2
                }
TrieLeafNode a v = TrieLeafNode
                {nullable_suffix :: [a]  # may empty
                ,value :: v
                }


example:
    >>> trie = CharTrie()
    >>> len(trie)
    0
    >>> trie
    CharTrie()
    >>> trie.verify_trie_structure()
    True

    >>> trie[''] = 0
    >>> len(trie)
    1
    >>> trie
    CharTrie([('', 0)])
    >>> trie.verify_trie_structure()
    True
    >>> trie['']
    0
    >>> trie['1'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError

    >>> del trie['']
    >>> len(trie)
    0
    >>> trie
    CharTrie()
    >>> trie.verify_trie_structure()
    True

    >>> trie['1234'] = 4
    >>> trie.verify_trie_structure()
    True
    >>> trie['12345'] = 5
    >>> trie.verify_trie_structure()
    True
    >>> trie['123'] = 3
    >>> trie.verify_trie_structure()
    True
    >>> trie['12'] = 2
    >>> trie.verify_trie_structure()
    True
    >>> trie['1'] = 1
    >>> trie.verify_trie_structure()
    True
    >>> trie[''] = 0
    >>> trie.verify_trie_structure()
    True
    >>> len(trie)
    6
    >>> sorted(trie.iter_items())
    [('', 0), ('1', 1), ('12', 2), ('123', 3), ('1234', 4), ('12345', 5)]


    >>> trie['22'] = 22
    >>> trie.verify_trie_structure()
    True
    >>> trie['22']
    22
    >>> trie['22'] = 22222
    >>> trie.verify_trie_structure()
    True
    >>> trie['22']
    22222
    >>> len(trie)
    7

    >>> trie.clear()
    >>> len(trie)
    0
    >>> trie
    CharTrie()
    >>> trie.verify_trie_structure()
    True
    >>> trie['123'] = 3
    >>> trie.verify_trie_structure()
    True
    >>> trie['abc'] = -3
    >>> trie.verify_trie_structure()
    True
    >>> trie['123']
    3
    >>> trie['abc']
    -3

    >>> trie = CharTrie()
    >>> trie['111aaa'] = 1
    >>> trie.verify_trie_structure()
    True
    >>> trie['111bbb'] = 2
    >>> trie.verify_trie_structure()
    True
    >>> len(trie)
    2
    >>> sorted(trie.iter_items())
    [('111aaa', 1), ('111bbb', 2)]
    >>> trie['111aaa']
    1
    >>> trie['111bbb']
    2

    >>> trie[''] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError
    >>> trie['1'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError
    >>> trie['111'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError
    >>> trie['111a'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError
    >>> trie['111aa'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError
    >>> trie['111aaaa'] #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError

    >>> del trie['111aaa']
    >>> trie.verify_trie_structure()
    True
    >>> del trie['111bbb']
    >>> trie.verify_trie_structure()
    True
    >>> trie
    CharTrie()


    >>> symbols = 'javax.swing.UIManager'
    >>> trie = CharTrie([('java.', 'java.'), ('javax.', 'javax.')])
    >>> trie.query_maybe_longest_prefix_item(symbols)
    (6, 'javax.')
'''


__all__ = '''
    ITrie
    CharTrie
    '''.split()

from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from collections import namedtuple
from collections.abc import MutableMapping

from seed.iters.calc_common_prefix_length import calc_common_prefix_length
from seed.types.view.SeqSliceView import SeqSliceView
from nn_ns.ops.MaybeOps.StdMaybeOps import theStdMaybeOps
from nn_ns.ops.MaybeOps.MaybeCharOps import theMaybeCharOps
from seed.tiny import null_iter, echo
from seed.helper.repr_input import repr_helper

class IXTrieNode(ABC):
    __slots__ = ()
    @not_implemented
    def is_root(self):
        raise NotImplementedError
    @not_implemented
    def is_branch(self):
        raise NotImplementedError
class IOpGetSymbolsSegment(IXTrieNode):
    __slots__ = ()
    @not_implemented
    def get_symbols_segment(self):
        raise NotImplementedError
class IOpGetMaybeSymbol2Child(IOpGetSymbolsSegment):
    __slots__ = ()
    @not_implemented
    def get_maybe_symbol2child(self):
        raise NotImplementedError
    @override
    def is_branch(self):
        return True
class ITrieNode(IOpGetSymbolsSegment, IXTrieNode):
    __slots__ = ()
    @not_implemented
    def is_leaf(self):
        raise NotImplementedError
    @override
    def is_root(self):
        return False




class ITrieNullableRoot(IXTrieNode):
    __slots__ = ()
    @not_implemented
    def is_empty(self):
        raise NotImplementedError
    @override
    def is_root(self):
        return True
class TrieEmptyRoot(ITrieNullableRoot):
    # trie has no node at all
    __slots__ = ()
    @override
    def is_empty(self):
        return True
    @override
    def is_branch(self):
        return False
    pass
theTrieEmptyRoot = TrieEmptyRoot()


class TrieNonEmptyRoot(IOpGetMaybeSymbol2Child, ITrieNullableRoot):
    # trie has some nodes
    __slots__ = '''
        __nullable_common_prefix
        __maybe_symbol2child__ge1
        '''.split()

    @override
    def is_empty(self):
        return False

    def __init__(self, nullable_common_prefix, maybe_symbol2child__ge1):
        assert hasattr(nullable_common_prefix, '__len__')
        assert len(maybe_symbol2child__ge1) >= 1
        self.nullable_common_prefix = nullable_common_prefix
        self.maybe_symbol2child__ge1 = maybe_symbol2child__ge1
    @property
    def nullable_common_prefix(self):
        #return getattr(self, '__nullable_common_prefix')
        return self.__nullable_common_prefix
    @nullable_common_prefix.setter
    def nullable_common_prefix(self, nullable_common_prefix):
        if not hasattr(nullable_common_prefix, '__len__'): raise ValueError
        #setattr(self, '__nullable_common_prefix', nullable_common_prefix)
        self.__nullable_common_prefix = nullable_common_prefix

    @property
    def maybe_symbol2child__ge1(self):
        #return getattr(self, '__maybe_symbol2child__ge1')
        return self.__maybe_symbol2child__ge1
    @maybe_symbol2child__ge1.setter
    def maybe_symbol2child__ge1(self, maybe_symbol2child__ge1):
        if not len(maybe_symbol2child__ge1) >= 1: raise ValueError
        #setattr(self, '__maybe_symbol2child__ge1', maybe_symbol2child__ge1)
        self.__maybe_symbol2child__ge1 = maybe_symbol2child__ge1
    @override
    def get_symbols_segment(self):
        return self.nullable_common_prefix
    @override
    def get_maybe_symbol2child(self):
        return self.maybe_symbol2child__ge1


class ITrie(MutableMapping, ABC):
    '''
nn_ns.ops.IMaybeOps
nn_ns.ops.IMappingOps

nn_ns.ops.MaybeOps.MaybeCharOps

'''
    __slots__ = '''
        __nullable_root
        __size
        '''.split()
    '''
    @not_implemented
    def get_mapping_ops(self):
        # for (Map (Maybe symbol) ITrieNode)
        # () -> IMappingOps
        pass
    @not_implemented
    def get_maybe_value_ops(self):
        # for (Maybe value)
        # () -> IMaybeOps
        pass
    '''

    @not_implemented
    def new_maybe_symbol_mapping(self):
        # () -> Map (Maybe symbol) ITrieNode
        pass
    @not_implemented
    def get_maybe_symbol_ops(self):
        # for (Maybe symbol)
        # () -> IMaybeOps
        pass

    def __init__(self, items=()):
        # .__nullable_root :: ITrieNullableRoot
        self.__init()
        self.update_from_items(items)

    def __repr__(self):
        [*items] = self.iter_items()
        may_items = theStdMaybeOps.mkMaybe(items, lambda: items)
        return repr_helper(self, *may_items)

    def __len__(self):
        return self.__size
    def __contains__(self, symbols):
        return self.contains(symbols)
    def __iter__(self):
        # () -> Iter symbols
        for symbols, value in iter_items():
            yield symbols
    def iter_items(self):
        # () -> Iter (symbols, value)
        nullable_root = self.__nullable_root
        if nullable_root.is_empty():
            return null_iter

        nonempty_root = nullable_root
        empty_symbols = nonempty_root.nullable_common_prefix[0:0]
        return self.__iter_items(empty_symbols, nonempty_root)

    def __iter_items(self, nullable_prefix, nonnull_xnode):
        # nonnull_xnode = nonempty_root | nonleaf_node | leaf_node
        #   empty_root is not nonnull_xnode
        if not nonnull_xnode.is_branch():
            assert nonnull_xnode.is_leaf()
            leaf = nonnull_xnode

            symbols = nullable_prefix + leaf.nullable_suffix
            yield (symbols, leaf.value)
            return
        symbols = nonnull_xnode.get_symbols_segment()
        nullable_prefix = nullable_prefix + symbols

        for child_node in nonnull_xnode.get_maybe_symbol2child().values():
            yield from self.__iter_items(nullable_prefix, child_node)
        return


    def __getitem__(self, symbols):
        return self.get_item(symbols)
    def __delitem__(self, symbols):
        return self.remove_item(symbols)
    def __setitem__(self, symbols, value):
        self.set_item(symbols, value)
    def update_from_items(self, items):
        for symbols, value in items:
            self.set_item(symbols, value)
    def set_item(self, symbols, value):
        maybe_value_ops = theStdMaybeOps
        def symbols_may_old_value2may_new_value(symbols, may_old_value):
            # -> may_new_value
            return maybe_value_ops.mkJust(value)
        self.alter(symbols, symbols_may_old_value2may_new_value
                    , maybe_value_ops)
    def discard_item(self, symbols):
        maybe_value_ops = theStdMaybeOps
        def symbols_may_old_value2may_new_value(symbols, may_old_value):
            # -> may_new_value
            return maybe_value_ops.mkNothing()
        self.alter(symbols, symbols_may_old_value2may_new_value
                    , maybe_value_ops)
    def remove_item(self, symbols):
        maybe_value_ops = theStdMaybeOps
        def symbols_may_old_value2may_new_value(symbols, may_old_value):
            # -> may_new_value
            if maybe_value_ops.isNothing(may_old_value):
                raise KeyError(f'remove nonexist key: {symbols!r}')
            return maybe_value_ops.mkNothing()
        self.alter(symbols, symbols_may_old_value2may_new_value
                    , maybe_value_ops)

    @classmethod
    def __does_value_exist(cls, symbols
        , total_ancestor_symbols, remain_common_prefix_length, xnode):
        # (remain_common_prefix_length, xnode) are from self.find
        does_exist = (not xnode.is_root()
                    and xnode.is_leaf()
                    and remain_common_prefix_length == len(xnode.nullable_suffix)
                    #bug: without below line:
                    and len(symbols) == total_ancestor_symbols+remain_common_prefix_length
                    )
        assert not does_exist or xnode.is_leaf()
        return does_exist
    def get_item(self, symbols, fresult=None, value2result=None):
        # [symbol] -> (()->result) -> (value->result) -> result
        # default:
        #   fresult = raise KeyError
        #   value2result = echo
        if value2result is None:
            value2result = echo
        if fresult is None:
            def fresult():
                raise KeyError(f'get nonexist key: {symbols!r}')
        (total_ancestor_symbols, remain_common_prefix_length
            , ancestors, xnode) = self.find(symbols)
        #rint(total_ancestor_symbols)
        #rint(remain_common_prefix_length)
        #rint(ancestors)
        #rint(xnode)
        does_exist = self.__does_value_exist(symbols
            , total_ancestor_symbols, remain_common_prefix_length, xnode)
        assert not does_exist or xnode.is_leaf()

        if does_exist:
            leaf = xnode
            value = leaf.value
            #bug:result = value2result(value2result)
            result = value2result(value)
        else:
            result = fresult()
        return result
    def contains(self, symbols):
        return self.get_item(symbols, lambda:False, lambda _:True)



    def __query_maybe_longest_prefix_item__def__(self, symbols):
        for i in range(len(symbols),-1,-1):
            prefix = symbols[:i]
            if prefix in self:
                return len(prefix), self[prefix]
        return None
    def query_maybe_longest_prefix_item(self, symbols):
        '''-> None|(UInt, value)
-> None|(longest_prefix_length, value)

def query_maybe_longest_prefix_item(self, symbols):
    for i in range(L,-1,-1):
        prefix = symbols[:i]
        if prefix in self:
            return len(prefix), self[prefix]
    return None
'''
        ans = self.__query_maybe_longest_prefix_item__(symbols)
        '''
        ans_def = self.__query_maybe_longest_prefix_item__def__(symbols)
        try:
            assert ans_def == ans
        except:
            print(ans_def)
            print(ans)
            print(symbols)
            print(self)
            raise
        '''
        return ans
    def __query_maybe_longest_prefix_item__(self, symbols):
        # bug: forgot TrieEmptyRoot
        if not self: return None

        (total_ancestor_symbols, remain_common_prefix_length
            , ancestors, xnode) = self.find(symbols)

        '''bug: neednot exist, symbols may be longer than leaf
        does_exist = self.__does_value_exist(symbols
            , total_ancestor_symbols, remain_common_prefix_length, xnode)
        assert not does_exist or xnode.is_leaf()

        if does_exist:
            leaf = xnode
            return (len(symbols), leaf.value)
        if not ancestors:
            return None
        '''
        if remain_common_prefix_length == len(xnode.get_symbols_segment()):
            if xnode.is_branch():
                ancestors.append(xnode)
                pass
            else:
                assert xnode.is_leaf()
                leaf = xnode
                longest_prefix_length = total_ancestor_symbols + remain_common_prefix_length
                return (longest_prefix_length, leaf.value)

        # search ancestors
        maybe_symbol_ops = self.get_maybe_symbol_ops()
        Nothing = maybe_symbol_ops.mkNothing()
        #for ancestor in reversed(ancestors):
        while ancestors:
            ancestor = ancestors.pop()
            maybe_symbol2child = ancestor.get_maybe_symbol2child()
            may_leaf = maybe_symbol2child.get(Nothing)
            if may_leaf is not None:
                # found
                leaf = may_leaf
                leaf.value
                longest_prefix_length = sum(
                    len(branch.get_symbols_segment())
                    for branch in ancestors)
                return (longest_prefix_length, leaf.value)
        return None

    def find(self, symbols):
        '''-> (UInt, UInt, [TrieNonLeafNode], IXTrieNode)
-> (total_ancestor_symbols, remain_common_prefix_length, ancestors, xnode)

total_ancestor_symbols + remain_common_prefix_length <= len(symbols)
remain_common_prefix_length == 0
    or remain_common_prefix_length <= len(xnode.get_symbols_segment())

xnode :: IXTrieNode
IXTrieNode a v = ITrieNullableRoot a v | ITrieNode a v
not ancestors or ancestors[0] is self.__nullable_root
not ancestors ==>> xnode is self.__nullable_root
'''
        symbols_input = symbols; del symbols
        symbols_input_view = SeqSliceView(
                    symbols_input, range(len(symbols_input)))
        del symbols_input

        total_ancestor_symbols = 0
        ancestors = []
        def put_ancestor(ancestor):
            nonlocal total_ancestor_symbols
            ancestors.append(ancestor)
            total_ancestor_symbols += len(ancestor.get_symbols_segment())

        nullable_root = xnode = self.__nullable_root
        if nullable_root.is_empty():
            remain_common_prefix_length = 0
            return (total_ancestor_symbols, remain_common_prefix_length
                    , ancestors, xnode)

        maybe_symbol_ops = self.get_maybe_symbol_ops()
        Nothing = maybe_symbol_ops.mkNothing()
        while True:
            symbols_xnode = xnode.get_symbols_segment()
            tail_input = symbols_input_view[total_ancestor_symbols:]

            L = calc_common_prefix_length(tail_input, symbols_xnode)
            if L < len(symbols_xnode):
                remain_common_prefix_length = L
                break

            assert L == len(symbols_xnode)
            if not xnode.is_branch():
                assert xnode.is_leaf()
                remain_common_prefix_length = L
                break

            # branch
            may_head = maybe_symbol_ops.mkMaybe(
                    L != len(tail_input), lambda: tail_input[L])
            may_node = xnode.get_maybe_symbol2child().get(may_head)

            if may_node is None:
                remain_common_prefix_length = L
                break
            next_xnode = may_node

            put_ancestor(xnode)
            xnode = next_xnode
        return (total_ancestor_symbols, remain_common_prefix_length
                , ancestors, xnode)

    def alter(self, symbols
            , symbols_may_old_value2may_new_value
            , maybe_value_ops):
        # [symbol] -> ([symbol] -> Maybe old_value -> new_value) -> IMaybeOps -> None
        k_mv2mv = symbols_may_old_value2may_new_value

        (total_ancestor_symbols, remain_common_prefix_length
            , ancestors, xnode) = self.find(symbols)

        # exist ==>> TrieLeafNode
        does_exist = self.__does_value_exist(symbols
            , total_ancestor_symbols, remain_common_prefix_length, xnode)
        assert not does_exist or xnode.is_leaf()

        may_old_value = maybe_value_ops.mkMaybe(
                        does_exist, lambda:xnode.value)

        may_new_value = k_mv2mv(symbols, may_old_value)
        for new_value in maybe_value_ops.iter(may_new_value):
            # set
            if does_exist:
                # replace
                leaf = xnode
                leaf.value = new_value
            else:
                new_leaf_symbols = symbols[total_ancestor_symbols+remain_common_prefix_length:]
                new_leaf = TrieLeafNode(new_leaf_symbols, new_value)
                self.__add_new_leaf(ancestors, xnode, remain_common_prefix_length, new_leaf)

            break
        else:
            # discard symbols
            if does_exist:
                leaf = xnode
                self.__remove_leaf(ancestors, leaf)
            else:
                # discard but not exists
                pass
        return

    def clear(self):
        self.__init()
    def __init(self):
        self.__nullable_root = theTrieEmptyRoot
        self.__size = 0
    def __make_node_from_root_(self, root):
        # if not leaf_root, then nullable_common_prefix should not be empty
        root_maybe_symbol2child__ge1 = root.maybe_symbol2child__ge1
        if len(root_maybe_symbol2child__ge1) == 1:
            [(_, leaf)] = root_maybe_symbol2child__ge1.items()
            leaf.nullable_suffix = root.nullable_common_prefix
            return leaf
        root_maybe_symbol2child__ge2 = root_maybe_symbol2child__ge1

        if not root.nullable_common_prefix: raise Exception
        root_nonempty_common_prefix = root.nullable_common_prefix

        return TrieNonLeafNode(
            root_nonempty_common_prefix, root_maybe_symbol2child__ge2)
    def __make_root_from_nonleaf(self, nonleaf):
        return TrieNonEmptyRoot(nonleaf.nonempty_common_prefix, nonleaf.maybe_symbol2child__ge2)
    def __make_root_from_leaf(self, leaf):
        root_common_prefix = leaf.nullable_suffix
        new_leaf_suffix = leaf.nullable_suffix[0:0]
        new_leaf_value = leaf.value
        new_leaf = TrieLeafNode(new_leaf_suffix, new_leaf_value)

        root_maybe_symbol2child = self.new_maybe_symbol_mapping()
        self.__update_children(root_maybe_symbol2child, new_leaf)
        root_maybe_symbol2child__ge1 = root_maybe_symbol2child
        return TrieNonEmptyRoot(
            root_common_prefix, root_maybe_symbol2child__ge1)
    def __remove_leaf(self, ancestors, leaf):
        assert ancestors # since leaf cannot be root; root in ancestors
        parent = ancestors[-1]

        assert parent.is_branch()
        # parent :: TrieNonEmptyRoot | TrieNonLeafNode
        #   since exist leaf
        assert self.__size > 0
        self.__size -= 1

        may_head = self.__symbols2may_head(leaf.nullable_suffix)
        parent_maybe_symbol2child = parent.get_maybe_symbol2child()
        del parent_maybe_symbol2child[may_head]; del may_head
        if len(parent_maybe_symbol2child) >= 2:
            return
        elif len(parent_maybe_symbol2child) == 0:
            assert not self.__size
            assert parent is self.__nullable_root
            self.__init()
            return

        assert len(parent_maybe_symbol2child) == 1
        #bug: if parent.is_root(): return

        [(_, child)] = parent_maybe_symbol2child.items()

        old_parent = parent
        new_node = child
        old_parent_may_common_prefix = old_parent.get_symbols_segment()
        new_node_may_symbols_segment = old_parent_may_common_prefix + new_node.get_symbols_segment()
        if new_node.is_leaf():
            new_node.nullable_suffix = new_node_may_symbols_segment
        else:
            # new_node is nonleaf
            nonempty = new_node_may_symbols_segment
            assert nonempty
            new_node.nonempty_common_prefix = nonempty

        # replace old_parent by new_node
        if old_parent.is_root():
            # new_node -> new_root
            if new_node.is_leaf():
                new_root_leaf = new_node
                new_leaf_root = self.__make_root_from_leaf(new_root_leaf)
                self.__nullable_root = new_leaf_root
            else:
                new_nonleaf = new_node
                new_root = self.__make_root_from_nonleaf(new_nonleaf)
                self.__nullable_root = new_root
            return

        # replace old_parent by new_node
        assert len(ancestors) >= 2
        grandpa_xnode = ancestors[-2]

        assert old_parent_may_common_prefix
        # replace not add_new
        self.__update_children(
            grandpa_xnode.get_maybe_symbol2child()
            , new_node)
        return
    def __symbols2may_head(self, symbols):
        maybe_symbol_ops = self.get_maybe_symbol_ops()
        may_head = maybe_symbol_ops.mkMaybe(symbols, lambda:symbols[0])
        return may_head


    def __add_new_leaf(self, ancestors, xnode, remain_common_prefix_length, new_leaf):
        # "!!new!!" i.e. there are no node at the given position
        #
        # ["!!new!!"][xnode is leaf]
        #   (d1) ==>> [0 < remain_common_prefix_length < len(xnode.nullable_suffix)]
        #  * remain_common_prefix_length > 0
        #    * xnode.nullable_suffix == []:
        #       then self.find go to xnode iff new_leaf.nullable_suffix == []
        #       ==>> new_leaf has same position as xnode
        #       ==>> not "!!new!!"
        #    * xnode.nullable_suffix == (head:_):
        #       then self.find go to xnode iff new_leaf.nullable_suffix[0] == head
        #       ==>> remain_common_prefix_length >= 1
        #
        #  * remain_common_prefix_length < len(xnode.nullable_suffix)
        #       if remain_common_prefix_length == len(xnode.nullable_suffix):
        #           ==>> new_leaf has same position as xnode
        #           ==>> not "!!new!!"
        #   since remain_common_prefix_length <= len(xnode.nullable_suffix)
        #       ==>> remain_common_prefix_length < len(xnode.nullable_suffix)
        #
        # [remain_common_prefix_length==0] ==>> [xnode is root]
        #   * ==>> [xnode is not leaf]
        #       from (d1)
        #   * ==>> [xnode is not nonleaf]
        #       otherwise self.find cannot go to nonleaf-xnode
        #
        # [xnode is not TrieEmptyRoot][remain_common_prefix_length==len(xnode.get_symbols_segment())]
        #   * ==>> [xnode is not leaf]
        #       from (d1)
        #   * ==>> [new_leaf can add to xnode.get_maybe_symbol2child() directly]


        self.__size += 1
        if xnode.is_root() and xnode.is_empty():
            new_leaf_root = self.__make_root_from_leaf(new_leaf)
            self.__nullable_root = new_leaf_root
            return

        if remain_common_prefix_length == len(xnode.get_symbols_segment()):
            assert xnode.is_branch()
            # add to branch directly
            branch = xnode
            self.__update_children(
                branch.get_maybe_symbol2child()
                , new_leaf)
            return


        (new_xnode_nullable_segment, new_child
            ) = self.__split_nonnull_xnode_at_symbols_segment_position(
                    xnode, remain_common_prefix_length)

        new_xnode_maybe_symbol2child = self.new_maybe_symbol_mapping()
        self.__update_children(
            new_xnode_maybe_symbol2child
            , new_child, new_leaf)
        new_xnode_maybe_symbol2child__ge2 = new_xnode_maybe_symbol2child

        if xnode.is_root():
            nonempty_root = xnode
            assert nonempty_root is self.__nullable_root
            nonempty_root.nullable_common_prefix = new_xnode_nullable_segment
            nonempty_root.maybe_symbol2child__ge1 = new_xnode_maybe_symbol2child__ge2
            return

        assert remain_common_prefix_length
        assert new_xnode_nullable_segment
        new_xnode_nonempty_segment = new_xnode_nullable_segment
        if not xnode.is_leaf():
            nonleaf = xnode
            nonleaf.nonempty_common_prefix = new_xnode_nonempty_segment
            nonleaf.maybe_symbol2child__ge2 = new_xnode_maybe_symbol2child__ge2
            return

        # replace old_leaf by new_nonleaf
        old_leaf = xnode
        new_nonleaf = TrieNonLeafNode(
            new_xnode_nonempty_segment
            ,new_xnode_maybe_symbol2child__ge2
            )
        # replace old_leaf by new_nonleaf
        assert ancestors
        parent = ancestors[-1]
        parent_maybe_symbol2child = parent.get_maybe_symbol2child()
        self.__update_children(
            parent_maybe_symbol2child
            , new_nonleaf)
        return


    def __split_nonnull_xnode_at_symbols_segment_position(
        self, xnode, remain_common_prefix_length):
        # -> (new_xnode_nullable_segment, new_child)
        assert not (xnode.is_root() and xnode.is_empty())
        assert remain_common_prefix_length < len(xnode.get_symbols_segment())

        if remain_common_prefix_length == 0:
            assert xnode.is_root()

        xnode_symbols_segment = xnode.get_symbols_segment()
        new_child_node_nonempty_segment = xnode_symbols_segment[remain_common_prefix_length:]
        new_xnode_nullable_segment = xnode_symbols_segment[:remain_common_prefix_length]
        assert new_child_node_nonempty_segment

        # new_child := ??
        xnode_maybe_symbol2child = xnode.get_maybe_symbol2child()
        assert xnode_maybe_symbol2child
        if len(xnode_maybe_symbol2child) == 1:
            assert xnode.is_root()
            [(_, leaf)] = xnode_maybe_symbol2child.items()
            leaf.nullable_suffix = new_child_node_nonempty_segment
            new_child = leaf
        else:
            xnode_maybe_symbol2child__ge2 = xnode_maybe_symbol2child
            new_child = TrieNonLeafNode(
                new_child_node_nonempty_segment
                ,xnode_maybe_symbol2child__ge2
                )

        return new_xnode_nullable_segment, new_child



    def __update_children(self, maybe_symbol2child, *nodes):
        for node in nodes:
            assert not node.is_root()
            symbols = node.get_symbols_segment()
            may_head = self.__symbols2may_head(symbols)
            maybe_symbol2child[may_head] = node
        return
    def verify_trie_structure(self):
        # -> bool
        nullable_root = self.__nullable_root
        if nullable_root.is_empty():
            return True
        nonempty_root = nullable_root

        nonnull_xnode = nonempty_root
        return self.__verify_trie_nonnull_xnode(nonnull_xnode, is_root=True)
    def __verify_trie_nonnull_xnode(self, nonnull_xnode, is_root:bool):
        if bool(nonnull_xnode.is_root()) != bool(is_root):
            return False

        if not nonnull_xnode.is_branch():
            assert nonnull_xnode.is_leaf()
            return hasattr(nonnull_xnode.nullable_suffix, '__len__')

        branch = nonnull_xnode
        symbols = branch.get_symbols_segment()
        if not (symbols or is_root):
            return False

        maybe_symbol2child = branch.get_maybe_symbol2child()
        L = len(maybe_symbol2child)
        if L <= 0:
            return False
        elif L == 1:
            if not is_root:
                return False

        maybe_symbol_ops = self.get_maybe_symbol_ops()
        for may_head, child_node in maybe_symbol2child.items():
            for head in maybe_symbol_ops.iter(may_head):
                symbols = child_node.get_symbols_segment()
                if not (symbols and symbols[0] == head):
                    return False
                break
            else:
                if child_node.is_branch():
                    return False
                assert child_node.is_leaf()
                if len(child_node.nullable_suffix):
                    return False
            if not self.__verify_trie_nonnull_xnode(child_node, is_root=False):
                return False

        return True

class CharTrie(ITrie):
    __slots__ = ()
    @override
    def new_maybe_symbol_mapping(self):
        # () -> Map (Maybe symbol) ITrieNode
        return dict()
    @override
    def get_maybe_symbol_ops(self):
        # for (Maybe symbol)
        # () -> IMaybeOps
        return theMaybeCharOps


class TrieNonLeafNode(IOpGetMaybeSymbol2Child, ITrieNode):
    __slots__ = '''
        __nonempty_common_prefix
        __maybe_symbol2child__ge2
        '''.split()

    def __init__(self, nonempty_common_prefix, maybe_symbol2child__ge2):
        assert len(nonempty_common_prefix)
        assert len(maybe_symbol2child__ge2) >= 2
        self.nonempty_common_prefix = nonempty_common_prefix
        self.maybe_symbol2child__ge2 = maybe_symbol2child__ge2
    @property
    def nonempty_common_prefix(self):
        #return getattr(self, '__nonempty_common_prefix')
        return self.__nonempty_common_prefix
    @nonempty_common_prefix.setter
    def nonempty_common_prefix(self, nonempty_common_prefix):
        if not len(nonempty_common_prefix): raise ValueError
        #setattr(self, '__nonempty_common_prefix', nonempty_common_prefix)
        self.__nonempty_common_prefix = nonempty_common_prefix

    @property
    def maybe_symbol2child__ge2(self):
        #return getattr(self, '__maybe_symbol2child__ge2')
        return self.__maybe_symbol2child__ge2
    @maybe_symbol2child__ge2.setter
    def maybe_symbol2child__ge2(self, maybe_symbol2child__ge2):
        if not len(maybe_symbol2child__ge2) >= 2: raise ValueError
        #setattr(self, '__maybe_symbol2child__ge2', maybe_symbol2child__ge2)
        self.__maybe_symbol2child__ge2 = maybe_symbol2child__ge2

    @override
    def is_leaf(self):
        return False
    @override
    def get_symbols_segment(self):
        return self.nonempty_common_prefix
    @override
    def get_maybe_symbol2child(self):
        return self.maybe_symbol2child__ge2



class TrieLeafNode(ITrieNode):
    __slots__ = '''
        __nullable_suffix
        __value
        '''.split()

    def __init__(self, nullable_suffix, value):
        assert hasattr(nullable_suffix, '__len__')
        self.nullable_suffix = nullable_suffix
        self.value = value
    @property
    def nullable_suffix(self):
        #return getattr(self, '__nullable_suffix')
        return self.__nullable_suffix
    @nullable_suffix.setter
    def nullable_suffix(self, nullable_suffix):
        if not hasattr(nullable_suffix, '__len__'): raise ValueError
        #setattr(self, '__nullable_suffix', nullable_suffix)
        self.__nullable_suffix = nullable_suffix

    @property
    def value(self):
        #return getattr(self, '__value')
        return self.__value
    @value.setter
    def value(self, value):
        #setattr(self, '__value', value)
        self.__value = value

    @override
    def is_branch(self):
        return False
    @override
    def is_leaf(self):
        return True
    @override
    def get_symbols_segment(self):
        return self.nullable_suffix




def _t():
    trie = CharTrie()
    assert len(trie) == 0
    assert repr(trie) == 'CharTrie()'

    trie[''] = 0
    assert len(trie) == 1
    assert repr(trie) == "CharTrie([('', 0)])"
    assert trie[''] == 0

if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()


