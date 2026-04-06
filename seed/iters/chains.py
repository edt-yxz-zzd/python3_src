
__all__ = 'chains'.split()
from itertools import chain
chains = chain.from_iterable
del chain

from seed.iters.chains import chains
