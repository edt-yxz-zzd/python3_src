
__all__ = ['print_err']
import sys
print_err = lambda *args, **kwargs: print(*args, file=sys.stderr, **kwargs)
