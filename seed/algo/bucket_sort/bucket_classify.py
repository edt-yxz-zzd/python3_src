'''
bucket_classify
    how?
        use OneTimeMap
    where?
        "[Planar_Graph_Isomorphism_1974]Linear time algorithm for isomorphism of planar graphs[good].pdf"
            O(n) for classify many planar graph by isomorphism at same time
            but not for canon_labelling


    like bucket_sort_with_table(
            may_alphabet_size, iterable, sorted_wheres, table
            , *, key=None, reverse=False):
        but sorted_wheres are not neccesary sorted since we donot known the order
'''


def bucket_classify(iterable, buffer__uint_mapping, *, key):
    ''' :: Iter a -> OneTimeMap -> (a->UInt) -> [[a]]

buffer__uint_mapping::OneTimeMap
'''
    buffer__uint_mapping.clear()
    for a in iterable:
        u = key(a)
        try:
            ls = buffer__uint_mapping[u]
        except KeyError:
            ls = buffer__uint_mapping[u] = []

        ls.append(a)
    return list(buffer__uint_mapping.values())



