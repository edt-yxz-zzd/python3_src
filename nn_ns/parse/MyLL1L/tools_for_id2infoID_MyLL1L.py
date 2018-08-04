from itertools import chain
from root.graph.directed_graph import dedges2u2vtc
from root.graph.directed_acyclic_graph import \
     reversed_topological_ordering, find_a_circle, NotDAGError
from .InfoID_MyLL1L import FOLLOW, FIRST

__all__ = ['fill_raw_id2info_MyLL1L']

'''
result1_InfoDict                  is raw_id2info
result2_tIDDict, result2_InfoDict :  set tID and output a dict of key tID
result3_tIDDict, result3_InfoDict :  set FIRST and id2info

to save result3, we keep raw_id2info (or a factory) and tID2FIRST

'''


def tIDDict_2_id2info(result3_tIDDict):
    return {k[0] : v for k, v in result3_tIDDict.items() if len(k) == 1}

def id2info_2_define(result3_InfoDict):
    d = result3_InfoDict
    ks = sorted(d.keys())
    cs = (d[k] for k in ks)
    body = '\n'.join(c.get_define() for c in cs)
    return body

def tIDDict_2_define(result3_tIDDict):
    d = tIDDict_2_id2info(result3_tIDDict)
    return id2info_2_define(d)

def id2info_2_raw_init_repr(result3_InfoDict):
    d = result3_InfoDict
    ks = sorted(d.keys())
    kr = ((k, d[k].get_raw_init_repr()) for k in ks)
    body = ', '.join('{!r} : {}' for k, r in kr)
    body = '{{ {} }}'.format(body)
    return body

def tIDDict2tID2FIRST(result3_tIDDict):
    d = result3_tIDDict
    return {k : v.first for k, v in d.items()}



def save_result3(result3_tIDDict, result3_InfoDict):
    r = _save_result3(result3_tIDDict, result3_InfoDict)
    define, init, tID2FIRST = r
    tpl = '({!r}, {}, {})'
    s = tpl.format(define, init, tID2FIRST)

    assert r == _save_result3(read_result3(s))
    return s

def _save_result3(result3_tIDDict, result3_InfoDict):
    d = result3_tIDDict
    define = id2info_2_define(result3_InfoDict)
    init = id2info_2_raw_init_repr(result3_InfoDict)
    tID2FIRST = tIDDict2tID2FIRST(d)
    return define, init, tID2FIRST

def read_result3(save_str):
    define, init, tID2FIRST = eval(save_str)
    raw_id2info = eval(init)
    result2_tIDDict, result2_InfoDict = result1_InfoDict2tIDDict(raw_id2info)

    
    for tID, FIRST in tID2FIRST.items():
        info = result2_tIDDict[tID]
        info.set_FIRST(FIRST)
        info.set_id2info(result2_InfoDict)
        
    result3_tIDDict, result3_InfoDict = result2_tIDDict, result2_InfoDict
    return result3_tIDDict, result3_InfoDict



###############################################################
def fix_tID(parent_tID, infoID, add):
    tID = tuple(chain(parent_tID, [infoID.ID]))
    add(tID, infoID)
    if not infoID.isLeaf():
        for child in infoID:
            fix_tID(tID, child, add)
    return


# result1_InfoDict is raw_id2info
def result1_InfoDict2tIDDict(result1_InfoDict):
    tIDDict = {}
    def add(tID, infoID):
        assert infoID.tID == None
        assert tID not in tIDDict
        infoID.set_tID(tID)
        tIDDict[tID] = infoID
        return
    tID = ()
    for ID, item in result1_InfoDict.items():
        fix_tID(tID, item, add)

    result2_InfoDict = result1_InfoDict
    return tIDDict, result2_InfoDict

#result2_tIDDict, result2_InfoDict = result1_InfoDict2tIDDict(result1_InfoDict)

def check_nullable(result2_InfoDict):
    for ID, info in result2_InfoDict.items():
        if info.nullable():
            raise Exception('ID {!r} is nullable'.format(ID))
    return
    
#check_nullable(result2_InfoDict)

def init_ftID2FRef(tIDs):
    d = {}
    fs = [FIRST, FOLLOW]#, TTYPES]
    for tID in tIDs:
        for f in fs:
            assert tID not in d
            ftID = (f, tID)
            d[ftID] = set()
    return d

##def fill_ftID2FRef_TTYPES(ftID2FRef, result2_tIDDict):
##    f = TTYPES
##    for tID, info in result2_tIDDict.items():
##        ftID = (f, tID)
##        ftID2FRef[ftID] = info.getPreKnownFirst()
##    return

def fill_ftID2FRef_FIRST(ftID2FRef, result2_tIDDict):
    f = FIRST
    for tID, info in result2_tIDDict.items():
        ftID = (f, tID)
        ftID2FRef[ftID] = info.getFirstRef()
    return

def fill_ftID2FRef_FOLLOW(ftID2FRef, result2_tIDDict):
    for info in result2_tIDDict.values():
        info.exportFollowRef(ftID2FRef)
    return

def fill_ftID2FRef(ftID2FRef, result2_tIDDict):
    fs = [fill_ftID2FRef_FIRST, fill_ftID2FRef_FOLLOW] #fill_ftID2FRef_TTYPES]
    for f in fs:
        f(ftID2FRef, result2_tIDDict)
    return

#ftID2FRef = init_ftID2FRef(result2_tIDDict.keys())
#fill_ftID2FRef(ftID2FRef, result2_tIDDict)




def gen_idx_key_map(keys):
    idx2key = sorted(keys)
    key2idx = dict((key, i) for i, key in enumerate(idx2key))
    return idx2key, key2idx


