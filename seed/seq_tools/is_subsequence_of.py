
def is_subsequence_of_ex(sub, seq, sub_begin, sub_end, seq_begin, seq_end):
    subL = sub_end - sub_begin
    seqL = seq_end - seq_begin
    # assert subL >= 0
    # assert seqL >= 0
    if subL <= 0: return True
    if subL > seqL: return False
    assert 0 < subL <= seqL
    while subL:
        if sub[sub_begin] == seq[seq_begin]:
            # drop sub_begin
            subL -= 1
            sub_begin += 1
            # drop seq_begin
            seqL -= 1
            seq_begin += 1
        else:
            # drop seq_begin
            seqL -= 1
            seq_begin += 1
            if subL > seqL: return False
    return True

def is_subsequence_of(sub, seq):
    return is_subsequence_of_ex(sub, seq, 0, len(sub), 0, len(seq))


