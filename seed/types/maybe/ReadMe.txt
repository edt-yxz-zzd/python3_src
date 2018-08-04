Maybe a

two types of maybe:
    * None or not None # None_based_maybe
        # it is incomplete
        # the wrapped object should not be None
        # not allow (Maybe (Maybe a))
    * false or sized_singletion_container
        # not obj or (obj in Collection and obj not in Iterator and len(obj) == 1)
        # it is complete

