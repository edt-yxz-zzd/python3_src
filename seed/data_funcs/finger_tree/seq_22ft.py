#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/seq_22ft.py

seq_22ft:
    sequence using (2,2)-finger_tree:

    # kw:reverse
    push_ :: xtree -> xnode -> xtree
    pop_ :: xtree -> (xtree, xnode)
    len :: xtree -> num_elements
    get_ :: xtree -> idx -> element
    iter_ :: xtree -> Iter element
    iter__with_idx_path_ :: xtree -> Iter (idx, path, element)
    path5idx_ :: xtree -> idx -> path
    path2idx_ :: xtree -> idx -> path
    split__idx_ :: xtree -> idx -> (xtree, xtree)
    split__path_ :: xtree -> path -> (xtree, xtree)

(2,2)-finger_tree:
    [len(hnode.sub_nodes) == 2]

    [len(btree.sub_nodes) <- {0,1}]
    [len(wing.sub_nodes) <- {1,2}]

    [hnode.num_elements == 2 * 2**hnode.depth == 2**(1+hnode.depth)]
    [btree.num_elements == len(btree.sub_nodes) * 2**btree.depth]
    [wing.num_elements == len(wing.sub_nodes) * 2**wing.depth]

    [htree.num_elements == htree.lwing.num_elements + htree.stem.num_elements + htree.rwing.num_elements]

hnode:
    `.depth
    `.num_elements
    .sub_nodes  :: [xnode{depth}]{len=2}

    [xnode == (hnode|element)]
    [xnode{depth} == (hnode{depth-1} if depth else element)]
btree:
    .depth
    `.num_elements
    .sub_nodes  :: [xnode{depth}]{0<=len<2}
wing:
    .depth
    `.num_elements
    .sub_nodes  :: [xnode{depth}]{1<=len<3}
htree:
    .depth
    .height
    `.num_elements
    .lwing  :: wing{depth}
    .stem   :: xtree{depth,height}
    .rwing  :: wing{depth}

    [xtree == (htree|btree)]
    [xtree{depth,height} == (htree{depth+1,height-1} if height else btree{depth})]


seed.data_funcs.finger_tree.seq_22ft
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.seq_22ft -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.seq_22ft:__doc__ -ht
py_adhoc_call   seed.data_funcs.finger_tree.seq_22ft   @f
from seed.data_funcs.finger_tree.seq_22ft import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__



__all__
from seed.data_funcs.finger_tree.seq_22ft import *
