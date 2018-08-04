


from graph.directed_acyclic_graph import reversed_topological_ordering, find_a_circle
from graph.directed_graph import dedges2u2vtc


def rnode_tree_to_tID2tnode(rnode_tree_of_XL_in_CFGL):
    tID2tnode, gf_tID2leaf_tIDs, tID2child_tIDs = \
               raw_parse_result_of_XL_in_CFGL2tnode_and_other_infos(
                   rnode_tree_of_XL_in_CFGL)
    return tID2tnode

def tID2tnode_to_inodes_and_tIDs(tID2tnode):
    tIDs = list(tID2tnode)
    tIDs.sort()
    tID2iID = dict((tID, i) for i, tID in enumerate(tIDs))

    ls = []
    def tIDs2iIDs(tIDs):
        return [tID2iID[tID] for tID in tIDs]
    for iID in range(len(tIDs)):
        tID = tIDs[iID]
        tnode = tID2tnode[tID]
        case = tnode[0]
        if case == 'token':
            _, tID, token_name = tnode
            inode = case, iID, token_name
        elif case == 'lchild':
            _, tID, ref_id, count, argname_endflag, tags = tnode
            iref_id = tID2iID[ref_id]
            inode = case, iID, iref_id, count, argname_endflag, tags
        elif case == 'list':
            _, tID, child_tIDs = tnode
            child_iIDs = tIDs2iIDs(child_tIDs)
            inode = case, iID, child_iIDs
        elif case == 'filter':
            _, tID, child_tIDs, leaves = tnode
            child_iIDs = tIDs2iIDs(child_tIDs)
            ileaves = tIDs2iIDs(leaves)
            inode = case, iID, child_iIDs, ileaves
        elif case == 'group':
            _, tID, gref_ids, leaves = tnode
            ref_iIDs = tIDs2iIDs(gref_ids)
            ileaves = tIDs2iIDs(leaves)
            inode = case, iID, ref_iIDs, ileaves
        else:
            raise ValueError('unknown case: {!r}'.format(case))

        ls.append(inode)
    inodes = ls
    return inodes, tIDs

            
        
            

    



            
            




def raw_parse_result_of_XL_in_CFGL2tnode_and_other_infos(
    raw_parse_result_of_XL_in_CFGL):
    
    tID_node_ls, ref_ids = \
                 raw_parse_result_of_XL_in_CFGL2tID_node_ls_and_ref_ids(
                     raw_parse_result_of_XL_in_CFGL)

    tID2idx, tID2node = tID_node_ls_to_tID2idx_and_tID2node(tID_node_ls)

    undefined_tIDs = set(ref_ids) - set(tID2idx)
    if undefined_tIDs:
        raise ValueError('undefined_tIDs: {}'.format(undefined_tIDs))

    tID2child_tIDs = tID_node_ls_to_tID2child_tIDs(tID_node_ls)

    DAG_edges = group_and_filter_dependency_DAG_edges(tID_node_ls, tID2idx, tID2child_tIDs)
    DAG_u2vtc = dedges2u2vtc(len(tID_node_ls), DAG_edges)
    circle = find_a_circle(DAG_u2vtc)
    if circle:
        circle_dependency_tIDs = [tID_node_ls[v][0] for v in circle]
        raise ValueError('group circle dependency: {}'.format(circle_dependency_tIDs))
    vtc = reversed_topological_ordering(DAG_u2vtc)
    gf_tID2leaf_tIDs = expand_group_and_filter(tID_node_ls, tID2node, tID2child_tIDs, vtc)
            
    gf_tID2leaf_tIDs = reduce_group_leaves(gf_tID2leaf_tIDs, tID2idx, tID2node)
    tID2tnode = make_tID2tnode(gf_tID2leaf_tIDs, tID_node_ls, tID2child_tIDs)

    return tID2tnode, gf_tID2leaf_tIDs, tID2child_tIDs





def raw_parse_result_of_XL_in_CFGL2tID_node_ls_and_ref_ids(raw_parse_result_of_XL_in_CFGL):
    node_ls = raw_parse_result_of_XL_in_CFGL
    pair_ls, ref_ids = [], []
    def _i(p_tID, node):
        case = node[0]
        ID = node[1]
        tID = p_tID + (ID,)
        pair_ls.append((tID, node))
        
        if case == 'token':
            _, _, token_name = node
        elif case == 'lchild':
            raise logic-error
        elif case == 'top_list':
            _, IDs, children = node
            pair_ls.pop()
            del tID

            if not IDs:
                raise ValueError('no ID!')
            elif p_tID:
                raise ValueError('top_list has no parents')

            ls = []            
            for ID, ref_topID in zip(IDs[-1], ID[1:]):
                ref_id = (ref_topID,)
                new_lc_node = ('lchild', ref_id, None, None, [])
                new_li_node = ('list', ID, [new_lc_node])
                ls.append(new_li_node)
            ID = IDs[-1]
            new_li_node = ('list', ID, children)
            ls.append(new_li_node)
            for node in ls:
                _i(p_tID, node)
                    
        elif case == 'list':
            _, _, children = node
            for case, ref_id, count, argname_endflag, tags in children:
                assert case == 'lchild'
                ref_ids.append(ref_id)
            for i, c in enumerate(children):
                c_tID = tID + (i,)
                pair_ls.append((c_tID, c))
        elif case == 'group':
            _, _, children = node
            ref_ids.extend(children)
        elif case == 'filter':
            _, _, children = node
            cases = {'filter', 'list', 'fref'}
            for c in children:
                case = c[0]
                if case not in cases:
                    raise ValueError('filter children should be filter/list/fref')

                _i(tID, c)
        elif case == 'fref':
            _, ID = node
            pair_ls.pop()
            
            ref_id = (ID,)
            new_lc_node = ('lchild', ref_id, None, None, [])
            new_li_node = ('list', ID, [new_lc_node])
            _i(p_tID, new_li_node)
        else:
            raise ValueError('unkown case: {case} @{tID}'\
                             .format(case=case, tID=tID))
        return

    for node in node_ls: _i((), node)
    return pair_ls, ref_ids



