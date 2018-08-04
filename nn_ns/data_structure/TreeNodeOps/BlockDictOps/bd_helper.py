
__all__ = '''
    is_one_piece_block_key
    is_exactly_block_key
    block_key2iter_block_entities
    bd_subtract
    bd_intersection
    '''.split()


from seed.tiny import fst, snd, null_iter
from seed.iters.handle_first_middles_last import handle_first_middles_last

def is_one_piece_block_key(
        block_key
        , entity2block_key
        , block_dict_key_ops
        , iter_all_touch_or_overlap_block_entities, *args_for_iter):
    # not empty range and inside one of iter_block_keys()

    isEmptyRange = block_dict_key_ops.isEmptyRange
    insideRange = block_dict_key_ops.insideRange
    iter_all_of = iter_all_touch_or_overlap_block_entities

    if isEmptyRange(block_key): return False

    for first_entity in iter_all_of(*args_for_iter, block_key, True):
        break
    else:
        return False

    first_block_key = entity2block_key(first_entity)
    return insideRange(block_key, first_block_key)

def is_exactly_block_key(
        block_key
        , entity2block_key
        , block_dict_key_ops
        , iter_all_touch_or_overlap_block_entities, *args_for_iter):
    # be one of iter_block_keys()
    isEmptyRange = block_dict_key_ops.isEmptyRange
    eqRange = block_dict_key_ops.eqRange
    iter_all_of = iter_all_touch_or_overlap_block_entities

    if isEmptyRange(block_key): return False

    #bug: for first_block_key in iter_all_of(block_key, True):
    for first_entity in iter_all_of(*args_for_iter, block_key, True):
        break
    else:
        return False

    first_block_key = entity2block_key(first_entity)
    return eqRange(block_key, first_block_key)



def block_key2iter_block_entities(
        block_key
        , reverse:bool
        , entity2block_key
        , ireplace_block_key_of_entity
            # :: entity -> block_key -> new_entity
        , block_dict_key_ops
        , iter_all_touch_or_overlap_block_entities
        , *args_for_iter
        ):
    # intput_block_key may be empty
    #
    # -> Iter (block_key, dict_value)
    #   all output_block_keys are nonempty and inside input_block_key

    isEmptyRange = block_dict_key_ops.isEmptyRange
    intersection_ranges1 = block_dict_key_ops.intersection_ranges1
    iter_all_of = iter_all_touch_or_overlap_block_entities

    if isEmptyRange(block_key):
        # yield nothing
        return null_iter

    def handle_end_block_entity(end_block_entity):
        # end_block_entity is left_or_right_end_block_entity
        rng = entity2block_key(end_block_entity)
        common_range = intersection_ranges1(block_key, rng)
        if isEmptyRange(common_range):
            # yield nothing
            return
        yield ireplace_block_key_of_entity(end_block_entity, common_range)


    iter_affected_block_entities = iter_all_of(*args_for_iter
                , block_key, False, reverse=bool(reverse))

    return handle_first_middles_last(
            iter_affected_block_entities
            , handle_end_block_entity # first
            , lambda middle_block_entity: [middle_block_entity]
            , handle_end_block_entity # last
            , handle_end_block_entity # only one
            )


def bd_intersection(
            entity2block_item
            , block_item2entity
            , combine
                # :: self_dict_value -> other_dict_value -> dict_value
            , block_dict_key_ops
            , self_iter_block_entities
                # :: Iter entity
            , other_block_key2iter_block_entities
            , *args_for_other_block_key2iter_block_entities
            ):
    # -> [entity]
    # self_iter_block_entities :: sorted nonoverlapped(Iter nonempty_range)
    #       may touch
    #
    o_bk2bes = other_block_key2iter_block_entities
    args = args_for_other_block_key2iter_block_entities
    common_entities = []
    for s_entity in self_iter_block_entities:
        s_block_key, s_dict_value = entity2block_item(s_entity)
        o_entities = o_bk2bes(*args, s_block_key)

        for o_block_key, o_dict_value in map(entity2block_item, o_entities):
            dict_value = combine(s_dict_value, o_dict_value)
            entity = block_item2entity((o_block_key, dict_value))
            common_entities.append(entity)
    return common_entities

def bd_subtract(
            entity2block_key
            , ireplace_block_key_of_entity
                # :: entity -> block_key -> new_entity
            , block_dict_key_ops
            , self_iter_block_entities
                # :: Iter entity
            , other_block_key2iter_block_entities
            , *args_for_other_block_key2iter_block_entities
            ):
    # -> [entity]
    # self_iter_block_entities :: sorted nonoverlapped(Iter nonempty_range)
    #       may touch
    #
    # self_iter_block_entities = self.iter_block_keys()
    # other_block_key2iter_block_entities = other.block_key2iter_block_keys
    subtract = block_dict_key_ops.subtract_two_touch_or_cross_ranges
    o_bk2bes = other_block_key2iter_block_entities
    args = args_for_other_block_key2iter_block_entities
    s_entities = []
    for s_entity in self_iter_block_entities:
        s_block_key = entity2block_key(s_entity)
        o_block_keys = map(entity2block_key, o_bk2bes(*args, s_block_key))

        #s_block_keys.append(s_block_key)
        s_entities.append(s_entity)
        for o_block_key in o_block_keys:
            s_block_key = entity2block_key(s_entities.pop())

            s_entities.extend(
                ireplace_block_key_of_entity(s_entity, rng)
                for rng in subtract(s_block_key, o_block_key))
    return s_entities

