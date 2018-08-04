

def _replace_substrings(string, sub2replace_ls, start):
    if start == len(sub2replace_ls):
        return string
    
    sub, replace = sub2replace_ls[start]
    ls = string.split(sub)
    for i, block in enumerate(ls):
        new = _replace_substrings(block, sub2replace_ls, start+1)
        ls[i] = new

    r = replace.join(ls)
    return r
def replace_substrings(string, sub2replace_ls):
    sub2replace_ls = tuple((s,r) for s,r in sub2replace_ls)
    r = _replace_substrings(string, sub2replace_ls, 0)
    return r
    