def tID_node_ls_to_tID2idx_and_tID2node(tID_node_ls):
    tID2node = dict(tID_node_ls)
    tID2idx = {tID: idx for idx, (tID, node) in enumerate(tID_node_ls)}
    if len(tID2idx) != len(tID_node_ls):
        raise ValueError('tID duplicate')
    return tID2idx, tID2node


def tID_node_ls_to_tID2child_tIDs(tID_node_ls):
    tID2child_tIDs = {}
    for tID, node in tID_node_ls:
        case = node[0]
        assert tID not in tID2child_tIDs
        ls = []
        if case  == 'filter':
            _, _, children = node
            for c in children:
                cID = c[1]
                c_tID = tID + (cID,)
                ls.append(c_tID)
        elif case == 'group':
            _, _, gref_ids = node
            ls.extend(gref_ids)
        elif case == 'list':
            _, _, children = node
            for cID in range(len(children)):
                c_tID = tID + (cID,)
                ls.append(c_tID)
        else:
            continue
        tID2child_tIDs[tID] = ls
    return tID2child_tIDs


    
            
def group_and_filter_dependency_DAG_edges(tID_node_ls, tID2idx, tID2child_tIDs):
    other_cases = {'list', 'lchild', 'token'}
    bad_cases = {'top_list', 'fref'}
    target_cases = {'filter', 'group'}

    DAG_edges = []
    for tID, node in tID_node_ls:
        case = node[0]
        if case in target_cases:
            child_tIDs = tID2child_tIDs[tID]
            me = tID2idx[tID]
            for c_tID in child_tIDs:
                i = tID2idx[c_tID]
                DAG_edges.append((me, i))
                
        elif case in other_cases:
            pass
        elif case in bad_cases:
            raise ValueError('case: {!r} should not in tID_node_ls'.format(case))
        else:
            raise ValueError('unknown case: {!r}'.format(case))

            
    return DAG_edges

            
                



def expand_group_and_filter(tID_node_ls, tID2node, tID2child_tIDs,
                            reversed_topological_ordering_vtc):
    gf2leaf_tIDs = {}
    cases = {'filter', 'group'}
    
    for v in reversed_topological_ordering_vtc:
        tID, node = tID_node_ls[v]
        case = node[0]
        if case not in cases: continue
        ls = []
        for c_tID in tID2child_tIDs[tID]:
            c_node = tID2node[c_tID]
            c_case = c_node[0]
            if c_case in cases:
                ls.extend(gf2leaf_tIDs[c_tID])
            else:
                # is leaf
                ls.append(c_tID)
        assert tID not in gf2leaf_tIDs
        gf2leaf_tIDs[tID] = ls
        
    group_filter_tID2leaf_tIDs = gf2leaf_tIDs

    return group_filter_tID2leaf_tIDs
        
            
def reduce_group_leaves(group_filter_tID2leaf_tIDs, tID2idx, tID2node):

    new_gf2leaf_tIDs = {}
    for tID, leaves in group_filter_tID2leaf_tIDs.items():
        node = tID2node[tID]
        case = node[0]
        if case != 'group':
            new_gf2leaf_tIDs[tID] = leaves
            continue

        exists = bytearray(len(tID2idx))
        ls = []
        for leaf in leaves:
            i = tID2idx[leaf]
            if not exists[i]:
                ls.append(leaf)
                exists[i] = 1

        new_gf2leaf_tIDs[tID] = ls

    return new_gf2leaf_tIDs






def make_tID2tnode(gf_tID2leaf_tIDs, tID_node_ls, tID2child_tIDs):
    tID2tnode = {}
    for tID, node in tID_node_ls:
        case = node[0]
        leaf_tIDs = gf_tID2leaf_tIDs.get(tID)
        if leaf_tIDs is None:
            # leaf
            if case == 'token':
                _, ID, token_name = node
                tnode = case, tID, token_name
            elif case == 'lchild':
                _, ref_id, count, argname_endflag, tags = node
                tnode = case, tID, ref_id, count, argname_endflag, tags
            elif case == 'list':
                _, ID, children = node
                children = tID2child_tIDs[tID]
                tnode = case, tID, children
            else:
                raise ValueError('unkown-case: {!r}'.format(case))
        elif case == 'filter':
            _, ID, children = node
            children = tID2child_tIDs[tID]
            tnode = case, tID, children, leaf_tIDs
        elif case == 'group':
            _, ID, gref_ids = node
            tnode = case, tID, gref_ids, leaf_tIDs
        else:
            raise ValueError('unkown-case: {!r}'.format(case))

        tID2tnode[tID] = tnode
        
    return tID2tnode






from raw_node_tree_of_CFGL_in_CFGL import cfgl_rnode_tree_of_xtokenized_style_CFGL




tID2tnode_of_CFGL_in_CFGL = rnode_tree_to_tID2tnode(cfgl_rnode_tree_of_xtokenized_style_CFGL)
##import pprint
##p=pprint.PrettyPrinter(indent=4).pprint
##
##p(tID2tnode)