def gen_tID_forest(idx2tID, tID2idx):
    n = len(idx2tID)
    edges = []
    for tID in idx2tID:
        if len(tID) == 1:
            continue
        p = tID[:-1]
        c = tID
        p = tID2idx[p]
        c = tID2idx[c]
        edges.append((p,c))
        
        
    forest = dedges2u2vtc(n, edges)
    return forest


def gen_dgraph(node2nodes, node2idx):
    n = len(node2idx)
    ls = [None] * n
    
    for node, nodes in node2nodes.items():
        u = node2idx[node]
        assert ls[u] == None
        ls[u] = list(node2idx[node] for node in nodes)

    for i in range(n):
        if ls[u] == None:
            ls[u] = []
    return ls

def rorder_dgraph(dgraph, idx2item=None):
    r = reversed_topological_ordering(dgraph)
    if r == None:
        raise Exception('cycle depency')

    if idx2item != None:
        ls = [idx2item[i] for i in r]
    else:
        ls = r
    return ls

def order_ftIDs(ftID2FRef, idx2ftID, ftID2idx):
    ftID_dgraph = gen_dgraph(ftID2FRef, ftID2idx)
    r = find_a_circle(ftID_dgraph)
    if r:
        r = [idx2ftID[i] for i in r]
        raise NotDAGError(repr(r))
    ls = rorder_dgraph(ftID_dgraph, idx2ftID)
    return ls

def gen_ftID2TTypes(ftID2FRef, result2_tIDDict):
    tID2info = result2_tIDDict

    assert len(ftID2FRef) == len(tID2info) * 2
    idx2ftID, ftID2idx = gen_idx_key_map(ftID2FRef.keys())
    ordered_ftIDs = order_ftIDs(ftID2FRef, idx2ftID, ftID2idx)

    assert len(set(ordered_ftIDs)) == len(ftID2FRef) == len(ordered_ftIDs)

    ftID2TTypes = {}
    for ftID in ordered_ftIDs:
        assert ftID not in ftID2TTypes
        
        ftID2TTypes[ftID] = s = set()
        f, tID = ftID
        if f == FIRST:
            info = tID2info[tID]
            s |= info.getPreKnownFirst()
        
        ftIDs = ftID2FRef[ftID]
        for _ftID in ftIDs:
            token_types = ftID2TTypes[_ftID]
            s |= token_types

        #if not s: print(ftID)
        # main entry will be empty. error : assert s

    assert len(ftID2FRef) == len(ftID2TTypes)
    return ftID2TTypes


def check_disjoint(ftID2TTypes, result2_tIDDict):
    tID2info = result2_tIDDict
    
    idx2tID, tID2idx = gen_idx_key_map(tID2info.keys())

    forest = gen_tID_forest(idx2tID, tID2idx)
    tIDs = rorder_dgraph(forest, idx2tID)

    for tID in tIDs:
        info = tID2info[tID]
        for disjoint_sets in info.getDisjointRules():
            disjoint_sets = [(ftID, ftID2TTypes[ftID]) for ftID in disjoint_sets]
            alls = set()
            for ftID, s in disjoint_sets:
                if not alls.isdisjoint(s):
                    for ftID0, s0 in disjoint_sets:
                        if s0 is s:
                            raise impossible
                        if not s0.isdisjoint(s):
                            break
                    else:
                        raise cant.go.here
                    
                    raise Exception('DisjointRule fails: {} {}'.format(ftID, ftID0))
                
                alls |= s
    
    return



#ftID2TTypes = gen_ftID2TTypes(ftID2FRef, result2_tIDDict)
#check_disjoint(ftID2TTypes, result2_tIDDict)

def fill_InfoDict_FIRST_id2info(ftID2TTypes, result2_tIDDict, result2_InfoDict):
    f = FIRST
    id2info = result2_InfoDict
    for tID, info in result2_tIDDict.items():
        ftID = (f, tID)
        first = ftID2TTypes[ftID]
        info.set_FIRST(first)
        info.set_id2info(id2info)

    result3_tIDDict, result3_InfoDict = result2_tIDDict, result2_InfoDict
    return result3_tIDDict, result3_InfoDict

##result3_tIDDict, result3_InfoDict = fill_InfoDict_FIRST_id2info(\
##    ftID2TTypes, result2_tIDDict, result2_InfoDict)



def fill_raw_id2info(raw_id2info):
    result1_InfoDict = raw_id2info
    result2_tIDDict, result2_InfoDict = result1_InfoDict2tIDDict(result1_InfoDict)
    check_nullable(result2_InfoDict)

    ftID2FRef = init_ftID2FRef(result2_tIDDict.keys())
    fill_ftID2FRef(ftID2FRef, result2_tIDDict)

    ftID2TTypes = gen_ftID2TTypes(ftID2FRef, result2_tIDDict)
    check_disjoint(ftID2TTypes, result2_tIDDict)

    result3_tIDDict, result3_InfoDict = fill_InfoDict_FIRST_id2info(\
        ftID2TTypes, result2_tIDDict, result2_InfoDict)

    tIDDict, id2info = result3_tIDDict, result3_InfoDict
    for i in id2info:
        assert (i,) in tIDDict
    return tIDDict, id2info

fill_raw_id2info_MyLL1L = fill_raw_id2info

if __name__ == '__main__':
    from .raw_id2infoID_MyLL1L_of_MyLL1L import build_raw_id2infoID_MyLL1L
    result1_InfoDict = build_raw_id2infoID_MyLL1L()
    tIDDict, id2info = fill_raw_id2info_MyLL1L(result1_InfoDict)

