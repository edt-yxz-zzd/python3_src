
#e ../../python3_src/seed/seq_tools/force_reversed.py
def force_reversed(xs, /):
    try:
        xs = reversed(xs)
    except TypeError:
        xs = list(xs)
        xs = reversed(xs)
    return xs

from seed.seq_tools.force_reversed import force_reversed
