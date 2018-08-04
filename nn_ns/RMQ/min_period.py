
'''
min_period seq = arg<i> min {seq2[i:i+L] | i <- [0..L-1]}
    where
        seq2 = seq*2
        L = len(seq)
min_period seq =
    for (Leaf, (begin, end)) in preorder(tree):
        if end - begin >= L:
            return begin
    tree = suffix_tree (seq*2)

??? wrong: used in triconnected planar graph isomorphism
    min_period pseudo-walk for embedding in the_2_planar_embeddings for direction in the_2_edge_directions

'''

from .make_SA_LCP import make_SA

def canon_colored_cycle_graph(colores_in_cycle_order):
    colores = list(colores_in_cycle_order)
    min_period0 = find_min_period(colores)
    colores.reverse()
    min_period1 = find_min_period(colores)
    return min(min_period0, min_period1)

def find_min_period(uint_array):
    isuffix = find_offset_of_min_period(uint_array)
    min_period = uint_array[isuffix:] + uint_array[:isuffix]
    return min_period

def find_offset_of_min_period(uint_array):
    '''[UInt] -> ArrayIdx

what?
    shifts(array) = [array[i:]+array[:i] | i <- [0..len(array)-1]]
    min_period(array) =[def]= min shifts(array)
    find_offset_of_min_period(array) =[def]= shifts(array).index(min_period)
why?
    how to encode/canon a colored cycle graph?
        for clockwise and anti-:
            find the min shift colors...
'''
    L = len(uint_array)
    double = uint_array + uint_array
    SA = make_SA(double)
    for isuffix in SA:
        if isuffix < L:
            return isuffix
    raise logic-error





