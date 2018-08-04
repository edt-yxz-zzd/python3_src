
def inv_automap(old_vtx2new_vtx):
    n = len(old_vtx2new_vtx)
    if not all(0 <= v < n for v in old_vtx2new_vtx):
        raise ValueError('domain should be range(n)')
    
    new_vtx2old_vtx = [None] * n
    for old_vtx, new_vtx in enumerate(old_vtx2new_vtx):
        if new_vtx2old_vtx[new_vtx] != None:
            raise ValueError('not 1 to 1 map')
        new_vtx2old_vtx[new_vtx] = old_vtx

    assert not any(v == None for v in new_vtx2old_vtx)
    return new_vtx2old_vtx

def item_map(old_ls, old_idx2new_idx, new_idx2old_idx):
    return list(map(lambda old_item: old_idx2new_idx[old_item], old_ls))

def rows_map(old_idx2row, old_idx2new_idx, new_idx2old_idx):
    n = len(old_idx2row)
    assert n == len(old_idx2new_idx)
    return [old_idx2row[old_idx] for old_idx in new_idx2old_idx]

def mx_map(old_mx, old_idx2new_idx, new_idx2old_idx):
    mx = list(map(lambda row: ls_map(row, old_idx2new_idx),
                  old_mx))
    return rows_map(mx, new_idx2old_idx)
    
    
