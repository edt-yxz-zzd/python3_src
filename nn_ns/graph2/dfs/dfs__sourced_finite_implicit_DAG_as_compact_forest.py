
'''
see: "def - 2.1. infinite implicit graph.txt"
    implicit graph
        * finite sourced DAG_as_compact_forest
            # need not vertex_eq to avoid parent since DAG

DAG_as_tree_dfs/DAG_as_forest_dfs
    treat DAG as a tree
        so we will not color vertices
    output vertex may be duplicated
        since it or its ancestors may have multiparents
    used at:
        implicit graph dfs
            game state graph dfs    [duplicated states]
            filesystem dfs          [duplicated dirs/files]

    when dfs, we have to hold ancestor_stack or iterator_stack
    * for unparented tree
    * DAG with multiparents # e.g. non-tree
'''


