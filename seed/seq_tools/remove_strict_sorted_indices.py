r'''[[[
e ../../python3_src/seed/seq_tools/remove_strict_sorted_indices.py





#]]]'''#'''


def remove_strict_sorted_indices__emplace_(idc4remove, seq, /):
    idc4remove = iter(idc4remove)
    for i in idc4remove:
        break
    else:
        return
    begin, end = i, i+1
        #gap/spaces
    for j in idc4remove:
        if j == end:
            end += 1
        else:
            assert end < j
            for begin, end in enumerate(range(end, j), begin):
                seq[begin] = seq[end]
            begin += 1
            end = j+1
    else:
        assert begin < end
        j = len(seq)
        if end < j:
            for begin, end in enumerate(range(end, j), begin):
                seq[begin] = seq[end]
            begin += 1
            end += 1
        assert begin < end == len(seq)
        del seq[begin:]
    return

def remove_strict_sorted_indices__emplace_(idc4remove, seq, /):
    ls = []
    for i in reversed(idc4remove):
        while seq:
            ls.append(seq.pop())
            if len(seq) == i:
                ls.pop()
                break
        else:
            raise ValueError((idc4remove, i))
    seq.extend(reversed(ls))
    return










from seed.seq_tools.remove_strict_sorted_indices import remove_strict_sorted_indices__emplace_

