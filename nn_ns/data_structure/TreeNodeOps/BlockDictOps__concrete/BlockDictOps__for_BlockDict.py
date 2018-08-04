
__all__ = '''
    BlockDictOps__for_BlockDict
    BlockDictOps__constructor__for_BlockDict
    '''.split()


from .abc import override
from ..BlockDictOps.IBlockDictOps import IBlockDictOps
from ..BlockDictOps.IBlockDictOps__constructor import \
    IBlockDictOps__constructor
from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.EqOps import python_eq_key_ops
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase



class BlockDictOps__for_BlockDict(IBlockDictOps):
    '''
self :: IBlockDict
ops :: BlockDictOps__for_BlockDict <: IBlockDictOps
        not IBlockDictOps__constructor
'''
    __slots__ = '''
        _block_dict_key_ops
        _block_dict_key_ops
        '''.split()
    def __init__(ops, block_dict_key_ops, eq_dict_value_ops):
        '''
input:
    block_dict_key_ops :: IBlockDictKeyOps<dict_key>
        # about dict_key instead of tree_key

    # no: dict_key2tree_key :: None | (dict_key -> tree_key)
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops
'''
        if not isinstance(block_dict_key_ops, IBlockDictKeyOps): raise TypeError
        if eq_dict_value_ops is None:
            eq_dict_value_ops = python_eq_key_ops
        elif not isinstance(eq_dict_value_ops, IEqOps): raise TypeError


        total_left_bound_ops = block_dict_key_ops.make_total_left_bound_ops()
        assert isinstance(total_left_bound_ops, ITotalOrderingOps)

        # left_bound = tree_key

        ops._block_dict_key_ops = block_dict_key_ops
        ops._eq_dict_value_ops = eq_dict_value_ops
        return

    @override
    def get_args_for_eq_hash(ops):
        return (ops.block_dict_key_ops, ops.eq_dict_value_ops)


    def __repr__(ops):
        block_dict_key_ops = ops.block_dict_key_ops
        eq_dict_value_ops = ops.eq_dict_value_ops

        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None

        return repr_helper(ops, block_dict_key_ops, eq_dict_value_ops)



    @override
    def _get_block_dict_key_ops_(ops):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        return ops.block_dict_key_ops
    @override
    def _get_eq_dict_value_ops_(ops):
        # -> IEqOps<dict_value>
        return ops.eq_dict_value_ops



    @override
    def iter_all_touch_or_overlap_block_items(ops, self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        return self.iter_all_touch_or_overlap_block_items(
                block_key, overlap_only, reverse=reverse)

    @override
    def get_num_block_keys(ops, self):
        # no __len__
        return self.get_num_block_keys()
    @override
    def iter_block_items(ops, self, *, reverse=False):
        # no items
        return self.iter_block_items(reverse=reverse)
    @override
    def copy_block_dict(ops, self):
        return self.copy()
    @override
    def _index_block_item_at_(ops, self, i:'UInt'):
        return self._index_block_item_at_(i)
    @override
    def index_block_item_at(ops, self, i:'Int'):
        return self.index_block_item_at(i)
    @override
    def get_first_or_last_block_item(ops, self, last:bool):
        return self.get_first_or_last_block_item(last)
    @override
    def get_first_block_item(ops, self):
        return self.get_first_block_item()
    @override
    def get_last_block_item(ops, self):
        return self.get_last_block_item()

    @override
    def is_one_piece_block_key(ops, self, block_key):
        return self.is_one_piece_block_key(block_key)
    @override
    def is_exactly_block_key(ops, self, block_key):
        # be one of iter_block_keys()
        return self.is_exactly_block_key(block_key)

    @override
    def list_all_touch_or_overlap_block_items(ops, self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        # block_key may be empty
        return self.list_all_touch_or_overlap_block_items(
                block_key, overlap_only, reverse=reverse)



    @override
    def block_key2block_items(ops, self, block_key, *, reverse=False):
        # block_key may be empty
        # -> [(block_key, dict_value)]
        return self.block_key2block_items(block_key, reverse=reverse)
    @override
    def iter_block_keys(ops, self, *, reverse=False):
        # no __iter__/keys
        return self.iter_block_keys(reverse=reverse)
    @override
    def iter_dict_values(ops, self, *, reverse=False):
        # no values
        return self.iter_dict_values(reverse=reverse)




    @override
    def dict_key2block_items(ops, self, dict_key):
        return self.dict_key2block_items(dict_key)




    # __bool__
    @override
    def is_empty(ops, self):
        return not self

    # __getitem__
    @override
    def dict_key2dict_value(ops, self, dict_key, *
            , dict_key2default=None
            , dict_value2result=None):
        if dict_key2default is None:
            r = self[dict_key] # KeyError
        else:
            Nothing = object()
            r = self.get(dict_key, Nothing)
            if r is Nothing:
                return dict_key2default(dict_key)

        if dict_value2result is None:
            return r
        return dict_value2result(r)


    # __contains__
    @override
    def contains_dict_key(ops, self, dict_key):
        return dict_key in self

    # get
    @override
    def getdefault(ops, self, dict_key, default=None, *, dict_value2result=None):
        def dict_key2default(dict_key):
            return default
        return ops.dict_key2dict_value(self, dict_key
                    , dict_key2default=dict_key2default
                    , dict_value2result=dict_value2result)




    # __eq__
    @override
    def block_dict_eq(ops, self, other):
        if self is other: return True
        return self == other



    @override
    def block_key2iter_block_items(ops, self, block_key, *, reverse=False):
        # intput_block_key may be empty
        #
        # -> Iter (block_key, dict_value)
        #   all output_block_keys are nonempty and inside input_block_key

        return self.block_key2iter_block_items(block_key, reverse=reverse)



class BlockDictOps__constructor__for_BlockDict(
        BlockDictOps__for_BlockDict
        , IBlockDictOps__constructor):
    '''
self :: IBlockDict
ops :: BlockDictOps__for_BlockDict <: IBlockDictOps__constructor
        not IBlockDictOps__imodify
'''
    __slots__ = '''
        _block_dict_key_ops
        _block_dict_key_ops
        _make_empty_block_dict
        _empty_block_dict
        '''.split()
    '''
    def __init__(ops, self):
        empty = self.self_make_empty_block_dict()

        ops._empty_block_dict = empty # but how to hash??
        BlockDictOps__for_BlockDict.__init__(
            empty.block_dict_key_ops, empty.eq_dict_value_ops)
    '''
    def __init__(ops
            , block_dict_key_ops
            , eq_dict_value_ops
            , make_empty_block_dict):
        '''
make_empty_block_dict :: () -> IBlockDict
    hashable
# make_block_dict_from_iterable :: (Iter item|Iter block_item) -> is_block_items -> IBlockDict
'''
        if not callable(make_empty_block_dict): raise TypeError
        hash(make_empty_block_dict)

        ops._make_empty_block_dict = make_empty_block_dict
        empty = ops._empty_block_dict = make_empty_block_dict()
        assert isinstance(empty, IBlockDict)

        BlockDictOps__for_BlockDict.__init__(
            block_dict_key_ops, eq_dict_value_ops)
        return

    @override
    def get_args_for_eq_hash(ops):
        return (ops.block_dict_key_ops
                , ops.eq_dict_value_ops
                , ops._make_empty_block_dict)
    @override
    def __repr__(ops):
        block_dict_key_ops = ops.block_dict_key_ops
        eq_dict_value_ops = ops.eq_dict_value_ops

        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None
        make_empty_block_dict = ops._make_empty_block_dict

        return repr_helper(ops
            , block_dict_key_ops
            , eq_dict_value_ops
            , make_empty_block_dict)






    @property
    @override
    def make_empty_block_dict(ops):
        return ops._make_empty_block_dict
    @override
    def make_block_dict_from_items(ops, items):
        self = ops._empty_block_dict.self_make_block_dict_from_items(items)
        return self
    @override
    def make_block_dict_from_block_items(ops, block_items):
        self = ops._empty_block_dict.self_make_block_dict_from_block_items(block_items)
        return self
    @override
    def make_block_dict_from_iterable(ops, iterable, is_block_items:bool):
        self = ops._empty_block_dict.self_make_block_dict_from_iterable(
                        iterable, is_block_items)
        return self





if __name__ == '__main__':
    XXX = BlockDictOps__for_BlockDict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



if __name__ == '__main__':
    input('to continue...: BlockDictOps__constructor__for_BlockDict')
    YYY = BlockDictOps__constructor__for_BlockDict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(YYY)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(YYY)






