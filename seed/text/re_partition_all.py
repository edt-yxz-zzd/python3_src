# re.split
# If capturing parentheses are used in pattern,
# then the text of all groups in the pattern are also
# returned as part of the resulting list.


#from seed.iters.zip_me import zip_me
from seed.iters.icut_to import icut_seq_to

# like re.split, but assume 'capturing parentheses are used in pattern'
def iter_re_partition_all(re_sep, txt):
    begin = 0
    for m in re_sep.finditer(txt):
        if not m:
            raise logic-error
        yield txt[begin:m.start()]
        yield m.group(0)

        begin = m.end()
    else:
        yield txt[begin:]

    return


def re_partition_all(re_sep, txt):
    return list(iter_re_partition_all(re_sep, txt))
def re_partition_to_head_bodyls(re_sep, txt):
    # ([[Char]], [Char]) -> ([Char], ([Char], [Char]))
    ls = re_partition_all(re_sep, txt)
    assert sum(map(len, ls)) == len(txt)
    if len(ls) % 2 != 1:
        raise logic-error
    
    head = ls[0]
    # bodyls = list(zip_me(2, ls[1:])) # bug: once zip_me update
    bodyls = list(icut_seq_to(ls, 2, 1))
    assert len(bodyls) == len(ls)//2
    return head, bodyls

    
    for i in range(1, len(ls), 2):
        bodyls.append((ls[i], ls[i+1]))
    return head, bodyls

