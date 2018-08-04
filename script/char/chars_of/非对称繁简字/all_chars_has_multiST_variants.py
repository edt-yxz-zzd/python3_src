
from simplified2multi_traditionals_obj import simplified2multi_traditionals
from traditional2multi_simplifieds_obj import traditional2multi_simplifieds
from itertools import chain

def get_all_chars(d):
    for k, v in d.items():
        yield from k
        yield from v
        assert len(k) == 1

ds = [simplified2multi_traditionals, traditional2multi_simplifieds]
all_chars_has_multiST_variants = ''.join(sorted(set(chain.from_iterable(map(get_all_chars, ds)))))

print(all_chars_has_multiST_variants)


